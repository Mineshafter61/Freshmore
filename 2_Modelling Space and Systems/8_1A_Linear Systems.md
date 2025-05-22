# 8_1A_Linear Systems

## Systems of Linear Equations

- All variables must be of degree 1.
- Such a **linear system** can be written as:

$$
\begin{cases}
a_{11}x_{1}+a_{12}x_{2}+\dots+a_{1n}x_n=b_{1} \\
a_{21}x_{1}+a_{22}x_{2}+\dots+a_{2n}x_n=b_{2} \\
\vdots \\
a_{m1}x_{1}+a_{m2}x_{2}+\dots+a_{mn}x_n=b_{m}
\end{cases}
$$

- Each of the $m$ equations describes a **hyperplane** in $\R^n$

## Row view

- Each row corresponds to one equation
- Example:

$$
\begin{cases}
2x-4y=-1 \\
x+3y=7 \\
\end{cases}
$$

- As a linear system, each equation can be interpreted as a straight line.
- **Solution**: The set of $(x,y,\dots)$ where **all equations are true**.

## Column view

- Written as a vector equation
- Example:

$$
x\begin{bmatrix}2\\1\end{bmatrix}+y\begin{bmatrix}-4\\3\end{bmatrix}=\begin{bmatrix}-1\\7\end{bmatrix}
$$

- Like a weighted sum where x and y are the scalars of each vector.
- Solution: the amount of “scaling” of the vectors.

## Classifications

- A linear system is called **consistent** if it has *at least one solution*, otherwise it has *no solutions* and is called **inconsistent**
- When a linear system has a *unique* solution, it is called **nonsingular**. Otherwise it has *either no solution or infinitely many solutions*, and is called **singular**
    - Unique means exctly one solution
    - Singular means "exceptional" and **not** single

| 1 solution           | Infinite solutions  | No solutions        |
| -------------------- | ------------------- | ------------------- |
| Consistent           | Consistent          | Inconsistent        |
| Unique/Nondegenerate | Singular/Degenerate | Singular/Degenerate |
