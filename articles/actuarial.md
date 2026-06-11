# 寿险精算数学复习笔记

## 1. 单生命生存模型

### 1.1 寿命、生存函数与剩余寿命

设新生个体的寿命为随机变量 \(X\)。其分布函数、密度函数与生存函数分别为

\[
F_X(x)=\mathbb{P}(0\le X\le x),\qquad f_X(x)=F_X'(x),
\]

\[
s(x)=\mathbb{P}(X>x)=1-F_X(x),
\]

因此

\[
f_X(x)=-\frac{d}{dx}s(x).
\]

对已经活到 \(x\) 岁的个体，记为 \((x)\)。其未来生存时间，即剩余寿命，为

\[
T(x)=X-x.
\]

其分布函数、密度函数和生存函数分别记为

\[
F_{T(x)}(t),\qquad f_{T(x)}(t),\qquad s_{T(x)}(t).
\]

由条件概率可得

\[
F_{T(x)}(t)=\mathbb{P}(X-x\le t\mid X>x)
=\frac{\mathbb{P}(x<X\le x+t)}{\mathbb{P}(X>x)}.
\]

所以

\[
F_{T(x)}(t)=\frac{F_X(x+t)-F_X(x)}{1-F_X(x)}
=\frac{s(x)-s(x+t)}{s(x)},
\]

\[
f_{T(x)}(t)=\frac{f_X(x+t)}{s(x)}.
\]

> 注：这里 \(x\) 表示已经达到的年龄，\(t\) 表示从 \(x\) 岁开始向后看的未来时间。

### 1.2 常用生存概率与死亡概率符号

\[
{}_tp_x=\mathbb{P}(T(x)>t)=\frac{s(x+t)}{s(x)}.
\]

\[
{}_tq_x=\mathbb{P}(0<T(x)\le t)
=\frac{s(x)-s(x+t)}{s(x)}=1-{}_tp_x.
\]

\[
{}_{u|t}q_x=\mathbb{P}(u<T(x)\le u+t)
=\frac{s(x+u)-s(x+u+t)}{s(x)}.
\]

进一步有

\[
{}_{u|t}q_x={}_up_x\,{}_tq_{x+u}={}_up_x-{}_{u+t}p_x.
\]

当 \(t=1\) 时，简记为

\[
{}_1p_x=p_x,\qquad {}_1q_x=q_x,
\]

\[
{}_{u|1}q_x={}_{u|}q_x.
\]

### 1.3 整值剩余寿命

记 \(K(x)\) 为 \(T(x)\) 的整数部分，\(S(x)\) 为小数部分，则

\[
T(x)=K(x)+S(x).
\]

对 \(k=0,1,2,\ldots\)，有

\[
\mathbb{P}(K(x)=k)=\mathbb{P}(k\le T(x)<k+1)
={}_kp_x-{}_{k+1}p_x={}_{k|}q_x.
\]

也可以写为

\[
\mathbb{P}(K(x)=k)={}_kp_x q_{x+k}.
\]

### 1.4 死亡力

死亡力，也称死力、瞬时死亡率，定义为

\[
\mu_x=\lim_{\Delta x\to 0^+}
\frac{\mathbb{P}(x<X\le x+\Delta x\mid X>x)}{\Delta x}
=\frac{f_X(x)}{s(x)}.
\]

> 注：\(\mu_xdx\) 可理解为在很短年龄区间 \([x,x+dx]\) 内死亡的人数占 \(x\) 岁生存人数的比例。

对 \((x)\) 的剩余寿命，有

\[
f_{T(x)}(t)={}_tp_x\mu_{x+t}.
\]

该式可理解为：“先活到 \(x+t\) 岁”乘以“在 \(x+t\) 附近瞬时死亡”。同时

\[
\frac{d}{dt}({}_tp_x)=-{}_tp_x\mu_{x+t}.
\]

因此

\[
{}_tp_x=\exp\left(-\int_0^t\mu_{x+s}\,ds\right).
\]

若 \(0<h<t\)，则

\[
{}_tp_x={}_hp_x\,{}_{t-h}p_{x+h}.
\]

### 1.5 剩余寿命期望

完整剩余寿命的期望记为

\[
\overset{\circ}{e}_x=\mathbb{E}(T(x)).
\]

整值剩余寿命的期望记为

\[
e_x=\mathbb{E}(K(x)).
\]

常用计算公式为

\[
\overset{\circ}{e}_x=\int_0^{\infty}{}_tp_x\,dt,
\]

\[
e_x=\sum_{n=1}^{\infty}{}_np_x.
\]

