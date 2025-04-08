# 6_2A_Conservative Vector Fields

A vector field $\vec{F}:\mathbb{R}^n\to \mathbb{R}^n$ is called **conservative** if there exists an $\vec{f}:\mathbb{R}^n\to \mathbb{R}^n$ such that
$$
\vec{F}=\nabla f
$$
that is, $\vec{F}$ is the gradient of a scalar field. In this situation, $f$ is called a **potential function** for $\vec{F}$.

Steps:

1. Do partial differentiation on $\vec{F}(x,y)$ to obtain $f_x$ and $f_y$
2. Integrate $f_x$ w.r.t $x$ to obtain $f = \cdots + \phi(y)$, and the integration constant becomes an **ansatz** $\phi (y)$, some function of $y$ only
3. Differentiate this integrated value from (2) to obtain $f_y = \cdots + \frac{d\phi}{dy}$
4. Integrate $\frac{d\phi}{dy}$ to obtain $\phi$
5. Sub $\phi$ back into the integrated $f_x$ equation in (2) to obtain a new $f(x, y)$. If conservative, the partial derivatives should be equivalent to the original $f(x)$ and $f(y)$ respectively

## Gradient theorem

Let $\vec{F} = \nabla f$ be a **conservative vector field** from $\mathbb{R}^n$ to $\mathbb{R}^n$ and $\gamma$ be *any* differentiable curve in $\mathbb{R}^n$ parameterised by $\vec{p}:[a,b]\to \mathbb{R}^n$. Then
$$
\int_\gamma \vec{F}(\vec{p})\cdot d\vec{p}=f(\vec{p}(b))-f(\vec{p}(a))
$$
That is, if the vector field is **conservative**, the line integral of this vector field is **path independent**. Only the end points matter. (integration not needed!)

### Observations

- For closed loop $\gamma$, $\oint_\gamma \vec{F}(\vec{p})\cdot d\vec{p}=0$.
