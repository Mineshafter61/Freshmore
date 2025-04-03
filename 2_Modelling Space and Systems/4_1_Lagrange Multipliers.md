# 4_1_Lagrange Multipliers

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
  \nabla f(x_0, y_0) + \lambda \nabla g(x_0, y_0) = \vec{0}

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

- Other method (Lagrangian function): $L(x,y,\lambda)=f(x,y)+\lambda g(x,y)=\vec{0}$ (TODO)
- The optimum point obtained using method of Lagrange Multipliers can be a maximum, a minimum or saddle point
    - This method does **not** tell us which is the case
- Depending on the context of the problem, you have to make appropriate arguments to justify whether the obtained point is a maximum or a minimum
    - E.g. EVT, AM-GM

### Several constraints

- A function of $n$ variables subject to $m$ constraints.
- Theorem: Let $P_0$ be a local maximum (or minimum) of $f(x_1,\dots,x_n)$ subject to $g_i(x_1,\dots,x_n)=0$, where $i=1,\dots,m$ and assume $\nabla g_1(P_0),\dots,\nabla g_m(P_0)$ are linearly independent. There exists unique Lagrange Multipliers $\lambda_1,\dots,\lambda_m \in \mathbb{R}$ such that

$$
\nabla f(P_0)+\sum_{i=1}^{m}\lambda_i\nabla g_i(P_0)=\vec{0}

$$

and $P_0$ is not an endpoint of the constraints.

- Linearly independent means that $\nabla g_i(P_0)\neq \vec{0}$ and all $g_i(P_0)$ are not parallel to one another.

#### Solving

- We drop the inequality constraints. We obtain an **equality constrained** problem that is called the **relaxed problem**
- If the optimal solution for the relaxed problem **satisfies the inequality constraints**, then it is also optimal for the original problem

## Interpretation of the Lagrange Multiplier

To interpret $\lambda$, we look at how the optimal value of the function $f$ changes as the value of the constraint function $g$ is varied.

$$
g(x,y)=0 \text{ changes to } g(x,y)=c

$$

In general, the optimal point depends on the constraint value $c$ as follows (chain rule):

$$
\frac{df}{dc}=\frac{\partial f}{\partial x} \frac{dx_0}{dc}+\frac{\partial f}{\partial y} \frac{dy_0}{dc}

$$

At the optimal point $x_0,y_0$, we have $f_x=-\lambda g_x$ and $f_y=-\lambda g_y$, therefore

$$
\frac{df}{dc}=-\lambda \left( \frac{\partial g}{\partial x} \frac{dx_0}{dc}+\frac{\partial g}{\partial y} \frac{dy_0}{dc} \right)=-\lambda\frac{dg}{dc}

$$

Since $g(x_0(c),y_0(c))=c$, $\frac{dg}{dc}=1$. Thus,

$$
\frac{\Delta f}{\Delta c}\approx \frac{df}{dc}=-\lambda

$$

If $\Delta c$ in $g(x,y)$ is small,

$$
\Delta f=f_{new}-f_{old}\approx(-\lambda)\Delta c

$$

### Interpretation

- Up to the first order, the change in objective function value is equal to the **negative** of the Lagrange Multiplier times the change in the constraint function value c.
- **Generalisation**: If there are multiple constraints, each Lagrange multiplier indicates the **rate of change** of the optimal objective function value with respect to the **change in the value of the corresponding constraint**.
