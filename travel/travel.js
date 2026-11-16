(() => {
  'use strict';
  const data = window.TRAVEL_DATA;
  if (!data) return;
  const page = document.body.dataset.page;
  const trip = data.trips.find(item => item.id === page);
  const reducedMotion = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const escapeHTML = value => String(value).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const colours = {car:'#225e79', transit:'#7b8d99', bus:'#738b9b', walk:'#8d9b91', bike:'#a87743', ferry:'#2585a7',flight:'#866b9a',train:'#47726e',activity:'#99845f'};
  const scrollTo = selector => document.querySelector(selector)?.scrollIntoView({behavior:reducedMotion?'instant':'smooth', block:'start'});

  function createMap(id) {
    const container = document.getElementById(id);
    if (!container) return null;
    if (!window.L) {
      container.innerHTML = '<div style="padding:35px;color:#526d7c">互动地图暂不可用。可继续阅读下方的地点、每日行程与照片。</div>';
      return null;
    }
    const map = L.map(container, {scrollWheelZoom:false, zoomControl:false, zoomSnap:0.5, attributionControl:true, zoomAnimation:false, markerZoomAnimation:false, fadeAnimation:false});
    L.control.zoom({position:'bottomright'}).addTo(map);
    if(page==='yellowstone')map.attributionControl.addAttribution('路线 &copy; <a href="https://www.openstreetmap.org/copyright" target="_blank">OpenStreetMap</a> contributors');
    const isWebPage=/^https?:$/.test(location.protocol);
    let message=container.parentElement.querySelector('.map-message');
    if(!message){message=document.createElement('p');message.className='map-message';message.setAttribute('aria-live','polite');container.insertAdjacentElement('afterend',message);}
    map.createPane('offline-base');map.getPane('offline-base').style.zIndex='190';
    map.createPane('offline-labels');map.getPane('offline-labels').style.zIndex='250';
    const cityLabels=L.layerGroup();
    for(const [name,lat,lon] of [['温哥华',49.28,-123.13],['西雅图',47.60,-122.33],['洛杉矶',34.05,-118.25],['Riverside',33.98,-117.3755],['盐湖城',40.76,-111.89],['黄石国家公园',44.65,-110.60]]){
      L.marker([lat,lon],{pane:'offline-labels',interactive:false,keyboard:false,icon:L.divIcon({className:'basemap-city-label',html:'<span>'+name+'</span>',iconSize:[85,18],iconAnchor:[-15,-12]})}).addTo(cityLabels);
    }
    const offline=window.TRAVEL_OFFLINE_MAP?L.geoJSON(window.TRAVEL_OFFLINE_MAP,{pane:'offline-base',interactive:false,
      renderer:L.canvas({pane:'offline-base'}),
      style:feature=>feature.properties.kind==='land'?{color:'#b5c9c4',weight:0.8,fillColor:'#f0efe5',fillOpacity:1}:
        feature.properties.kind==='lake'?{color:'#afcdd6',weight:0.7,fillColor:'#d9e9ee',fillOpacity:1}:{color:'#a8cbd7',weight:1,opacity:0.8},
      attribution:'<a href="https://www.naturalearthdata.com/about/terms-of-use/" target="_blank">Natural Earth</a> · 地理简图'
    }).addTo(map):null;
    const tiles=L.tileLayer(data.map.tileUrl,{maxZoom:19,attribution:'&copy; <a href="https://www.openstreetmap.org/copyright" target="_blank">OpenStreetMap</a> contributors'});
    let mode=isWebPage?'online':'offline';let loaded=false;let fallbackScheduled=false;
    const control=L.control({position:'topright'});
    let select;
    function switchMode(next,failed=false){
      mode=next;
      if(select)select.value=next;
      if(next==='online'&&isWebPage){
        if(map.hasLayer(cityLabels))map.removeLayer(cityLabels);
        loaded=false;fallbackScheduled=false;
        if(!map.hasLayer(tiles))tiles.addTo(map);
        message.textContent='';
      }else{
        if(map.hasLayer(tiles))map.removeLayer(tiles);
        if(!map.hasLayer(cityLabels))cityLabels.addTo(map);
        message.textContent=failed?'在线底图暂不可用，已显示离线地理简图。':!isWebPage?'本地文件模式：使用离线地理简图。在线街道图需通过本地预览或网站地址打开。':'离线地理简图不含详细街道；地点与路线仍可查看。';
      }
    }
    control.onAdd=()=>{
      const box=L.DomUtil.create('div','basemap-control');
      const label=document.createElement('label');label.textContent='底图 ';select=document.createElement('select');select.setAttribute('aria-label','选择地图底图');
      const simple=new Option('离线地理简图','offline');const online=new Option(isWebPage?'在线街道图':'在线街道图（需HTTP预览）','online');online.disabled=!isWebPage;
      select.add(simple);select.add(online);select.value=mode;select.addEventListener('change',()=>switchMode(select.value));
      label.append(select);box.append(label);L.DomEvent.disableClickPropagation(box);L.DomEvent.disableScrollPropagation(box);return box;
    };
    control.addTo(map);
    tiles.on('tileload',()=>{loaded=true;if(mode==='online')message.textContent='';});
    tiles.on('tileerror',()=>{
      if(mode==='online'&&!loaded&&!fallbackScheduled){fallbackScheduled=true;setTimeout(()=>{if(mode==='online')switchMode('offline',true);},0);}
    });
    switchMode(mode);
    return map;
  }

  if (page === 'index') {
    const map = createMap('overview-map');
    const layers = map ? L.featureGroup().addTo(map) : null;
    function filterHome(country) {
      document.querySelectorAll('[data-trip-country]').forEach(card => {card.hidden=country!=='all' && card.dataset.tripCountry!==country;});
      document.querySelectorAll('[data-country]').forEach(button => button.setAttribute('aria-pressed', String(button.dataset.country===country)));
      if (!map) return;
      layers.clearLayers();
      const trips=data.trips.filter(item => country==='all' || item.country===country);
      const bounds=[];
      for (const item of trips) {
        const point=item.id==='yellowstone'?[44.73,-110.70]:[49.28,-123.13];
        bounds.push(point);
        const marker=L.marker(point,{icon:L.divIcon({className:'overview-pin',html:'<span>'+escapeHTML(item.title)+' ↗</span>',iconSize:[1,36],iconAnchor:[0,18]})}).addTo(layers);
        marker.bindPopup('<strong>'+escapeHTML(item.title)+'</strong><p>'+escapeHTML(item.dateLabel)+'</p><a href="'+item.id+'.html">打开这段旅行 →</a>');
      }
      map.stop();
      if (bounds.length===1) map.setView(bounds[0],6,{animate:false});
      else map.fitBounds(bounds,{padding:[65,55],maxZoom:5,animate:false});
    }
    document.querySelectorAll('[data-country]').forEach(button => button.addEventListener('click',()=>filterHome(button.dataset.country)));
    filterHome('all');
    return;
  }
  if (!trip) return;

  let selectedDay='all';
  let selectedStop=null;
  let visiblePhotos=trip.photos.slice();
  const places=new Map(trip.stops.map((place,index)=>[place.id,{...place,index:index+1}]));
  const map=createMap('trip-map');
  const routeLayer=map?L.featureGroup().addTo(map):null;
  const markerLayer=map?L.featureGroup().addTo(map):null;
  const markers=new Map();
  const photoLayer=map?L.layerGroup().addTo(map):null;
  let mapPhotosVisible=true;

  function renderMapPhotos() {
    if(!map)return;
    photoLayer.clearLayers();
    const hint=document.getElementById('map-photo-hint');
    if(!mapPhotosVisible){hint.textContent='';return;}
    if(map.getZoom()<10){hint.textContent='放大地图查看照片';return;}
    const photos=trip.photos.filter(photo=>photo.mapCoordinates&&(selectedDay==='all'||photo.date===selectedDay)&&(!selectedStop||photo.stop===selectedStop));
    const groups=new Map();
    for(const photo of photos){
      const point=map.project(photo.mapCoordinates,map.getZoom());
      const key=Math.floor(point.x/120)+':'+Math.floor(point.y/92);
      if(!groups.has(key))groups.set(key,[]);
      groups.get(key).push(photo);
    }
    for(const group of groups.values()){
      const photo=group[0];
      const label=photo.locationLabel||places.get(photo.stop).name;
      const title=group.length===1?'查看照片：'+photo.caption:label+' · '+group.length+' 张照片';
      const icon=L.divIcon({className:'map-photo-marker',html:'<img src="'+escapeHTML(photo.small)+'" alt="">'+(group.length>1?'<span class="map-photo-count">'+group.length+'</span>':''),iconSize:[96,72],iconAnchor:[-10,78],tooltipAnchor:[58,-78],popupAnchor:[58,-78]});
      const marker=L.marker(photo.mapCoordinates,{icon,title,alt:title,keyboard:true,zIndexOffset:500}).addTo(photoLayer);
      marker.bindTooltip(group.length===1?photo.caption+' · '+label+(photo.mapLocationType==='place'?'（景点范围）':''):title,{direction:'top',offset:[0,-6]});
      if(group.length===1)marker.on('click',()=>openPhoto(photo.id));
      else{
        const thumbs=group.map(item=>'<button type="button" data-photo="'+escapeHTML(item.id)+'" aria-label="查看大图：'+escapeHTML(item.caption)+'"><img src="'+escapeHTML(item.small)+'" alt="'+escapeHTML(item.caption)+'" loading="lazy"></button>').join('');
        marker.bindPopup('<div class="map-photo-popup-grid">'+thumbs+'</div><p>'+group.length+' 张照片 · 点击查看大图</p>',{className:'map-photo-popup',maxWidth:280,autoPan:true,autoPanPaddingTopLeft:[12,95],autoPanPaddingBottomRight:[12,12]});
      }
    }
    hint.textContent=photos.length?'点击缩略图查看大图':'暂无照片位置';
  }
  if(map)map.on('zoomend',renderMapPhotos);

  function availableStops() {
    return selectedDay==='all' ? trip.stops.map(s=>s.id) : trip.days.find(day=>day.date===selectedDay)?.stops || [];
  }

  function renderMap(fit=true) {
    if (!map) return;
    routeLayer.clearLayers(); markerLayer.clearLayers(); markers.clear();
    const routes=trip.routes.filter(route=>selectedDay==='all'||route.day===selectedDay);
    for (const route of routes) {
      const dashed=route.status==='schematic'||route.status==='transfer-schematic'||route.status==='flight-connection'||route.mode==='walk'||route.mode==='bike';
      const line=L.polyline(route.coordinates,{color:colours[route.mode]||colours.transit,weight:route.mode==='ferry'?4:3,opacity:0.85,dashArray:dashed?'6 7':null,lineCap:'round'}).addTo(routeLayer);
      line.bindTooltip(route.label,{sticky:true,direction:'top'});
      line.bindPopup('<strong>'+escapeHTML(route.label)+'</strong><p>'+(route.status==='road-reconstruction'?'自驾路段示意。':route.mode==='flight'?'机场间航班连接，非实际飞行轨迹。':route.mode==='ferry'?'Lonsdale Quay → Waterfront。':route.mode==='bike'?'10 月 19 日下午环园骑行。':'行程接续示意。')+'</p>');
      if (route.mode==='ferry') {
        const points=route.coordinates, a=points[points.length-2], b=points[points.length-1];
        const rotation=Math.atan2(b[1]-a[1],b[0]-a[0])*180/Math.PI;
        L.marker([(a[0]+b[0])/2,(a[1]+b[1])/2],{interactive:false,icon:L.divIcon({className:'ferry-direction',html:'<span style="display:block;transform:rotate('+rotation+'deg)">▲</span>',iconSize:[20,20],iconAnchor:[10,10]})}).addTo(routeLayer);
      }
    }
    for (const id of availableStops()) {
      const place=places.get(id); if (!place) continue;
      const marker=L.marker(place.coordinates,{title:place.name,alt:place.name,keyboard:true,icon:L.divIcon({className:'map-number'+(selectedStop===id?' active':''),html:'<span>'+place.index+'</span>',iconSize:[27,27],iconAnchor:[13,13]})}).addTo(markerLayer);
      marker.bindPopup('<strong>'+escapeHTML(place.name)+'</strong><p>'+escapeHTML(place.note)+'</p><button type="button" class="popup-photo-link" data-gallery-stop="'+escapeHTML(id)+'">看这里的照片 →</button>');
      marker.on('click',()=>{selectStop(id,false);});
      markers.set(id,marker);
    }
    if (fit) {
      const coords=routes.flatMap(route=>route.coordinates).concat(availableStops().map(id=>places.get(id)?.coordinates).filter(Boolean));
      map.stop();
      if (coords.length) map.fitBounds(coords,{padding:[36,40],maxZoom:13,animate:false});
      else map.fitBounds(trip.mapFocus,{padding:[22,22],animate:false});
    }
  }

  function filterGallery() {
    visiblePhotos=trip.photos.filter(photo=>(selectedDay==='all'||photo.date===selectedDay)&&(!selectedStop||photo.stop===selectedStop));
    document.querySelectorAll('.gallery-item').forEach(figure=>{figure.hidden=(selectedDay!=='all'&&figure.dataset.photoDate!==selectedDay)||(selectedStop&&figure.dataset.photoStop!==selectedStop);});
    document.getElementById('gallery-count').textContent=visiblePhotos.length+' 张照片';
    const labels=[];
    if (selectedDay!=='all') labels.push(selectedDay.replace(/-/g,'.'));
    if (selectedStop) labels.push(places.get(selectedStop).name);
    document.getElementById('gallery-filter').textContent=labels.length?'当前查看：'+labels.join(' · '):'';
    document.getElementById('gallery-reset').hidden=selectedDay==='all'&&!selectedStop;
    const empty=document.querySelector('.gallery-empty');
    empty.hidden=visiblePhotos.length>0;
    empty.textContent=selectedStop?'这个地点暂无照片。':'这一天暂无照片。';
    renderMapPhotos();
  }

  function selectStop(id,pan=true) {
    if (!places.has(id)) return;
    selectedStop=id;
    document.querySelectorAll('.stop-button').forEach(button=>button.setAttribute('aria-pressed',String(button.dataset.stop===id)));
    for (const [sid,marker] of markers) {
      const place=places.get(sid);
      marker.setIcon(L.divIcon({className:'map-number'+(sid===id?' active':''),html:'<span>'+place.index+'</span>',iconSize:[27,27],iconAnchor:[13,13]}));
    }
    if (pan&&map&&markers.has(id)) {map.stop();map.setView(places.get(id).coordinates,Math.max(map.getZoom(),12),{animate:false});markers.get(id).openPopup();}
    filterGallery();
  }

  function applyDay(day,fit=true) {
    if (day!=='all'&&!trip.days.some(item=>item.date===day)) return;
    selectedDay=day;selectedStop=null;
    document.querySelectorAll('.day-controls [data-day]').forEach(button=>button.setAttribute('aria-pressed',String(button.dataset.day===day)));
    const current=trip.days.find(item=>item.date===day);
    document.getElementById('route-active-summary').textContent=current?current.date.replace(/-/g,'.')+' · '+current.title:'';
    document.getElementById('route-day-summary').textContent=current?current.summary:'点击地点，在地图上定位。';
    const panel=document.querySelector('.itinerary-panel');
    if(day==='all')panel.scrollTop=0;
    const ids=availableStops();
    document.querySelectorAll('[data-stop-row]').forEach(row=>{row.hidden=!ids.includes(row.dataset.stopRow);});
    document.querySelectorAll('.stop-button').forEach(button=>button.setAttribute('aria-pressed','false'));
    renderMap(fit);filterGallery();
  }

  const dialog=document.querySelector('.photo-dialog');
  let lightboxPhotos=[];
  let photoIndex=0;
  let previousFocus=null;
  function renderPhoto() {
    const photo=lightboxPhotos[photoIndex]; if (!photo) return;
    const img=dialog.querySelector('.lightbox-image');
    img.src=photo.large;img.alt=photo.caption;
    dialog.querySelector('.lightbox-caption').textContent=photo.caption;
    dialog.querySelector('.lightbox-meta').textContent=photo.date.replace(/-/g,'.')+' '+photo.time+' · '+(photo.locationLabel||places.get(photo.stop).name);
    document.getElementById('photo-counter').textContent=(photoIndex+1)+' / '+lightboxPhotos.length;
    dialog.querySelector('.lightbox-prev').disabled=lightboxPhotos.length<2;
    dialog.querySelector('.lightbox-next').disabled=lightboxPhotos.length<2;
  }
  function openPhoto(id) {
    lightboxPhotos=visiblePhotos.some(p=>p.id===id)?visiblePhotos.slice():trip.photos.slice();
    photoIndex=lightboxPhotos.findIndex(photo=>photo.id===id);if(photoIndex<0)return;
    previousFocus=document.activeElement;
    renderPhoto();
    if (!dialog.open) dialog.showModal();
    document.body.classList.add('photo-open');
    dialog.querySelector('.lightbox-close').focus();
  }
  function advancePhoto(delta) {if(!lightboxPhotos.length)return;photoIndex=(photoIndex+delta+lightboxPhotos.length)%lightboxPhotos.length;renderPhoto();}
  dialog.querySelector('.lightbox-close').addEventListener('click',()=>dialog.close());
  dialog.querySelector('.lightbox-prev').addEventListener('click',()=>advancePhoto(-1));
  dialog.querySelector('.lightbox-next').addEventListener('click',()=>advancePhoto(1));
  dialog.addEventListener('keydown',event=>{if(event.key==='ArrowRight'){event.preventDefault();advancePhoto(1);}if(event.key==='ArrowLeft'){event.preventDefault();advancePhoto(-1);}});
  dialog.addEventListener('click',event=>{if(event.target===dialog)dialog.close();});
  dialog.addEventListener('close',()=>{document.body.classList.remove('photo-open');if(previousFocus?.isConnected)previousFocus.focus();});

  document.addEventListener('click',event=>{
    const button=event.target.closest('button');if(!button)return;
    if(button.dataset.day){applyDay(button.dataset.day);return;}
    if(button.dataset.showGallery){applyDay(button.dataset.showGallery);scrollTo('#gallery');return;}
    if(button.id==='gallery-reset'){applyDay('all',false);return;}
    if(button.dataset.photo){openPhoto(button.dataset.photo);return;}
    if(button.dataset.galleryStop){selectStop(button.dataset.galleryStop,false);scrollTo('#gallery');return;}
    if(button.dataset.stop){
      if(button.dataset.stopDay)applyDay(button.dataset.stopDay,false);
      selectStop(button.dataset.stop);
      if(button.dataset.stopDay)scrollTo('#route');
      return;
    }
    if(button.dataset.mapAction&&map){
      if(button.dataset.mapAction==='all')applyDay('all');
      else if(button.dataset.mapAction==='photos'){
        mapPhotosVisible=!mapPhotosVisible;
        button.setAttribute('aria-pressed',String(mapPhotosVisible));
        renderMapPhotos();
      }
      else {map.stop();map.fitBounds(trip.mapFocus,{padding:[20,20],animate:false});}
    }
  });
  document.querySelectorAll('.trip-anchor-nav a').forEach(link=>link.addEventListener('click',()=>{
    if(link.hash==='#transit')document.getElementById('transit').open=true;
    if(link.hash==='#days')document.querySelector('.days-fold').open=true;
  }));
  applyDay('all');
})();