递推关系为

\[
e_x=p_x(1+e_{x+1}).
\]

### 1.6 寿命分布参数模型

| 模型 | 死亡力或生存函数特征 |
|---|---|
| de Moivre | 生存函数线性，常见形式为 \(s(x)=1-\frac{x}{\omega}\) |
| Gompertz | 死亡力为指数形式，\(\mu(x)=BC^x\) |
| Makeham | 在 Gompertz 死亡力基础上加常数项，\(\mu(x)=A+BC^x\) |
| Weibull | 死亡力为幂函数形式 |

> 注：参数模型主要用于用简单解析式拟合寿命分布；传统寿险精算中，更常用生命表描述寿命分布。

### 1.7 随机生存群与生命表

设初始有 \(\ell_0\) 个个体，寿命服从共同生存分布。记实际活到 \(x\) 岁的人数为 \(\mathscr{L}(x)\)，其期望为

\[
\ell_x=\mathbb{E}(\mathscr{L}(x)).
\]

记 \([x,x+t)\) 内死亡人数为 \({}_t\mathscr{D}_x\)，其期望为

\[
{}_td_x=\mathbb{E}({}_t\mathscr{D}_x).
\]

则

\[
{}_td_x=\ell_x-\ell_{x+t}.
\]

> 易错点：死亡人数应为期初生存人数减期末生存人数，即 \(\ell_x-\ell_{x+t}\)，不是 \(\ell_{x+t}-\ell_x\)。

生命表中的常用关系为

\[
{}_tp_x=\frac{\ell_{x+t}}{\ell_x},\qquad
{}_tq_x=\frac{{}_td_x}{\ell_x}.
\]

死亡力与生命表函数满足

\[
\frac{d\ell_x}{dx}=-\ell_x\mu_x.
\]

生命表的历史脉络可简记为：约翰·格朗特于 1662 年提出生命表思想，哈雷于 1693 年构造第一张完整生命表。

### 1.8 分数年龄上的分布假设

生命表通常只给出整数年龄处的信息。对于 \(x+t\) 这样的分数年龄，需要额外假设。

#### UDD 假设

UDD，即死亡均匀分布假设，也可理解为生存函数在整数年龄之间线性插值：

\[
s(x+t)=(1-t)s(x)+t s(x+1),\qquad 0<t<1.
\]

此时

\[
\ell_{x+t}=(1-t)\ell_x+t\ell_{x+1},
\]

\[
{}_td_x=t d_x,
\]

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
\mu_{x+t}=\frac{q_x}{1-tq_x}.
\]

若每一年龄年都满足 UDD，则 \(K(x)\) 与 \(S(x)\) 相互独立，且 \(S(x)\sim U(0,1)\)。因此

\[
\overset{\circ}{e}_x=e_x+\frac12.
\]

#### 常数死亡力假设

常数死亡力假设是指在 \([x,x+1)\) 上 \(\ln s(x+t)\) 线性：

\[
\ln s(x+t)=(1-t)\ln s(x)+t\ln s(x+1).
\]

此时死亡力为常数：

\[
\mu_{x+t}=-\ln p_x.
\]

并且

\[
{}_tp_x=p_x^t,
\]

\[
{}_tq_x=1-p_x^t,
\]

\[
f_{T(x)}(t)=-p_x^t\ln p_x.
\]

#### Balducci 假设

Balducci 假设是指 \(1/s(x+t)\) 在整数年龄之间线性：

\[
\frac1{s(x+t)}=\frac{1-t}{s(x)}+\frac{t}{s(x+1)}.
\]

此时

\[
{}_tp_x=\frac{p_x}{1-(1-t)q_x},
\]

\[
{}_tq_x=\frac{tq_x}{1-(1-t)q_x},
\]

\[
\mu_{x+t}=\frac{q_x}{1-(1-t)q_x}.
\]

> 对比记忆：UDD 下死亡力随 \(t\) 上升；常数死亡力假设下死亡力不变；Balducci 假设下死亡力随 \(t\) 下降。

### 1.9 选择生命表与终极生命表

若投保前需要体检，新参保人群短期死亡率通常低于已参保人群。为了刻画这种“选择效应”，可使用选择-终极生命表：在选择期内采用选择死亡率；选择期结束后，死亡率回到终极生命表状态。

> 记忆：选择期内死亡率较低；选择期过后回到普通的终极表。

## 2. 死亡保险

### 2.1 基本险种与符号

死亡保险以被保险人在保险期限内死亡为给付条件。常见险种包括定期寿险、终身寿险、延期寿险、生存保险和生死合险。

