# W8D2 - Functions of a Random Variable
## Normal approximation to Binomial
**Normal** random variables can be used to **approximate** other random variables, for example binomial random variables.

Suppose that $X\sim \mathrm{binomial}(n,p)$. $\mathbb{E}(X)=np$ and $\mathrm{Var}(X)=np(1-p)$. 
- Let $Y\sim\mathcal N(np, np(1-p))$. 
- For large $n$, $X\approx Y$
- The approximation is particularly accurate when $p$ is close to $1/2$.

For any integer $k$ between $0$ and $n$, we have $\mathbb{P}(X\leq k)\approx \Phi\left( \frac{k+0.5-np}{\sqrt{np(1-p)}} \right)$
- The $k+0.5$ represents the discrepancy between the cut-off between the normal random variable (placed **between** two integers, thus $+0.5$), and the binomial random variable ($k$).
![[binormal.png]]
For example, the picture above shows the pmf (histogram) of a **binomial** random variable $X$ with $n= 20$ and $p= 0.4$, together with the pdf (bell curve) of a **normal** random variable $Y$ with $µ= np= 8$ and $σ^2 = np(1−p) = 4.8$.

The curve closely approximates the histogram; in particular, the area of each rectangle in the histogram is approximated by a corresponding *area* under the bell curve.

---

**Example:** Airlines often overbook their flights. Suppose that each passenger has a 5% chance of not showing up (independent of any other passenger). Suppose that a flight has 300 seats.
- If 318 passengers are booked, then use a normal distribution to estimate the probability that at most 3 passengers do not get a seat.
- How many passengers can the airline book, in order to be (at least) 90% sure that at most 3 passengers do not get a seat?

**First part**: Let $X\sim\mathrm{binomial}(318, 0.95)$ be the number of passengers who show up. Then, for at most $3$ passengers to not get a seat, we require $X≤303$.

We find that
$$
\begin{align}
\mathbb P(X\leq303)&\approx\Phi\left( \frac{303+0.5-318\times0.95}{\sqrt{318\times0.95\times0.05}} \right) \\
&\approx\Phi(0.36022) \\
&\approx64\%
\end{align}
$$

**Second part**: Let $X\sim \mathrm{binomial}(n, 0.95)$ be the number of passengers who show up, where $n$ (the unknown here) is the number of passengers the airline can book. We still require $X≤303$.

We get
$$
\mathbb P(X≤303)\approx \Phi\left( \frac{303.5-0.95n}{\sqrt{0.0475n}} \right)
$$
Equating this to 90%, we find that
$$
\frac{303.5-0.95n}{\sqrt{0.0475n}}=\Phi^{-1}(0.9)\approx 1.282
$$
If we let $x=\sqrt{n}$, we obtain $0.95x^2+0.2793x-303.5\approx0$, so the quadratic formula gives $x\approx17.7$ or $n\approx 314.3$. Thus, the airline can book 314 (or fewer) passengers.
## Q-Q Plot
Let X be a continuous random variable, and let $p \in \mathbb{R}$ be strictly between 0 and 1. The $(100p)^{th}$ percentile of X is defined to be an x-value $Q_p$, such that $P(X ≤ Qp) = F(Q_p) = p$.
- The $(100p)^{th}$ percentile of X is also called the pth quantile of X
- If $F$, the cdf of X, is invertible (such as the case when X is normal or exponential), then $Q_p$ = $F^{−1}(p)$
  - e.g If X is standard normal, then $Q_{0.025} = \Phi^{-1}(0.025) = -1.96$
- **If the sample is drawn from a population that can be modelled by a random variable X, then $x_i$ should be close to $Q_{i/(n+1)}$, the $\frac{i}{n+1}{th}$ quantile of X**
### Procedure
1. Order the data values as $x_{1}\leq x_{2}\leq x_{3}\leq\cdots\leq x_n$
2. Construct a scatter plot of $x_i$ against the $\frac{i}{n+1}$th quantiles of the standard normal $Z$.
    - That is, construct a scatter plot for the points $\left( \Phi^{-1}\left( \frac{i}{n+1} \right),x_i \right)$ for $i=1,2,\dots,n$.
3. If the scatter plot looks close to a **straight line**, then it is plausible that the data comes from a **normal** distribution.

The above steps can be modified to check for other distributions; for example, if we replace ‘**normal**’ by ‘**exponential**’, then we need to replace $\Phi^{−1}$ by $F^{−1}$, where $F$ is the cdf of an exponential RV.
![[qqPlot.png]]
## Functions of a random variable
Let $X$ be a continuous random variable, and $Y=g(X)$ for a function $g$. For clarity, we denote the pdf of $X$ and $Y$ by $f_X$ and $f_Y$ respectively, and the cdf of $X$ and $Y$ by $F_X$ and $F_Y$ respectively.

Finding the pdf $f_Y$ from $f_X$:

1. Determine the **interval** on which $Y$ can take positive probability. On that interval, we start with the **cdf** $F_Y$: $$ F_Y(y)=\mathbb P(Y\leq y)=\mathbb P(g(X)\leq y) $$
2. Rearrange the inequality $g(X)\leq y$ and make $X$ the subject.
3. After rearranging, $F_Y$ will be expressible in terms of $F_X$ (known); now **differentiate** with respect to $y$ to obtain $f_Y$.
---
**Example:** Let $X\sim \mathrm{uniform}(0,1)$, and $Y=-\ln(1-X)$. Find the pdf of $Y$.

First, observe that since $X$ can only take positive probability on $[0,1]$, then $Y=-\ln(1-X)$ can only take positive probability on $[0,\infty)$. All our computations will be done on these intervals.

Next, on these intervals, we follow the procedure:
$$
\begin{align}
F_Y(y)&=\mathbb P(Y\leq y)=\mathbb P(-\ln(1-X)\leq y) \\
&=\mathbb P(\ln(1-X)\geq-y)~\mathbb P(1-X\geq e^{-y}) \\
&=\mathbb P(X\leq 1-e^{-y})=F_X(1-e^{-y})
\end{align}
$$
Finally, we differentiate both sides with respect to $y$, and apply the chain rule:
$$
f_Y(y)=\frac{d}{dy}F_X(1-e^{-y})=f_X(1-e^{-y})e^{-y}=e^{-y}
$$
where we have used the fact that $f_X(x)=1$ on the interval $[0,1]$.

Therefore,
$$
f_Y(y)=\begin{cases}
e^{-y}, & \text{if }y \in [0,\infty) \\
0, & \text{otherwise}
\end{cases}
$$
In other words, $Y\sim \mathrm{exponential}(1)$

---

**Example:** A real number $X$ is generated uniformly randomly from the interval $[0,1]$. Let $Y=\sqrt{X}$. Find the **cdf** of $Y$, then use it to compute $\mathbb P(0.6\leq Y<0.7)$.