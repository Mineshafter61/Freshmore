
## Areas between curves
- Area between curves $y=f(x)$ and $y=g(x)$ for $a ≤ x ≤ b$
$$
\begin{gather}
A = \displaystyle\lim_{n \to \infty}\sum_{i=1}^n[f(x_i^*) - g(x_i^*)]\Delta x = \int_a^b[f(x) - g(x)] \, dx, \\
\text{ where } f(x) ≥ g(x) \text{ for all } x \in [a,b]
\end{gather}
$$
- Break the graph into sections where $f(x)$ intersects with $g(x)$
- Need to apply **negative** sign for sections where $g(x) > f(x)$
### Horizontally oriented curves
- Used when equations do not satisfy the vertical line test
	- 1 $x$ value maps to multiple $y$ values
	- i.e $y = ±\sqrt{2x+6}$
- Write $y$ in terms of $x$ (swap the roles of $x$ and $y$)
- Integrate w.r.t $y$
## Volumes of solids
- Cross sectional area is **perpendicular** to $x$-axis
- [Example](https://www.geogebra.org/m/ng7skevk)
- Volume with **cross-sectional area** $A(x)$ for $a ≤ x ≤ b$
- Find $A(x)$ in terms of a variable which **varies** the cross sectional area
$$
V = \int_a^b A(x) \, dx, \text{ where } A(x) \text{ is continuous}
$$
- A **cross-section** perpendicular to the x axis at a distance x away from the origin is a **triangle**.
- Relate $x$ with final given dimensions
### Solids of revolution
- Since the area of a circle is $π r^2$, and the area under an arbitrary point of a graph is given by $\int f(x)$, the volume of a solid of revolution is, by substituting $r=\int f(x)$: $$
π r^2 \implies π\left( \int_a^b f(x)\,dx \right)^2
$$
> Example: volume of a sphere
> $$
V = \int_{-r}^r A(x) \, dx = \int_{-r}^r π(r^2-x^2) \, dx = int_{0}^r 2π(r^2-x^2) = \frac{4}{3}π r^3
$$
### Volume bounded between 2 curves
- About the $x$-axis, $y=0$
	- $\displaystyle A(x) = π[(\text{outer radius})^2 - (\text{inner radius})^2]$
	- $\displaystyle V = \int_{\text{intersection 1}}^{\text{intersection 2}}A(x) \, dx$
- About a horizontal line, $y=n$
	- $r = n - y = n - f(x)$
	- $\displaystyle V = \int_{\text{intersection 1}}^{\text{intersection 2}} π[(n-f(x))^2 - (n-g(x))^2] \, dx$
- **Be careful of the outer and inner radius relative to the line of rotation**

> Example: Volume between $y=x$ and $y=x^2$, rotated about $x=-1$
> Outer radius: $1+\sqrt{y}$
> Inner radius: $1+y$
### Method of cylindrical shells
- Used when a volume is formed by a **single function**
- Finding volume of object about $y$-axis.
- Divides volume into $n$ small cylindrical shells with thickness $\Delta x=\frac{b-a}{n}$, as $n\to∞$
- Formula: $$
V=\lim_{n\to∞}\sum_{i=1}^{n}V_i=\lim_{n\to∞}\sum_{i=1}^{n}2π\,\bar{x_i}\cdot f(x)\cdot\Delta x=\int_a^b2πx\,f(x)\,dx 
$$
- $V_i = \text{circumference due to rotation about y-axis with radius } \bar{x}_i \text{ from the y-axis} \times \text{height of shell} \times \text{thickness of shell}$