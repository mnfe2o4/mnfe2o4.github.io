# 寿险精算数学复习笔记

## 0. 通用符号

寿险精算的核心是把未来随机现金流折现到签单时点，然后取期望。

常用利息符号：

\[
v=\frac{1}{1+i},\qquad d=\frac{i}{1+i}=1-v,\qquad \delta=\ln(1+i),\qquad v^t=e^{-\delta t}.
\]

寿命与未来寿命：

\[
X=\text{新生个体寿命},\qquad T(x)=X-x\mid X>x.
\]

其中 \(T(x)\) 是 \((x)\) 的未来寿命。其整值部分和小数部分记为

\[
K(x)=\lfloor T(x)\rfloor,\qquad S(x)=T(x)-K(x).
\]

常用符号约定：

- 上横线，例如 \(\bar A\)、\(\bar a\)，通常表示连续模型或死亡即刻给付。
- 无横线的 \(A\)、\(a\)、\(\ddot a\)，通常表示离散模型。
- \(\ddot a\) 表示期初付年金，\(a\) 表示期末付年金。
- \(A^1_{x:\overline{n}|}\) 表示 \(n\) 年定期死亡保险；\(A_{x:\overline{n}|}\) 表示 \(n\) 年生死合险。
- \({}_nE_x=v^n{}_np_x\) 表示 \(n\) 年期纯生存保险的精算现值。

---

# 第 1 章 单生命生存模型

## 1.1 寿命、生存函数与密度函数

设新生个体寿命为随机变量 \(X\)。其分布函数、密度函数、生存函数分别为

\[
F_X(x)=P(X\le x),\qquad f_X(x)=F_X'(x),\qquad s(x)=P(X>x)=1-F_X(x).
\]

因此

\[
f_X(x)=-\frac{d}{dx}s(x).
\]

生存函数 \(s(x)\) 表示新生个体能活过 \(x\) 岁的概率。寿险中更常研究已经生存到 \(x\) 岁的个体未来还能活多久。

## 1.2 \(x\) 岁个体的未来寿命分布

对已经生存到 \(x\) 岁的个体，未来寿命为

\[
T(x)=X-x\mid X>x.
\]

其分布函数为

\[
F_{T(x)}(t)=P(T(x)\le t)=1-\frac{s(x+t)}{s(x)}.
\]

因此定义

\[
{}_tp_x=P(T(x)>t)=\frac{s(x+t)}{s(x)},
\]

\[
{}_tq_x=P(T(x)\le t)=1-{}_tp_x.
\]

其中：

- \({}_tp_x\)：\((x)\) 至少再活 \(t\) 年的概率；
- \({}_tq_x\)：\((x)\) 在未来 \(t\) 年内死亡的概率；
- 当 \(t=1\) 时，记 \(p_x={}_1p_x\)，\(q_x={}_1q_x\)。

未来寿命密度函数为

\[
f_{T(x)}(t)=\frac{f_X(x+t)}{s(x)}.
\]

## 1.3 延期死亡概率与乘法公式

延期死亡概率：

\[
{}_{u|t}q_x=P(u<T(x)\le u+t).
\]

它可以写成

\[
{}_{u|t}q_x={}_up_x\,{}_tq_{x+u}={}_up_x-{}_{u+t}p_x.
\]

当 \(t=1\) 时，常简写为

\[
{}_{u|}q_x={}_{u|1}q_x.
\]

生存概率满足乘法公式：

\[
{}_tp_x={}_hp_x\,{}_{t-h}p_{x+h},\qquad 0<h<t.
\]

这个公式的含义是：先从 \(x\) 活到 \(x+h\)，再从 \(x+h\) 活 \(t-h\) 年。

## 1.4 死亡力

死亡力定义为瞬时死亡率：

\[
\mu_x=\frac{f_X(x)}{s(x)}.
\]

对 \((x)\) 的未来寿命，有

\[
f_{T(x)}(t)={}_tp_x\mu_{x+t}.
\]

同时

\[
\frac{d}{dt}{}_tp_x=-{}_tp_x\mu_{x+t}.
\]

因此，若已知死亡力，则

\[
{}_tp_x=\exp\left(-\int_0^t\mu_{x+s}\,ds\right).
\]

## 1.5 整值未来寿命

整值未来寿命为

\[
K(x)=\lfloor T(x)\rfloor.
\]

它表示 \((x)\) 未来能够完整活过的年数。

其概率分布为

\[
P(K(x)=k)=P(k\le T(x)<k+1)={}_kp_x-{}_{k+1}p_x={}_{k|}q_x,
\]

其中 \(k=0,1,2,\ldots\)。

## 1.6 期望余命

完全期望余命：

\[
\mathring e_x=E[T(x)]=\int_0^\infty {}_tp_x\,dt.
\]

整值期望余命：

\[
e_x=E[K(x)]=\sum_{k=1}^\infty {}_kp_x.
\]

整值期望余命递推式：

\[
e_x=p_x+p_xe_{x+1}.
\]

这个递推式的含义是：若 \((x)\) 能活过第一年，则先贡献 1 年，再加上 \((x+1)\) 的未来整值期望余命。

## 1.7 生命表函数

生命表中常用 \(\ell_x\) 表示期初生存人数，\(d_x\) 表示 \([x,x+1)\) 年龄段死亡人数。基本关系为

