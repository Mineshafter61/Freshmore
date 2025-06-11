# W4D1 - Bayes' Theorem

- $A$ and $B$ are events
- Given $\mathbb P(B|A)$, find $\mathbb P(A|B)$

$$
\mathbb{P}(A|B)=\frac{\mathbb{P}(B|A)\mathbb{P}(A)}{\mathbb{P}(B)}
$$

- Where $\mathbb{P}(B)$ can be computed from the law of total probability

$$
\mathbb{P}(B)=\mathbb{P}(B|A)\mathbb{P}(A)+\mathbb{P}(B|A^{c})\mathbb{P}(A^{c})
$$

## Independence

- If events $A$ and $B$ are independent, then

$$
\mathbb{P}(A|B) = \mathbb{P}(A) \\
\mathbb{P}(B|A) = \mathbb{P}(B) \\
\mathbb{P}(A \cap B) = \mathbb{P}(A)\mathbb{P}(B)
$$

## Disjoint

$$
\mathbb{P}(A \cap B) = \mathbb{P}(\emptyset) = 0
$$

- Not related to independence