| 险种 | 年末给付符号 | 死亡即刻给付符号或说明 |
|---|---|---|
| \(n\) 年期定期寿险 | \(A^1_{x:\overline{n}|}\) | \(\bar A^1_{x:\overline{n}|}\) |
| 终身寿险 | \(A_x\) | \(\bar A_x\) |
| 延期 \(m\) 年 \(n\) 年期寿险 | \({}_{m|n}A_x\) | \({}_{m|n}\bar A_x\) |
| 延期 \(m\) 年终身寿险 | \({}_{m|}A_x\) | \({}_{m|}\bar A_x\) |
| \(n\) 年期生存保险 | \({}_nE_x\) | 生存给付在 \(n\) 年末 |
| \(n\) 年期生死合险 | \(A_{x:\overline{n}|}\) | \(\bar A_{x:\overline{n}|}\) |

> 注：\({}_nE_x=v^n{}_np_x\) 同时包含贴现因子和生存概率。它在寿险中也可看作 \(n\) 年期生存保险的精算现值。

### 2.2 定期寿险、终身寿险和生存保险

死亡即刻给付的 \(n\) 年期定期寿险：

\[
\bar A^1_{x:\overline{n}|}=\int_0^n v^t{}_tp_x\mu_{x+t}\,dt.
\]

死亡保单年度末给付的 \(n\) 年期定期寿险：

\[
A^1_{x:\overline{n}|}=\sum_{k=0}^{n-1}v^{k+1}{}_{k|}q_x.
\]

终身寿险为定期寿险期限趋于无穷时的情形：

\[
\bar A_x=\int_0^{\infty}v^t{}_tp_x\mu_{x+t}\,dt,
\]

\[
A_x=\sum_{k=0}^{\infty}v^{k+1}{}_{k|}q_x.
\]

生存保险为

\[
{}_nE_x=v^n{}_np_x.
\]

### 2.3 生死合险

\(n\) 年期生死合险由 \(n\) 年期定期寿险和 \(n\) 年期生存保险组成。

死亡即刻给付时：

\[
\bar A_{x:\overline{n}|}=\bar A^1_{x:\overline{n}|}+{}_nE_x.
\]

死亡保单年度末给付时：

\[
A_{x:\overline{n}|}=A^1_{x:\overline{n}|}+{}_nE_x.
\]

> 易错点：定期寿险 \(A^1_{x:\overline{n}|}\) 不包含生存给付；生死合险 \(A_{x:\overline{n}|}\) 包含期满生存给付。

### 2.4 分解与递推公式

对 \(0<m<n\)，死亡即刻给付的定期寿险有

\[
\bar A^1_{x:\overline{n}|}=\bar A^1_{x:\overline{m}|}+{}_mE_x\bar A^1_{x+m:\overline{n-m}|}.
\]

死亡保单年度末给付的定期寿险有

\[
A^1_{x:\overline{n}|}=A^1_{x:\overline{m}|}+{}_mE_xA^1_{x+m:\overline{n-m}|}.
\]

生死合险有

\[
A_{x:\overline{n}|}=A^1_{x:\overline{m}|}+{}_mE_xA_{x+m:\overline{n-m}|}.
\]

终身寿险可分解为前 \(n\) 年定期寿险和 \(n\) 年后延期终身寿险：

\[
A_x=A^1_{x:\overline{n}|}+{}_nE_xA_{x+n}.
\]

延期 \(m\) 年、期限 \(n\) 年的寿险可写为

\[
{}_{m|n}A_x=A^1_{x:\overline{m+n}|}-A^1_{x:\overline{m}|}.
\]

### 2.5 UDD 假设下不同给付时刻的关系

在每一年龄年 UDD 假设成立时，死亡即刻给付和死亡年末给付之间有

\[
\bar A_x=\frac{i}{\delta}A_x,
\]

等价地

\[
\delta\bar A_x=iA_x.
\]

类似地，定期寿险也有

\[
\bar A^1_{x:\overline{n}|}=\frac{i}{\delta}A^1_{x:\overline{n}|}.
\]

> 易错点：\(\frac{i}{\delta}\) 转换适用于“死亡给付”部分。生死合险包含期满生存给付，所以不能把整个 \(A_{x:\overline{n}|}\) 直接乘 \(\frac{i}{\delta}\)。

生死合险在 UDD 假设下应写为

\[
\bar A_{x:\overline{n}|}=\frac{i}{\delta}A^1_{x:\overline{n}|}+{}_nE_x.
\]

### 2.6 矩与方差