\[
{}_tp_x=\frac{\ell_{x+t}}{\ell_x},\qquad {}_tq_x=\frac{{}_td_x}{\ell_x},\qquad {}_td_x=\ell_x-\ell_{x+t}.
\]

特别地，

\[
d_x=\ell_x-\ell_{x+1},\qquad q_x=\frac{d_x}{\ell_x},\qquad p_x=\frac{\ell_{x+1}}{\ell_x}.
\]

若用连续死亡力表示生命表函数，则

\[
\ell_{x+t}=\ell_x\exp\left(-\int_x^{x+t}\mu_s\,ds\right).
\]

## 1.8 常用参数寿命模型

### 1. de Moivre 模型

若极限年龄为 \(\omega\)，则

\[
s(x)=1-\frac{x}{\omega},\qquad 0\le x\le \omega.
\]

死亡力为

\[
\mu_x=\frac{1}{\omega-x}.
\]

对 \((x)\)，

\[
{}_tp_x=\frac{\omega-x-t}{\omega-x},\qquad 0\le t\le \omega-x.
\]

### 2. Gompertz 模型

若

\[
\mu_x=BC^x,
\]

则

\[
s(x)=\exp\left[-\frac{B}{\ln C}(C^x-1)\right].
\]

### 3. Makeham 模型

若

\[
\mu_x=A+BC^x,
\]

则

\[
s(x)=\exp\left[-Ax-\frac{B}{\ln C}(C^x-1)\right].
\]

### 4. Weibull 模型

若

\[
\mu_x=kx^n,
\]

则

\[
s(x)=\exp\left(-\frac{k}{n+1}x^{n+1}\right).
\]

## 1.9 分数年龄假设

生命表通常只给出整数年龄的死亡率。要处理非整数年龄，需要对每个年龄年内的分布作假设。

### 1. UDD 假设

UDD 是死亡均匀分布假设。对 \(0\le t\le 1\)，定义

\[
s(x+t)=(1-t)s(x)+ts(x+1).
\]

等价地，生命表人数满足

\[
\ell_{x+t}=(1-t)\ell_x+t\ell_{x+1}.
\]

主要公式：

\[
{}_tq_x=tq_x,
\]

\[
{}_tp_x=1-tq_x,
\]

\[
f_{T(x)}(t)=q_x,
\]

\[
\mu_{x+t}=\frac{q_x}{1-tq_x},\qquad 0<t<1.
\]

若从 \(x+t\) 再看未来 \(u\) 年，且 \(t+u\le 1\)，则

\[
{}_uq_{x+t}=\frac{uq_x}{1-tq_x}.
\]

若每一年都满足 UDD，则 \(K(x)\) 与 \(S(x)\) 独立，且

\[
S(x)\sim U(0,1).
\]

因此

\[
\mathring e_x=e_x+\frac12.
\]

### 2. 常数死亡力假设

常数死亡力假设为

\[
\ln s(x+t)=(1-t)\ln s(x)+t\ln s(x+1),\qquad 0\le t<1.
\]

主要公式：

\[
\mu_{x+t}=-\ln p_x,
\]

\[
{}_tp_x=p_x^t,
\]

\[
{}_tq_x=1-p_x^t.
\]

### 3. Balducci 假设

Balducci 假设为

\[
\frac{1}{s(x+t)}=\frac{1-t}{s(x)}+\frac{t}{s(x+1)},\qquad 0\le t<1.
\]

主要公式：

\[
{}_tq_x=\frac{tq_x}{1-(1-t)q_x},
\]

\[
{}_tp_x=\frac{p_x}{1-(1-t)q_x},
\]

\[
\mu_{x+t}=\frac{q_x}{1-(1-t)q_x}.
\]

## 1.10 分数年龄三种假设对比

对 \(0<t<1\)：

| 假设 | \({}_tq_x\) | \({}_tp_x\) | \(\mu_{x+t}\) |
|---|---:|---:|---:|
| UDD | \(tq_x\) | \(1-tq_x\) | \(\dfrac{q_x}{1-tq_x}\) |
| 常数死亡力 | \(1-p_x^t\) | \(p_x^t\) | \(-\ln p_x\) |
| Balducci | \(\dfrac{tq_x}{1-(1-t)q_x}\) | \(\dfrac{p_x}{1-(1-t)q_x}\) | \(\dfrac{q_x}{1-(1-t)q_x}\) |

记忆重点：UDD 下死亡力随年龄年内时间上升，常数死亡力下死亡力不变，Balducci 下死亡力随年龄年内时间下降。

---

# 第 2 章 死亡保险的精算现值

## 2.1 精算现值的基本思想

死亡保险的精算现值等于保险金现值随机变量的期望。构造模型时要明确四件事：

1. 什么时候给付；
2. 给付金额是多少；
3. 用什么利率折现；
4. 给付事件发生的概率是多少。

## 2.2 纯生存保险

\(n\) 年期纯生存保险：若 \((x)\) 生存至 \(n\) 年末，给付 1；否则不给付。

现值随机变量：

\[
Z=v^nI_{\{T(x)\ge n\}}.
\]

精算现值：

\[
E(Z)=v^n{}_np_x={}_nE_x.
\]

在寿险中也常记为

\[
A^1_{x:\overline{n}|}={}_nE_x.
\]

这里的 \({}_nE_x\) 又称 \(n\) 年生存因子。

## 2.3 \(n\) 年定期死亡保险

