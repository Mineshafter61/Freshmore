# W5D1 - Binomial and Poisson Random Variables

## Binomial Random Variable

Models the number of "successes" when a random experiment is repeated $n$ times, where each experiment has a probability of success $p$, independent of any other experiment.

Consider an experiment in which a weighted coin, with

$$\mathbb P(T)=p \text{ and } \mathbb P(H) = 1-p$$
is tossed $n$ times. Let $X$ be the number of $\texttt T$'s obtained. Then $X$ is called a binomial random variable, and is denoted by $X \textasciitilde \mathrm{binomial}(n, p)$.

The probability that there are exactly $k$ $\texttt T$'s is
$$
\mathbb P(\textsf{ exactly } k\,\texttt{T}'s) = \mathbb P(X=k) = {n \choose k} p^k (1-p)^{n-k}
$$
- **Expected value**, $\mathbb E(X)=np$
- **Variance**, $\mathrm{Var}(X)=np(1-p)$

## Poisson Random Variable

For a binomial random variable $X$ with large $n$, small $p$ and its **mean** $\lambda=np$,
$$
\mathbb P(X=k)\to e^{-\lambda}\frac{\lambda^k}{k!}
$$
Therefore, a random variable $X$ is said to satisfy a Poisson distribution if its probability mass function is given by 
$$
\mathbb P(X=k)=e^{-\lambda}\frac{\lambda^k}{k!}
$$
We denote this by $X \sim \mathrm{Poisson}(\lambda)$.

- **Expected value**, $\mathbb E(X)=\lambda$
- **Variance**, $\mathrm{Var}(X)=\lambda$