若保险给付现值为 \(Z\)，且给付额为 1，\(Z\) 的 \(j\) 阶矩通常可以通过把利息力 \(\delta\) 替换为 \(j\delta\) 来计算：

\[
\mathbb{E}(Z^j)@\delta=\mathbb{E}(Z)@j\delta.
\]

例如，死亡即刻给付的定期寿险有

\[
\mathbb{E}(Z^j)={}^{j}\bar A^1_{x:\overline{n}|},
\]

其中左上标 \(j\) 表示计算时采用利息力 \(j\delta\)，不是保额的 \(j\) 次方。

因此

\[
\operatorname{Var}(Z)=\mathbb{E}(Z^2)-[\mathbb{E}(Z)]^2.
\]

对生死合险，若 \(Z=Z_D+Z_S\)，其中 \(Z_D\) 为死亡给付现值，\(Z_S\) 为生存给付现值，由于二者不能同时发生，\(Z_DZ_S=0\)，故

\[
\operatorname{Var}(Z)=\operatorname{Var}(Z_D)+\operatorname{Var}(Z_S)-2\mathbb{E}(Z_D)\mathbb{E}(Z_S).
\]

这说明两全保险的方差小于对应死亡保险方差与生存保险方差之和。

### 2.7 一年划分为 \(m\) 个区间给付

设一年分为 \(m\) 个等间隔区间，死亡在所在区间末给付。在 UDD 假设下，终身寿险有

\[
A_x^{(m)}=\frac{i}{i^{(m)}}A_x.
\]

当 \(m\to\infty\) 时，区间末给付趋近于死亡即刻给付：

\[
A_x^{(m)}\to \bar A_x.
\]

## 3. 生存年金

### 3.1 生存年金分类与符号

生存年金是以年金领取人生存为给付条件的一系列给付。

| 类别 | 连续给付 | 期初给付 | 期末给付 |
|---|---|---|---|
| 终身生存年金 | \(\bar a_x\) | \(\ddot a_x\) | \(a_x\) |
| \(n\) 年定期生存年金 | \(\bar a_{x:\overline{n}|}\) | \(\ddot a_{x:\overline{n}|}\) | \(a_{x:\overline{n}|}\) |
| 延期 \(m\) 年终身生存年金 | \({}_{m|}\bar a_x\) | \({}_{m|}\ddot a_x\) | \({}_{m|}a_x\) |
| 延期 \(m\) 年、给付 \(n\) 年生存年金 | \({}_{m|}\bar a_{x:\overline{n}|}\) | \({}_{m|}\ddot a_{x:\overline{n}|}\) | \({}_{m|}a_{x:\overline{n}|}\) |

### 3.2 基本精算现值

连续终身生存年金：

\[
\bar a_x=\int_0^{\infty}v^t{}_tp_x\,dt.
\]

期初终身生存年金：

\[
\ddot a_x=\sum_{k=0}^{\infty}v^k{}_kp_x.
\]

期末终身生存年金：

\[
a_x=\sum_{k=1}^{\infty}v^k{}_kp_x.
\]

定期年金只需把求和或积分的范围限制在给付期限内。

### 3.3 年金与寿险的关系

连续终身生存年金与死亡即刻给付终身寿险满足

\[
\delta\bar a_x+\bar A_x=1.
\]

期初终身生存年金与死亡年末给付终身寿险满足

\[
d\ddot a_x+A_x=1.
\]

\(n\) 年定期期初生存年金与 \(n\) 年期生死合险满足

\[
d\ddot a_{x:\overline{n}|}+A_{x:\overline{n}|}=1.
\]

> 易错点：定期年金关系式中对应的是生死合险 \(A_{x:\overline{n}|}\)，不是定期寿险 \(A^1_{x:\overline{n}|}\)。原因是年金停止时对应“死亡或期满”两种终止方式。

期末终身年金也可以写出关系。由于 \(\ddot a_x=1+a_x\)，由 \(d\ddot a_x+A_x=1\) 可得

\[
1=ia_x+(1+i)A_x.
\]

同理，定期期末年金有

\[
a_{x:\overline{n}|}=\ddot a_{x:\overline{n}|}-1+{}_nE_x
=\ddot a_{x:\overline{n+1}|}-1.
\]

### 3.4 延期年金、递推与保证期年金

延期 \(m\) 年终身连续生存年金满足

\[
{}_{m|}\bar a_x={}_mE_x\bar a_{x+m}.
\]

也可以写成

\[
{}_{m|}\bar a_x=\bar a_x-\bar a_{x:\overline{m}|}.
\]

定期连续生存年金递推公式为