定期死亡保险：若 \((x)\) 在未来 \(n\) 年内死亡，给付 1；若期满仍生存，则不给付。

### 2.3.1 死亡后立即给付

现值随机变量：

\[
Z=v^{T(x)}I_{\{T(x)<n\}}.
\]

精算现值：

\[
\bar A^1_{x:\overline{n}|}=\int_0^n v^t{}_tp_x\mu_{x+t}\,dt.
\]

若要计算 \(j\) 阶矩：

\[
E(Z^j)=\int_0^n e^{-j\delta t}{}_tp_x\mu_{x+t}\,dt.
\]

这等于把利息力由 \(\delta\) 改为 \(j\delta\) 后计算同一保险的精算现值。

递推分解式：

\[
\bar A^1_{x:\overline{n}|}=\bar A^1_{x:\overline{m}|}+{}_mE_x\bar A^1_{x+m:\overline{n-m}|},\qquad 0<m<n.
\]

### 2.3.2 死亡保单年度末给付

若死亡发生在第 \(K(x)+1\) 个保单年度，则在该保单年度末给付。

现值随机变量：

\[
Z=v^{K(x)+1}I_{\{T(x)<n\}}.
\]

精算现值：

\[
A^1_{x:\overline{n}|}=\sum_{k=0}^{n-1}v^{k+1}{}_{k|}q_x.
\]

递推式：

\[
A^1_{x:\overline{n}|}=vq_x+vp_xA^1_{x+1:\overline{n-1}|}.
\]

生命表形式：

\[
\ell_xA^1_{x:\overline{n}|}=\sum_{k=0}^{n-1}v^{k+1}d_{x+k}.
\]

### 2.3.3 死亡即刻给付与年末给付的关系

在每一年龄年 UDD 假设下：

\[
\bar A^1_{x:\overline{n}|}=\frac{i}{\delta}A^1_{x:\overline{n}|}.
\]

这个关系只适用于死亡给付部分。不能直接套到包含生存给付的整个生死合险上。

## 2.4 终身寿险

终身寿险：无论何时死亡，都给付 1。

### 2.4.1 死亡后立即给付

现值随机变量：

\[
Z=v^{T(x)}.
\]

精算现值：

\[
\bar A_x=\int_0^\infty v^t{}_tp_x\mu_{x+t}\,dt.
\]

\(j\) 阶矩：

\[
E(Z^j)=\int_0^\infty e^{-j\delta t}{}_tp_x\mu_{x+t}\,dt={}^{j}\bar A_x.
\]

其中 \({}^{j}\bar A_x\) 表示利息力取 \(j\delta\) 时的 \(\bar A_x\)。

### 2.4.2 死亡保单年度末给付

现值随机变量：

\[
Z=v^{K(x)+1}.
\]

精算现值：

\[
A_x=\sum_{k=0}^\infty v^{k+1}{}_{k|}q_x.
\]

递推式：

\[
A_x=vq_x+vp_xA_{x+1}.
\]

在 UDD 假设下：

\[
\bar A_x=\frac{i}{\delta}A_x.
\]

## 2.5 生死合险

生死合险又称两全保险。若 \((x)\) 在 \(n\) 年内死亡，给付死亡保险金；若生存至 \(n\) 年末，给付生存保险金。这里先考虑死亡保险金和生存保险金都为 1。

### 2.5.1 死亡后立即给付、生存期满给付

现值随机变量：

\[
Z=v^{T(x)\wedge n},
\]

其中

\[
T(x)\wedge n=\min\{T(x),n\}.
\]

精算现值：

\[
\bar A_{x:\overline{n}|}=\bar A^1_{x:\overline{n}|}+{}_nE_x.
\]

递推分解：

\[
\bar A_{x:\overline{n}|}=\bar A^1_{x:\overline{m}|}+{}_mE_x\bar A_{x+m:\overline{n-m}|},\qquad 0<m<n.
\]

### 2.5.2 死亡年末给付、生存期满给付

现值随机变量：

\[
Z=v^{(K(x)+1)\wedge n}.
\]

精算现值：

\[
A_{x:\overline{n}|}=A^1_{x:\overline{n}|}+{}_nE_x.
\]

递推式：

\[
A_{x:\overline{n}|}=A^1_{x:\overline{m}|}+{}_mE_xA_{x+m:\overline{n-m}|}.
\]

特别地，一年递推形式为

\[
(1+i)A_{x:\overline{n}|}=q_x\left(1-A_{x+1:\overline{n-1}|}\right)+A_{x+1:\overline{n-1}|}.
\]

### 2.5.3 UDD 下生死合险两种给付方式的关系

在 UDD 假设下，死亡给付部分满足

\[
\bar A^1_{x:\overline{n}|}=\frac{i}{\delta}A^1_{x:\overline{n}|}.
\]

但生存给付部分仍为 \({}_nE_x\)，所以

\[
\bar A_{x:\overline{n}|}=\bar A^1_{x:\overline{n}|}+{}_nE_x
=\frac{i}{\delta}A^1_{x:\overline{n}|}+{}_nE_x.
\]

又因为

\[
A_{x:\overline{n}|}=A^1_{x:\overline{n}|}+{}_nE_x,
\]

所以

\[
\bar A_{x:\overline{n}|}=A_{x:\overline{n}|}+\frac{i-\delta}{\delta}A^1_{x:\overline{n}|}.
\]

