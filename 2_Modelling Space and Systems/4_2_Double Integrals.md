- For integration, where $n$ is the number of subintervals, $\Delta x = \frac{b − a}{n}$ is the length of each subinterval and $c_k$ is a point in the $k^{th}$ interval
$$
\text{Signed Area} = \int_{a}^{b}\,f(x)\,d x\,\longrightarrow\,\lim_{ n \to \infty }\sum_{k=1}^{n}\,f(c_{k})\,\Delta x
$$
- The definite integral of a continuous function $f(x,y)$ over the region $R=[a,b]\times[c,d]$ is
$$
\text{signed volume}=\iint_{R} f(x,y)\,dA=\lim_{ \Delta x,\Delta y \to 0 } \sum i,j(u_{ij},v_{ij})\Delta x\Delta y
$$
> - where $(u_{ij},v_{ij})$ is some point in the $(i,j)$<sup>th</sup> rectangle.
> - Such an integral is called a **double integral**.
## Iterated Integrals
### Fubini's Theorem
- Let $R$ be the bounded rectangular region $[a,b]\times[c,d]$. If $f(x,y)$ is continuous on $R$, then
$$
\iint f(x,y)dA=\int_{a}^{b}\int_{c}^{d} f(x,y)\,dy\,dx=\int_{c}^{d}\int_{a}^{b} f(x,y)\,dx\,dy
$$
- More generally, this is true if:
	- $f$ is bounded on $R$ and discontinuous only at a finite number of smooth curves, or
	- $f$ is non-negative and $R$ does not need to be bounded.
- *Example:*
$$
\begin{align}
\int_{0}^{2}\int_{0}^{2} 16-x^2-2y^2\,dx\,dy&=\int_{0}^{2}\left[ 16x-\frac{x^3}{3} -2y^2x\right]\,dy \\
&=\left[  \left[  16xy-\frac{x^3y}{3}-\frac{2y^3x}{3}  \right]_{x=0}^{x=2} \right]_{y=0}^{y=2} \\
&=\left[ 32y-\frac{8}{3}y-\frac{4y^3}{3} \right]_{y=0}^{y=2} \\
&=64-\frac{16}{3}-\frac{32}{3} \\
&=48
\end{align}
$$
## General Regions
- Not a rectangle
- **Vertically simple** and **horizontally simple** are properties of the **REGION**, not the function.
### Vertically simple
- Describable by $a≤x≤b$, $y_1(x)≤y≤y_2(x)$ where $y_1(x)$ and $y_2(x)$ are continuous functions of $x$ on $[a,b]$.
- If $R$ is vertically simple, then
$$
\iint_R f(x,y) dA=\int_{a}^{b}\int_{y_1(x)}^{y_2(x)} f(x,y)\,dy\,dx 
$$
### Horizontally simple
- Describable by $a≤y≤b$, $x_1(y)≤x≤x_2(y)$ where $y_1(x)$ and $y_2(x)$ are continuous functions of $x$ on $[a,b]$.
- If $R$ is horizontally simple, then
$$
\iint_R f(x,y) dA=\int_{a}^{b}\int_{x_1(y)}^{x_2(y)} f(x,y)\,dx\,dy 
$$
### Guidelines for evaluating a double integral
- **Sketch** the integration region (this tells you the limit).
- Determine whether it is vertically or horizontally simple, and pick the correct formula to use.
- Sometimes, doing the iterated integral in a different order can simplify calculations.