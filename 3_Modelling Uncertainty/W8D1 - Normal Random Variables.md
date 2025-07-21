# W8D1 - Normal Random Variables

## Standard Normal Distribution

A continuous random variable Z is said to satisfy a **standard normal distribution** if its probability density function is given by
$$
\phi(x)=\frac{1}{\sqrt{2\pi}}e^{-x^2/2}
$$

- pdf is denoted by $\phi$
- cdf is denoted by $\Phi$
- $\phi$ is a **valid** pdf, i.e. its total area under it is 1.
- $\Phi(x)=\mathbb P(Z\leq x)=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{x} e^{-t^2/2} \, dt$ **cannot be expressed as a finite combination of elementary functions**.

Proof that $\Phi(-x)=1-\Phi(x)$:
$$
\Phi(-x)=\mathbb P(Z\leq x)=\mathbb P(Z>x)=1-\mathbb P(Z\leq x)=1-\Phi(-x)
$$
Proof that $\mathbb E(Z)=0$:
$$
\begin{align}
f_x(z)&=\frac{1}{\sqrt{2\pi}}e^{-z^2/2} \\
\mathbb E(Z)&=\int_{-\infty}^{\infty} z\cdot f_x(z) \, dz  \\
&=\textcolor{red}-\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} \textcolor{red}-ze^{-z^2/2} \, dz \\
\text{Since }\int f'(x)\,e^{f(x)}\,dx&=e^{f(x)}+c, \\
&=-\frac{1}{\sqrt{2\pi}}\left[ -e^{-\frac{1}{2}z^2} \right]_{-\infty}^{\infty} \\
&=-\frac{1}{\sqrt{2\pi}}\left( e^{-\infty}-e^{-\infty} \right) \\
&=0-0=0
\end{align}
$$

## General Normal Distribution

### Transformation

Consider the random variable $X = \sigma Z + \mu$
$$
F(x) = \mathbb{P}(X \leq x) = \mathbb{P}(\sigma Z + \mu \leq x) = \mathbb{P}\left(Z \leq \frac{x - \mu}{\sigma} \right) = \Phi\left(\frac{x - \mu}{\sigma} \right)
$$
$$
f(x) = F'(x) = \frac{d}{dx} \Phi\left(\frac{x - \mu}{\sigma} \right) = \frac{1}{\sigma} \, \phi\left(\frac{x - \mu}{\sigma} \right) = \frac{1}{\sqrt{2 \pi} \, \sigma} \, e^{-(x - \mu)^2/2 \sigma^2}
$$

- A normal distribution is denoted by $X \sim N(\mu, \sigma ^2)$
    - $\mathbb{E}(X) = \mu =$ Mean
    - Var$(X) = \sigma ^2 =$ Standard deviation
    - $Z$ is a special case of the general normal RV, with mean 0 and variance 1
    - $\textcolor{red}{Z=\frac{X-\mu}{\sigma}}$
    - $f_x(z)=\frac{1}{\sqrt{2\pi \sigma^2}}e^{-\frac{1}{2\sigma^2}(x-\mu)^2}$
## Summary

| RV | pdf, $x$ range | $\mathbb{E}$ | $\text{Var}$ | example usage |
|------------|-----------------------------------------------------|---------------------------|------------------------------|----------------------------------|
| uniform | $\frac{1}{b - a},\ a \leq x \leq b$ | $\frac{a + b}{2}$ | $\frac{(b - a)^2}{12}$ | random number generation |
| exponential| $\lambda e^{-\lambda x},\ x \geq 0$ | $\frac{1}{\lambda}$ | $\frac{1}{\lambda^2}$ | time until an event occurs |
| normal | $\frac{1}{\sqrt{2\pi}\sigma} e^{-(x - \mu)^2 / (2\sigma^2)},\ x \in \mathbb{R}$ | $\mu$ | $\sigma^2$ | ubiquitous |
$\mathbb{E}(e^{tx})$ when $X\sim N(\mu,\sigma^2)$
## Examples
We have a normal distribution of mean 160 and standard deviation 5, i.e. $X\sim \mathcal N(160, 5^2)$.
- Probability that a randomly selected value is between 150 and 170
$$
\mathbb P(150<X<170)=\mathbb P(\mu-2\sigma\leq X\leq \mu+2\sigma)\approx 0.9545
$$
- Probability that 20 randomly selected values are between 150 and 170
    - For independent events