注意不能写成 \(\bar A_{x:\overline{n}|}=\dfrac{i}{\delta}A_{x:\overline{n}|}\)。

### 2.5.4 生死合险方差关系

设

\[
Z=Z_1+Z_2,
\]

其中 \(Z_1\) 为死亡保险部分现值，\(Z_2\) 为生存保险部分现值。由于死亡给付与生存期满给付不会同时发生，

\[
Z_1Z_2=0.
\]

因此

\[
\operatorname{Var}(Z)=\operatorname{Var}(Z_1)+\operatorname{Var}(Z_2)-2E(Z_1)E(Z_2).
\]

所以生死合险的方差小于对应死亡保险和生存保险方差之和。

## 2.6 延期死亡保险

### 2.6.1 延期终身寿险

\(m\) 年延期终身寿险：若 \((x)\) 在前 \(m\) 年内死亡，不给付；若活过 \(m\) 年后死亡，给付 1。

死亡即刻给付：

\[
{}_{m|}\bar A_x={}_mE_x\bar A_{x+m}.
\]

死亡年末给付：

\[
{}_{m|}A_x={}_mE_xA_{x+m}.
\]

并且

\[
A_x=A^1_{x:\overline{m}|}+{}_{m|}A_x.
\]

### 2.6.2 延期定期寿险

\(m\) 年延期、\(n\) 年期死亡保险：前 \(m\) 年死亡不给付，之后 \(n\) 年内死亡才给付。

离散年末给付时：

\[
{}_{m|n}A_x=A^1_{x:\overline{m+n}|}-A^1_{x:\overline{m}|}.
\]

## 2.7 每年划分为 \(m\) 个区间

若每年划分为 \(m\) 个等间隔区间，死亡发生所在区间末给付。记

\[
J(x)=\lfloor mS(x)\rfloor.
\]

则死亡给付时刻为

\[
K(x)+\frac{J(x)+1}{m}.
\]

在 UDD 假设下，\(J(x)\) 在 \(0,1,\ldots,m-1\) 上均匀分布，且与 \(K(x)\) 独立。

终身寿险区间末给付的精算现值满足

\[
A_x^{(m)}=\frac{i}{i^{(m)}}A_x,
\]

其中

\[
i^{(m)}=m\left((1+i)^{1/m}-1\right).
\]

当 \(m\to\infty\) 时，

\[
A_x^{(m)}\to\bar A_x.
\]

## 2.8 变额寿险

变额寿险的保险金额随死亡时间变化。

### 2.8.1 一般公式

若死亡即刻给付，时刻 \(t\) 的给付额为 \(b_t\)，则

\[
\operatorname{APV}=\int_0^\infty b_tv^t{}_tp_x\mu_{x+t}\,dt.
\]

若死亡年末给付，第 \(k+1\) 个保单年度末给付额为 \(b_{k+1}\)，则

\[
\operatorname{APV}=\sum_{k=0}^\infty b_{k+1}v^{k+1}{}_{k|}q_x.
\]

### 2.8.2 标准年递增终身寿险

第一年死亡给付 1，第二年死亡给付 2，依此类推。

年末给付：

\[
(IA)_x=\sum_{k=0}^\infty (k+1)v^{k+1}{}_{k|}q_x.
\]

### 2.8.3 标准年递减 \(n\) 年期寿险

第一年死亡给付 \(n\)，第二年死亡给付 \(n-1\)，依此类推。

年末给付：

\[
(DA)^1_{x:\overline{n}|}=\sum_{k=0}^{n-1}(n-k)v^{k+1}{}_{k|}q_x.
\]

---

# 第 3 章 生存年金

## 3.1 生存年金的定义

生存年金是在被保险人生存时按期给付的一系列款项。其精算现值是各期给付现值乘以对应生存概率后求和或积分。

年金类型主要有：

- 连续年金：连续支付；
- 期初付年金：每期初支付；
- 期末付年金：每期末支付；
- 定期年金：只支付有限期限；
- 终身年金：只要生存就一直支付；
- 延期年金：延期若干年后才开始支付。

## 3.2 终身生存年金

### 3.2.1 连续终身年金

连续支付，每年支付率为 1：

\[
\bar a_x=\int_0^\infty v^t{}_tp_x\,dt.
\]

### 3.2.2 终身初付年金

每年年初支付 1，只要年初仍生存就支付：

\[
\ddot a_x=\sum_{k=0}^\infty v^k{}_kp_x.
\]

### 3.2.3 终身期末付年金

每年年末支付 1，只要年末仍生存就支付：

\[
a_x=\sum_{k=1}^\infty v^k{}_kp_x.
\]

期初付和期末付关系：

\[
\ddot a_x=1+a_x.
\]

## 3.3 定期生存年金

### 3.3.1 连续 \(n\) 年期年金

\[
\bar a_{x:\overline{n}|}=\int_0^n v^t{}_tp_x\,dt.
\]

### 3.3.2 \(n\) 年期初付年金

\[
\ddot a_{x:\overline{n}|}=\sum_{k=0}^{n-1}v^k{}_kp_x.
\]

### 3.3.3 \(n\) 年期末付年金

\[
a_{x:\overline{n}|}=\sum_{k=1}^{n}v^k{}_kp_x.
\]

## 3.4 年金与寿险的关系

这些关系非常重要，常用于化简计算。

