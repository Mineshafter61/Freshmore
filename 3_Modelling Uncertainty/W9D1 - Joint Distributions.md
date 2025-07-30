 W9D1 - Joint Distributions

## Discrete

### Joint pmf

- Let $X$ and $Y$ be **discrete** random variables. The **joint probability mass function (joint pmf)** $f(x,y)$ is a function of two variables, defined as
$$f(x,y):=\mathbb P((X=x)\cap \mathbb P(Y=y))$$
- $\displaystyle\sum_{\text{all }x}\sum_{\text{all }y}f(x,y)=1$

### Marginal pmf

- The **marginal probability mass function (marginal pmf)** of $X$, denoted by $f_X$, is just the pmf of $X$, and can be computed using
$$f_X(x):=\mathbb P(X=x)=\sum_{\text{all }y}f(x,y)$$
- Similarly, the **marginal probability mass function (marginal pmf)** of $Y$, denoted by $f_Y$, is just the pmf of $Y$, and can be computed using
$$f_Y(y):=\mathbb P(Y=y)=\sum_{\text{all }x}f(x,y)$$
- Marginal pmf's are the **row and column sums** of the joint pmf table.

### Independence of RV

X and Y are independent if and only if
$$
\begin{gather*}
\mathbb{P}{\big(}(X=x)\cap(Y=y){\big)}=\mathbb{P}(X=x)\operatorname{P}(Y=y) \text{ for all } x, y,\\\text{and/or}\\f(x,y) = f_X(x)f_Y(y) \text{ for all } x,y \in \mathbb{R}
\end{gather*}
$$

This means that **if X and Y are independent**, the **joint pmf is the product of the marginal pmf's**.
### Expected Value

$$
\mathbb{E}\bigl(g(X,\,Y)\bigr)\,=\,\sum_{\mathrm{all}\;x}\sum_{\mathrm{all}\;y}g(x,\,y)\,f\bigr(x,\,y\bigr)
$$

- Alternatively, linearity of expectation holds true regardless of independence
$$
E(X+Y) = E(X) + E(Y)
$$
- This can be expanded to
$$
\mathbb E(X_1+X_2+\cdots+X_n)=\mathbb E(X_1)+\mathbb E(X_2)+\cdots+\mathbb E(X_n)
$$
## Continuous

Let X and Y be continuous random variables. A two-variable function f is called the joint probability density function (joint pdf) of X and Y , if for any region C in the plane,
$$
\mathbb{P}((X, Y) \in C) = \iint_{(x,y)\in C}f(x, y) \, dx \, dy
$$
- **Important example:** If $C$ is the rectangle $[a, b] \times [c, d]$,
$$
\mathbb{P}((X, Y) \in C) =  \mathbb{P}((a \leq X \leq b) \cap (c \leq Y \leq d)) = \int^d_c \int^b_a f(x, y) \, dx \, dy
$$

- Since the total probability needs to be 1, we have

$$
\int_{-\infty}^{\infty}\int_{-\infty}^{\infty}f(x,\,y)\,\mathrm{d}x\,\mathrm{d}y=1
$$

- $f(x, y)$ is **not** the probability by itself, it is small $\delta x, \delta y$
    - $f(x, y)$ is the probability per unit area
    - **Volumes** under f(x, y) represent the probability

$$
f(x,\,y)\,\delta x\,\delta y\approx\mathbb{P}(x\leq X\leq x+\delta x,\,y\leq Y\leq y+\delta y)
$$

An example of a joint pdf is shown as a **surface** $z=f(x,y)$.
- The total volume under the surface and above the $xy$-plane must be 1.
- The probability that the pair $(X,Y)$ is found in the rectangle $C$, is equal to the **volume** of the solid with base $C$ and bounded above by $f(x,y)$.
![[jointPdf.png]]
### Marginal pdf
Let $X$ and $Y$ be **continuous random variables**. The **marginal probability density function (marginal pdf)** of $X$, denoted by $f_X$, is the pdf of $X$, and can be computed using
$$
f_X(x)=\int_{-\infty}^{\infty}f(x,y)\,dy 
$$
Similarly, the **marginal pdf** of $Y$, denoted by $f_Y$, is the pdf of $Y$, and can be computed using
$$
f_Y(y)=\int_{-\infty}^{\infty}f(x,y)\,dx
$$
### Independence, expected value
Let $X$ and $Y$ be continuous random variables. $X$ and $Y$ are said to be **independent** if and only if
$$
\mathbb P((X \in A)\cap(Y \in B))=\mathbb P(X \in A)\mathbb P(Y \in B), \text{for all } A,B\subseteq \mathbb R
$$
Equivalently, it can be shown that $X$ and $Y$ are **independent** if and only if
$$
f(x,y)=f_X(x)\,f_Y(y), \text{ for all }x,y\in \mathbb R
$$
**Expected values** can be computed using
$$
\mathbb E(g(X,Y))=\int_{-\infty}^{\infty}\int_{-\infty}^{\infty} g(x,y)f(x,y)\,dx\,dy 
$$
## Joint cdf
For any random variables $X$ and $Y$, the **joint cumulative distribution function** is defined as
$$
F(x,y):=\mathbb P((X\leq x)\cap(Y\leq y))
$$
## Examples
Let $c$ be a constant, and let $T$ be the triangle in $\mathbb R^2$ bounded by ($x \geq 0, y \geq 0$, $x+y\leq 1$). Suppose that the joint pdf of $X$ and $Y$ is given by
$$
f(x,y)=\begin{cases}
c,&\text{on the triangle }T \\
0,&\text{otherwise}
\end{cases}
$$
**Finding $c$:**

