## Tangent plane
- The tangent plane to a surface at a point is a plane that “best approximates” the surface near the point
- Equation of a tangent plane to a surface $z=f(x,y)$ at a point $P=(x_0,y_0,f(x_0,y_0)): $$z=f(x_0,y_0)+f_x(x_0,y_0)(x−x_0)+f_y(x_0,y_0)(y−y_0)$$
- The equation can also be written as $$z-z_0=f_x(x_0,y_0)(x−x_0)+f_y(x_0,y_0)(y−y_0)$$
## Tangent Plane Approximation
- The tangent plane is very close to the surface near the point of contact
- We can approximate the surface value near the point by using the value of the plane near that point
- The tangent plane approximation to a differentiable function $f$ of two variables $x$ and $y$ near the point $(x_0,y_0)$ is given by (same as above): $$f(x,y)≈f(x_0,y_0)+f_x(x_0,y_0)(x−x_0)+f_y(x_0,y0_)(y−y0)$$, i.e. we approximate $f(x,y)$ by the $z$-value of the tangent plane.
## Directional Derivatives
- The directional derivative of a two-variable function $f$ at $(x_0,y_0)$ in the direction of a *unit vector* $\vec{u}=\begin{bmatrix}u_1\\u_2\end{bmatrix}$ is $$D_{\vec{u}}f(x_0,y_0)=\lim_{ h \to 0 } \frac{f(x_0+h\,u_1, y_0+h\,u_2)-f(x_0,y_0)}{h}$$, provided the limit exists
- If the given vector $\vec{v}$ is **not a unit vector**, we let $\displaystyle\vec{u}=\frac{\vec{v}}{||\vec{v}||}$ (normalisation).
### Directional derivative from partial derivative
- Let f be a differentiable function of $x$ and $y$. The directional derivative of $f$ at $(x_0,y_0)$ in the direction of unit vector $\vec{u}=\begin{bmatrix}u_1\\u_2\end{bmatrix}$ is given by $$D_{\vec{u}}f(x_0,y_0)=f_x(x_0,y_0) u_1 + f_y (x_0,y_0) u_2$$
- **Proof**: Consider 
$$
\begin{align}
D_{\vec{u}}f(x_0,y_0)&=\lim_{ h \to 0 } \frac{f(x_0+h\,u_1, y_0+h\,u_2)-f(x_0,y_0)}{h} \\
&=\lim_{ h \to 0 } \frac{\Delta f}{h}&(1)
\end{align}
$$
Let $\Delta x=(x_0+hu_1)-x_0$ and $\Delta y=(y_0+hu_1)-y_0$. The tangent plane approximation gives
$$
\begin{align}
\Delta f &\approx f_x(x_0,y_0)\Delta x+f_y(x_0,y_0)\Delta y \\
&=f_x(x_0,y_0)hu_1+f_y(x_0,y_0)hu_2
\end{align}
$$
Rearranging, we get $\frac{\Delta f}{h}\approx f_x(x_0,y_0)u_1+f_y(x_0,y_0)u_2$. This approximation becomes exact as $h\to0$. Thus (1) becomes
$$
D_{\vec{u}}f(x_0,y_0)=f_x(x_0,y_0)u_1+f_y(x_0,y_0)u_2
$$
## Gradient Vector
- The expression for $D_{\vec{u}}f(x_0,y_0)$ could also be written as a dot product of $\vec{u}$ and another vector:
$$
\begin{align*}
D_{\vec{u}}f(x_0,y_0)&=f_x(x_0,y_0)u_1+f_y(x_0,y_0)u_2\\
&=\begin{bmatrix}
f_x(x_0,y_0)\\f_y(x_0,y_0)
\end{bmatrix}\cdot \begin{bmatrix}
u_1\\u_2
\end{bmatrix}\\&=\nabla f(x_0,y_0)\cdot \vec{u}
\end{align*}
$$
- Gradient vector function: 
$$
\nabla f(x,y)=\begin{bmatrix}
f_x(x,y)\\f_y(x,y)
\end{bmatrix}=f_x(x,y)\vec{e}_{1}+f_y(x,y)\vec{e}_{2}
$$
- where $\vec{e}_{1} = \begin{bmatrix}1\\0\end{bmatrix}, \vec{e}_{2}=\begin{bmatrix}0\\1\end{bmatrix}$
### Higher dimensions
- For higher dimensions, we consider a function $f(x_1,\dots,x_n)$, $x_i\in\mathbb{R}^n$.
- The gradient is
$$
\begin{align*}
\nabla f(x_1,\dots,x_n)&=f_{x_1}\vec{e}_1+f_{x_2}\vec{e}_2+\dots+f_{x_n}\vec{e}_n\\
&=\begin{bmatrix}
f_{x_1}\\f_{x_2}\\ \vdots \\f_{x_n}
\end{bmatrix}
\end{align*}
$$
- Here $f_{x_{i}}$ are functions of $x_{1},\dots,x_n$.
### Geometric properties
- If $f$ is a differentiable function at the point $(x_0, y_0)$ and $\nabla f(x_0, y_0) \neq \vec{0}$
    - The maximum rate of increase of $f$ is in the direction of $\nabla f(x_0, y_0)$, perpendicular to the contour of $f$ through $(x_0, y_0)$.
    - The magnitude of the gradient vector $||\nabla f||$ is the maximum rate of change of $f$ at that point, large when contours are close together and small when they are far apart.
- Contour lines in gradient descent:
    - Gradient vector is $\vec{0}$ at the point tangent to the contour line.