### 3.4.1 连续模型

对终身情形：

\[
\delta\bar a_x+\bar A_x=1.
\]

对 \(n\) 年生死合险：

\[
\delta\bar a_{x:\overline{n}|}+\bar A_{x:\overline{n}|}=1.
\]

### 3.4.2 离散初付模型

对终身情形：

\[
d\ddot a_x+A_x=1.
\]

对 \(n\) 年生死合险：

\[
d\ddot a_{x:\overline{n}|}+A_{x:\overline{n}|}=1.
\]

### 3.4.3 离散期末付模型

对终身情形：

\[
ia_x+A_x=1.
\]

因为

\[
\ddot a_x=1+a_x,
\qquad d=\frac{i}{1+i}.
\]

注意常见等式

\[
(1+i)(1-d)=1
\]

成立，因为 \(1-d=v\)。

## 3.5 延期年金

\(m\) 年延期终身初付年金：

\[
{}_{m|}\ddot a_x={}_mE_x\ddot a_{x+m}.
\]

也可以写为

\[
{}_{m|}\ddot a_x=\ddot a_x-\ddot a_{x:\overline{m}|}.
\]

连续情形：

\[
{}_{m|}\bar a_x={}_mE_x\bar a_{x+m}.
\]

## 3.6 每年支付 \(m\) 次的年金

每年支付 \(m\) 次时，要先明确每次给付金额。若每年总给付额为 1，则每次给付额通常为 \(1/m\)。

记每年 \(m\) 次期初付年金为 \(\ddot a_x^{(m)}\)，期末付年金为 \(a_x^{(m)}\)。当 \(m\to\infty\) 时，离散高频支付趋近于连续支付。

## 3.7 精算终值

若一个 \(n\) 年期初付生存年金的精算现值为 \(\ddot a_{x:\overline{n}|}\)，则其以生存至 \(n\) 年末为条件的精算终值为

\[
\ddot s_{x:\overline{n}|}=\frac{\ddot a_{x:\overline{n}|}}{{}_nE_x}.
\]

精算终值的含义：把年金的精算现值积累到第 \(n\) 年末，并且条件化到被保险人生存至第 \(n\) 年末这一状态。

---

# 第 4 章 净保费

## 4.1 损失变量

保险人签单时的损失现值定义为

\[
L_0=\text{未来给付现值}+\text{未来费用现值}-\text{未来保费现值}.
\]

若只讨论净保费，通常不考虑费用，则

\[
L_0=\text{未来给付现值}-\text{未来净保费现值}.
\]

## 4.2 等价原则

净保费按等价原则确定：

\[
E(L_0)=0.
\]

也就是

\[
\text{未来净保费精算现值}=\text{未来给付精算现值}.
\]

## 4.3 趸缴净保费

趸缴净保费是签单时一次性缴纳的净保费。由于没有后续保费，趸缴净保费直接等于给付现值的期望。

常见例子：

\[
\text{纯生存保险趸缴净保费}={}_nE_x.
\]

\[
\text{终身寿险趸缴净保费}=A_x\text{ 或 }\bar A_x.
\]

\[
\text{生死合险趸缴净保费}=A_{x:\overline{n}|}\text{ 或 }\bar A_{x:\overline{n}|}.
\]

## 4.4 均衡净保费

若保费按期缴纳，且被保险人生存时才缴费，则均衡净保费为

\[
P=\frac{\text{未来给付精算现值}}{\text{未来缴费年金精算现值}}.
\]

### 4.4.1 完全离散终身寿险

每年年初缴费，死亡年末给付：

\[
P_x=\frac{A_x}{\ddot a_x}.
\]

### 4.4.2 完全离散 \(n\) 年期生死合险

\[
P_{x:\overline{n}|}=\frac{A_{x:\overline{n}|}}{\ddot a_{x:\overline{n}|}}.
\]

### 4.4.3 \(h\) 年限期缴费

若给付为终身寿险，但只缴费 \(h\) 年，则

\[
{}^hP_x=\frac{A_x}{\ddot a_{x:\overline{h}|}}.
\]

## 4.5 变额保费或变额给付

如果给付额或保费额随时间变化，应逐项写出现金流并求精算现值。

例如第 \(k\) 年年初缴保费 \(\pi_k\)，则保费现值为

\[
Y=\sum_{k\ge0}\pi_kv^kI_{\{T(x)\ge k\}}.
\]

其期望为

\[
E(Y)=\sum_{k\ge0}\pi_kv^k{}_kp_x.
\]

## 4.6 保费方差

若

\[
L_0=Z-PY,
\]

其中 \(Z\) 为给付现值，\(Y\) 为每单位保费对应的缴费年金现值，则

\[
\operatorname{Var}(L_0)=\operatorname{Var}(Z-PY).
\]

展开得

\[
\operatorname{Var}(L_0)=\operatorname{Var}(Z)+P^2\operatorname{Var}(Y)-2P\operatorname{Cov}(Z,Y).
\]

如果是趸缴净保费，保费本身不是随机变量，故损失方差只来自给付现值随机变量。

## 4.7 总保费

总保费在净保费基础上加入费用、风险边际和利润加载。

一般可写为

\[
\text{总保费现值}=\text{给付现值}+\text{费用现值}+\text{风险附加}+\text{利润附加}.
\]

费用通常包括：

