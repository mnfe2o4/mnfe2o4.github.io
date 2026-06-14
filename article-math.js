(function () {
  "use strict";

  var renderQueue = Promise.resolve();

  function typeset(element) {
    if (!element || element.dataset.mathTypeset === "true") {
      return;
    }

    element.dataset.mathTypeset = "true";
    renderQueue = renderQueue.then(function () {
      return MathJax.typesetPromise([element]);
    });
    renderQueue = renderQueue.then(null, function (error) {
        element.dataset.mathTypeset = "error";
        if (window.console && console.error) {
          console.error("MathJax typesetting failed:", error);
        }
      }
    );
  }

  function initializeLazyTypesetting() {
    var cards = Array.prototype.slice.call(
      document.querySelectorAll(".article-shell .card")
    );

    if (!cards.length) {
      return;
    }

    if (!("IntersectionObserver" in window)) {
      cards.forEach(typeset);
      return;
    }

    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            observer.unobserve(entry.target);
            typeset(entry.target);
          }
        });
      },
      { rootMargin: "700px 0px" }
    );

    cards.forEach(function (card) {
      observer.observe(card);
    });

    window.addEventListener("beforeprint", function () {
      cards.forEach(function (card) {
        observer.unobserve(card);
        typeset(card);
      });
    });
  }

  window.MathJax = {
    tex: {
      inlineMath: [["\\(", "\\)"]],
      displayMath: [["\\[", "\\]"]]
    },
    startup: {
      typeset: false,
      ready: function () {
        MathJax.startup.defaultReady();
        MathJax.startup.promise.then(function () {
          if (document.readyState === "loading") {
            document.addEventListener(
              "DOMContentLoaded",
              initializeLazyTypesetting,
              { once: true }
            );
          } else {
            initializeLazyTypesetting();
          }
        });
      }
    }
  };
})();
