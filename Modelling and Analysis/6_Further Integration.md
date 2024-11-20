## Improper integrals
- Definite integral when the **interval** is **infinite**
	- **Convergent** if the corresponding (final value) limit exists
	- **Divergent** if the corresponding (final value) limit does not exist
1. Provided that this limit exists (i.e. a finite number), if $\int_{a}^{b} f(x) \, dx$ exists for every number $b ≥ a$, then $$ \int_{a}^{\infty}f(x)\,dx=\lim_{b\to \infty}\int_{a}^{b}f(x)\,dx $$
2. Provided that this limit exists (i.e. a finite number), if $\int_{a}^{b} f(x) \, dx$ exists for every number $a ≥ b$, then $$ \int_{-\infty}^{b}f(x)\,dx=\lim_{a\to -\infty}\int_{a}^{b}f(x)\,dx $$
3. If the improper integrals $\int_{a}^{\infty} f(x) \, dx$ and $\int_{-\infty}^{a} f(x) \, dx$ are convergent, then we define the sum $\int_{-\infty}^{\infty} f(x) \, dx$ to also be convergent, where $a$ is any real number

> Example:
> $$\begin{align}\int_{-\infty}^{\infty} \frac{1}{1+x^2} \, dx&=\int_{-\infty}^{0}\frac{1}{1+x^2}\,dx+\int_{0}^{\infty}\frac{1}{1+x^2}\, dx \\
&=\lim_{ b \to -\infty }\int_{b}^{0}\frac{1}{1+x^2}\,dx+\lim_{ b \to \infty } \int_{0}^{b} \frac{1}{1+x^2}\,dx \\
&=\lim_{ b \to -\infty }[\tan^{-1}x]_{b}^{0}+\lim_{ b \to \infty }[\tan^{-1}x]_{0}^{b} \\
&=\lim_{ b \to -\infty }[\tan^{-1}0-\tan^{-1}b]+\lim_{ b \to \infty }[\tan^{-1}b-\tan^{-1}0] \\
&=-\tan^{-1}(-\infty)+\tan^{-1}(\infty) \\
&=-\left( -\frac{π}{2} \right)+\frac{π}{2} \\
&=π\end{align}
$$
### Finding convergence/divergence
- Find integral for edge case
- Find integral for non-edge case
- Determine the $<$ and $>$ between the edge cases

> Example: For what values of $p$ is $\int_{1}^{\infty} \frac{1}{x^p} \, dx$ convergent?
> $$\begin{gather}
p=1: \int_{1}^{\infty} \frac{1}{x^{p}} \, dx=\lim_{ b \to \infty } \int_{1}^{b} \frac{1}{x}\,dx=\lim_{ b \to \infty }[\ln(x)]_1^b=\lim_{ b \to \infty } [\ln b-1]=\infty \\
p\neq1: \int_{1}^{\infty} \frac{1}{x^{p}} \, dx=\lim_{ b \to \infty } \int_{1}^{b} \frac{1}{x^p}\,dx=\lim_{ b \to \infty } \left[\frac{x^{-p+1}}{-p+1}\right]_1^b=\lim_{ b \to \infty } \frac{1}{1-p}\left[ \frac{1}{b^{p-1}}-1 \right]\\
p>1\implies(p-1)>0\implies \lim_{ b \to \infty } b^{p-1}=\infty \implies \lim_{ b \to \infty } \frac{1}{b^{p-1}}=0\\\implies \lim_{ b \to \infty } \frac{1}{1-p}\left[ \frac{1}{b^{p-1}}-1 \right]=-\frac{1}{1-p}=-\frac{1}{p-1}\\
p<1 \implies (p-1)<0 \implies\lim_{ b \to \infty } b^{p-1}=0 \implies \lim_{ b \to \infty } \frac{1}{b^{p-1}}=\infty\\
\implies\lim_{ b \to \infty } \frac{1}{1-p}\left[ \frac{1}{b^{p-1}}-1 \right]=\infty\\
∴ \int_{1}^{\infty} \frac{1}{x^{p}}\,dx \text{ converges when } p>1 \text{ and diverges when } p≤1
\end{gather}$$
### Discontinuity in f(x)
1. If $f$ is continuous on $[a,b)$ and is discontinuous at $b$, then $\displaystyle\int_{a}^{b} f(x) \, dx =\lim_{ t \to b^- } \int_{a}^{t} f(x) \, dx$ if this limit exists.
2. If $f$ is continuous on $(a,b]$ and is discontinuous at $a$, then $\displaystyle\int_{a}^{b} f(x) \, dx =\lim_{ t \to a^+ } \int_{t}^{b} f(x) \, dx$ if this limit exists.
3. If $f$ has a **discontinuity** at $c$, where $a < c < b$, and both $\int_a^c f(x) \, dx$ and $\int_c^b f(x) \, dx$ are convergent, then we define $\displaystyle\int_{a}^{b} f(x) \, dx=\int_{a}^{c} f(x) \, dx+\int_{c}^{b} f(x) \, dx$