- 首年佣金；
- 续年佣金；
- 保单签发费用；
- 维持费用；
- 理赔费用；
- 税费和利润加载。

## 4.8 聚合风险与正态近似

设单张保单损失为 \(L\)，满足

\[
E(L)=\mu,\qquad \operatorname{Var}(L)=\sigma^2.
\]

若组合中有 \(n\) 张独立同分布保单，聚合损失为

\[
L_{\rm agg}=\sum_{j=1}^nL_j.
\]

则

\[
E(L_{\rm agg})=n\mu,
\]

\[
\operatorname{Var}(L_{\rm agg})=n\sigma^2.
\]

当 \(n\) 较大时，可用正态近似：

\[
L_{\rm agg}\approx N(n\mu,n\sigma^2).
\]

若要求破产概率不超过 \(\alpha\)，常用分位数条件确定安全附加。

---

# 第 5 章 责任准备金

## 5.1 责任准备金的含义

责任准备金是保单已经生效一段时间后，保险公司为了履行未来保险责任需要持有的资金。

在 \(t\) 时刻，未来损失随机变量为

\[
L_t=\text{未来给付现值}-\text{未来保费现值}.
\]

净责任准备金定义为

\[
{}_tV=E(L_t\mid T(x)>t).
\]

## 5.2 未来法

未来法准备金等于未来给付精算现值减未来保费精算现值：

\[
{}_tV=E_t(\text{未来给付现值})-E_t(\text{未来净保费现值}).
\]

### 5.2.1 完全离散终身寿险

\[
{}_tV=A_{x+t}-P_x\ddot a_{x+t}.
\]

### 5.2.2 \(n\) 年期生死合险

\[
{}_tV=A_{x+t:\overline{n-t}|}-P\ddot a_{x+t:\overline{n-t}|},\qquad 0\le t\le n.
\]

期满时准备金通常满足

\[
{}_nV=1
\]

表示若被保险人生存至期满，需要支付满期给付。

## 5.3 过去法

过去法从已收保费和已发生给付的积累值角度计算准备金。基本思想是：

\[
{}_tV=\frac{\text{过去净保费积累值}-\text{过去给付积累值}}{\text{生存到 }t\text{ 的条件}}.
\]

在净保费原则和同一组精算假设下，未来法与过去法等价。

## 5.4 完全离散一年递推式

对单位死亡保险金、年初缴费、死亡年末给付的完全离散寿险，有

\[
{}_tV+P=v\left(q_{x+t}+p_{x+t}{}_{t+1}V\right).
\]

等价地，

\[
({}_tV+P)(1+i)=q_{x+t}+p_{x+t}{}_{t+1}V.
\]

整理得

\[
{}_{t+1}V=\frac{({}_tV+P)(1+i)-q_{x+t}}{p_{x+t}}.
\]

若第 \(t+1\) 年死亡给付额为 \(b_{t+1}\)，则

\[
{}_tV+P=v\left(q_{x+t}b_{t+1}+p_{x+t}{}_{t+1}V\right).
\]

## 5.5 责任准备金的直观解释

在 \(t\) 年末，保险公司手上已有准备金 \({}_tV\)，并收取下一期保费 \(P\)。这一笔资金积累一年后，要么用于死亡给付，要么成为下一年仍有效保单的准备金。

所以递推式可以理解为

\[
\text{本年初资金}=\text{未来一年死亡给付的现值}+\text{生存者下一年准备金的现值}.
\]

## 5.6 亏损随机变量的方差

\(t\) 时刻未来损失为

\[
L_t=\text{未来给付现值}-\text{未来保费现值}.
\]

责任准备金为其条件期望：

\[
{}_tV=E(L_t\mid T(x)>t).
\]

方差为

\[
\operatorname{Var}(L_t)=E(L_t^2)-[E(L_t)]^2.
\]

计算时通常先按死亡年份或生存状态分解 \(L_t\) 的取值，再求一阶矩和二阶矩。

## 5.7 Thiele 微分方程

连续模型下，设保费率为 \(\pi_t\)，死亡给付额为 \(b_t\)，利息力为 \(\delta_t\)，则责任准备金满足

\[
\frac{d}{dt}{}_tV=\delta_t{}_tV+\pi_t-\mu_{x+t}(b_t-{}_tV).
\]

各项含义：

- \(\delta_t{}_tV\)：准备金产生的利息；
- \(\pi_t\)：连续缴入的保费；
- \(\mu_{x+t}(b_t-{}_tV)\)：死亡发生时保险公司相对准备金还需额外支付的净额。

## 5.8 修正责任准备金

均衡净保费法将净保费均匀分摊到整个缴费期，但实际新契约首年费用通常较高，例如佣金、核保和签单费用。因此，直接用均衡净保费计算首年准备金可能不符合实际经营压力。

修正净保费法的思想是：

- 首年修正净保费较低；
- 续年修正净保费较高；
- 未来给付精算现值仍与修正后保费精算现值相等。

常见形式为

\[
\alpha+\beta\ddot a_{x+1}=A_x,
\]

其中 \(\alpha\) 是首年修正净保费，\(\beta\) 是续年修正净保费。

修正准备金并不是降低客户实际首年缴纳的总保费，而是在准备金评估中把首年高费用因素反映出来，从而降低首年准备金压力。

---

# 第 6 章 多生命模型

## 6.1 联合分布

设两个个体未来寿命分别为 \(T(x)\) 和 \(T(y)\)。联合分布函数为

