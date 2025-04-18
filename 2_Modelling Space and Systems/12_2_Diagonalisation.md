# 12_2_Diagonalisation
- Changing a matrix into a diagonal matrix
- To diagonalise a matrix,
$$
d_i=m_i \,\forall \lambda_i
$$
- (dimension is the same as multiplicity (number of repeated eigenvalues) for all eigenvectors, always true if $m=1$)
- $A$ is only diagonalisable **if and only if** $A$ has $n$ linearly independent eigenvectors.
- Diagonalisation:
$$
A=PDP^{-1}
$$
- where 
    - $D$ is a diagonal matrix, where the $(i, i)$th entry is an eigenvalue.
    - $P$ is an invertible matrix, where the $i$th column is the corresponding eigenvector.
- Generally, we have
$$
A^k=PD^kP^{-1}
$$
- where $D^k$ is $\begin{bmatrix}d_{11}^{k} & 0 & 0 & \dots\\0 & d_{22}^{k} & 0 & \dots\\0 & 0 & d_{33}^{k} & \dots\\\vdots & \vdots & \vdots & \ddots\end{bmatrix}$
- $A$ and $D$ have the **same determinant** and **trace**.
## Markov Chains
**Stochastic** (random) process that satisfies the relation
$$
\vec{x}_{k+1}=P\vec{x}_{k}, \text{for }k=1,2,\dots
$$
where $\vec{x}_{k}\in \mathbb R^n$ and $P$ is an $n\times n$ matrix.

$\vec{x}_{k}$ is called the **state vector** and $P$ is called the **transition matrix**.
The $(i,j)th$ entry in $P$ is the probability of transiting from state $j$ to state $i$.