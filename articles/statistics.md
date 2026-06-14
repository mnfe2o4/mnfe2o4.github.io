# 数理统计知识整理

> 把课程中反复出现的分布、公式和关系整理在同一页，方便复习和后续补充。

## 1. 各分布之间的联系

这里先梳理数理统计中常用到的一些分布及它们之间的转换关系。

### 1.1 Gamma 分布族

Gamma 分布 $\Gamma(\gamma, \lambda)$ 有两个重要参数：形状参数 $\gamma$ 和率参数 $\lambda$。其密度函数为：

$$
f(x; \gamma, \lambda) = \frac{\lambda^\gamma}{\Gamma(\gamma)} x^{\gamma - 1} e^{-\lambda x}
\operatorname{1}_{\{x>0\}}.
$$

其中，$\Gamma(\gamma)$ 是 Gamma 函数，定义为：

$$
\Gamma(\gamma) = \int_0^\infty t^{\gamma - 1} e^{-t} dt.
$$

Gamma 分布族包含了很多重要分布，例如：

- 当 $\gamma = 1$ 时，Gamma 分布退化为指数分布：$\Gamma(1, \lambda) = \operatorname{Exp}(\lambda)$。
- 当 $\gamma = \dfrac{n}{2}, \lambda = \dfrac{1}{2}$ 时，Gamma 分布退化为卡方分布：$\Gamma\left(\dfrac{n}{2}, \dfrac{1}{2}\right) = \chi^2_n$。

Gamma 分布的一些常见性质：

- 若 $X \sim \Gamma(\gamma, \lambda)$，则对任意常数 $c>0$，有 $cX \sim \Gamma\left(\gamma, \dfrac{\lambda}{c}\right)$。
- 若 $X_1 \sim \Gamma(\gamma_1, \lambda)$ 和 $X_2 \sim \Gamma(\gamma_2, \lambda)$ 相互独立，则 $X_1 + X_2 \sim \Gamma(\gamma_1 + \gamma_2, \lambda)$。
- 若 $X_1, X_2, \ldots, X_n \overset{\text{i.i.d.}}{\sim} \operatorname{Exp}(\lambda)$，设 $Y = \sum_{i=1}^n X_i$，则 $2\lambda Y \sim \chi^2_{2n}$。

### 1.2 正态分布族

正态分布 $N(\mu, \sigma^2)$ 由均值 $\mu$ 和方差 $\sigma^2$ 定义，其密度函数为：

$$
f(x; \mu, \sigma^2) = \frac{1}{\sqrt{2\pi \sigma^2}} e^{-\frac{(x - \mu)^2}{2\sigma^2}}.
$$

正态分布的矩生成函数和特征函数分别为：

$$
\begin{aligned}
M_X(t) &= e^{\mu t + \frac{1}{2} \sigma^2 t^2}, \\
\phi_X(t) &= e^{i \mu t - \frac{1}{2} \sigma^2 t^2}.
\end{aligned}
$$

由此可以导出正态分布的前 4 阶中心矩：

$$
\mathbb{E}[X] = \mu, \quad \operatorname{Var}(X) = \sigma^2, \quad \mathbb{E}[(X - \mu)^3] = 0, \quad \mathbb{E}[(X - \mu)^4] = 3\sigma^4.
$$

#### 1.2.1 多元正态分布

$p$ 元正态分布 $N_p(\boldsymbol{\mu}, \Sigma)$ 由均值向量 $\boldsymbol{\mu}$ 和协方差矩阵 $\Sigma$ 定义。

多元正态分布的线性变换仍是正态分布：设 $A$ 是一个 $q \times p$ 矩阵，$\boldsymbol{b}$ 是一个 $q$ 维向量，则

$$
Y = A\boldsymbol{X} + \boldsymbol{b} \sim N_q(A\boldsymbol{\mu} + \boldsymbol{b}, A\Sigma A^T).
$$

推论：

- 若 $X_1, X_2, \ldots, X_n \overset{\text{i.i.d.}}{\sim} N(\mu, \sigma^2)$，则样本均值 $\bar{X} = \frac{1}{n} \sum_{i=1}^n X_i$ 服从 $N\left(\mu, \frac{\sigma^2}{n}\right)$。
- 若 $X_1, X_2, \ldots, X_n \overset{\text{i.i.d.}}{\sim} N(\mu, \sigma^2)$，$\boldsymbol{X} = (X_1, X_2, \ldots, X_n)^T$，且 $A$ 是一个 $n \times n$ 正交阵，则 $Y = A\boldsymbol{X} \sim N_n(A\boldsymbol{\mu}, \sigma^2 I_n)$。
- 若 $\boldsymbol{X} \sim N_p(\boldsymbol{\mu}, \Sigma)$，其中 $\Sigma > 0$，则

$$
(\boldsymbol{X} - \boldsymbol{\mu})^T \Sigma^{-1} (\boldsymbol{X} - \boldsymbol{\mu}) \sim \chi^2_p.
$$

Delta 方法：设 $p$ 维随机向量序列 $\{\boldsymbol{X}_n\}$ 满足

$$
\sqrt{n}(\boldsymbol{X}_n - \boldsymbol{\mu}) \xrightarrow{d} N(\boldsymbol{0}, \Sigma),
$$

其中 $\Sigma > 0$，$\boldsymbol{\mu}$ 有限。若 $p$ 维实函数 $g$ 的梯度 $\nabla g(\boldsymbol{\mu})$ 在 $\boldsymbol{\mu}$ 处连续且不为零，则

$$
\sqrt{n}(g(\boldsymbol{X}_n) - g(\boldsymbol{\mu})) \xrightarrow{d} N\left(0, \nabla g(\boldsymbol\mu)^T \Sigma \nabla g(\boldsymbol{\mu})\right).
$$

#### 1.2.2 正态分布构造的其他分布

由正态分布可以构造出很多重要的分布：

- 设 $X_1, X_2, \ldots, X_n \overset{\text{i.i.d.}}{\sim} N(0, 1)$，则 $Y = \sum_{i=1}^n X_i^2 \sim \chi^2_n$。
- 设 $X \sim N(0, 1)$ 和 $Y \sim \chi^2_n$ 相互独立，则 $T = \dfrac{X}{\sqrt{Y/n}} \sim t_n$。
- 设 $X \sim \chi^2_m$ 和 $Y \sim \chi^2_n$ 相互独立，则 $F = \dfrac{X/m}{Y/n} \sim F_{m,n}$。

