# W10D1 - Central Limit Theorem
## Sample mean of RV’s
Let $X_1, X_2, \dots, X_n$ be random variables. The **sample mean** of these random variables is defined as
$$
\bar{X}_n:=\frac 1n \sum_{i=1}^n X_i
$$
- $\bar{X}_n \neq \mathbb E(X_i)$
- $\bar{X}_n \neq \bar{x}$
- Note that $\bar{X}_n$ is a **random variable**.
- If $X_1, X_2, \dots, X_n$ are **independent and all have the same distribution**, then they are said to be **independent and identically distributed (i.i.d.)**.
- $X_1, X_2, \dots, X_n$ have the same mean $\mu$ and variance $\sigma^2$.
$$
\mathbb E(\bar{X}_n)=\mu
$$
$$
\mathrm{Var}(\bar{X}_n)=\frac{\sigma^2}{n}
$$
## Law of Large Numbers
$$
\operatorname*{lim}_{n\rightarrow\infty}\mathbb{P}\bigl(\vert\bar{X}_{n}-\mu\vert\,<\epsilon\bigr)\,=\,1
$$
- Mean reverting nature if you have many trials (n)
## Central Limit Theorem (CLT)
CLT describes the behaviour of the sum and average of a large number of i.i.d random variables
$$
\lim_{n \to \infty} \mathbb{P} \left( \frac{\overline{X}_n - \mu}{\sigma / \sqrt{n}} \leq x \right) = \Phi(x)
$$
When $X_i$'s are i.i.d and $n$ is large (>=30)
$$
\frac{\overline{X}_n - \mu}{\sigma / \sqrt{n}} \approx \mathcal{N}(0, 1) = Z, \\
\overline{X}_n \approx \mathcal{N} \left( \mu, \frac{\sigma^2}{n} \right), \\
\sum_{i=1}^{n} X_i \approx \mathcal{N}(n\mu, n\sigma^2).
$$
- **0.5 Correction is only needed when approximating from discrete RVs to normal RV**
