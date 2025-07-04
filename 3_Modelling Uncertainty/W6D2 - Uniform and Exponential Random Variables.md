# W6D2 - Exponential Random Variables
## Definition
A continuous random variable X is said to satisfy an **exponential distribution** with (constant) parameter $λ>0$, if its probability density function is given by
$$
f(x)=\begin{cases}
\lambda e^{-\lambda x},&\text{if }x\geq0 \\
0,&\text{if }x<0
\end{cases}
$$
- Denoted by $X \sim \text{exponential} (\lambda)$
- CDF is given by
$$
F(x)=\mathbb{P}(X\leq x)=\begin{cases}
1-e^{-\lambda x},&\text{if }x\geq0 \\
0,&\text{if }x<0
\end{cases}
$$
- Useful identity
$$
\mathbb P(X>x)=e^{-\lambda x}
$$
- Plot
![[exponential.png]]
- Application: Often used to model the amount of **time** until an event of interest occurs.
    - Time until the next earthquake.
    - Time until the next phone call.
    - Time until the next machine failure.
    - Time until a radioactive particle decays.
    - Service times and inter-arrival times in a queue.
- The parameter λ can be interpreted as the average rate of occurrence.
- **Note: ERVs have a property known as memorylessness**
    - e.g The probability of a call lasting more than 15m, given it has already lasted 10m, is the same as the probability of a call lasting more than 5m

$$
\mathbb{P}(X>(s+t)\mid X>t)=\mathbb{P}(X>s)
$$
> Proof:
> $$
\begin{align}
\mathbb{P}(X>(s+t)\mid X>t)&=\frac{\mathbb{P}(X>(s+t))}{\mathbb{P}(X>t)}\\
&=\frac{e^{-\lambda (s+t)}}{e^{-\lambda t}}\\
&=e^{-\lambda s}\\
&=\mathbb{P}(X\ >\ s)
\end{align}
$$
## Expectation and Variance
- Expectation, $\mathbb E(X)= \frac{1}{\lambda}$
    - Proof: (The first $\textcolor{red}{0}$ can be justified using L’Hôpital’s rule.)
$$
\begin{align}
\mathbb{E}(X) &= \int_{-\infty}^{\infty} x f(x)\, dx = \int_0^{\infty} x \cdot \lambda e^{-\lambda x}\, dx \\
&= \int_0^{\infty} 
\underbrace{x}_{u}
\underbrace{(-e^{-\lambda x})'}_{v'}\, dx \\
&= \underbrace{x}_{u} \cdot \underbrace{-e^{-\lambda x}}_{v} \Bigg|_0^{\infty} - \int_0^{\infty} \underbrace{(x)'}_{u'} \cdot \underbrace{-e^{-\lambda x}}_{v} \, dx \\
&= \textcolor{red}{0} - 0 + \int_0^{\infty} 1 \cdot e^{-\lambda x} \, dx \\
&= -\frac{1}{\lambda} e^{-\lambda x} \Bigg|_0^{\infty}
= -\frac{1}{\lambda}(0 - 1) \\
&= \frac{1}{\lambda}.
\end{align}
$$
- Variance, $\operatorname{Var}(X)=\frac{1}{\lambda^2}$