> $\chi^2$ 分布、$t$ 分布和 $F$ 分布的上侧 $\alpha$ 分位数分别记为 $\chi^2_n(\alpha)$、$t_n(\alpha)$ 和 $F_{m,n}(\alpha)$。

上述分布有以下关系：

- 设 $F \sim F_{m,n}$，则 $\dfrac{1}{F} \sim F_{n,m}$。
- 设 $T \sim t_n$，则 $T^2 \sim F_{1,n}$。
- $F_{m,n}(1 - \alpha) = \dfrac{1}{F_{n,m}(\alpha)}$。

由上述性质可以导出正态总体的统计量分布：

- 设 $X_1, X_2, \ldots, X_n \overset{\text{i.i.d.}}{\sim} N(\mu, \sigma^2)$，则样本均值 $\bar{X}$ 和样本方差 $S^2$ 相互独立，且 $\dfrac{(n-1)S^2}{\sigma^2} \sim \chi^2_{n-1}$。
- 设 $X_1, X_2, \ldots, X_n \overset{\text{i.i.d.}}{\sim} N(\mu, \sigma^2)$，则统计量 $T = \dfrac{\bar{X} - \mu}{S/\sqrt{n}} \sim t_{n-1}$。
- 设 $X_1, X_2, \ldots, X_m \overset{\text{i.i.d.}}{\sim} N(\mu_1, \sigma_1^2)$ 和 $Y_1, Y_2, \ldots, Y_n \overset{\text{i.i.d.}}{\sim} N(\mu_2, \sigma_2^2)$，且两组样本相互独立，则统计量

$$
F = \frac{S_1^2/\sigma_1^2}{S_2^2/\sigma_2^2} \sim F_{m-1,n-1}.
$$

- 设 $X_1, X_2, \ldots, X_m \overset{\text{i.i.d.}}{\sim} N(\mu_1, \sigma^2)$ 和 $Y_1, Y_2, \ldots, Y_n \overset{\text{i.i.d.}}{\sim} N(\mu_2, \sigma^2)$，且两组样本相互独立，则统计量

$$
T = \frac{(\bar{X} - \bar{Y}) - (\mu_1 - \mu_2)}{S_{\omega} \sqrt{\frac{1}{m} + \frac{1}{n}}} \sim t_{m+n-2},
$$

其中

$$
S_{\omega}^2 = \frac{(m-1)S_1^2 + (n-1)S_2^2}{m+n-2}.
$$

### 1.3 均匀分布

设 $X_1, X_2, \ldots, X_n \overset{\text{i.i.d.}}{\sim} U(\theta_1, \theta_2)$，则次序统计量 $X_{(1)}$ 和 $X_{(n)}$ 的密度函数分别为：

$$
\begin{aligned}
f_{X_{(1)}}(x) &= \frac{n}{(\theta_2 - \theta_1)^n} (\theta_2 - x)^{n-1} \operatorname{1}_{\{\theta_1 < x < \theta_2\}},\\
f_{X_{(n)}}(x) &= \frac{n}{(\theta_2 - \theta_1)^n} (x - \theta_1)^{n-1} \operatorname{1}_{\{\theta_1 < x < \theta_2\}}.
\end{aligned}
$$

对于 $\theta_1$ 和 $\theta_2$ 不同的情况，均匀分布的极小充分统计量和完全统计量如下：

| 分布 | 极小充分统计量 | 完全统计量 |
|---|---|---|
| $U(\theta_1, \theta_2)$ | $(X_{(1)}, X_{(n)})$ | 无简单完全统计量 |
| $U(\theta, \theta + 1)$ | $(X_{(1)}, X_{(n)})$ | 无简单完全统计量 |
| $U(0, \theta)$ | $X_{(n)}$ | $X_{(n)}$ |
| $U(\theta, 1)$ | $X_{(1)}$ | $X_{(1)}$ |

## 2. 点估计

### 2.1 充分统计量和完全统计量

设有样本 $X_1, X_2, \ldots, X_n \overset{\text{i.i.d.}}{\sim} f(x;\boldsymbol{\theta})$，记 $\boldsymbol{X} = (X_1, X_2, \ldots, X_n)^T$。

- 充分统计量 $T(\boldsymbol{X})$ 满足：关于 $T(\boldsymbol{X})$ 的条件分布不依赖于参数 $\boldsymbol{\theta}$。
- 极小充分统计量 $T(\boldsymbol{X})$ 满足：$T(\boldsymbol{X})$ 是 $\boldsymbol{\theta}$ 的充分统计量，且对于任意 $\boldsymbol{\theta}$ 的充分统计量 $S(\boldsymbol{X})$，存在可测函数 $g$ 使得 $T(\boldsymbol{X}) = g(S(\boldsymbol{X}))$ 几乎处处成立。
- 完全统计量 $T(\boldsymbol{X})$ 满足：对于任意可测函数 $g$，如果 $\mathbb{E}_{\boldsymbol{\theta}}[g(T(\boldsymbol{X}))] = 0$ 对所有 $\boldsymbol{\theta}$ 都成立，则 $g(T(\boldsymbol{X})) \overset{\text{a.s.}}{=} 0$ 对所有 $\boldsymbol{\theta}$ 都成立。

> 完全统计量可以理解为：统计量保留的信息足以使任何“均值恒为零”的函数只能是平凡函数。

Fisher 因子分解定理：统计量 $T(\boldsymbol{X})$ 是 $\boldsymbol{\theta}$ 的充分统计量的充要条件是存在函数 $g$ 和 $h$ 使得联合密度可以写成

$$
f(\boldsymbol{x}; \boldsymbol{\theta}) = g(T(\boldsymbol{x}); \boldsymbol{\theta}) h(\boldsymbol{x}).
$$

极小充分统计量的判别准则：若充分统计量 $T(\boldsymbol{X})$ 满足

$$
\frac{f(\boldsymbol{x};\boldsymbol{\theta})}{f(\boldsymbol{y};\boldsymbol{\theta})}\text{ 与 }\boldsymbol{\theta}\text{ 无关}
\quad\Longleftrightarrow\quad
T(\boldsymbol{x}) = T(\boldsymbol{y}),
$$