\[
\bar a_{x:\overline{n}|}=\bar a_{x:\overline{m}|}+{}_mE_x\bar a_{x+m:\overline{n-m}|}.
\]

对有 \(n\) 年保证期的终身连续年金，前 \(n\) 年为确定年金，之后若仍生存才继续给付：

\[
\bar a_{\overline{n}|}+{}_nE_x\bar a_{x+n}.
\]

### 3.5 一年给付 \(m\) 次的年金

一年给付 \(m\) 次的期初年金记为 \(\ddot a_x^{(m)}\)。与寿险的关系为

\[
d^{(m)}\ddot a_x^{(m)}+A_x^{(m)}=1.
\]

其中

\[
d^{(m)}=m(1-v^{1/m}),
\]

\[
i^{(m)}=m((1+i)^{1/m}-1).
\]

### 3.6 精算终值

定期生存年金的精算终值可理解为：在已生存到期末的条件下，把年金现值折算到期末的价值。常用形式为

\[
S_{x:\overline{n}|}=\frac{a_{x:\overline{n}|}}{{}_nE_x}.
\]

> 直观理解：分母 \({}_nE_x\) 是从现在到第 \(n\) 年末且生存的精算折现因子；除以它相当于把现值转到第 \(n\) 年末的生存状态下。

### 3.7 年金模型在金融中的应用

生存年金思想可用于含随机终止时间的金融现金流建模，例如：

- 包含违约风险的债券模型；
- 包含提前赎回风险的债券模型。

## 4. 净保费

### 4.1 平衡原则与签单损失量

净保费由平衡原则确定：

\[
\text{投保人缴纳保费的精算现值}=\text{保险人未来给付的精算现值}.
\]

设保险人的签单损失量为

\[
L=\text{保险人未来给付现值}-\text{投保人缴纳净保费现值}.
\]

平衡原则等价于

\[
\mathbb{E}(L)=0.
\]

趸交净保费即一次性缴纳的净保费，数值上等于给付责任的精算现值。

### 4.2 均衡净保费的一般计算方式

若每年期初缴纳均衡净保费，则

\[
\text{均衡净保费}=\frac{\text{给付责任精算现值}}{\text{缴费期内期初生存年金精算现值}}.
\]

例如，完全离散终身寿险的净保费为

\[
P_x=\frac{A_x}{\ddot a_x}.
\]

半连续终身寿险，即死亡即刻给付、保费年初缴纳，有

\[
P(\bar A_x)=\frac{\bar A_x}{\ddot a_x}.
\]

完全连续终身寿险，即死亡即刻给付、保费连续缴纳，有

\[
\bar P(\bar A_x)=\frac{\bar A_x}{\bar a_x}.
\]

### 4.3 常用净保费符号

| 类别 | 完全连续 | 半连续：保费年初缴，死亡即刻给付 | 完全离散 |
|---|---|---|---|
| 定期寿险 | \(\bar P(\bar A^1_{x:\overline{n}|})\) | \(P(\bar A^1_{x:\overline{n}|})\) | \(P^1_{x:\overline{n}|}\) |
| 终身寿险 | \(\bar P(\bar A_x)\) | \(P(\bar A_x)\) | \(P_x\) |
| 两全保险 | \(\bar P(\bar A_{x:\overline{n}|})\) | \(P(\bar A_{x:\overline{n}|})\) | \(P_{x:\overline{n}|}\) |
| 缴费期 \(h\) 年终身寿险 | \({}_h\bar P(\bar A_x)\) | \({}_hP(\bar A_x)\) | \({}_hP_x\) |
| 缴费期 \(h\) 年定期寿险 | \({}_h\bar P(\bar A^1_{x:\overline{n}|})\) | \({}_hP(\bar A^1_{x:\overline{n}|})\) | \({}_hP^1_{x:\overline{n}|}\) |
| 延期终身生存年金保费 | \(\bar P({}_{m|}\bar a_x)\) | \(P({}_{m|}\bar a_x)\) | \(P({}_{m|}\ddot a_x)\) |

### 4.4 UDD 假设下的保费关系

在 UDD 假设下，死亡即刻给付与死亡年末给付满足 \(\bar A=(i/\delta)A\)。若缴费方式相同，则对应净保费也满足类似关系。例如

\[
P(\bar A^1_{x:\overline{n}|})=\frac{i}{\delta}P^1_{x:\overline{n}|},
\]

即

\[
\delta P(\bar A^1_{x:\overline{n}|})=iP^1_{x:\overline{n}|}.
\]

