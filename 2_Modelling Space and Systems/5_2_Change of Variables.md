## Steps
1. Let $x=g(u,v)$ and $y=h(u,v)$
2. Vertices of the integration region $R$ (in $x, y$, this is NOT a rectangle) :
	1. $(x_0,y_0)=(g(u_0,v_0),h(u_0,v_0))$
	2. $(x_1,y_1)=(g(u_0+\Delta u,v_0),h(u_0+\Delta u,v_0))$
	3. $(x_2,y_2)=(g(u_0,v_0+\Delta v),h(u_0,v_0+\Delta v))$
3. When $\Delta u\to 0$ and $\Delta v\to 0$, the integration region $R$ is approximately a parallelogram. The edge vectors of this parallelogram are:
$$
\begin{align}
\begin{bmatrix} g(u_0+\Delta u,v_0) \\ h(u_0+\Delta u,v_0) \end{bmatrix} - \begin{bmatrix} g(u_0,v_0) \\ h(u_0,v_0) \end{bmatrix} = \begin{bmatrix} \frac{\Delta g}{\Delta u} \\ \frac{\Delta h}{\Delta u} \end{bmatrix}\Delta u \\
\begin{bmatrix} g(u_0,v_0+\Delta v) \\ h(u_0,v_0+\Delta v) \end{bmatrix} - \begin{bmatrix} g(u_0,v_0) \\ h(u_0,v_0) \end{bmatrix} = \begin{bmatrix} \frac{\Delta g}{\Delta v} \\ \frac{\Delta h}{\Delta v} \end{bmatrix}\Delta v
\end{align}
$$
4. The parallelogram has an area $\Delta A$. The area is given by the magnitude of the **cross product** of these vectors
$$
\Delta A=\left|\left| \begin{bmatrix} \frac{\Delta g}{\Delta u}\\\frac{\Delta h}{\Delta u}\\0 \end{bmatrix} \times \begin{bmatrix} \frac{\Delta g}{\Delta v}\\\frac{\Delta h}{\Delta v}\\0 \end{bmatrix} \right|\right|\Delta u\Delta v=\left|\left| \begin{bmatrix} 0\\0\\ \frac{\Delta g}{\Delta u}\frac{\Delta h}{\Delta v} - \frac{\Delta g}{\Delta v}\frac{\Delta h}{\Delta u} \end{bmatrix} \right|\right|\Delta u\Delta v
$$
5. In the limit $∆u,∆v→0$, the area of the parallelogram tends to the the area of $R$. Thus the area element $dA= dxdy$ in the xy-plane can be expressed in terms of the variables $u$ and $v$. That is
$$
dxdy=dA=|g_uh_v-g_vh_u|dudv
$$
- $|g_uh_v-g_vh_u|$ is the Jacobian.
## Jacobian
- The Jacobian of the transformation given by $x=g(u,v)$ and $y=h(u,v)$ is
$$
\begin{vmatrix} g_u&g_v \\ h_u&h_v \end{vmatrix}=g_uh_v-g_vh_u
$$
- $\begin{vmatrix} g_u&g_v \\ h_u&h_v \end{vmatrix}$ is the determinant of the matrix $\begin{bmatrix} g_u&g_v \\ h_u&h_v \end{bmatrix}$.
## General Approach
1. Propose a one-to-one transformation that changes the region of integration $R$ to a region of integration $S$.
2. Find bounds on region of integration $S$.
3. Find the Jacobian $|g_uh_v -g_vh_u|$.
4. Check to see if we can express our answer in terms of elementary functions. That is the integral becomes easier to integrate. If yes, declare success. Otherwise, repeat Step 1.

*Example*:
Let R be a square with corners at $(x,y)=(0,0),(1,1),(2,0),(1,-1)$. Consider the integral $\iint_Rf(x,y)\,dxdy$ and the change of variables $x=u+v$ and $y=u-v$.

> $g(u,v)=x=u+v$, $h(u,v)=y=u-v$
> $g_u=1,g_v=1,h_u=1,h_v=-1$
> The new integral will therefore be $\iint_R f(u+v,u-v) |(1)(-1)-(1)(1)|\,dudv=\iint_R 2f(u+v,u-v)\,dudv$
## Vector Fields
Let $D$ be a set in $\mathbb{R}^n$. A **vector field** on $D$ is a vector-valued function $\vec{F}$ that assigns to each point $(x,y,z,...)$ in $D$ a n-dimensional vector $\vec{F}(x,y,z,...)$
