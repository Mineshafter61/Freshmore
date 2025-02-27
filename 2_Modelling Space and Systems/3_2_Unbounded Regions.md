## Completing the Square
1. Compute $\nabla f$ by finding $f_x$ and $f_y$
2. Equate $\nabla f = \vec{0}$
3. Complete the square for the equation
	- Recall $(x+a)^2 = x^2 + 2ax + a^2$
*Example*
Consider the function $f(x,y)=x^2+3x+y^2-2y$ where $x,y ∈ \mathbb{R}$. Find the global extrema of $f$.
> First we compute $\nabla f$, i.e. $f_{x}=2x+3$ and $f_{y}=2y-2$. Setting $\nabla f=\vec{0}$, we get the point $-\frac{3}{2},1$ and $f\left( -\frac{3}{2},1 \right)=-\frac{13}{4}$.
> Notice that we can rewrite the function as follows:
$$
\begin{align*}
f(x,y)&=x^{2}+3x+y^2-2y \\
&=x^{2}+2 \frac{3}{2}x+\left( \frac{3}{2} \right)^{2}+y^{2}-2y+1-\left( \frac{3}{2} \right)^{2}-1 \\
&=\left( x+\frac{3}{2} \right)^{2}+(y-1)^{2}-\frac{13}{4}
\end{align*}
$$
> It is clear that the first two terms are non-negative and the function is always greater than or equals to $-\frac{13}{4}$.
> We can conclude that $f$ has a global minimum value of $-\frac{13}{4}$ at the point $\left( -\frac{3}{2},1 \right)$.

## AM-GM Inequality
- For **non-negative real numbers** $x_1+x_2+\dots+x_n$, the arithmetic mean is always at least the geometric mean. That is, 
$$\frac{x_1+x_2+\dots+x_n}{n}>\sqrt[n]{x_1x_2\dots x_n}$$
- If $x_1=x_2=\dots=x_n$,
$$\frac{x_1+x_2+\dots+x_n}{n}=\sqrt[n]{x_1x_2\dots x_n}$$
- Sub $(x_1, y_1)$ obtained from $\nabla f = \vec{0}$ into the RHS of the inequality to determine global minimum (via ≥)
## Gradient Vector's Direction
TODO