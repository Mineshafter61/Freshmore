# 11_1_Basis, Orthogonal Basis and Change of Basis

## Basis

- A set of vectors $s={\vec{v}_1,\dots,\vec{v}_n}$ is called a **basis** for a subspace $W$ if
    1. $S$ **spans** $W$, and
    2. vectors in $S$ are **linearly independent**.
    ![[MSS_bases.png]]
- $\vec{e}_1,\vec{e}_2,\dots,\vec{e}_n$ is a basis for $\mathbb{R}^n$. This is known as the **standard basis**, denoted by ℰ.
- Every basis of $\mathbb{R}^n$ has **exactly** $n$ vectors.
    - **Must be a square matrix**
- Basis is not unique.
- **Basis Theorem:** Any **two bases for a subspace** have the **same number of vectors**.

### Dimension

- The dimension of subspace $W$, denoted by $\dim(W)$, is defined to be the **number of vectors** in **any basis** for $W$.

$$
\begin{align}
\text{dim}(\mathbb{R}^k) &= k \\
\text{dim}({\{\vec{0}\}}) &= 0
\end{align}
$$

### Check for basis

$S = \{\vec{v}_1, \ldots, \vec{v}_n\}$ is a **basis** for $\mathbb{R}^n$ if and only if the $n \times n$ matrix $A = [\vec{v}_1\ |\ \cdots\ |\ \vec{v}_n]$ is **invertible**.

- Proof: Suppose $S$ is a basis for $\mathbb{R}^n$. Then $A\vec{x} = \vec{0}$ has a unique (trivial) solution as all vectors in $S$ are linearly independent. This implies $A$ is invertible.
- **Algorithmic method**:
    1. Form a matrix of all the vectors in the set.
    2. Check if that matrix is invertible. If it is, the vectors in the set are a basis.
    - **Checking matrix invertibility**:
        - Determinant is not equal to 0
        - RREF is the identity matrix

### Link to Fundamental Theorem

- Both the rows and columns of the matrix formed from the basis vectors are themselves basis vectors.
-