> Example:
> $$\begin{align}
\int_{0}^{π/2}\sec(x)\,dx &=\lim_{t\toπ/2^-}\int_{0}^{t} \sec(x)\,dx \\
&=\lim_{t\toπ/2^-}[\ln|\sec x+\tan x|]_0^t \\
&=\lim_{t\toπ/2^-}[\ln|\sec t+\tan t|-\ln|\sec 0+\tan 0|] \\
&=\lim_{t\toπ/2^-}[\ln|\sec t+\tan t|-\ln(1+0)] \\
&=\lim_{t\toπ/2^-}[\ln|\sec t+\tan t|] \\
&=\ln|\sec (π/2^-)+\tan (π/2^-)| \\
&=\infty
\end{align}
$$
### Laplace Transform
- If $f(t)$ is continuous for $t ≥ 0$, then the *Laplace transform* of the function $F$ is defined by
$$
F(s) = \int_0^\infty f(t)e^{-st}dt
$$
and the domain of $F$ is the set consisting of all numbers $s$ for which the integral converges
### Probability density function
- The probability density function (pdf) of a random variable $X$ satisfies the condition $f(x) ≥ 0$ for all real values of $x$
- Because probabilities (area under the curve) are measured from 0 to 1, it follows that
$$
\int_{-\infty}^{\infty}f(x)\,dx=1
$$
### Median
- Half the population have a variable less than $m$ while the other half have the same variable more than $m$.
$$
\int_{m}^{\infty}f(x)\,dx=\frac{1}{2}
$$
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
- Since the area of a circle is $π r^2$, and the area under an arbitrary point of a graph is given by $\int f(x)$, the volume of a solid of revolution is, by substituting $r=f(x)$: $$
π r^2 \implies π\left( \int_a^b f(x)\,dx \right)^2
$$
> Example: volume of a sphere
> $$
V = \int_{-r}^r A(x) \, dx = \int_{-r}^r π(r^2-x^2) \, dx = int_{0}^r 2π(r^2-x^2) = \frac{4}{3}π r^3
$$
- Similarly, for volume bounded between 2 curves,
	- About the $x$-axis, $y=0$
		$$
		A(x) = π[(\text{outer radius})^2 - (\text{inner radius})^2] \\
		V = \int_{\text{intersection 1}}^{\text{intersection 2}}A(x) \, dx
		$$
	- About a horizontal line, $y=n$
		- $r = n - y = n - f(x)$
		$$
		V = \int_{\text{intersection 1}}^{\text{intersection 2}} π[(n-f(x))^2 - (n-g(x))^2] \, dx
		$$
	- **Be careful of the outer and inner radius relative to the line of rotation**