Area of $T$ is $\frac{1}{2}\times1\times1=\frac{1}{2}$ (since the triangle has its vertices at (0,0), (1,0) and (0,1)).

Since the total volume of the solid representing the probability must be 1, $c=1/ \frac{1}{2}=2$.

**Finding the probability** $\mathbb P(0\leq X\leq 1/2, 0\leq Y\leq \frac{1}{3})$:

The region is entirely within $T$, so the probability is given by the volume of a rectangular prism with length $1/2$, width $1/3$ and height $2$, thus $\mathbb P(0\leq X\leq 1/2, 0\leq Y\leq \frac{1}{3})=1/2\times 1/3 \times 2=1/3$.

Alternatively,
$$\mathbb P\left( 0\leq X\leq 1/2, 0\leq Y\leq \frac{1}{3} \right)=\int_0^{1/3}\int_0^{1/2}2\,dx\,dy=\frac{1}{3}$$

**Finding the marginal pdf of $X$**:

When $0\leq x\leq1$, we have
$$
f_X(x)=\int_{-\infty}^{\infty} f(x,y) \, dy=\int_{0}^{1-x} 2 \, dy =2(1-x) 
$$
Hence, the full answer is 
$$
f_X(x)=\begin{cases}
2(1-x),&\text{if }0\leq x\leq1, \\
0,&\text{otherwise}
\end{cases}
$$
---
Let $X$ and $Y$ denote the lifetime (in years) of an iPhone and an Android phone respectively. Suppose $X\sim \mathrm{exponential}(\alpha)$, $Y\sim \mathrm{exponential}(\lambda)$, and that $X$ and $Y$ are independent. Find the probability that the iPhone fails before the Android phone.

**Joint pdf**: Due to **independence**, the joint pdf is given by
$$
f(x,y)=f_X(x)f_Y(y)=\alpha e^{-\alpha x}\lambda e^{-\lambda y}
$$
if x ≥ 0 and y ≥ 0, and 0 otherwise.

We are interested in $\mathbb P(X<Y)$:
$$
\mathbb P(X<Y)=\iint_{x<y}f(x,y)\,dx\,dy
$$
**Region of integration**: Since the equation of the region is $x<y$, the region is equivalent to everything above the line $y=x$. Hence, $\iint_{x<y}$ resolves to $\iint_{0<x<y<\infty}$ (the lower bound 0 comes from the fact that both x ≥ 0 and y ≥ 0, and the upper bound ∞ comes from the lack of an upper bound stated in the question). When split, this double integral evaluates to $\int_{x=0}^{x=\infty}\int_{y=x}^{y=\infty}$.

Hence,
$$
\begin{align}
\mathbb P(X<Y)&=\iint_{x<y}f(x,y)\,dx\,dy \\
&=\int_{x=0}^{x=\infty}\int_{y=x}^{y=\infty}\alpha e^{-\alpha x}\lambda e^{-\lambda y}\,dy\,dx \\
&=\int_{x=0}^{x=\infty}\alpha e^{-\alpha x}\left[-e^{-\lambda y}\right]_{y=x}^{y=\infty}\,dx \\
&=\int_{x=0}^{x=\infty}\alpha e^{-\alpha x}e^{-\lambda x}\,dx \\
&=\int_{x=0}^{x=\infty}\alpha e^{-(\alpha+\lambda)x}\,dx \\
&=\left[ -\frac{\alpha}{\alpha+\lambda}e^{-(\alpha+\lambda)x} \right]_{0}^{\infty} \\
&=\frac{\alpha}{\alpha+\lambda}
\end{align}
$$