若一年缴费 \(m\) 次，完全离散终身寿险的年缴总额记为 \(P_x^{(m)}\)，则

\[
P_x^{(m)}=\frac{A_x}{\ddot a_x^{(m)}}
=\frac{P_x\ddot a_x}{\ddot a_x^{(m)}}.
\]

### 4.5 毛保费

毛保费是在净保费基础上加入费用因素后得到的保费。基本思想为

\[
\text{毛保费收入现值}=\text{给付现值}+\text{费用现值}.
\]

费用通常包括初始费用、续期费用、缴费费用、理赔费用和投资费用等。

若毛保费为 \(G\)，且每期保费中有比例费用，则计算时要把“每期随保费变化的费用”从保费年金中扣除，再列平衡方程。

### 4.6 组合百分数原则

组合百分数原则用于考虑一组同质且相互独立的保单。设单张保单签单损失量均值为 \(\mu\)，方差为 \(\sigma^2\)，组合规模为 \(n\)。记组合总损失为

\[
L_{\mathrm{agg}}=L_1+L_2+\cdots+L_n.
\]

由中心极限定理，近似有

\[
L_{\mathrm{agg}}\sim N(n\mu,n\sigma^2).
\]

若要求破产或亏损概率不超过 \(\alpha\)，即

\[
\mathbb{P}(L_{\mathrm{agg}}>0)\le \alpha,
\]

等价于

\[
\mathbb{P}(L_{\mathrm{agg}}\le 0)\ge 1-\alpha.
\]

标准化得到

\[
\mathbb{P}\left(
\frac{L_{\mathrm{agg}}-n\mu}{\sqrt n\sigma}
\le
\frac{-n\mu}{\sqrt n\sigma}
\right)
\ge 1-\alpha.
\]

因此通常令

\[
\frac{-\sqrt n\mu}{\sigma}=z_{1-\alpha},
\]

从而确定安全附加水平。

> 注：若 \(L\) 定义为“未来给付现值减保费现值”，加入安全附加后通常会使 \(\mu<0\)。

## 5. 净责任准备金

### 5.1 净责任准备金的含义

净责任准备金是在保单生效后某一时刻，为覆盖未来净责任而需要提取的准备金。其基本思想是

\[
\text{准备金}=\text{未来给付现值}-\text{未来保费现值}.
\]

设 \({}_tL\) 为 \(t\) 时刻保险人的未来损失量，则净责任准备金为

\[
{}_tV=\mathbb{E}({}_tL).
\]

### 5.2 常用符号

| 类别 | 完全连续 | 半连续 | 完全离散 |
|---|---|---|---|
| 终身寿险 \(t\) 时刻准备金 | \({}_t\bar V(\bar A_x)\) | \({}_tV(\bar A_x)\) | \({}_tV_x\) |
| 缴费期 \(h\) 年终身寿险 | \({}_t^h\bar V(\bar A_x)\) | \({}_t^hV(\bar A_x)\) | \({}_t^hV_x\) |

### 5.3 前瞻法

完全离散终身寿险在第 \(t\) 年末的准备金为

\[
{}_tV_x=A_{x+t}-P_x\ddot a_{x+t}.
\]

若为 \(n\) 年期两全保险，则第 \(t\) 年末准备金为

\[
{}_tV_{x:\overline{n}|}=A_{x+t:\overline{n-t}|}-P_{x:\overline{n}|}\ddot a_{x+t:\overline{n-t}|}.
\]

若缴费期已满，则未来保费现值为 0，准备金只等于未来给付责任的精算现值。

### 5.4 未来损失量方差

以完全连续终身寿险为例，在 \(t\) 时刻且被保险人仍生存的条件下，未来损失量可写为

\[
{}_tL=v^{T(x)-t}-\bar P(\bar A_x)\bar a_{\overline{T(x)-t}|}.
\]

其中

\[
\bar a_{\overline{T(x)-t}|}=\frac{1-v^{T(x)-t}}{\delta}.
\]

因此

\[
{}_tL=v^{T(x)-t}-\bar P(\bar A_x)\frac{1-v^{T(x)-t}}{\delta}.
\]

整理得

\[
{}_tL=\left(1+\frac{\bar P(\bar A_x)}{\delta}\right)v^{T(x)-t}-\frac{\bar P(\bar A_x)}{\delta}.
\]

常数项不影响方差，所以

\[
\operatorname{Var}({}_tL)
=\left(1+\frac{\bar P(\bar A_x)}{\delta}\right)^2
\left({}^2\bar A_{x+t}-\bar A_{x+t}^{\,2}\right).
\]

由于

