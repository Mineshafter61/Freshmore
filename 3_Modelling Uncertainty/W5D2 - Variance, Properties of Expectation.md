# W5D2 - Variance, Properties of Expectation
## Population Variance

Let the expectation of a population, $\mathbb E(X)=\mu_X$.

The **population variance** is defined as

$$ \sigma^2=\mathrm{Var}(X):=\mathbb E((X-\mu_X)^2) $$

Moreover, the **standard deviation** is defined as

$$ \sigma=\mathrm{SD}(X):=+\sqrt{\mathrm{Var}(X)}=+\sqrt{\mathbb E((X-\mu_X)^2)} $$

- If $\mathrm{Var}(X)=0$, $X$ is a constant value.
- The SD is used as a standard way to measure distance from the centre.

## Properties of Expectation
### Theorem 1

Suppose that $f(x)$, the pmf of $X$, is given by:

| $x$    | $x_1$    | $x_2$    | $\dots$ | $x_n$    |
| ------ | -------- | -------- | ------- | -------- |
| $f(x)$ | $f(x_1)$ | $f(x_2)$ | $\dots$ | $f(x_n)$ |

In many cases (such as when $g$ is one-to-one), the pmf of $Y = g(X)$ is:

| $y$    | $g(x_1)$    | $g(x_2)$    | $\dots$ | $g(x_n)$    |
| ------ | -------- | -------- | ------- | -------- |
| $\mathbb P(Y=y)$ | $f(x_1)$ | $f(x_2)$ | $\dots$ | $f(x_n)$ |

Therefore, (**Theorem 1**)
$$\mathbb E(Y)=\mathbb E(g(X))=\sum_{i=1}^{n}g(x_i)f(x_i)=\sum_{i=1}^{n}g(x_i)\mathbb P(X=x_i)$$

### Consequences of Theorem 1

For any constants $a$ and $b$, we have:

$$
\begin{align}
\mathbb E(a\,X+b)&=a\mathbb E(X)+b &(1)\\
\mathrm{Var}(X)&=\mathbb E(X^2)-\mathbb E(X)^2 &(2)\\
\mathrm{Var}(a\,X+b)&=a^2\mathrm{Var}(X) &(3)
\end{align}
$$

**Proofs**:

$$
\begin{align*}
(1)\\
\mathbb{E}(aX + b) &= \mathbb{E}(g(X)) \\
&= \sum_{\text{all } x_i} g(x_i) \, \mathbb{P}(X = x_i) \\
&= \sum_{\text{all } x_i} (a x_i + b) \, \mathbb{P}(X = x_i) \\
&= a \sum_{\text{all } x_i} x_i \, \mathbb{P}(X = x_i) + b \sum_{\text{all } x_i} \mathbb{P}(X = x_i) \\
&= a \cdot \mathbb{E}(X) + b \cdot 1 \\
&= a \mathbb{E}(X) + b \\\\
(2) \\
\mathrm{Var}(X) &= \mathbb{E}\left((X - \mu_X)^2\right) \\
&= \sum_{\text{all } x_i} (x_i - \mu_X)^2 f(x_i) \qquad \text{(by Theorem \textcolor{blue}{1})} \\
&= \sum_{\text{all } x_i} \left(x_i^2 - 2\mu_X x_i + \mu_X^2\right) f(x_i) \\
&= \sum_{\text{all } x_i} x_i^2 f(x_i) - 2\mu_X \sum_{\text{all } x_i} x_i f(x_i) + \mu_X^2 \sum_{\text{all } x_i} f(x_i) \\
&= \mathbb{E}(X^2) - 2\mu_X \mathbb{E}(X) + \mu_X^2 \cdot 1 \\
&= \mathbb{E}(X^2) - 2\mathbb{E}(X)^2 + \mathbb{E}(X)^2 \\
&= \mathbb{E}(X^2) - \mathbb{E}(X)^2. \\\\
(3) \\
\text{Let }W&=a\,X+b. \\
\text{By definition, }&\mathrm{Var}(a\,X+b)=\mathrm{Var}(W)=\mathbb E((W-\mu_W)^2) \\
\text{From }(1),\,&\text{we have }\mu_W=\mathbb E(W)=a\mathbb E(X)+b, \text{so} \\
(W - \mu_W)^2 &= (aX + \cancel{ b } - a\mathbb{E}(X) - \cancel{ b })^2 = a^2 (X - \mu_X)^2 \\
\text{Then, from}(1), \\
\mathrm{Var}(a\,X+b)&=\mathbb E(a^2(X-\mu_X)^2) \\
&=a^2\mathbb E((X-\mu_X)^2) \\
&=a^2\mathrm{Var}(X)
\end{align*}
$$

### Theorem 2

For any random variables $X_1,X_2,\dots,X_m$, if each of them has a finite expected value, then the expectation of the sum of the random variable is equal to the sum of the expectation of the random variable.
$$
\mathbb E\left( \sum_{i=1}^m X_i \right)=\sum_{i=1}^m \mathbb E(X_i)
$$

## Bernoulli random variable

$X$ is called a **Bernoulli** random variable if it can only take 2 values, 1 (success) or 0 (failure), where
$$\begin{align}\mathbb{P}(X=1)&=p \\ \mathbb{P}(X=0)&=1-p\end{align}$$
If $X \sim \text{Bernoulli}(p)$, then
$$
\begin{align}
\mathbb{E}(X)&=p\\
Var(X)&=p(1-p)
\end{align}
$$

- **Bionomial random variable is the sum of Bernoulli variables**
