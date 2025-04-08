# 2_1C_Gradient

## Gradient Vector

- The expression for $D_{\vec{u}}f(x_0,y_0)$ could also be written as a dot product of $\vec{u}$ and the gradient vector:

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