\[
\bar P(\bar A_x)=\frac{\bar A_x}{\bar a_x},\qquad \delta\bar a_x+\bar A_x=1,
\]

所以也可写为

\[
\operatorname{Var}({}_tL)=
\frac{{}^2\bar A_{x+t}-\bar A_{x+t}^{\,2}}{(\delta\bar a_x)^2}.
\]

### 5.5 其他形式

完全离散终身寿险准备金还可写为

\[
{}_tV_x=(P_{x+t}-P_x)\ddot a_{x+t}.
\]

也可写为

\[
{}_tV_x=\left(1-\frac{P_x}{P_{x+t}}\right)A_{x+t}.
\]

> 注：这两式常用于利用保费符号快速表达准备金。

### 5.6 后溯公式

完全离散终身寿险的后溯准备金为

\[
{}_tV_x=\frac{P_x\ddot a_{x:\overline{t}|}-A^1_{x:\overline{t}|}}{{}_tE_x}.
\]

也可写为

\[
{}_tV_x=P_x\ddot s_{x:\overline{t}|}-{}_t\kappa_x,
\]

其中

\[
{}_t\kappa_x=\frac{A^1_{x:\overline{t}|}}{{}_tE_x}.
\]

> 注：后溯法从过去累积角度看准备金，分子是过去保费累积值减过去保险责任累积值，再除以生存到 \(t\) 时刻的精算折现因子。

### 5.7 递推公式

完全离散终身寿险的递推公式为

\[
{}_tV_x+P_x=vq_{x+t}+vp_{x+t}{}_{t+1}V_x.
\]

> 易错点：若死亡保险金在年末给付，第一项应为 \(vq_{x+t}\)，因为死亡给付发生在下一年年末，需要贴现一年。

### 5.8 每年缴纳 \(m\) 次保费

若每年缴费 \(m\) 次，准备金仍按同一原则计算：

\[
\text{准备金}=\text{未来给付精算现值}-\text{未来保费精算现值}.
\]

例如在保费尚未缴满时，\(n\) 年期两全保险可按形式写为

\[
{}_tV^{(m)}_{x:\overline{n}|}
=A_{x+t:\overline{n-t}|}-P^{(m)}_{x:\overline{n}|}\ddot a^{(m)}_{x+t:\overline{n-t}|}.
\]

若缴费期为 \(h\) 年，则未来保费年金的期限应取剩余缴费期，而不是剩余保障期。

### 5.9 修正责任准备金

实际业务中，保险公司签单初期费用较高。若仍按均衡净保费提取准备金，第一年准备金压力可能偏大。因此可采用修正净保费方法：降低第一年用于准备金计算的净保费，增加后续年度用于准备金计算的净保费。

设第一年修正净保费为 \(\alpha\)，以后各年修正净保费为 \(\beta\)。则修正准备金通常写为

\[
{}_tV^{\mathrm{MOD}}=\text{未来给付现值}-\beta\times\text{未来保费年金现值}.
\]

对 \(n\) 年期两全保险，可写为

\[
{}_tV^{\mathrm{MOD}}
=A_{x+t:\overline{n-t}|}-\beta\ddot a_{x+t:\overline{n-t}|}.
\]

完全初年定期法，即 FPT 法，常取

\[
\alpha=A^1_{x:\overline{1}|}.
\]

对 \(n\) 年期两全保险，\(\beta\) 由等价原则确定：

\[
\alpha+\beta\,{}_1E_x\ddot a_{x+1:\overline{n-1}|}=A_{x:\overline{n}|}.
\]

> 记忆：FPT 法把第一年看成一年期定期寿险，第一年只为第一年死亡风险筹资；后续年度再承担剩余责任。

## 6. 多生命生存模型

### 6.1 联合分布与联合生存函数

设 \((x)\)、\((y)\) 的未来生存时间分别为 \(T(x)\)、\(T(y)\)。其联合分布函数为

\[
F_{T(x),T(y)}(s,t)=\mathbb{P}(T(x)\le s,T(y)\le t).
\]

联合生存函数为

\[
S_{T(x),T(y)}(s,t)=\mathbb{P}(T(x)>s,T(y)>t).
\]

二者满足

\[
F_{T(x),T(y)}(s,t)
=1-S_{T(x)}(s)-S_{T(y)}(t)+S_{T(x),T(y)}(s,t).
\]

联合密度函数可写为

\[
f_{T(x),T(y)}(s,t)
=\frac{\partial^2F_{T(x),T(y)}(s,t)}{\partial s\partial t}
=\frac{\partial^2S_{T(x),T(y)}(s,t)}{\partial s\partial t}.
\]

