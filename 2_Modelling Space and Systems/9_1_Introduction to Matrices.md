# 9_1_Introduction to Matrices

- **Zero matrix**: all entries are 0, denoted by $O$.
- **Square matrix:** no. of columns = no. of rows
- **Diagonal matrix**: only entries along the diagonal ($a_{11}, a_{22}, \dots, a_{nn}$) are non-zero
- **Identity matrix**: all diagonal entries are 1, all other entries are 0. Denoted by $I$.
- **Symmetric matrix**: $a_{ij}=a_{ji}$ for all i, j
- **Upper triangular matrix**: all entries **on and above** the diagonal are non-zero
- **Lower triangular matrix**: all entries **on and below** the diagonal are non-zero

## Matrix operations

- Equality: two matrices are equal if they have the **same size** and their **corresponding entries are equal**.
- **Addition**: If two matrices $A$ and $B$ are the **same size** of $m\times n$, the sum of a matrix $C=A+B$ is an $m\times n$ matrix with the $(i,j)$th entry $c_{ij}=a_{ij}+b_{ij}$.
- **Scalar multiplication**: If $A$ is an $m\times n$ matrix and $c$ is a scalar, the scalar multiplication $B=cA$ is an $m\times n$ matrix with $(i,j)$th entry $b_{ij}=c\,a_{ij}$.
- All $m\times n$ matrices form a [vector space](https://www.geeksforgeeks.org/vector-space/).

### Matrix multiplication

If $A$ is an $m\times n$ matrix and B is an $n\times r$ matrix, the product $C=AB$ is an $m\times n$ matrix with $(i,j)$th entry
$$c_{ij}=\sum_{k=1}^{n} a_{ik}b_{kj}$$

- Size of $C$: $m\times r$ ($\underset{ m\times n }{ A }\,\underset{ n\times r }{ B }=\underset{ m\times r }{ AB }$)
- Generalisation of vector dot product.
  - The $(i,j)$th entry of $C=AB$ is the dot product of $i$th row of $A$ and the $j$th column of $B$.
  - $c_{ij} = \begin{bmatrix}a_{i1}&a_{i2}&\dots&a_{in}\end{bmatrix}•\begin{bmatrix}b_{1j}\\b_{2j}\\\vdots\\b_{nj}\end{bmatrix}$
- Matrix multiplication is **not commutative**.
- $AB=O$ does **not** imply $A=O$ or $B=O$.
- *Examples*

$$
\begin{bmatrix}
1&3&5
\end{bmatrix}
\begin{bmatrix}
2 \\
4 \\
6
\end{bmatrix}=[44]
$$
$$
\begin{bmatrix}
2 \\
4 \\
6
\end{bmatrix}
\begin{bmatrix}
1 & 3 & 5
\end{bmatrix}=
\begin{bmatrix}
2 & 6 & 10 \\
4 & 12 & 20 \\
6 & 18 & 30
\end{bmatrix}
$$
$$
\begin{bmatrix}
1.5 & 10 \\
4 & 9 \\
12 & -8
\end{bmatrix}
\begin{bmatrix}
0 & 1 \\
2 & 3
\end{bmatrix}
=
\begin{bmatrix}
20 & 31.5 \\
18 & 31 \\
-16 & -12
\end{bmatrix}
$$

### Power of Square Matrices

If A is a square matrix and k is a non-negative integer, we define A^k as
$$
A^k=\begin{cases}
I & \text{if }k=0\\
\prod_{i=0}^k A & \text{if }k\geq 1
\end{cases}
$$

- Do **not** individually square each term in the matrix

### System of Linear Equations

A system of linear equations
$$
\begin{cases}
a_{11}x_{1}+a_{12}x_{2}+\dots a_{1n}x_{n}=b_{1}\\
a_{21}x_{1}+a_{21}x_{2}+\dots a_{2n}x_{n}=b_{2}\\
\vdots\\
a_{m1}x_{1}+a_{m2}x_{2}+\dots a_{mn}x_{n}=b_{m}\\
\end{cases}
$$
can be written as $A\vec{x}=\vec{b}$ or
$$
\begin{bmatrix}
a_{11} & a_{12} & \dots & a_{1n} \\
a_{21} & a_{22} & \dots & a_{2n} \\
\vdots & \vdots & \ddots& \vdots \\
a_{m1} & a_{m2} & \dots & a_{mn}
\end{bmatrix}
\begin{bmatrix}
x_1\\ x_2\\\vdots\\ x_n
\end{bmatrix}
=
\begin{bmatrix}
b_1\\ b_2\\\vdots\\ b_n
\end{bmatrix}
$$

### Transpose

- Notation: $A^T$
- Rotate matrix by 90˚and flip vertically
- **Rows become columns, columns become rows**
- Dot product $\vec{u}\cdot \vec{v}$ can also be defined by $\vec{u}^T\vec{v}$
- A square matrix $A$ is **symmetric** if and only if $A=A^T$

## Inverses of Square Matrices

An $n\times n$ square matrix $A$ is called **invertible** if there exists an $n\times n$ matrix $B$ such that
$$AB=BA=I$$
We call $B$ the **inverse** of $A$, and denote it by $A^{-1}$, which is **unique**.

A square matrix is called **singular** if it has no inverse.
