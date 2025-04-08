# 2_1B_Directional Derivatives

- The directional derivative of a two-variable function $f$ at $(x_0,y_0)$ in the direction of a *unit vector* $\vec{u}=\begin{bmatrix}u_1\\u_2\end{bmatrix}$ is
$$D_{\vec{u}}f(x_0,y_0)=\lim_{ h \to 0 } \frac{f(x_0+h\,u_1, y_0+h\,u_2)-f(x_0,y_0)}{h}$$
provided the limit exists
- If the given vector $\vec{v}$ is **not a unit vector**, we let $\displaystyle\vec{u}=\frac{\vec{v}}{||\vec{v}||}$ (normalisation).
- The **quickest rate of increase** is simply $\nabla f$.

## Directional derivative from partial derivative

- Let f be a differentiable function of $x$ and $y$. The directional derivative of $f$ at $(x_0,y_0)$ in the direction of unit vector $\vec{u}=\begin{bmatrix}u_1\\u_2\end{bmatrix}$ is given by
$$D_{\vec{u}}f(x_0,y_0)=f_x(x_0,y_0) u_1 + f_y (x_0,y_0) u_2$$
- **Proof**: Consider

$$
\begin{align}
D_{\vec{u}}f(x_0,y_0)&=\lim_{ h \to 0 } \frac{f(x_0+h\,u_1, y_0+h\,u_2)-f(x_0,y_0)}{h} \\
&=\lim_{ h \to 0 } \frac{\Delta f}{h}
\end{align}
$$
Let $\Delta x=(x_0+hu_1)-x_0$ and $\Delta y=(y_0+hu_1)-y_0$. The tangent plane approximation gives
$$
\begin{align}
\Delta f &\approx f_x(x_0,y_0)\Delta x+f_y(x_0,y_0)\Delta y \\
&=f_x(x_0,y_0)hu_1+f_y(x_0,y_0)hu_2
\end{align}
$$
Rearranging, we get $\frac{\Delta f}{h}\approx f_x(x_0,y_0)u_1+f_y(x_0,y_0)u_2$. This approximation becomes exact as $h\to0$. Thus (2) becomes
$$
D_{\vec{u}}f(x_0,y_0)=f_x(x_0,y_0)u_1+f_y(x_0,y_0)u_2
$$
