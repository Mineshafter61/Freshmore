# 6_1_Line Integrals

- Integral along a line, $\gamma$
  - $f(x)$ in a scalar field
  - $\vec{F}(x)$ in a vector field (e.g. work done, flux, etc.)

## Parametrisation

- Parametrisation is the process of **specifying a function by one or more variables** called the parameters.
- A curve in $\mathbb{R}^3$ can be parametrised by some $x=f(t)$, $y=g(t)$, $z=h(t)$, where $t$ is a parameter. As we vary $t$, the point $(x,y,z)$ will trace out the curve.
- There are infinite ways to parametrise the same curve. One (naive) way is to let $x=t$, $y=f(x)$. This means that parametrisation is **not unique**.

### Parametrising Lines

The segment of the line $y=mx+c$ starting at $(x_{1},y_{1})$ and ending at $(x_{2},y_{2})$ can be parameterised by

$$
\vec{p}(t)=\begin{bmatrix}t \\ mt+c\end{bmatrix},t \in [x_{1},x_{2}]
$$

If only $(x_{1},y_{1},z_{1},\dots)$ and $(x_{2},y_{2}z_{2},\dots)$ are given, the line $\vec{p}(t)$ will be

$$
\vec{p}(t)=\begin{bmatrix}x_{1}\\y_{1}\\\vdots\end{bmatrix}+t\left(\begin{bmatrix}x_{1}-x_{2}\\y_{1}-y_{2}\\\vdots\end{bmatrix}\right)
$$

## Line Integrals of Scalar Fields

The **line integral** of a continuous function $f(x,y)$ **(scalar field)** along a smooth curve $\gamma$ is the **signed cross-sectional area** bounded by the surface $f(x,y)$ and the curve $\gamma$ (i.e., curved **line**) in the $xy$-plane given by

$$ \int_{\gamma} f(x,y) \, ds = \lim_{n \to \infty} \sum_{i=1}^{n} f(x_i, y_i) \Delta s_i.$$

From this we can derive

$$\Delta s = ||\vec{p^\prime}(t)|| \,dt$$

where

$$||\vec{p^{\prime}}(t)||=\sqrt{\left(\frac{d x}{d t}\right)^{2}+\left(\frac{d y}{d t}\right)^{2}}$$

For a continuous function $f : \mathbb{R}^n \rightarrow \mathbb{R}$, the line integral along a smooth curve $\gamma$ parametrised by $\vec{p} : [a,b] \rightarrow \mathbb{R}^n$ is given by

$$\int_{\gamma}f(x_{1},\cdots, x_{n})\,d s=\int_{a}^{b}f\left(\vec{p}(t)\right)\,||\vec{p^\prime}(t)||\,d t$$

The **length of curve** is $\int_\gamma 1 \,ds$, where we have set $f = 1$ (dimensionless)

### Extras

For helix,

$$\vec{p}(t)=\begin{bmatrix}\cos(t)\\\sin(t)\\t\end{bmatrix}$$

## Line Integrals of Vector Fields

Consider a continuous vector field $\vec{F}:\mathbb{R}^{n}\to\mathbb{R}^{n}$ and a smooth curve $\gamma$ in $\mathbb{R}^{n}$ parametrised by $\vec{p}:[a,b]\to\mathbb{R}^{n}$. The **tangential component** of $\vec{F}$ in the direction of, or **along**, $\gamma$ is a scalar field given by
$$
\vec{F}(\vec{p}(t))\cdot \frac{\vec{p}'(t)}{||\vec{p}'(t)||}
$$
The line integral, in the *scalar* field sense, of this tangential component is
$$
\int_{a}^{b} \vec{F}(\vec{p}(t))\cdot \frac{\vec{p}'(t)}{||\vec{p}'(t)||} ||\vec{p}'(t)||\, dt= \int_{a}^{b} \vec{F}(\vec{p}(t))\cdot \vec{p}'(t)\, dt
$$
This is known as a **line integral of a vector field along a curve**; it takes into account how much the curve follows along the field.

Final formula:
$$
\int_{\gamma}\vec{F}(\vec{p})\cdot d\vec{p}=\int_{a}^{b}\vec{F}(\vec{p}(t))\cdot\vec{p}^{\prime}(t)\,d t
$$
