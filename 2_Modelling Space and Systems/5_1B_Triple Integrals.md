# 5_1B_Triple Integrals

The triple integral of a continuous function $f(x, y, z)$over the solid region
$R = [a, b] \times [c, d] \times [p, q]$is a signed hypervolume given by

$$
\iiint_R f(x, y, z) \, dV =
\lim_{\Delta x, \Delta y, \Delta z \to 0}
\sum_{i,j,k} f(u_{ijk}, v_{ijk}, w_{ijk}) \Delta x \Delta y \Delta z
$$

where $(u_{ijk}, v_{ijk}, w_{ijk})$ is some point in the $(i,j,k)^{th}$ sub-box.

[[4_2_Double Integrals#Fubini's Theorem|Fubini's Theorem]] also applies.

## Cylindrical Coordinates

$$
\begin{align*}
x &= r\cos\theta \\
y &= r\sin\theta \\
z &= z \\
r &= \sqrt{x^2+y^2} \\
\theta &= \arctan(\frac{y}{x}) \text{ for } x > 0 \\
z &= z \\
dV &= r \, drd\theta dz
\end{align*}
$$

## Spherical Coordinates

$$
\begin{align*}
x &= \rho\sin\phi\cos\theta \\
y &= \rho\sin\phi\sin\theta \\
z &= \rho\cos\theta \\
\rho &= \sqrt{x^2+y^2+z^2} \\
\phi &= \arctan(\frac{\sqrt{x^2+y^2}}{z}) \text{ for } x > 0 \\
dV &= \rho^2\sin\phi\, d\rho\, d\theta\, d\phi
\end{align*}
$$

- **Note:** $0≤\theta≤2π, 0≤\phi≤π$
  - Using $\theta = 2\pi$, $\phi = 2\phi$ would give 2 spheres