则 $T(\boldsymbol{X})$ 是 $\boldsymbol{\theta}$ 的极小充分统计量。极小充分统计量在一一变换意义下唯一。

#### 2.1.1 指数族的充分完全统计量

指数族：如果密度函数可以表示为

$$
f(x; \boldsymbol{\theta}) = C(\boldsymbol{\theta}) \exp\left\{\boldsymbol{Q}(\boldsymbol{\theta})^T T(x)\right\} h(x),
$$

则称 $f(x; \boldsymbol{\theta})$ 属于 $\boldsymbol{\theta}$ 的指数族。

指数族的自然形式：如果密度函数可以表示为

$$
f(x; \boldsymbol{\eta}) = C(\boldsymbol{\eta}) \exp\left\{\boldsymbol{\eta}^T T(x)\right\} h(x),
$$

则称该指数族写成了自然形式，其中 $\boldsymbol{\eta}$ 称为自然参数。

满秩：对于指数族的自然形式，若自然参数空间有内点，则称该指数族是满秩的。

指数族的极小充分统计量：设 $X_1, X_2, \ldots, X_n \overset{\text{i.i.d.}}{\sim} f(x; \boldsymbol{\theta})$，且 $f(x; \boldsymbol{\theta})$ 属于指数族，则

$$
\sum_{i=1}^n T(X_i)
$$

通常是 $\boldsymbol{\theta}$ 的极小充分统计量。

指数族的完全统计量：若分布族是满秩自然指数族，则

$$
\sum_{i=1}^n T(X_i)
$$

通常是 $\boldsymbol{\theta}$ 的完全统计量。

### 2.2 UMVUE

Rao-Blackwell 定理：设 $T=T(\boldsymbol{X})$ 是一个充分统计量，$\hat{g}(\boldsymbol{X})$ 是参数 $g(\boldsymbol{\theta})$ 的一个无偏估计，则

$$
h(T) = \mathbb{E}_{\boldsymbol{\theta}}[\hat{g}(\boldsymbol{X})\mid T]
$$

也是 $g(\boldsymbol{\theta})$ 的一个无偏估计，并且

$$
\operatorname{Var}_{\boldsymbol{\theta}}(h(T)) \leq \operatorname{Var}_{\boldsymbol{\theta}}(\hat{g}(\boldsymbol{X})).
$$

Lehmann-Scheffé 定理：设 $T=T(\boldsymbol{X})$ 是一个充分完全统计量，$\hat{g}(T)$ 是参数 $g(\boldsymbol{\theta})$ 的一个无偏估计，则 $\hat{g}(T)$ 是 $g(\boldsymbol{\theta})$ 唯一的 UMVUE。

> 求 UMVUE 的步骤：先找到一个无偏估计 $\hat{g}(\boldsymbol{X})$，再找到一个充分完全统计量 $T(\boldsymbol{X})$，最后计算 $h(T) = \mathbb{E}[\hat{g}(\boldsymbol{X})\mid T]$。

### 2.3 得分函数与 Fisher 信息阵

设样本联合密度为 $f(\boldsymbol{x}; \boldsymbol{\theta})$，似然函数为

$$
L(\boldsymbol{\theta};\boldsymbol{x})=f(\boldsymbol{x};\boldsymbol{\theta}),
$$

对数似然函数统一记为

$$
\ell_n(\boldsymbol{\theta}) = \log L(\boldsymbol{\theta};\boldsymbol{x}).
$$

样本得分函数定义为

$$
S_n(\boldsymbol{\theta}) = \nabla \ell_n(\boldsymbol{\theta}).
$$

Fisher 信息阵定义为

$$
I_n(\boldsymbol{\theta}) = \mathbb{E}_{\boldsymbol{\theta}}[S_n(\boldsymbol{\theta})S_n(\boldsymbol{\theta})^T].
$$

在一定正则条件下，Fisher 信息阵也可以表示为

$$
I_n(\boldsymbol{\theta}) = -\mathbb{E}_{\boldsymbol{\theta}}\left[\nabla^2 \ell_n(\boldsymbol{\theta})\right].
$$

若 $I(\boldsymbol{\theta})$ 表示单个观测对应的 Fisher 信息阵，则

$$
I_n(\boldsymbol{\theta}) = n I(\boldsymbol{\theta}).
$$

### 2.4 Cramér-Rao 不等式

设 $X_1, X_2, \ldots, X_n \overset{\text{i.i.d.}}{\sim} f(x; \boldsymbol{\theta})$，且满足一定正则条件，则对于任何 $g(\boldsymbol{\theta})$ 的无偏估计 $\hat{g}(\boldsymbol{X})$，都有

$$
\operatorname{Var}_{\boldsymbol{\theta}}(\hat{g}(\boldsymbol{X})) \geq \nabla g(\boldsymbol{\theta})^T I_n(\boldsymbol{\theta})^{-1} \nabla g(\boldsymbol{\theta}).
$$

特别地，对于一元参数情形，

