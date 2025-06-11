# W3D2 - Conditional Probability

## Birthday Problem

What is the probability that among $n$ people, at least 2 people share the same birthday?
> Let $d$ be the number of days i. a year, and let the event that at least 2 people share the same birthday. It is easier to work with the complement in this case.
>
> We ignore leap years, and assume each person is equally likely to be born on any day of the year.

Computing $\mathbb P(E^c)=\frac{|E^c|}{|\mathcal S|}$ using enumeration:

Let $n$ be the number of people and $d$ be the number of days (365 in this case)

$$\begin{align*}\mathbb P(E)&=1-\mathbb P(E^c)\\&=1-\frac{E^c}{\mathcal S}\\&=1-\frac{^dP_n}{d^n}\\&=1-(\frac dd)(\frac{d-1}d)(\frac{d-2}d)\dots(\frac{d-(n-1)}d)\\&=1-(1- \frac 1d)(1- \frac 2d)\dots(1- \frac{n-1}{d})\\&=1-e^{-n^2/(2d)}\end{align*}$$

## Conditional probability

Given that event $B$ has occurred (*'condition'*), the probability of event $B$ is now 1. Therefore, the new probability of all other events is $\mathbb P(A)=\frac{A}{B}=\mathbb P(A|B)$ (A given B)

- $\mathbb P(A|B) \neq \mathbb P(B|A)$
- $\mathbb P(A|B) = \frac{|A \cap B|}{|B|}=\frac{|A \cap B|}{|\mathcal S|} \frac{\mathcal S}{|B|}$
- $\mathbb P(A\cap B)=\mathbb P(B)\mathbb P(A|B)=\mathbb P(A)\mathbb P(B|A)$

## Series

### Taylor series for $e^x$

$$\sum_{n=0}^\infty \frac{x^n}{n!}=1+x+\frac{x^2}{2}+\frac{x^3}{6}+\dots=e^x$$

- In particular, when $|x|$ is small, $e^x≈1+x$ and $e^{-x}≈1-x$

### Arithmetic series

For any positive integer $n$,
$$1+2+3+\dots+n=\frac{n(n+1)}{2}$$

### Geometric series

For any positive integer $n$,
$$1+r+r^2+\dots+r^{n-1}=\frac{1-r^n}{1-r}$$

- In particular, when $|r|<1$ and $n\to\infty$, we have the infinite geometric series
$$1+r+r^2+\dots=\frac{1}{1-r}$$

## Law of total probability

- The events $B_1, B_2, \dots B_n$ are said to **partition** the sample space $\mathcal S$ if they are disjoint and their union is $\mathcal S$.
- Let there be an event A where the intersections $A \cap B_1=A_1, A \cap B_2=B_2,\cdots$ exists.

$$
\mathbb{P}(A)=\mathbb{P}(B_{1})\mathbb{P}(A|B_{1})+\mathbb{P}(B_{2})\mathbb{P}(A|B_{2})+\cdots+\mathbb{P}(B_{n})\mathbb{P}(A|B_{n})
$$

- Useful variation (2 partitions):

$$
\mathbb P(A)=\mathbb P(B)\mathbb P(A|B)+\mathbb P(B^c)\mathbb P(A|B^c)
$$
