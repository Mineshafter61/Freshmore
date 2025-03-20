# 8_2_Gauss Jordan Elimination

- Process to bring a matrix into reduced row echelon form
- Algorithm:
  - Apply steps 1 to 4 in algorithm for Gaussian Elimination to bring the matrix into REF.
  - Multiply a suitable constant to each row so that all the leading entries become 1.
  - Starting with the last non-zero row and working upward, add suitable multiples of each row to the rows above to produce zeros above the leading entries. (All entries above leading 1’s will become zero.)

## Reduced Row Echelon Form (RREF)

- In row echelon form
- The leading entry in each non-zero row is 1 (leading 1)
- For each **column** containing a leading 1, all other entries are 0

$$
\left[\begin{array}{ccc|c}
    1 & 0 & 0 & 5 \\
    0 & 1 & 5 & 6 \\
    0 & 0 & 1 & 6
\end{array}\right]
$$

- Example 1

$$
\begin{align}
\begin{bmatrix}
1 & -1 & 1 & 0 \\
0 & 1 & 0 & 1 \\
3 & -2 & 3 & 1
\end{bmatrix}
\underrightarrow{R_3 \rightarrow R_3-3R_1}
&\begin{bmatrix}
1 & -1 & 1 & 0 \\
0 & 1 & 0 & 1 \\
0 & 1 & 0 & 1
\end{bmatrix}\\
\underrightarrow{R_3 \rightarrow R_3-R_2}
&\begin{bmatrix}
1 & -1 & 1 & 0 \\
0 & 1 & 0 & 1 \\
0 & 0 & 0 & 0
\end{bmatrix}\\
\underrightarrow{R_1 \rightarrow R_1+R_2}
&\begin{bmatrix}
1 & 0 & 1 & 1 \\
0 & 1 & 0 & 1 \\
0 & 0 & 0 & 0
\end{bmatrix}
\end{align}
$$

- Example 2

$$
\begin{align}
\left[\begin{array}{cccc|c}
1 & -1 & -1 & 2 & 1 \\
2 & -2 & -1 & 3 & 3 \\
-1 & 1 & -1 & 0 & -3
\end{array}\right]
\underrightarrow{R_2 \rightarrow R_2-2R_1}
&\left[\begin{array}{cccc|c}
1 & -1 & -1 & 2 & 1 \\
0 & 0 & 1 & -1 & 1 \\
-1 & 1 & -1 & 0 & -3
\end{array}\right] \\
\underrightarrow{R_3 \rightarrow R_3+R_1}
&\left[\begin{array}{cccc|c}
1 & -1 & -1 & 2 & 1 \\
0 & 0 & 1 & -1 & 1 \\
0 & 0 & -2 & 2 & -2
\end{array}\right] \\
\underrightarrow{R_3 \rightarrow R_3+R_2}
&\left[\begin{array}{cccc|c}
1 & -1 & -1 & 2 & 1 \\
0 & 0 & 1 & -1 & 1 \\
0 & 0 & 0 & 0 & 0
\end{array}\right] \\
\underrightarrow{R_1 \rightarrow R_1+R_2}
&\left[\begin{array}{cccc|c}
1 & -1 & 0 & 1 & 2 \\
0 & 0 & 1 & -1 & 1 \\
0 & 0 & 0 & 0 & 0
\end{array}\right]
\end{align}
$$

## General Solutions of Linear Systems

- **Leading variables** are from **leading entries**
- **Free variables** are non-leading variables

1. Express leading variables as the subject (LHS) in terms of free variables (RHS)
2. Assign constant value variables to free variables
3. Express back in vector form, split into **$[\textbf{constants}] + s[\textbf{constants for s}] + t[\textbf{constants for t}]$**, where $s$ and $t$ are constants assigned in step (2)

### Observations

- A linear system is **inconsistent** (i.e. has no solutions) if the last column of a row echelon form of the augmented matrix contains a leading entry, i.e. the last column is a pivot column.
- A **consistent** linear system has **a unique solution** if except for the last column, every column of a row echelon form of the augmented matrix contains a leading entry, i.e. all columns (except the last column) are pivot columns.
- A **consistent** linear system has **infinitely many solutions** if apart from the last column, a row echelon form of the augmented matrix has at least one more column that does NOT contain a leading entry, i.e. at least one more column (apart from the last) is a non-pivot column. The variable corresponding to this non-pivot column is a free variable.

## Homogeneous Linear Systems

A system of linear equations is **homogeneous** if it takes the following form
$$
\begin{cases}
a_{11}x_{1}+a_{12}x_{2}+\dots+a_{1n}x_{n}=0 \\
a_{21}x_{1}+a_{22}x_{2}+\dots+a_{2n}x_{n}=0 \\
\vdots \\
a_{m1}x_{1}+a_{m2}x_{2}+\dots+a_{mn}x_{n}=0
\end{cases}
$$
where $a_{ij}$’s are constants. A linear system is **non-homogeneous** if it is not homogeneous.

- $\vec{x}=\vec{0}$ is **always** a solution to the homogeneous system and is called the **trivial solution**. Any other solutions are called **non-trivial**.
- A homogeneous system is always **consistent**.
- A homogeneous system with **more unknowns than equations** will have infinitely many solutions.
