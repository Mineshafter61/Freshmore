

## Implicit Differentiation
- Implicit differentiation can be used for multivariable functions when $z$ is implicitly defined in terms of $x$ and $y$, and solving for z may be difficult.
- **Example**:
> Find the tangent plane to $x^2+y^2-z^2=0$ at the point $(3,4,5)$.
> Note that $z=f(x,y)$ is a function of $x$ and $y$, but $x$ does not depend on $y$ and $y$ does not depend on $x$.
> $$
2x-2z \frac{\partial z}{\partial x}=0 \implies \frac{\partial z}{\partial x}=\frac{x}{z}; 2y-2z \frac{\partial z}{\partial y}=0\implies \frac{\partial z}{\partial y}=\frac{y}{z}
$$
> The equation of the tangent plane is therefore:
> $$
\begin{align}
z&=z_0+f_x(x_0,y_0)(x-x_0)+f_y(x_0,y_0)(y-y_0) \\
&=z_0+\frac{x_0}{z_0}(x-x_0)+\frac{y_0}{z_0}(y-y_0)=5+\frac{3}{5}(x-3)+\frac{4}{5}(y-4)
\end{align}
$$
### Implicit Function Theorem
If $\frac{\partial F}{\partial z}\neq 0$ at a point $(x_{0},y_{0},z_{0})$ on a surface $F(x,y,z)=c$, then in a neighbourhood of this point, the surface defines a unique function $z=f(x,y)$ whose partial derivatives are $$
\frac{\partial z}{\partial x}=-\frac{\partial F / \partial x}{\partial F / \partial z},\frac{\partial z}{\partial y}=-\frac{\partial F / \partial y}{\partial F / \partial z}
$$