### 6.2 联合生存状态与最后生存状态

联合生存状态 \((xy)\) 表示“两人都生存”。其未来生存时间为

\[
T(xy)=\min\{T(x),T(y)\}.
\]

最后生存状态 \(\overline{xy}\) 表示“至少一人生存”。其未来生存时间为

\[
T(\overline{xy})=\max\{T(x),T(y)\}.
\]

由于

\[
\{T(xy),T(\overline{xy})\}=\{T(x),T(y)\},
\]

对任意对称函数 \(g\)，有

\[
g(T(x),T(y))=g(T(xy),T(\overline{xy})).
\]

### 6.3 独立情形下的常用关系

若 \(T(x)\) 与 \(T(y)\) 独立，则

\[
{}_tp_{xy}={}_tp_x\,{}_tp_y.
\]

最后生存状态满足

\[
{}_tp_{\overline{xy}}={}_tp_x+{}_tp_y-{}_tp_x{}_tp_y.
\]

死亡概率对应为

\[
{}_tq_{xy}=1-{}_tp_x{}_tp_y.
\]

联合生存状态的死亡力为

\[
\mu_{xy}(t)=\mu_{x+t}+\mu_{y+t}.
\]

完整期望余命之间有

\[
\overset{\circ}{e}_{xy}+\overset{\circ}{e}_{\overline{xy}}
=\overset{\circ}{e}_{x}+\overset{\circ}{e}_{y}.
\]

整值期望余命也有类似关系：

\[
e_{xy}+e_{\overline{xy}}=e_x+e_y.
\]

### 6.4 死亡次序相关概率

记 \({}_nq^1_{xy}\) 为：\((x)\) 先于 \((y)\) 死亡，且 \((x)\) 在未来 \(n\) 年内死亡的概率。若两人独立，则

\[
{}_nq^1_{xy}=\int_0^n{}_tp_x\mu_{x+t}{}_tp_y\,dt.
\]

记 \({}_nq^2_{xy}\) 为：\((x)\) 后于 \((y)\) 死亡，且 \((x)\) 在未来 \(n\) 年内死亡的概率。若两人独立，则

\[
{}_nq^2_{xy}=\int_0^n{}_tp_x\mu_{x+t}{}_tq_y\,dt.
\]

二者满足

\[
{}_nq^1_{xy}+{}_nq^2_{xy}={}_nq_x.
\]

并且

\[
{}_nq^1_{xy}={}_nq^2_{yx}+{}_np_y{}_nq_x.
\]

> 注：\({}_nq^1_{xy}\) 和 \({}_nq^2_{xy}\) 的上标是死亡次序，不是幂次。

### 6.5 多生命精算现值

多生命模型中的寿险和年金符号与单生命类似，只是把单生命状态 \((x)\) 换成联合生存状态 \((xy)\) 或最后生存状态 \(\overline{xy}\)。

例如，联合生存状态终身寿险现值可记为 \(A_{xy}\) 或 \(\bar A_{xy}\)；最后生存状态终身寿险现值可记为 \(A_{\overline{xy}}\) 或 \(\bar A_{\overline{xy}}\)。

死亡即刻给付下，常用关系为

\[
\bar A_{xy}+\bar A_{\overline{xy}}=\bar A_x+\bar A_y.
\]

年末给付下，类似地有

\[
A_{xy}+A_{\overline{xy}}=A_x+A_y.
\]

年金也有对应关系：

\[
\bar a_{xy}+\bar a_{\overline{xy}}=\bar a_x+\bar a_y,
\]

\[
\ddot a_{xy}+\ddot a_{\overline{xy}}=\ddot a_x+\ddot a_y,
\]

\[
a_{xy}+a_{\overline{xy}}=a_x+a_y.
\]

### 6.6 继承年金

继承年金是指：对某一人给付年金，但给付以另一人死亡为前提。

例如，连续终身继承年金 \(\bar a_{x|y}\) 表示：当 \((x)\) 死亡后，只要 \((y)\) 仍生存，就向 \((y)\) 连续给付年金；若 \((y)\) 先于 \((x)\) 死亡，则不给付。

其给付区间为

\[
[\min\{T(x),T(y)\},T(y)).
\]

因此现值可看作“\((y)\) 的终身年金”减去“\((x)\) 与 \((y)\) 都生存时的联合年金”：

\[
\bar a_{x|y}=\bar a_y-\bar a_{xy}.
\]

> 记忆：继承年金是“对 \((y)\) 的年金”中，扣掉 \((x)\) 还活着时不能给的那一段。
