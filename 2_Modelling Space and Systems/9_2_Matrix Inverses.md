# 9_2_Matrix Inverses

## Elementary matrices

- Matrix that can be obtained from an identity matrix by performing **one** elementary row operation.
- Invertible
- Their inverses are also elementary matrices

### $R_n \leftrightarrow R_m$

- Apply the same elemetary matrix to get the original
- Therefore $E_A = E^{-1}_A$

### $R_n \rightarrow kR_n$

- Replace the scale factor $k$ by a reciprocal of it $\frac{1}{k}$ in the elementary matrix

### $R_n \rightarrow R_n - kR_m$

- Replace the foreign number $k$ in the elementary matrix with its negative, $-k$

## Inverse

- Given a transformation of matrix $A$ to an identity matrix via 3 elementary matrices in the order $E_1, E_2, E_3$
$$\begin{matrix}E_3E_2E_1A = I \\A^{-1} = E_3E_2E_1\end{matrix}$$

- Similarly,
$$A = E_1^{-1}E_2^{-1}E_3^{-1}$$

## Gauss-Jordan Method

1. Form the augmented matrix $[A|I]$. For example, $\left[\begin{array}{cc|cc}1&2&1&0\\3&5&0&1\end{array}\right]$.
2. Perform **Gauss-Jordan elimination** on $[A|I]$.
3. If the left half is reduced to $I$, then the **RREF** is $[I|A^{−1}]$, so its **right half is $A^{-1}$**. If the left half **cannot be reduced** to $I$, then $A$ is **not invertible**.

## Fundamental Theorem of Invertible Matrices (Part 1)

Let $A$ be an $n \times n$ matrix. The following statements are equivalent

1. $A$ is invertible
2. $A\vec{x} = \vec{b}$ has a unique solution for any $\vec{b} \in \mathbb{R}^n$
3. $A\vec{x} = \vec{0}$ has only the trivial solution
4. The reduced row echelon form (RREF) of $A$ is $I_n$
5. $A$ can be expressed as a product of elementary matrices

Note: Statements in the Fundamental Theorem must either be **ALL TRUE** or **ALL FALSE**

## Inverse of an 2 × 2 Matrix

Let $A=\begin{bmatrix}a&b\\c&d\end{bmatrix}$. A is invertible if $ad−bc \neq 0$.
$$A^{-1}=\frac1{ad-bc}\begin{bmatrix}d&-b\\-c&a\end{bmatrix}$$
