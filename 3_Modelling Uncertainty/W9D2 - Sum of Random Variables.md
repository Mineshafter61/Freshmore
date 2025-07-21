# W9D2 - Sum of Random Variables
## Covariance
Let $X$ and $Y$ be **any** random variable. The variance of their sum is given by:
$$
\mathrm{Var}(X+Y)=\mathrm{Var}(X)+\mathrm{Var}(Y)+2(\textcolor{red}{\mathbb E(XY)−\mathbb E(X) \mathbb E(Y)})
$$
where $\textcolor{red}{\mathbb E(XY)−\mathbb E(X) \mathbb E(Y)}$ is the **covariance**, or $\mathrm{Cov}(X,Y)$.

### Theorem 1
**If** $X$ and $Y$ are **independent** random variables, **then** $\mathrm{Cov}(X, Y) = 0$, and hence
$$ \mathrm{Var}(X+Y)=\mathrm{Var}(X)+\mathrm{Var}(Y) $$
More generally, if $X_{1},X_{2},\dots X_{n}$ are **independent**, then
$$ \mathrm{Var}(X_{1}+X_{2}+\cdots+X_{n})=\mathrm{Var}(X_{1})+\mathrm{Var}(X_{2})+\cdots+\mathrm{Var}(X_{n}) $$
**Proof**

Suppose that $X$ and $Y$ are continuous, independent RV’s. Then,
$$
\begin{align}
\mathbb E(X,Y)&=\int_{-\infty}^{\infty} \int_{-\infty}^{\infty}x\,y\,f(x,y)\,dx \,dy\\
&=\int_{-\infty}^{\infty} \int_{-\infty}^{\infty}x\,y\,f_X(x)f_Y(y)\, dx\,dy\\
&=\int_{-\infty}^{\infty}x\,f_X(x)\,dx\int_{-\infty}^{\infty}y\,f_Y(y)\,dy\\
&=\mathbb E(X)\mathbb E(Y)
\end{align}
$$
Hence, $\mathrm{Cov}(X,Y)=\mathbb E(X,Y)-\mathbb E(X)\mathbb E(Y)=0$

## Sum of normal RV's

**Theorem**: Let $X\sim \mathcal N(\mu_{1},\sigma_{1}^{2})$ and $Y\sim \mathcal N(\mu_{2},\sigma_{2}^{2})$ be **independent normal random variables**. Then $X+Y\sim \mathcal N(\mu_{1}+\mu_{2},\sigma_{1}^{2}+\sigma_{2}^{2})$

## Sum of uniform RV's
Let $X\sim \mathrm{uniform}(0,1)$ and $Y\sim \mathrm{uniform}(0,1)$ be **uniform** random variables. We denote the **joint pdf** of $X$ and $Y$ by $f(x,y)$.

Using independence, we find that
$$f(x,y)=f_X(x)f_Y(y)=1\cdot1=1$$
on the unit square and 0 elsewhere.

To find the **cdf**, we find 
$$\begin{align}
F_{X+Y}(t)&=\mathbb P(X+Y\leq t) \\
&=\iint_{x+y\leq t}f(x,y)\,dx\,dy \\
\end{align}$$
Since $f(x,y)=\begin{cases}1, (0\leq x\leq1 \land 0\leq y\leq1)\\0, \text{otherwise}\end{cases}$, this integral can be computed using geometry.
- The equation $(x+y=t)$ is a straight line with gradient $-1$.
- When $t=0$, i.e. $(x+y=0)$, the line passes through $(0,0)$.
- When $t=1$, i.e. $(x+y=1)$, the line passes through $(0,1)$ and $(1,0)$. The region is thus a **right triangle** when $0<t\leq1$, and a **square minus a right triangle** when $1<t\leq2$.
    - This right triangle has short side lengths $(t)$ when $0<t\leq1$ and $(2-t)$ when $1<t\leq2$.
- When $t=2$, i.e. $(x+y=2)$, the line passes through $(1,1)$.
- Hence,
$$
F_{X+Y}(t)=\begin{cases}
0,&t\leq0 \\
t^2/2,& 0<t\leq1 \\
1-(2-t)^2,& 1<t\leq2 \\
1,& t>2
\end{cases}
$$
Differentiating the above equation, we get
$$
f_{X+Y}(t)=\begin{cases}
t, & 0<t\leq1 \\
2-t, & 1<t\leq2 \\
0, & \text{otherwise}
\end{cases}
$$
## Sum of exponential RV's
Let $X$ and $Y$ be **independent** exponential random variables with $\lambda=2$. We want to find $X+Y$. Write down $f(x,y)$, the joint pdf of $X$ and $Y$, including where it is 0, then express  as a double integral, and finally, evaluate the integral to find the cdf of $X+Y$.

Using **independence**, we have
$$ f(x,y)=f_X(x)f_Y(y)=\begin{cases} 2e^{-2x}2e^{-2y}, & x\geq0\land y\geq0 \\ 0, & \text{otherwise} \end{cases} $$
For any $t\geq0$,
$$\begin{align}
F_{X+Y}(t)&=\mathbb P(X+Y\leq t)=\iint_{x+y\leq t}f(x,y)\,dx\,dy \\
&=\int_{y=0}^{y=t} \int_{x=0}^{x=t-y} 2e^{-2x}2e^{-2y}\,dx\,dy \\
&=\int_{y=0}^{y=t}\left[-e^{-2x}\right]_0^{t-y}\,2e^{-2y}\,dy \\
&=\int_{y=0}^{y=t}(-e^{-2t+2y}+1)\,2e^{-2y}\,dy \\
&=\int_{y=0}^{y=t}(-e^{-2t+2y}\,2e^{-2y}+2e^{-2y})\,\,dy \\
&=\int_{y=0}^{y=t}(-2e^{-2t+2y}e^{-2y}+2e^{-2y})\,\,dy \\
&=\int_{y=0}^{y=t}(-2e^{-2t}+2e^{-2y})\,\,dy \\
&=\int_{y=0}^{y=t}(2e^{-2y}-2e^{-2t})\,\,dy \\
&=\left[-e^{-2y}-2e^{-2t}y\right]_{y=0}^{y=t}&(-2e^{-2t}\text{ is a constant}) \\
&=1-(2t+1)e^{-2t}
\end{align}$$
Since $t<0$ necessarily means that $x<0$ or $y<0$, and $\mathbb P(X<0)=0$ and $\mathbb P(Y<0)=0$, by intuition, $F_{X+Y}(t)$ will also be 0 if $t<0$. Thus we have
$$
F_{X+Y}(t)=\begin{cases}
1-(2t+1)e^{-2t}, & \text{if } t\geq 0 \\
0 & \text{if } t< 0
\end{cases}
$$
## Sum of binomial RV's
Let $X \sim \mathrm{binomial}(n, p)$ and $Y \sim \mathrm{binomial}(m, p)$ be independent binomial random variables. Then $X + Y \sim \mathrm{binomial}(n + m, p)$
## Sum of Poisson RV's
Let $X ∼ \mathrm{Poisson}(λ)$ and $Y ∼ \mathrm{Poisson}(μ)$ be independent Poisson random variables. Then $X + Y ∼ \mathrm{Poisson}(λ + μ)$
## Extras
- The **pdf of the sum** ($f_{X+Y}(t)$) is generally **NOT EQUAL** to the **joint pdf** ($f(x,y)$).
- It is equal to the **derivative of the double integral of the joint pdf** ($f_{X+Y}(t)=\frac{d}{dt}\iint_{x+y\leq t}f(x,y)\,dx\,dy$) (notice how the variables of integration/differentiation are different)