$$
\mathbb P(150<X<170)\text{ for 20 events}=0.9545^{20}
$$
- Given that a value is more than 165, the probability that it is more than 170 is
$$
\mathbb P(X>170|X>165)=\frac{\mathbb P(X>170)}{\mathbb P(X>165)}=\frac{\mathbb P(X>\mu+2\sigma)}{\mathbb P(X>\mu+\sigma)}
$$
---
Suppose that only values of $3±0.01$ are accepted and we have a normal distribution $X\sim \mathcal N(2.995, 0.01^2)$. What proportion of values will be rejected?

- Probability that a value will be accepted is
$$
\begin{align}
\mathbb P(2.99 \leq X \leq 3.01)&=\mathbb P\left( \frac{2.99-2.995}{0.01}\leq \frac{X-2.995}{0.01} \leq \frac{3.01-2.995}{0.01} \right) \\
&=\mathbb P(-0.5\leq Z\leq 1.5) \\
&=\Phi(1.5)-\Phi(-0.5) \\
&=1-\Phi(-1.5)-\Phi(-0.5) \\
&\approx06247
\end{align}
$$
---
We have a normal distribution of mean 64 and variance 0.6084. What maximum value $c$ ensures that the values of this normal distribution only exceed $c$ 0.5% of the time?

We wish to find $c$ such that
$$
\begin{align}
\mathbb P(X>c)=0.005 &\implies \mathbb P\left( \frac{X-64}{\sqrt{0.6084}}> \frac{c-64}{\sqrt{0.6084}} \right)=0.005 \\
&\implies \mathbb P\left( Z > \frac{c-64}{0.78} \right)=0.005 \\
&\implies \mathbb P\left( Z < \frac{64-c}{0.78} \right)=0.005 \\
\text{Using the table, we find that} \\
\Phi^{-1}(0.005)&\approx-2.575 \\
\text{Hence, }\frac{64-c}{0.78}&\approx-2.575 \\
c&\approx 66
\end{align}
$$
---
A random variable $X$ is normally distributed with $\mu=2$ and $\sigma=1$. If X exceeds $4$, damage will be caused, and the damage caused is $X-4$.

- Write down $f(x)$, the pdf of $X$.
- Let $g(x)$ denote the amount of damage, and write it as a piecewise function.
- Hence, write down an integral for $\mathbb E(g(X))$
$$
\begin{align}
X&\sim\mathcal N(2,1) \\
f(x)&=\frac{1}{\sqrt{2\pi}}e^{-(x-2)^2/2} \\
g(x)&=\begin{cases}
0, & \text{if}X\leq4 \\
X-4 & \text{if}X>4
\end{cases} \\
\mathbb E(g(X))&=\int_{-\infty}^{\infty} g(x)\,f(x) \, dx \\
&=\int_{4}^{\infty} \frac{x-4}{\sqrt{2\pi}}e^{-(x-2)^2/2} \, dx\\
\text{Let }t=x-2: \\
\mathbb E(g(X))&=\int_{2}^{\infty} \frac{t-2}{\sqrt{2\pi}}e^{-t^2/2} \, dt \\
&=\int_{2}^{\infty} \frac{1}{\sqrt{2\pi}}te^{-t^2/2}\,dt-2\int_{2}^{\infty} \frac{1}{\sqrt{2\pi}}e^{-t^2/2}\,dt \\
&=\frac{1}{\sqrt{2\pi}}e^{-t^2/2}\bigg\rvert_2^\infty-2\int_{2}^{\infty}\phi(t)dt \\
&=\frac{1}{\sqrt{2\pi}}e^{-2}-2\mathbb P(Z>2) \\
&=\frac{1}{\sqrt{2\pi}}e^{-2}-2\Phi(-2) \\
&=0.0085
\end{align}
$$