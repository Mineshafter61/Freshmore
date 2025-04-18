# 12_1_Eigenvalues and Eigenvectors

Let $A$ be an $n \times n$ matrix. A scalar $\lambda$ is called an **eigenvalue** of $A$, if there is a *non-zero vector* $\vec{v}$ such that
$$
A\vec{v} = \lambda \vec{v}
$$
Such that $\vec{v}$ is called an **eigenvector** of $A$ corresponding to $\lambda$

1. Eigenvectors **cannot** be $\vec{0}$, but eigenvalues **can** be $0$
2. For each eigenvalue $\lambda$, there are infinitely many choices of eigenvectors

- **Degenerate eigenvalues**: eigenvalues that appear more than once

## Finding eigenvalues

Let $A$ be an $n\times n$ matrix. The equation $A\vec{v}=\lambda\vec{v}$ can be written
as $A\vec{v}=\lambda I\vec{v}$, or as
$$(A-\lambda I)\vec{v}=0$$
(note: this is a homogenous solution)
The zero vector is always a solution to this system. For there to be a non-zero solution $\vec{v}$, $(A−λI)$ must be **non-invertible**; therefore,
$$\det(A-\lambda I)=0$$
$\det(A−λI)$ is a **polynomial** in $λ$, called the **characteristic polynomial** of $A$. (gives n roots, thus the number of eigenvalues is at most the size of the matrix).

## Finding eigenvectors

- For **each** eigenvalue $\lambda_i$, we solve the equation $(A-\lambda_iI)\vec{v} = \vec{0}$
- The null space of $(A-\lambda_iI)$ is the **eigenspace** corresponding to $\lambda_i$
    - The eigenspace is the solution of $\mathrm{null}(A-\lambda_iI)\implies[A-\lambda_iI|0]$
    - The eigenvectors are all scalar multiples of **any non-zero vector** in the eigenspace.
- Recall: Eigenvectors must be non-zero

## Eigenvectors and Eigenvalues of $A^k$

$A^k\vec{v}=\lambda^k\vec{v}$, therefore:

- Eigenvalue: $\lambda^k$
- Eigenvector: $\vec{v}$ (same as the eigenvector for A)

## Triangular matrices

- Eigenvalues of triangular matrices are the **entries on its main diagonal**.

## Determinant and trace

- $\det(A)=\prod_{i=1}^n\lambda_i$: the product of all the eigenvalues of $A$
- $\mathrm{tr}(A)=\sum_{i=1}^n\lambda_i$: the sum of all the eigenvalues of $A$
- Dimension of eigenspace, $\mathrm{dim}(E_{\lambda_i})=\mathrm{nullity}(A-\lambda I)=$ number of free variables in $(A-\lambda I)$

### Fundamental Theorem of Invertible Matrices (Part 5)

- A square matrix $A$ is invertible if and only if $0$ is **NOT** an eigenvalue of A
