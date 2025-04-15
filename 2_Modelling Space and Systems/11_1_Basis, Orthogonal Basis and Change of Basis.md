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

### Fundamental Theorem of Invertible Matrices (Part 3)

Let A be an $n\times n$ matrix. The following statements are equivalent.

1. $A$ is invertible.
2. The columns of $A$ are linearly independent.
3. The columns of $A$ span $\mathbb{R}^n$.
4. The columns of $A$ forms a basis for $\mathbb{R}^n$.
5. The rows of $A$ are linearly independent.
6. The rows of $A$ span $\mathbb{R}^n$.
7. The rows of $A$ form a basis for $\mathbb{R}^n$.

- We can deduce a short cut:
    - Every set of $n$ linearly independent vectors in $\mathbb{R}^n$ is a basis for $\mathbb{R}^n$.
    - Every set of $n$ vectors that spans $\mathbb{R}^n$ is a basis of $\mathbb{R}^n$.
- Required to state the fundamental theorem to use in exams

## Orthogonal set

A set of vectors $\{\vec{v}_{1},\vec{v}_{2},\dots,\vec{v}_{k}\}$ in $\mathbb{R}^{n}$ is called an **orthogonal set** if $\forall\,i,j\in 1,2,\dots,k$ where $i\neq j$,
$$\vec{v}_i\cdot \vec{v}_j=0$$
i.e. **all pairs of distinct vectors in the set are perpendicular.**

- **Any orthogonal set** of non-zero vectors in $\mathbb{R}^n$ is **linearly independent**, and by the fundamental theorem, **these vectors form a basis** of $\mathbb{R}^n$.

### Orthogonal and Orthonormal Basis

If an **orthogonal basis** consists only of **unit vectors**, it is called an **orthonormal** basis.

## Change of Basis

- Since both the standard basis $E$ and the ordered basis $B$ describe the same vector, we have:
$$ \vec{u} = B[\vec{u}]_B = [\vec{u}]_E $$
- $B$ is called the **change of basis matrix**. It converts the coordinate vector $[\vec{u}]_B$ with respect to basis $B$ into the coordinate vector $[\vec{u}]_E$ with respect to the standard basis $E$.

- Since $B$ is invertible, we have:
 $$ B^{-1}[\vec{u}]_E = [\vec{u}]_B $$
- $B^{-1}$ is the change of basis matrix that converts the coordinate vector $[\vec{u}]_E$ with respect to the standard basis $E$ into the coordinate vector $[\vec{u}]_B$ with respect to basis $B$.
![[MSS_changeOfBasis.png]]
In addition, $[\vec{u}]_{A}=A^{-1}B[\vec{u}]_{B}$
