# W2D2 - Enumeration

## Counting principles

### Addition principle

If there are $k$ disjoint categories, where the $i$th category contains $a_i$ objects,

- then the number of ways to pick one object from the union of these categories is $a_1 + a_2 + \dots + a_k$.

### Multiplication principle

If an activity is performed in $k$ steps, where:

- step 1 can be done in $n_1$ ways, and for each:
- step 2 can be done in $n_2$ ways, and for each:
- step 3 can be done in $n_3$ ways, etc,
- then the number of different activities is $n_1 × n_2 ×\dots× n_k$.

## Permutation

If we **do not allow the repetition** of choices, we call it a **permutation**, $^nP_k$.

- n is the number of possible choices
- k is the number of times choosing is performed
- **order matters** (e.g. the password `1234` is not the password `4321`)
 Notation:
 $$^nP_k=n\times(n-1)\times\dots \times(n-(k-1))=\frac{n!}{(n-k)!}$$
- The number of permutations of all $n$ distinct objects is $^nP_k=n!$
- Excel command for permutation: `PERMUT`
- Excel command for factorial: `FACT`

Formula for permutation when the $n$ objects are **not all distinct**:

- The number of permutations of all $n = n_1 + n_2 +· · · + n_r$ objects, **of which $n_1$ are identical, $n_2$ are identical, . . . , $n_r$ are identical**, is
$$\frac{n!}{n_1!n_2!\dots n_r!}$$

## Combination

When the **order does not matter**, then the number of ways to choose $k$ distinct objects from $n$ distinct objects is denoted by $^nC_k$ or $n\choose k$. This is called a **combination**.
Notation:
$$
{n\choose k}=^nC_k=\frac{nP_k}{k!}=\frac{n!}{k!(n-k)!}
$$

- Useful identities
    - ${n\choose 0}=1$
    - ${n\choose 1}=n$
    - ${n\choose 2}=\frac{n(n-1)}{2}$
    - ${n\choose k}={n\choose n-k}$
    - ${n\choose k}$ appears as **coefficients** in the expansion of $(a+b)^n$ (binomial theorem)

### Binomial theorem

$$
(a+b)^n=\sum_k=0^n {n\choose k} a^kb^{n-k}
$$
As such, ${n\choose k}$ is also called a **binomial coefficient**.
