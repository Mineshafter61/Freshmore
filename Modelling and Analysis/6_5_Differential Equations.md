### Separable equations
- Separate $x$ and $y$ terms into 2 groups
$$
\begin{align}
\frac{dy}{dx} &= \frac{h(x)}{g(y)} \\
g(y)dy &= h(x)dx \\
\int g(y) \, dy &= \int h(x) \, dx
\end{align}
$$
### Logistic differential equation
- Form: $\frac{dy}{dt}=k\left(1-\frac{y}{L}\right)y$
	- When $y > L, \frac{dy}{dt} < 0$
	- When $y < L, \frac{dy}{dt} > 0$
	- When $y = L, \frac{dy}{dt} = 0$
- Solving: $$
\begin{align}
\frac{dy}{dt}&=k\left(1-\frac{y}{L}\right)y \\
\implies\frac{dy}{ky\left(1-\frac{y}{L}\right)}&=dt \\
\implies \int\frac{dy}{ky\left(1-\frac{y}{L}\right)}&=\int dt \\
\implies \frac{1}{k}\int\frac{dy}{y\left(1-\frac{y}{L}\right)}&=t+c
\end{align}
$$
- Solving the left side: **Use partial fractions**
$$
\begin{align}
\text{Let }\frac{1}{y\left(1-\frac{y}{L}\right)}&=\frac{A}{y}+\frac{B}{1-\frac{y}{L}} \\
&=\frac{A\left( 1-\frac{y}{L} \right)+By}{y\left( 1-\frac{y}{L} \right)} \\
1&=A\left( 1-\frac{y}{L} \right)+By \\
A+y\left( -\frac{A}{L}+B \right)&=1 \\
A=1&,-\frac{A}{L}+B=0\implies B=\frac{A}{L}=\frac{1}{L}
\end{align}
$$
