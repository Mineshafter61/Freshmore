# 11_2_Subspaces Associated with Matrices and Rank
## Column Space

- The *span* of all the columns of $A$. It is a subspace of $\mathbb R^m$
- Denoted by $\mathrm{col}(A)$.
- $n$ entries in a $m\times n$ matrix
- $\mathrm{col}(A)$ is the set of all $\vec{b}$ for which $A\vec{x} = \vec{b}$ is consistent (1 solution)
- Elementary row operations **change** the column space
- Basis is the **transpose** of non-zero rows of RREF($A^T$)
    - This converts the columns to rows which aren't affected by elementary operations, and then convert them back to columns once we have found the row space
- Alternatively, map the columns with leading entries in the RREF to the original matrix, those columns are the basis for $\mathrm{col}(A)$
## Row Space
- The *span* of all the rows of $A$. It is a subspace of $\mathbb R^n$
- Denoted by $\mathrm{row}(A)$.
- $m$ entries in a $m\times n$ matrix
- Elementary row operations do **not** change the row space
- Non-zero rows of the RREF is the row space (basis)
## Null Space
- The set of all solutions to $A\vec{x}=\vec{0}$. It is a subspace of $\mathbb R^n$
- Denoted by $\mathrm{null}(A)$.
- Row space and null space are geometrically **perpendicular** (orthogonal)

## Ranks & Nullity

- **Rank**: \# of leading variables, dimension of the **row space**
    - Denoted by $\mathrm{rank}(A)$
    - Also the dimension of the **column space**, but not by definition
        - $\mathrm{dim}(\mathrm{col}(A))=\mathrm{dim}(\mathrm{row}(A))$
        - $\mathrm{rank}(A)=\mathrm{rank}(A^T)$
- **Nullity**: \# of free variables, dimension of the **null space**
    - Denoted by $\mathrm{nullity}(A)$

### The Rank Theorem

- For any $m\times n$ matrix $A$, $\mathrm{rank}(A)+\mathrm{nullity}(A)=n$
    - Where $n$ is the total number of columns
