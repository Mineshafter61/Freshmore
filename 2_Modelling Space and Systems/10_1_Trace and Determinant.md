# 10_1_Trace and Determinant

## Trace

For an $n\times n$ matrix $A$, the **trace** of $A$ is the sum of the entries on its *main diagonal* and is denoted by $\mathrm{tr}(A)$,
$$
\mathrm{tr}(A)=a_{11}+a_{22}+\dots+a_{nn}=\sum_{i=1}^{n} a_{ii}
$$

### Properties

1. $\mathrm{tr}(A+B)=\mathrm{tr}(A)+\mathrm{tr}(B)$
2. $\mathrm{tr}(sA)=s\,\mathrm{tr}(A)$
3. $\mathrm{tr}(A^T)=\mathrm{tr}(A)$
4. $\mathrm{tr}(CD)=\mathrm{tr}(DC)$
5. $\mathrm{tr}(ABC)=\mathrm{tr}(BCA)=\mathrm{tr}(CAB)\neq\mathrm{tr}(BAC)$ (Cyclic: invariant)

## Determinant

Notation: $\mathrm{det}(A)$ or $|A|$
Formula:
$$
\left|\begin{matrix}
a_1&b_1&c_1 \\
a_2&b_2&c_2 \\
a_3&b_3&c_3
\end{matrix}\right|=(a_1\cdot b_2\cdot c_3+b_1\cdot c_2\cdot a_3+c_1\cdot a_2\cdot b_3)-(c_1\cdot b_2\cdot a_3+b_1\cdot a_2\cdot c_3+a_1\cdot c_2\cdot b_3)
$$

### Minors

A minor $M_{ij}$ of the matrix $A$ is matrix $A$ without its $i$th row and $j$th column.

- e.g Given a matrix

$$
M = \begin{bmatrix} a_1 & b_1 & c_1 \\ a_2 & b_2 & c_2 \\ a_3 & b_3 & c_3 \end{bmatrix}, \\ M_{22} = \begin{bmatrix} a_1 & c_1 \\ a_3 & c_3 \end{bmatrix} \\
$$

### Cofactors

The $(i,j)$th cofactor of $A$, denoted by $c_{ij}$, is defined by
$$c_{ij}=(-1)^{i+j}\det(M_{ij})$$
The sign of the $(i,j)$th cofactor follows a checkerboard pattern:
$$
\begin{bmatrix}
+ & - & + & \dots \\
- & + & - & \dots\\
+ & - & + & \dots \\
\vdots & \vdots & \vdots & \ddots
\end{bmatrix}
$$

### Determinant definition using cofactors

$$
\det(A)=|A|=\sum_{j=1}^{n}a_{1j}c_{1j}
$$

### Cofactor Expansion

The determinant of a $3\times 3$ matrix by expanding along the first row: (TODO)
$$
\left|\begin{matrix} a_{11}&a_{12}&a_{13} \\
a_{21}&a_{22}&a_{23} \\
a_{31}&a_{32}&a_{33}
\end{matrix}\right|=a_{11}c_{11}+a_{12}c_{12}+a_{13}c_{13}
$$

- Choose a row or column with the most $0$s to find the determinant

### Laplace Expansion Theorem

- The determinant of an $n \times n$ matrix $A$ can be computed as
  - Cofactor expansion along row $i$ for any $i \in \{1,2,\cdots,n\}$, or
  - Cofactor expansion along column $j$ for any $j \in \{1,2,\cdots,n\}$
- Choose a row or column with the most $0$s to find the determinant

## Special Matrices

1. If $A$ is a **diagonal** or **triangular** $n \times n$ matrix, the determinant is the product of all entries on its main diagonal
$$\det(A) = a_{11}a_{22}\cdots a_{nn}$$
2. If $A$ has a row or column of zeros, then $\det(A) = 0$

## Finding Determinant via Row Operations

1. Row reduce $A$ to row echelon form $R$, keeping track of all the **row swaps**, and all instances when a row is changed through multiplication by a **constant**
2. The determinant of $A$ is

$$
\det(A)=\frac{\text{product of }R\text{'s diagonal entries}}{-1^{\text{no. of row swaps}}(\text{product of all constants used})}
$$

## Properties of Determinants

Let $A$ be a square matrix.

1. If matrix $B$ is obtained by swapping two rows of $A$, then $\det(B) = −\det(A)$
2. If matrix $B$ is obtained by multiplying one row of $A$ by a scalar $k$, then $\det(B) = k \det(A)$
3. If matrix $B$ is obtained by adding a multiple of one row of A to another row, then $\det(B) = \det(A)$.
4. If A has two identical rows, then $\det(A) = 0$
5. $\det(kA)=k^n\det(A)$
6. $\det(AB)=\det(A)\det(B)$
7. $\det(A^{-1})=\frac{1}{\det(A)} \text{ if }A\text{ is invertible}$
8. $\det(A^T)=\det(A)$ (implies that **all properties involving "rows" can be extended to "columns"**)
9. **A square matrix $A$ is *invertible* if and only if $\det(A)\neq 0$.**
