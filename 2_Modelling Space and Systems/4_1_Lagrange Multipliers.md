## Geometrical Meaning
- We illustrate the geometrical meaning with an example.
### Preamble
- We consider $f(x, y) = x + y$ subject to the constraint $x^2 + y^2 = 1$.
- The level curves of $f$ and the constraint are shown, with notable points $P_1, P_2, P_3$.
![[MSS_lagrangian.png]]
- **Observations:**  
	- At $P_1$, moving clockwise increases the function value, so $P_1$ is **not a maximum**.
	- We seek the maximum of $f$ along the circle constraint.
### Geometrical Meaning of Gradients
- At point $P_2$ (**potential maximum**):
	- The gradient of $f$ is $\nabla f\left(\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}\right) = \begin{bmatrix}1\\1\end{bmatrix}$.
	- The gradient of $g$ is $\nabla g\left(\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}\right) = \begin{bmatrix}\frac{\sqrt{2}}{\sqrt{2}}\\\frac{\sqrt{2}}{\sqrt{2}}\end{bmatrix}$.
	- **Key Insight:**  $\nabla f$ and $\nabla g$ are parallel at $P_2$.

- At point $P_3$ (**potential minimum**):
	- The gradient of $g$ is $\nabla g\left(-\frac{1}{\sqrt{2}}, -\frac{1}{\sqrt{2}}\right) = -\begin{bmatrix}\frac{\sqrt{2}}{\sqrt{2}}\\\frac{\sqrt{2}}{\sqrt{2}}\end{bmatrix}$.
	- Here, $\nabla f$ and $\nabla g$ are anti-parallel.
- **Conclusion:**  
	- At optimal points, $\nabla f$ and $\nabla g$ are either **parallel** or **anti-parallel**.  
	- Mathematically:  
    $$
    \nabla f(x_0, y_0) + \lambda \nabla g(x_0, y_0) = \mathbf{0}
    $$
		where $\lambda \in \mathbb{R}$ is the **Lagrange Multiplier**.
	- Note that $\nabla g(x_0,y_0)\neq \vec{0}$ and $x_0,y_0$ is not an endpoint of the constraint.
### Key Insights on Lagrange Multipliers
- **Optimal Points** occur when the gradients of $f$ and $g$ **align** or are in **opposite directions**.
- The **sign of $\lambda$** indicates whether the gradients are **parallel** ($\lambda > 0$) or **anti-parallel** ($\lambda < 0$).
- This method generalises the idea of constrained optimisation, providing a clear geometric interpretation.
### Takeaway
The geometric insight behind Lagrange multipliers is that the maximum and minimum of a function under a constraint occur when the function's gradient is parallel (or anti-parallel) to the gradient of the constraint. The Lagrange multiplier $\lambda$ captures the relationship between these gradients.
## Lagrange Multipliers
- **Theorem**: Let $(x_0,y_0)$ be a local maximum (or minimum) of $f(x,y)$ subject to a constraint $g(x,y) = 0$. There exits a **unique** Lagrange Multiplier $λ∈\mathbb{R}$ such that
$$
\nabla f(x_0,y_0)+\lambda \nabla g(x_0,y_0)=\vec{0}
$$
	where $\nabla g(x_0,y_0)\neq \vec{0}$ and $x_0,y_0$ is not an endpoint of the constraint.
- Other method (Lagrangian function): $L(x,y,\lambda)=f(x,y)+\lambda g(x,y)=\vec{0}$
### Several constraints
- A function of $n$ variables subject to $m$ constraints.
- Theorem: Let $P_0$ be a local maximum (or minimum) of $f(x_1,\dots,x_n)$ subject to $g_i(x_1,\dots,x_n)=0$, where $i=1,\dots,m$ and assume $\nabla g_1(P_0),\dots,\nabla g_m(P_0)$ are linearly independent. There exists unique Lagrange Multipliers $\lambda_1,\dots,\lambda_m \in \mathbb{R}$ such that
$$
\nabla f(P_0)+\sum_{i=1}^{m}\lambda_i\nabla g_i(P_0)=\vec{0}
$$
and $P_0$ is not an endpoint of the constraints.
- Linearly independent means that $\nabla g_i(P_0)\neq \vec{0}$ and all $g_i(P_0)$ are not parallel to one another.
## Interpretation of the Lagrange Multiplier
## Applications