\[
F_{T(x),T(y)}(s,t)=P(T(x)\le s,T(y)\le t).
\]

联合生存函数为

\[
S_{T(x),T(y)}(s,t)=P(T(x)>s,T(y)>t).
\]

若联合密度存在，则

\[
f_{T(x),T(y)}(s,t)=\frac{\partial^2}{\partial s\partial t}F_{T(x),T(y)}(s,t).
\]

也有

\[
f_{T(x),T(y)}(s,t)=\frac{\partial^2}{\partial s\partial t}S_{T(x),T(y)}(s,t).
\]

## 6.2 联合生命状态

联合生命状态 \(xy\) 的未来寿命定义为

\[
T(xy)=\min\{T(x),T(y)\}.
\]

含义：两人都活着时，联合生命状态存在；任一人死亡，状态终止。

生存概率：

\[
{}_tp_{xy}=P(T(x)>t,T(y)>t).
\]

若 \(T(x)\) 与 \(T(y)\) 独立，则

\[
{}_tp_{xy}={}_tp_x{}_tp_y.
\]

联合生命状态在 \(t\) 时刻的死亡力，在独立假设下为

\[
\mu_{xy}(t)=\mu_{x+t}+\mu_{y+t}.
\]

## 6.3 最后生存者状态

最后生存者状态 \(\overline{xy}\) 的未来寿命定义为

\[
T(\overline{xy})=\max\{T(x),T(y)\}.
\]

含义：至少一人活着时，最后生存者状态存在；两人都死亡后，状态终止。

生存概率：

\[
{}_tp_{\overline{xy}}=P(T(x)>t\text{ 或 }T(y)>t).
\]

因此

\[
{}_tp_{\overline{xy}}={}_tp_x+{}_tp_y-{}_tp_{xy}.
\]

若独立，则

\[
{}_tp_{\overline{xy}}={}_tp_x+{}_tp_y-{}_tp_x{}_tp_y.
\]

## 6.4 联合生命与最后生存者的期望余命

联合生命状态的完全期望余命：

\[
\mathring e_{xy}=\int_0^\infty {}_tp_{xy}\,dt.
\]

最后生存者状态的完全期望余命：

\[
\mathring e_{\overline{xy}}=\int_0^\infty {}_tp_{\overline{xy}}\,dt.
\]

由

\[
{}_tp_{\overline{xy}}={}_tp_x+{}_tp_y-{}_tp_{xy}
\]

可得

\[
\mathring e_{\overline{xy}}=\mathring e_x+\mathring e_y-\mathring e_{xy}.
\]

## 6.5 多生命年金

### 6.5.1 联合生命年金

只要两人都生存就给付的连续年金：

\[
\bar a_{xy}=\int_0^\infty v^t{}_tp_{xy}\,dt.
\]

### 6.5.2 最后生存者年金

只要至少一人生存就给付的连续年金：

\[
\bar a_{\overline{xy}}=\int_0^\infty v^t{}_tp_{\overline{xy}}\,dt.
\]

由生存概率关系可得

\[
\bar a_{\overline{xy}}=\bar a_x+\bar a_y-\bar a_{xy}.
\]

等价地，

\[
\bar a_{xy}+\bar a_{\overline{xy}}=\bar a_x+\bar a_y.
\]

### 6.5.3 转继年金

若 \(x\) 死亡后，只要 \(y\) 仍生存就给付，则连续转继年金精算现值为

\[
\bar a_{y|x}=\bar a_y-\bar a_{xy}.
\]

含义：\(\bar a_y\) 是只要 \(y\) 活着就给付；其中两人都活着时的给付 \(\bar a_{xy}\) 需要扣除，剩下的就是 \(x\) 已死亡且 \(y\) 仍生存时的给付。

## 6.6 多生命保险

### 6.6.1 首次死亡保险

首次死亡保险在联合生命状态终止时给付，即两人中第一人死亡时给付。

死亡即刻给付现值为

\[
Z=v^{T(xy)}.
\]

精算现值为

\[
\bar A_{xy}=E\left(v^{T(xy)}\right).
\]

### 6.6.2 最后死亡保险

最后死亡保险在最后生存者死亡时给付。

死亡即刻给付现值为

\[
Z=v^{T(\overline{xy})}.
\]

精算现值为

\[
\bar A_{\overline{xy}}=E\left(v^{T(\overline{xy})}\right).
\]

### 6.6.3 多生命保险恒等式

连续模型下：

\[
\delta\bar a_{xy}+\bar A_{xy}=1,
\]

\[
\delta\bar a_{\overline{xy}}+\bar A_{\overline{xy}}=1.
\]

并且

\[
\bar A_{xy}+\bar A_{\overline{xy}}=\bar A_x+\bar A_y.
\]

## 6.7 多生命模型常见判断

- 联合生命 \(xy\)：看两人是否都活着，寿命取 \(\min\)。
- 最后生存者 \(\overline{xy}\)：看是否至少一人活着，寿命取 \(\max\)。
- 首次死亡保险：第一人死亡时给付，对应 \(T(xy)\)。
- 最后死亡保险：最后一人死亡时给付，对应 \(T(\overline{xy})\)。
- 转继年金：通常用“单生命年金减联合生命年金”表示。

---

# 期末高频公式速查

## 1. 生存模型