## Arc Length
- For two points $(x_1, y_1)$ and $(x_2, y_2)$, the length $l$ between them is given by $l=\sqrt{(x_2-x_1)^2+(x_2-x_1)^2}$.
- If there are many segments on the line, arc length of each segment $\Delta s_i = \sqrt{(\Delta x)^2 + (\Delta y)^2}$ where $\Delta x$ is fixed while $\Delta y$ is kept variable to accommodate for vertical variations in the curve.
- The total length s of a continuous and differentiable curve $y=f(x)$ is defined over the interval $a ≤ x ≤ b$ is given by
$$\begin{align}s &= \lim_{n \to \infty} \sum_{i=1}^n \Delta s_i \\&= \lim_{n \to \infty} \sum_{i=1}^n \sqrt{(\Delta x)^2 + (\Delta y)^2} \\&= \lim_{n \to \infty} \sum_{i=1}^n \sqrt{1+\left(\frac{\Delta y}{\Delta x}\right)^2}\cdot \Delta x \\ &= \lim_{i=1} \sum_{i=1}^n \sqrt{1+(f'(x_i^*)^2}\cdot \Delta x \\&= \int_a^b \sqrt{1+[f'(x)]^2}\,dx\end{align}$$
- If the curve is expressed as $x=f(y)$, our formula for arc length is $\int_a^b \sqrt{1+[f'(y)]^2}\,dy$
### Trigonometric substitution
| Expression       | Substitution                              | Expression evaluation             |
| ---------------- | ------------------------------------ | ------------------------------------------ |
| $\sqrt{a^2-x^2}$ | $x=a\sin \theta, dx=a\cos \theta\,d\theta$              | $\sqrt{a^2-a^2\sin \theta}=a\cos \theta$  |
| $\sqrt{a^2+x^2}$ | $x=a\tan \theta, dx=a\sec^2 \theta\,d\theta$            | $\sqrt{a^2+a^2\tan^2 \theta}=a\sec \theta$ |
| $\sqrt{x^2-a^2}$ | $x=a\sec \theta, dx=a\sec^2 \theta \tan^2\theta\,d\theta$ | $\sqrt{a^2\sec^2\theta-a^2}=a\tan \theta$  |
> Example: arc length of $y^2=x$ from $(0,0)$ to $(1,1)$
> $$
\begin{align}
g(y)&=y^2 \implies g'(y)=2y \\
\text{Arc length }s&=\int_{0}^{1} \sqrt{1+[2y]^2} \, dy =\int_{0}^{1} \sqrt{1+4y^2} \, dy \\
\text{Let } y &:= \frac{\tan\theta}{2}, dy := \frac{\sec^2\theta}{2}\,d\theta \\
\sqrt{1+4y^2}&=\sqrt{1+\tan^2\theta}=\sec \theta \\
\implies\int \sqrt{1+4y^2} \, dy&=\int \sec(\theta)\, \frac{\sec^2 \theta}{2} \, d\theta=\frac{1}{2}\int \sec^3\theta\,d\theta \\
\text{Using integration by parts with }& f=\sec \theta \implies f'(\theta)=\sec \theta \tan \theta, g'(\theta)=\sec^2(\theta)=
\end{align}
$$
//todo
## Areas of Surface of Revolution
- Formed when a curve is rotated about a line
- Formula for the surface area of the i-th band of the surface area is $$\begin{align}
S_i&=2πrl\\&=π\cdot r\cdot \Delta s_i\\&=2π\frac{(y_{i-1}+y_{i})}{2}\cdot\sqrt{1+(f'(x_i^*))^2}\,\Delta x\\&=π \cdot[2f(x_i^*)]\cdot\sqrt{1+(f'(x_i^*))^2}\,\Delta x
\end{align}$$ as when $n \to \infty, f(x_{i-1})=f(x_{i})$
- This is also the average radius of the approximating band. Thus, the surface area of the object is $$
\begin{align}
S&=\lim_{ n \to \infty } \sum_{i=1}^{n}S_{i} \\
&=\lim_{ n \to \infty } \sum_{i=1}^{n}π \cdot[2f(x_i^*)]\cdot\sqrt{1+(f'(x_i^*))^2}\,\Delta x \\
&=\int_{a}^{b} 2π\,f(x)\sqrt{1+[f'(x)]^{2}} \, dx  \\
&=\int 2πy\,ds \\
\text{where } y&=f(x), \\
s&=\int_{a}^{b}\sqrt{1+[f'(x)]^{2}} \, dx, \\
ds&=\sqrt{1+[f'(x)]^{2}}
\end{align}
$$
- Likewise, if the curve is described by $x=f(y)$, the formula is $S=\int_{a}^{b}2π\,f(y)\sqrt{1+[f'(y)]^{2}}\,dy=\int2πx\,ds$