# 10_2_Span, Linear Independence and Subspaces

- Span: all linear combinations

## Linear Combination

The following are equivalent
$$x\begin{bmatrix}2\\1\end{bmatrix}+y\begin{bmatrix}-1\\5\end{bmatrix}=\begin{bmatrix}7\\9\end{bmatrix}\\\begin{bmatrix}2&-1\\1&5\end{bmatrix}\begin{bmatrix}x\\y\end{bmatrix}=\begin{bmatrix}7\\9\end{bmatrix}$$

- This allows us to check if the matrix is invertible & solvable via determinant.

## Span

- Set of **all** linear combinations
- *Example 1*: Span of $\vec{e}_1$, $\vec{e}_2$ and $\vec{e}_3$ is $\mathbb R^3$.
- *Example 2*: Span of $\begin{bmatrix}1\\2\end{bmatrix}$ is the straight line $y=2x$.
- Expression:
 $$\mathrm{span}(S_1)=\left\{c\begin{bmatrix}x\\y\end{bmatrix}:c\in\mathbb R\right\}$$
- For $\mathrm{span}(\mathbb R^n)$, we need **at least** n **independent** vectors.

## Linear Independence

Given a system
$$c_1\vec{v}_1 + c_2\vec{v}_2 + \cdots + c_k\vec{v}_k = \vec{0}$$

- If the equation has only the trivial solution (i.e all coefficients are 0), then all vectors in the set are linearly independent
    - No parallel vectors

### Algorithm

Consider a set of $n$ vectors $S = \{\vec{v}_1, \vec{v}_2, \cdots, \vec{v}_n\}$ in $R^m$

1. Form the linear system $A\vec{x} = \vec{0}$, where the columns of $A$ are made up of the vectors in $S$ (column view)
2. Find the REF of matrix A
3. If the REF of $A$ has $n$ pivot points or leading entries, the linear system has a unique solution. Thus the vectors in $S$ are **linearly independent**
4. If the REF of $A$ has less than $n$ pivot points or leading entries, the linear system is singular. Thus the vectors in S are **linearly dependent**

- Size of $A$ is $m \times n$
- If $m < n$, the vectors are linearly dependent
- \# of leading variables = \# of rows - \# of leading variables

## Subspaces

- Span of vectors in $\mathbb R^n$ → Subspace of $\mathbb R^n$
- A subset $W \subseteq \mathbb R^n$ os said to form a **subspace** of $\mathbb R^n$ if it satisfies the following three requirements:
    - $\vec{0}\in W$(passes through **origin**)
    - If $c\in\mathbb R$ and $\vec{v}\in\mathbb R$, then $c\vec{v}\in W$. (W is **closed under scalar multiplication**.)
    - If $\vec{v},\vec{w}\in W$, then $\vec{v}+\vec{w}\in W$. (W is **closed under addition**.)
- Subspace is **not** subset, subspace is a subset of subsets that passes through the origin.