\[
{}_tp_x=\frac{s(x+t)}{s(x)},\qquad {}_tq_x=1-{}_tp_x.
\]

\[
{}_{u|t}q_x={}_up_x\,{}_tq_{x+u}={}_up_x-{}_{u+t}p_x.
\]

\[
f_{T(x)}(t)={}_tp_x\mu_{x+t}.
\]

\[
P(K(x)=k)={}_{k|}q_x.
\]

\[
\mathring e_x=\int_0^\infty {}_tp_x\,dt,
\qquad
e_x=\sum_{k=1}^\infty {}_kp_x.
\]

## 2. UDD

\[
{}_tq_x=tq_x,
\qquad
{}_tp_x=1-tq_x,
\qquad
\mu_{x+t}=\frac{q_x}{1-tq_x}.
\]

\[
\mathring e_x=e_x+\frac12.
\]

## 3. 死亡保险

\[
{}_nE_x=v^n{}_np_x.
\]

\[
\bar A^1_{x:\overline{n}|}=\int_0^n v^t{}_tp_x\mu_{x+t}\,dt.
\]

\[
A^1_{x:\overline{n}|}=\sum_{k=0}^{n-1}v^{k+1}{}_{k|}q_x.
\]

\[
A_x=\sum_{k=0}^\infty v^{k+1}{}_{k|}q_x.
\]

\[
A_x=vq_x+vp_xA_{x+1}.
\]

UDD 下：

\[
\bar A^1_{x:\overline{n}|}=\frac{i}{\delta}A^1_{x:\overline{n}|},
\qquad
\bar A_x=\frac{i}{\delta}A_x.
\]

## 4. 生死合险

\[
A_{x:\overline{n}|}=A^1_{x:\overline{n}|}+{}_nE_x.
\]

\[
\bar A_{x:\overline{n}|}=\bar A^1_{x:\overline{n}|}+{}_nE_x.
\]

UDD 下：

\[
\bar A_{x:\overline{n}|}=A_{x:\overline{n}|}+\frac{i-\delta}{\delta}A^1_{x:\overline{n}|}.
\]

## 5. 年金

\[
\bar a_x=\int_0^\infty v^t{}_tp_x\,dt.
\]

\[
\ddot a_x=\sum_{k=0}^\infty v^k{}_kp_x,
\qquad
a_x=\sum_{k=1}^\infty v^k{}_kp_x.
\]

\[
\ddot a_x=1+a_x.
\]

\[
\delta\bar a_x+\bar A_x=1.
\]

\[
d\ddot a_x+A_x=1.
\]

\[
ia_x+A_x=1.
\]

\[
{}_{m|}\ddot a_x={}_mE_x\ddot a_{x+m}=\ddot a_x-\ddot a_{x:\overline{m}|}.
\]

## 6. 净保费

\[
L_0=\text{给付现值}-\text{保费现值}.
\]

\[
E(L_0)=0.
\]

\[
P=\frac{\text{未来给付精算现值}}{\text{未来缴费年金精算现值}}.
\]

\[
P_x=\frac{A_x}{\ddot a_x}.
\]

## 7. 责任准备金

\[
{}_tV=E_t(\text{未来给付现值})-E_t(\text{未来保费现值}).
\]

\[
{}_tV=A_{x+t}-P_x\ddot a_{x+t}.
\]

\[
{}_tV+P=v\left(q_{x+t}+p_{x+t}{}_{t+1}V\right).
\]

\[
\frac{d}{dt}{}_tV=\delta_t{}_tV+\pi_t-\mu_{x+t}(b_t-{}_tV).
\]

## 8. 多生命

\[
T(xy)=\min\{T(x),T(y)\},
\qquad
T(\overline{xy})=\max\{T(x),T(y)\}.
\]

\[
{}_tp_{xy}=P(T(x)>t,T(y)>t).
\]

独立时：

\[
{}_tp_{xy}={}_tp_x{}_tp_y.
\]

\[
{}_tp_{\overline{xy}}={}_tp_x+{}_tp_y-{}_tp_{xy}.
\]

\[
\bar a_{xy}+\bar a_{\overline{xy}}=\bar a_x+\bar a_y.
\]

\[
\bar A_{xy}+\bar A_{\overline{xy}}=\bar A_x+\bar A_y.
\]

---

# 易错点总结

1. \(A^1_{x:\overline{n}|}\) 是定期死亡保险，\(A_{x:\overline{n}|}\) 是生死合险。
2. \({}_nE_x=v^n{}_np_x\)，是纯生存保险现值，不是死亡保险。
3. UDD 下 \(\bar A=\dfrac{i}{\delta}A\) 只直接适用于死亡给付部分。
4. 生死合险在 UDD 下不能直接整体乘 \(\dfrac{i}{\delta}\)。
5. 年金与寿险关系要区分 \(i,d,\delta\)：

\[
\delta\bar a+\bar A=1,
\qquad
d\ddot a+A=1,
\qquad
ia+A=1.
\]

6. 责任准备金未来法是“未来给付现值减未来保费现值”。
7. 修正准备金不是降低实际总保费，而是调整评估用净保费结构以反映首年费用。
8. 多生命中，联合生命取 \(\min\)，最后生存者取 \(\max\)。
9. 首次死亡保险对应联合生命状态；最后死亡保险对应最后生存者状态。
10. 计算方差时不能只平方精算现值，应先写出现值随机变量，再求二阶矩。