$$
\operatorname{Var}_{\theta}(\hat{g}(\boldsymbol{X})) \geq \frac{[g'(\theta)]^2}{I_n(\theta)}.
$$

### 2.5 MLE 的渐近正态性

设 $\hat{\boldsymbol{\theta}}_n$ 是 $\boldsymbol{\theta}$ 的 MLE。在一定正则条件下，

$$
\sqrt{n}(\hat{\boldsymbol{\theta}}_n - \boldsymbol{\theta}) \xrightarrow{d} N(\boldsymbol{0}, I(\boldsymbol{\theta})^{-1}),
$$

其中 $I(\boldsymbol{\theta})$ 是单个观测对应的 Fisher 信息阵。若使用样本 Fisher 信息阵 $I_n(\boldsymbol{\theta})$，则等价地有

$$
\hat{\boldsymbol{\theta}}_n \approx N\left(\boldsymbol{\theta}, I_n(\boldsymbol{\theta})^{-1}\right).
$$

## 3. 区间估计

### 3.1 基本概念

设 $[\hat{\theta}_1, \hat{\theta}_2]$ 是参数 $\theta$ 的一个区间估计。区间估计通常有两个要素：

- 可靠度：区间包含真参数的概率，通常用置信水平或置信度衡量。
- 精度：区间长度 $\hat{\theta}_2 - \hat{\theta}_1$，区间越短，精度越高。

若对给定的 $0<\alpha<1$，有 $\mathbb{P}_\theta(\hat{\theta}_1 \leq \theta \leq \hat{\theta}_2) \geq 1-\alpha,\ \forall \theta\in\Theta$，则称 $[\hat{\theta}_1, \hat{\theta}_2]$ 是 $\theta$ 的置信水平为 $1-\alpha$ 的置信区间。其置信系数为 $\inf_{\theta\in\Theta}\mathbb{P}_\theta(\hat{\theta}_1 \leq \theta \leq \hat{\theta}_2)$。

若只关心参数的上界或下界，也可以构造置信上限或置信下限。若参数是多维的，则相应的区间估计推广为置信域或置信集。

Neyman 方法：在保证一定置信水平的前提下，使区间尽可能短。

### 3.2 枢轴量法

枢轴量 $Q(X,\theta)$ 是关于样本 $X$ 和待估参数 $\theta$ 的函数，满足：

- $Q(X,\theta)$ 的表达式与 $\theta$ 有关；
- $Q(X,\theta)$ 的分布与 $\theta$ 无关。

枢轴量法构造置信区间的一般步骤为：

1. 找到一个与参数 $\theta$ 有关、但分布不依赖于 $\theta$ 的枢轴量 $Q(X,\theta)$；
2. 取常数 $a,b$ 使得 $\mathbb{P}_\theta(a \leq Q(X,\theta) \leq b)=1-\alpha$；
3. 对不等式 $a \leq Q(X,\theta) \leq b$ 反解 $\theta$，得到置信区间。

从而可以构造置信水平为 $1-\alpha$ 的置信域 $C(X)=\{\theta\in\Theta: a\le Q(X,\theta)\le b\}$。

### 3.3 大样本方法

当精确枢轴量难以构造时，可以用渐近分布构造近似置信区间。

#### 3.3.1 基于 MLE 的渐近正态性

设 $\hat{\theta}_n$ 是 $\theta$ 的 MLE。在一定正则条件下，$\sqrt n(\hat\theta_n-\theta)\xrightarrow{d}N(0,I(\theta)^{-1})$，其中 $I(\theta)$ 是单个观测对应的 Fisher 信息量。由 Slutsky 定理，$\sqrt{nI(\hat\theta_n)}(\hat\theta_n-\theta)\xrightarrow{d}N(0,1)$。

因此可得置信水平近似为 $1-\alpha$ 的置信区间

$$
\left[
\hat\theta_n - \frac{u_{\alpha/2}}{\sqrt{nI(\hat\theta_n)}},
\hat\theta_n + \frac{u_{\alpha/2}}{\sqrt{nI(\hat\theta_n)}}
\right].
$$

#### 3.3.2 比率 $p$ 的置信区间

对于 $X_1,\ldots,X_n\overset{\text{i.i.d.}}{\sim}\operatorname{Bernoulli}(p)$，由中心极限定理，$\dfrac{\sqrt n(\bar X-p)}{\sqrt{p(1-p)}}\xrightarrow{d}N(0,1)$。由 Slutsky 定理，用 $\bar X$ 代替 $p$，有 $\dfrac{\sqrt n(\bar X-p)}{\sqrt{\bar X(1-\bar X)}}\xrightarrow{d}N(0,1)$。

因此 $p$ 的置信水平近似为 $1-\alpha$ 的置信区间为

$$
\left[
\bar X-u_{\alpha/2}\sqrt{\frac{\bar X(1-\bar X)}{n}},
\bar X+u_{\alpha/2}\sqrt{\frac{\bar X(1-\bar X)}{n}}
\right].
$$

#### 3.3.3 一般 CLT 方法

若 $X_1,\ldots,X_n\overset{\text{i.i.d.}}{\sim}F$，均值为 $\mu_F$，方差为 $\sigma_F^2$，则由中心极限定理，$\sqrt n(\bar X-\mu_F)/\sigma_F\xrightarrow{d}N(0,1)$。若 $\sigma_F$ 未知，可用样本标准差 $S$ 代替，得到 $\sqrt n(\bar X-\mu_F)/S\xrightarrow{d}N(0,1)$。

于是 $\mu_F$ 的置信水平近似为 $1-\alpha$ 的置信区间为 $[\bar X-Su_{\alpha/2}/\sqrt n,\ \bar X+Su_{\alpha/2}/\sqrt n]$。

#### 3.3.4 自助法

自助法：在初始样本中有放回地抽取辅助样本，并对每个辅助样本计算估计量 $\hat\theta$。重复足够多次后，用 $\hat\theta$ 的辅助样本经验分布近似 $\hat\theta$ 的抽样分布。

> 自助法通常用于枢轴量分布不易求得或样本量较小不足以使用大样本方法的场景。

## 4. Bayes 统计

### 4.1 先验分布与后验分布

Bayes 方法把参数 $\theta$ 看作随机变量。在抽样前，对 $\theta$ 的认识由先验分布描述，记为 $\pi(\theta)$。获得样本 $x$ 后，通过 Bayes 公式得到后验分布。

若样本密度为 $f(x\mid\theta)$，先验密度为 $\pi(\theta)$，则后验密度为 $\pi(\theta\mid x)=\dfrac{f(x\mid\theta)\pi(\theta)}{\int_\Theta f(x\mid\theta)\pi(\theta)\,d\theta}$。Bayes 推断通常基于后验分布进行。

### 4.2 Bayes 可信区间

给定后验分布 $\pi(\theta\mid x)$ 和 $0<\alpha<1$。若区间 $[\hat\theta_1,\hat\theta_2]$ 满足 $\mathbb{P}(\hat\theta_1\le \theta\le \hat\theta_2\mid x)\ge 1-\alpha$，则称 $[\hat\theta_1,\hat\theta_2]$ 为 $\theta$ 的可信水平为 $1-\alpha$ 的 Bayes 可信区间。

### 4.3 HPD 可信集

为了在给定可信水平下提高精度，可以考虑最大后验密度可信集，即 HPD 可信集。

若集合 $C(x)$ 满足 $\mathbb{P}(\theta\in C(x)\mid x)=1-\alpha$，且对于任意 $\theta_1\in C(x)$、$\theta_2\notin C(x)$，有 $\pi(\theta_1\mid x)\ge \pi(\theta_2\mid x)$，则称 $C(x)$ 为可信水平 $1-\alpha$ 的 HPD 可信集。

## 5. 假设检验

### 5.1 基本概念

#### 5.1.1 检验问题、拒绝域与检验函数

设有参数分布族 $\{f(x;\theta):\theta\in\Theta\}$，样本 $X_1,\ldots,X_n\overset{\text{i.i.d.}}{\sim} f(x;\theta)$。假设检验问题通常写为 $H_0:\theta\in\Theta_0\quad\text{vs.}\quad H_1:\theta\in\Theta_1=\Theta\setminus\Theta_0$。

其中 $H_0$ 称为原假设或零假设，$H_1$ 称为备择假设或对立假设。若 $\Theta_i$ 只包含一个参数值，则称为简单假设；否则称为复合假设。

拒绝域 $D\subset\mathscr X$ 表示拒绝 $H_0$ 的样本点集合，接受域为 $\bar D=\mathscr X\setminus D$。

检验函数： $\varphi(x):\mathscr X\to[0,1]$，其中 $\varphi(x)$ 表示给定样本 $x$ 后拒绝 $H_0$ 的概率。若 $\varphi(x)$ 只取 $0$ 和 $1$，则为非随机化检验；若某些样本点上 $0<\varphi(x)<1$，则为随机化检验。

#### 5.1.2 两类错误、功效函数与显著性水平

功效函数定义为 $\beta_\varphi(\theta)=\mathbb{E}_\theta[\varphi(X)]=\mathbb{P}_{\theta}(\text{用检验拒绝了} H_0)$。

**第一类错误**： $H_0$ 为真时拒绝 $H_0$，其概率可写为 $\alpha^*_\varphi(\theta)=\beta_\varphi(\theta)\operatorname{1}_{\Theta_0}(\theta)$；

**第二类错误**： $H_1$ 为真时接受 $H_0$，其概率可写为 $\gamma^*_\varphi(\theta)=(1-\beta_\varphi(\theta))\operatorname{1}_{\Theta_1}(\theta)$。

显著性水平：对 $0\le\alpha\le1$，若 $\sup_{\theta\in\Theta_0}\beta_\varphi(\theta)\le\alpha$，则称 $\varphi$ 为显著性水平为 $\alpha$ 的检验。Neyman-Pearson 准则的核心思想是：在控制第一类错误概率的原则下，使第二类错误概率尽可能小，也就是使功效尽可能大。

#### 5.1.3 假设检验与区间估计的对偶关系

- 若 $A(\theta')$ 是检验问题 $H_0:\theta=\theta'$ 的接受域，且该检验的显著性水平为 $\alpha$，则 $\mathcal C(x)=\{\theta':x\in A(\theta')\}$ 是一个置信水平为 $1-\alpha$ 的置信域。
- 若 $\mathcal C(x)$ 是待估参数 $\theta$ 的置信水平为 $1 - \alpha$ 的一个置信集，则 $A(\theta') = \{x:\theta' \in \mathcal C(x)\}$ 是关于检验问题 $H_0:\theta=\theta'$ 显著性水平为 $\alpha$ 的接受域。

#### 5.1.4 p 值

对于一族水平为 $\alpha$ 的检验 $\varphi_\alpha$，观测到样本 $x$ 后，p 值定义为使该样本刚好能够拒绝原假设的最小显著性水平 $\hat p=\inf\{\alpha\in(0,1):\varphi_\alpha(x)=1\}$。

当检验统计量取值越大越反对 $H_0$ 时，p 值通常可写为 $\hat p=\mathbb{P}\{T(X)\ge T(x)\mid H_0\}$。

给定显著性水平 $\alpha$ 时，若 $\hat p<\alpha$，则拒绝 $H_0$。

若检验统计量在 $H_0$ 下服从连续分布，则在 $H_0$ 下 p 值服从 $U(0,1)$。也就是说，对 $0\le q\le 1$，有 $\mathbb{P}_0(\hat p\le q)=q$。

### 5.2 似然比检验

#### 5.2.1 似然比统计量与拒绝域

对假设 $H_0:\theta\in\Theta_0\quad\text{vs.}\quad H_1:\theta\in\Theta_1$，将 $f(x;\theta)$ 看作 $\theta$ 的函数，即似然函数。记 $L_A(x)=\sup_{\theta\in A}f(x;\theta),\ A\subseteq \Theta$。
似然比统计量记为 $\lambda(x)=L_\Theta(x)/L_{\Theta_0}(x)$。因此 $\lambda(x)$ 越大，越倾向于拒绝 $H_0$。似然比检验函数可写为

$$
\varphi(x)=
\begin{cases}
1,&\lambda(x)>c,\\
r,&\lambda(x)=c,\\
0,&\lambda(x)<c,
\end{cases}
$$

其中 $c,r$ 由检验的显著性水平决定。若样本分布为连续型，通常可取 $r=0$。

>若 $\lambda(x)$ 是统计量 $T(x)$ 的单调函数，则似然比检验可以等价地写成关于 $T(x)$ 的检验。

>若 $\hat\theta_\Theta$ 是 $\Theta$ 上的 MLE，则 $\hat\theta_\Theta=\arg\max_{\theta\in\Theta} f(x;\theta)$，且 $L_\Theta(x)=f(x;\hat\theta_\Theta)$。类似地也有 $L_{\Theta_0}(x)=f(x;\hat\theta_{\Theta_0})$

#### 5.2.2 大样本分布

在一定正则条件下，若 $\dim(\Theta)>\dim(\Theta_0)$，记 $d=\dim(\Theta)-\dim(\Theta_0)$，则在 $H_0$ 下有 $2\log\lambda(X)\xrightarrow{d}\chi_d^2$。

#### 5.2.3 Wald 检验

考虑约束检验 $H_0:h(\theta)=0\quad\text{vs.}\quad H_1:h(\theta)\ne0$，其中 $h:\mathbb R^k\to\mathbb R^r$。记 Jacobi 矩阵为 $J(\theta)=\partial h(\theta)/\partial\theta$。

设 $\hat\theta_n$ 是 $\Theta$ 上的 MLE，$I(\theta)$ 是单个观测对应的 Fisher 信息矩阵。在一定正则条件下，Wald 统计量为

$$
W_n=n h(\hat\theta_n)^T
\left[J(\hat\theta_n)I(\hat\theta_n)^{-1}J(\hat\theta_n)^T\right]^{-1}
h(\hat\theta_n)
\xrightarrow{d}\chi_r^2.
$$

> Wald 检验的思想是：如果 $H_0$ 成立，则 $h(\theta)=0$，因而 $h(\hat\theta_n)$ 不应离 $0$ 太远。

#### 5.2.4 得分检验

设 $\ell_n(\theta)$ 为对数似然函数，$\nabla\ell_n(\theta)$ 为得分函数，记 $U_n(\theta)=n^{-1/2}\nabla\ell_n(\theta)$。设 $\hat\theta_n^R$ 为 $H_0$ 约束下的 MLE，$I(\theta)$ 为单个观测对应的 Fisher 信息矩阵。在一定正则条件下，得分检验统计量为

$$
S_n=U_n(\hat\theta_n^R)^T I(\hat\theta_n^R)^{-1}U_n(\hat\theta_n^R)
\xrightarrow{d}\chi_d^2,
$$

其中 $d=\dim(\Theta)-\dim(\Theta_0)$。

> 得分检验的思想是：若 $H_0$ 成立，则在约束 MLE 附近，非约束方向上的得分不应过大。

### 5.3 UMPT

#### 5.3.1 一致最大功效检验

一致最大功效检验（UMPT）：若 $\varphi^*$ 是显著性水平为 $\alpha$ 的检验，并且对于所有 $\theta\in\Theta_1$ 和所有显著性水平为 $\alpha$ 的检验 $\varphi$，都有 $\beta_{\varphi^*}(\theta)\ge\beta_\varphi(\theta)$，则称 $\varphi^*$ 为一致最大功效检验。

#### 5.3.2 Neyman-Pearson 引理

Neyman-Pearson 引理处理简单假设检验 $H_0:f(x)=f_0(x)\quad\text{vs.}\quad H_1:f(x)=f_1(x)$。存在显著性水平为 $\alpha$ 的 UMPT，其检验函数为

$$
\varphi^*(x)=
\begin{cases}
1,& f_1(x)>c f_0(x),\\
\gamma,& f_1(x)=c f_0(x),\\
0,& f_1(x)<c f_0(x),
\end{cases}
$$

其中 $c\ge0$、$\gamma\in[0,1]$ 由 $\mathbb{E}_0[\varphi^*(X)]=\alpha$ 确定。当样本分布为连续型时，通常可取 $\gamma=0$。

#### 5.3.3 单调似然比检验

若分布族 $\{f(x;\theta):\theta\in\Theta\}$ 满足：对于任意 $\theta_1<\theta_2$，存在统计量 $T(x)$，使得 $f(x;\theta_2)/f(x;\theta_1)$ 是 $T(x)$ 的单调非减函数，则称该分布族关于 $T(x)$ 具有单调似然比性质。

对单侧检验 $H_0:\theta\le\theta_0\quad\text{vs.}\quad H_1:\theta>\theta_0$，在单调似然比条件下，存在显著性水平为 $\alpha$ 的 UMPT，其形式为

$$
\varphi(x)=
\begin{cases}
1,&T(x)>c,\\
\gamma,&T(x)=c,\\
0,&T(x)<c,
\end{cases}
$$

其中 $c,\gamma$ 由 $\mathbb{E}_{\theta_0}[\varphi(X)]=\alpha$ 决定。

### 5.4 多重假设检验

当同时检验 $H_1,\ldots,H_s$ 时，如果逐个用水平 $\alpha$ 的检验，每一个单独检验的第一类错误概率仍受控制，但“至少犯一次第一类错误”的概率会随着检验个数增大而迅速上升。

多重检验中至少犯一次第一类错误的概率称为族错误率（family-wise error rate），记为 $\mathrm{FWER}=\mathbb{P}(\text{至少有一个真原假设被错误拒绝})$。

#### 5.4.1 Bonferroni 过程

设 $\hat p_i$ 是第 $i$ 个假设 $H_i$ 的 p 值。Bonferroni 过程为：

1. 对 $i=1,\ldots,s$，分别计算每个检验的 p 值 $\hat p_i$。
2. 若 $\hat p_i\le \frac{\alpha}{s}$，则拒绝 $H_i$。

若每个真原假设下都有 $\mathbb{P}(\hat p_i\le x)\le x$，则由 Bonferroni 不等式可得 $\mathrm{FWER}\le \alpha$。

> 但当 $s$ 很大时，控制 FWER 往往会过于严格。

#### 5.4.2 Benjamini-Hochberg（BH）过程

为降低 Bonferroni 过程的保守性，可以考虑错误发现率（false discovery rate, FDR）。

令 $N$ 为总拒绝数，$F$ 为错误拒绝数，并定义

$$
Q=
\begin{cases}
\frac{F}{N}, & N>0,\\
0, & N=0.
\end{cases}
$$

错误发现率定义为 $\mathrm{FDR}=\mathbb{E}[Q]$。

Benjamini-Hochberg 过程如下：

1. 将 $s$ 个 p 值从小到大排序为 $\hat p_{(1)}\le \hat p_{(2)}\le\cdots\le \hat p_{(s)}$，并记其对应的假设为 $H_{(1)},\ldots,H_{(s)}$。
2. 给定 FDR 水平 $\alpha$，找到最大的 $k$，使得 $\hat p_{(k)}\le \frac{k}{s}\alpha$。
3. 拒绝 $H_{(1)},\ldots,H_{(k)}$。

若真实原假设对应的 p 值相互独立，或满足适当的正回归依赖条件，则 Benjamini-Hochberg 过程控制 FDR。在相互独立且真实原假设的 p 值满足有效性条件 $\mathbb{P}(\hat p_i\le x)\le x$ 时，若真实原假设个数为 $s_0$，则

$$
\mathrm{FDR}\le \frac{s_0}{s}\alpha\le\alpha.
$$

## 6. 非参数假设检验

实际中常遇到总体分布形式未知，或不希望对总体分布作过强假定的检验问题。这类检验通常称为非参数假设检验。

本章整理几种常用的非参数检验方法。

### 6.1 符号检验

#### 6.1.1 符号检验

考虑成对样本的比较问题。例如，每个样本单位都有两个相关观测值 $X_i^{(1)}$ 和 $X_i^{(2)}$。令 $D_i=X_i^{(1)}-X_i^{(2)}$。

若要检验两种处理是否没有差异，可以检验正、负差值出现的概率是否相同；当差值分布连续时，这等价于检验其中位数是否为 $0$。

设差值相互独立，去掉 $D_i=0$ 的观测后，还剩 $n$ 个非零差值。记 $n_+=\#\{i:D_i>0\}$，$n_-=\#\{i:D_i<0\}$，令 $n=n_++n_-$，并记 $\pi=\mathbb{P}(D_i>0\mid D_i\ne0)$。

在原假设 $H_0:\pi=\frac12$ 下，正号和负号出现的概率相同，因此 $n_+\sim\operatorname{Bin}\left(n,\frac12\right)$。

若备择假设为双侧，即

$$
H_0:\pi=\frac12
\quad\text{vs.}\quad
H_1:\pi\ne\frac12,
$$

则拒绝域可写为 $\{n_+\ge c\}\cup\{n_+\le d\}$。

常取 $d=n-c$，并令

$$
\sum_{j=c}^n {n\choose j}\left(\frac12\right)^n\le \frac{\alpha}{2}
$$

来确定临界值。

也可以使用 p 值。令 $x_0=\min(n_+,n_-)$，则双侧 p 值为

$$
\hat p=
\sum_{j=0}^{x_0}{n\choose j}\left(\frac12\right)^n
+
\sum_{j=n-x_0}^{n}{n\choose j}\left(\frac12\right)^n.
$$

大样本时，由中心极限定理，

$$
\frac{n_+-\frac n2}{\sqrt{\frac n4}}
=
\frac{2n_+-n}{\sqrt n}
\xrightarrow{d}N(0,1).
$$

#### 6.1.2 Wilcoxon 符号秩和检验

符号检验只利用了差值的符号，没有利用差值绝对值的大小。若样本来自关于 $0$ 对称的连续分布，可以进一步使用 Wilcoxon 符号秩和检验。

对 Wilcoxon 符号秩和检验，令 $S_i=\operatorname{sgn}(X_i)$，并令 $R_i^+$ 为 $|X_i|$ 在 $|X_1|,\ldots,|X_n|$ 中的秩。

定义符号秩和统计量 $T_n=\sum_{i=1}^n S_iR_i^+$。等价地，也可使用正秩和统计量 $T_n^+=\sum_{i=1}^n \operatorname{1}_{(0,\infty)}(X_i)R_i^+$。

在 $H_0$ 成立且分布关于 $0$ 连续对称时，符号向量 $(S_1,\ldots,S_n)$、绝对值秩 $(R_1^+,\ldots,R_n^+)$ 与绝对值次序统计量 $(|X|_{(1)},\ldots,|X|_{(n)})$ 相互独立，并且每个符号取正、负的概率相同。

因此，在 $H_0$ 下，

$$
\mathbb{E}[T_n]=0,
\qquad
\operatorname{Var}(T_n)=\frac{n(n+1)(2n+1)}{6}.
$$

大样本时，$\frac{T_n}{\sqrt{\operatorname{Var}(T_n)}}\xrightarrow{d}N(0,1)$。

#### 6.1.3 Wilcoxon 两样本秩和检验

Wilcoxon 两样本秩和检验用于比较两个总体的位置差异。

设

$$
X_1,\ldots,X_m\overset{\text{i.i.d.}}{\sim}F(x),
\qquad
Y_1,\ldots,Y_n\overset{\text{i.i.d.}}{\sim}F(x-\theta).
$$

考虑检验

$$
H_0:\theta=0
\quad\text{vs.}\quad
H_1:\theta\ne0.
$$

将 $X_1,\ldots,X_m,Y_1,\ldots,Y_n$ 混合后从小到大排序为 $Z_1,\ldots,Z_N$，其中 $N=m+n$。

若 $Y_i=Z_{R_i}$，则称 $R_i$ 为 $Y_i$ 在混合样本中的秩。定义秩和统计量 $W=R_1+\cdots+R_n$。

在 $H_0$ 下，两组样本同分布，$Y$ 样本所占的 $n$ 个秩在 $1,\ldots,N$ 中等可能。也就是说，任意 $1\le r_1<\cdots<r_n\le N$，都有

$$
\mathbb{P}\bigl(\{R_1,\ldots,R_n\}=\{r_1,\ldots,r_n\}\bigr)
=\frac{1}{\binom Nn}.
$$

因此可以由秩和的精确分布求检验临界值。

大样本时，在 $H_0$ 成立下有

$$
\mathbb{E}[W]=\frac{n(N+1)}{2},
\qquad
\operatorname{Var}(W)=\frac{mn(N+1)}{12},
$$

并且

$$
\frac{W-\mathbb{E}[W]}{\sqrt{\operatorname{Var}(W)}}\xrightarrow{d}N(0,1).
$$

### 6.2 拟合优度检验

拟合优度检验用于检验总体分布是否为给定的理论分布 $F$。

基本思想是构造一个反映样本分布与理论分布偏离程度的统计量 $D$。若观测到的偏离值为 $d_0$，则定义拟合优度为 $p(d_0)=\mathbb{P}(D\ge d_0\mid H_0)$。

$p(d_0)$ 越大，表示样本与理论分布拟合得越好；$p(d_0)$ 越小，越倾向于拒绝 $H_0$。

#### 6.2.1 Pearson $\chi^2$ 检验

**1. 离散型总体且只取有限个值**

设理论分布为

$$
\mathbb{P}:
\begin{pmatrix}
a_1 & a_2 & \cdots & a_r\\
p_1 & p_2 & \cdots & p_r
\end{pmatrix},
\qquad
\sum_{i=1}^r p_i=1.
$$

检验问题为 $H_0:\mathbb{P}(X=a_i)=p_i$，其中 $i=1,\ldots,r$。

设样本 $X_1,\ldots,X_n$ 中取值为 $a_i$ 的个数为 $\nu_i$，称为观察频数。$np_i$ 称为理论频数。

Pearson $\chi^2$ 统计量为 

$$
K_n=\sum_{i=1}^r\frac{(\nu_i-np_i)^2}{np_i}.
$$

在 $H_0$ 下，当 $n\to\infty$ 时，$K_n\xrightarrow{d}\chi^2_{r-1}$。

因此，当 $K_n>\chi^2_{r-1}(\alpha)$ 时拒绝 $H_0$。若观测值为 $k_0$，则拟合优度近似为 $p(k_0)\approx\mathbb{P}(\chi^2_{r-1}\ge k_0)$。

**2. 连续型总体或取可列个值的离散型总体**

这时可以先分组，再化为有限离散情形。步骤为：

1. 将样本空间分成 $r$ 个互不相交的子域 $I_1,\ldots,I_r$。
2. 计算在 $H_0$ 下各子域的概率 $p_j=\mathbb{P}(X\in I_j)$，其中 $j=1,\ldots,r$。

3. 统计各子域中的观察频数 $\nu_j$，再使用有限离散情形下的 Pearson $\chi^2$ 检验。

分组应在观察样本之前确定。各组理论频数和观察频数都不宜过小，必要时可合并相邻区间。

**3. 理论分布含未知参数**

若理论分布为 $F(x;\theta)$，其中 $\theta=(\theta_1,\ldots,\theta_s)$ 含 $s$ 个未知参数，则先用 MLE 得到 $\hat\theta$，再计算 $\hat p_j=\mathbb{P}_{\hat\theta}(X\in I_j)$。

此时使用统计量 $K_n^*=\sum_{j=1}^r\frac{(\nu_j-n\hat p_j)^2}{n\hat p_j}$。

由 R.A. Fisher 定理，在 $H_0$ 成立且满足正则条件时，有 $K_n^*\xrightarrow{d}\chi^2_{r-s-1}$。

#### 6.2.2 独立性检验

独立性检验可看作拟合优度检验在列联表中的应用。

设总体中每个个体都有两种属性 $A$ 和 $B$。属性 $A$ 有 $r$ 个水平 $A_1,\ldots,A_r$，属性 $B$ 有 $s$ 个水平 $B_1,\ldots,B_s$。

第 $k$ 个个体的观测结果记为 $X_k=(X_k^{(1)},X_k^{(2)})$，于是可以形成 $r\times s$ 列联表。

| $X^{(1)}\backslash X^{(2)}$ | $1$ | $\cdots$ | $j$ | $\cdots$ | $s$ | 行和 |
|---|---:|---:|---:|---:|---:|---:|
| $1$ | $n_{11}$ | $\cdots$ | $n_{1j}$ | $\cdots$ | $n_{1s}$ | $n_{1\cdot}$ |
| $\vdots$ | $\vdots$ |  | $\vdots$ |  | $\vdots$ | $\vdots$ |
| $i$ | $n_{i1}$ | $\cdots$ | $n_{ij}$ | $\cdots$ | $n_{is}$ | $n_{i\cdot}$ |
| $\vdots$ | $\vdots$ |  | $\vdots$ |  | $\vdots$ | $\vdots$ |
| $r$ | $n_{r1}$ | $\cdots$ | $n_{rj}$ | $\cdots$ | $n_{rs}$ | $n_{r\cdot}$ |
| 列和 | $n_{\cdot1}$ | $\cdots$ | $n_{\cdot j}$ | $\cdots$ | $n_{\cdot s}$ | $n$ |

其中

$$
n_{i\cdot}=\sum_{j=1}^s n_{ij},
\qquad
n_{\cdot j}=\sum_{i=1}^r n_{ij}.
$$

设总体中落到 $(A_i,B_j)$ 的概率为 $p_{ij}$。若 $A$ 与 $B$ 独立，则 $\mathbb{P}(X^{(1)}=i,X^{(2)}=j)=p_{i\cdot}p_{\cdot j}$，其中 $p_{i\cdot} = \sum_j p_{ij}$，$p_{\cdot j} = \sum_i p_{ij}$。

因此检验问题为

$$
H_0:p_{ij}=p_{i\cdot}p_{\cdot j},
\qquad i=1,\ldots,r,
\quad j=1,\ldots,s.
$$

这就转化为了拟合优度检验。由 MLE 得

$$
\hat p_{i\cdot}=\frac{n_{i\cdot}}{n},
\qquad
\hat p_{\cdot j}=\frac{n_{\cdot j}}{n}.
$$

所以理论频数为

$$
n\hat p_{i\cdot}\hat p_{\cdot j}
=\frac{n_{i\cdot}n_{\cdot j}}{n}.
$$

独立性检验统计量为

$$
K_n^*
=\sum_{i=1}^r\sum_{j=1}^s
\frac{(n_{ij}-n\hat p_{i\cdot}\hat p_{\cdot j})^2}
{n\hat p_{i\cdot}\hat p_{\cdot j}}
=
n\sum_{i=1}^r\sum_{j=1}^s
\frac{\left(n_{ij}-\frac{n_{i\cdot}n_{\cdot j}}{n}\right)^2}
{n_{i\cdot}n_{\cdot j}}.
$$

由 R.A. Fisher 定理，在 $H_0$ 成立且满足正则条件时，$K_n^*\xrightarrow{d}\chi^2_{(r-1)(s-1)}$。

因此若观测值为 $k_0^*$，可用 $p(k_0^*)\approx\mathbb{P}\left(\chi^2_{(r-1)(s-1)}\ge k_0^*\right)$ 作出检验结论。

#### 6.2.3 其他方法

设来自于分布函数 $F$ 样本 $X_1, X_2, \ldots, X_n$ 的经验分布函数
$$
F_n(x) = \frac{1}{n} \sum_{i=1}^n \operatorname{1}_{\{X_i < x\}}
$$

则有性质：

- $F_n(x)$ 是 $F(x)$ 的一致相合估计，即 $F_n \xrightarrow{L^{\infty}} F$；
- $\operatorname{MSE}(F_n(x)) = O(n^{-1})$；
- $\sqrt{n} (F_n(x) - F(x)) \xrightarrow{d} N(0, F(x)(1 - F(x)))$。

考虑检验问题
$$
H_0:F=F_0
\quad\longleftrightarrow\quad
H_1:F\ne F_0.
$$

该问题有三种著名检验统计量：

- Kolmogorov-Smirnov 检验： 
$$
D_n = \sqrt{n} \|F_n - F_0\|_{L^{\infty}}
$$
- Cramér-von Mises 检验：
$$
C_n = n \int (F_n(x) - F_0(x))^2 dF_0(x)
$$
- Anderson-Darling 检验： 
$$
A_n = n \int \dfrac{(F_n(x) - F_0(x))^2}{F_0(x)(1-F_0(x))} dF_0(x)
$$
