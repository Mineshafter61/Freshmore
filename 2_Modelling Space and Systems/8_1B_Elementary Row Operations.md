# 8_1B_Elementary Row Operations

## Matrices

- A **matrix** of $m$ rows and $n$ columns has a size of $m \times n$

$$
\underset{m \times n}{A}=
\begin{bmatrix}
a_{11} & \dots & a_{1j} & \dots & a_{1n} \\
\vdots &\ddots& \vdots &\ddots& \vdots \\
a_{i1} & \dots & a_{ij} & \dots & a_{in} \\
\vdots &\ddots& \vdots &\ddots& \vdots \\
a_{m1} & \dots & a_{mj} & \dots & a_{mn}
\end{bmatrix}
$$

- **Augmented matrices**, where $b$ is the coefficient of the constant term

$$
\left[\begin{array}{cccc|c}
a_{11} & a_{12} & \dots & a_{1n} & b_1 \\
a_{21} & a_{22} & \dots & a_{2n} & b_2 \\
\vdots & \vdots & \ddots& \vdots & \vdots \\
a_{m1} & a_{m2} & \dots & a_{mn} & b_m
\end{array}\right]
$$

- The augmented matrix contains a **coefficient matrix** (the values left of the vertical line that do not correspond to the constant terms):

$$
\begin{bmatrix}
a_{11} & a_{12} & \dots & a_{1n} \\
a_{21} & a_{22} & \dots & a_{2n} \\
\vdots & \vdots & \ddots& \vdots \\
a_{m1} & a_{m2} & \dots & a_{mn}
\end{bmatrix}
$$

### Elementary row operations

- All operations are invertible and they do not change the solutions.
- Goal: Get the matrix into **row echelon form**.
- The process to convert a matrix into row echelon form is called **Gaussian elimination**.

1. Swap row $i$ and row $j$, denoted by $\underrightarrow{R_i \leftrightarrow R_j}$
2. Multiply row $i$ by a **non-zero** constant $c$, denoted by $\underrightarrow{R_i \rightarrow cR_i}$
3. Add $k$ times row $j$ to row $i$, denoted by $\underrightarrow{R_i \rightarrow R_i + kR_j}$

## Row Echelon Form

- A matrix is in row echelon form (REF) if
  - Any **rows of zeros** are grouped at the bottom.
  - In each *non-zero* row, the **first non-zero entry from the left** (called the **leading entry**) is in a **column to the left of any leading entries below it**.
- These properties guarantee that the leading entries form a staircase pattern.
- Leading entries are sometimes called the pivot points.
- e.g.

$$
\left[\begin{array}{ccc|c}
    2 & 1 & 1 & 5 \\
    0 & 8 & 5 & 6 \\
    0 & 0 & 1 & 6
\end{array}\right]
$$

### Gaussian Elimination

- Always work from **left to right** and **top to bottom**.
- The number at the **top left** should always be **as small as possible** (**best case: 1**)
- $R_1$, $R_2$ and $R_3$ always refers to the **current matrix**, not the original matrix, i.e. the row numbers get changed when rows are swapped.

1. Locate the leftmost column that is not entirely zeros.
2. Swap the top row with another row, if necessary, to bring a non-zero entry to the top of the column found in Step 1.
3. For **each row below the top row**, add a suitable multiple of the top row to it so that the entry below the leading entry of the top row becomes zero. (**All entries below the leading entry are zero.**)
4. Cover the top row containing the leading entry, and go back to Step 1 and repeat the procedure on the sub-matrix that remains. Continue in this way until the entire matrix is in row echelon form.
