# W10D2 - Confidence Intervals
- Population mean is approximately equal to sample mean: $\mu \approx \bar{x}$
- Population variance is approximately equal to sample variance: $\sigma^2 \approx s_x^2$
## Point estimate
- Let $\theta$ (‘theta’) stand for a fixed but unknown parameter; a **point estimate** $\hat{\theta}$ (‘theta hat’) is a statistic, computed from the $x_i$’s, and used to estimate $\theta$.
- For the **population mean** $\mu$, we typically estimate it using $\hat{\mu}=\bar{x}$
- For the **population variance** $\sigma^2$, we typically use $\hat{\sigma}^2=s_x^2$
- $s_x^2$ is an observed value of the random variable $S^2:=\frac{1}{n-1}\sum_{i=1}^{n}(X_i-\bar{X}_n)^2$
- $\mathbb{E}(S^2)=\sigma^2$
## Confidence interval
- Interval estimate $[L, U]$ of a parameter $\theta$, such that
$$
\mathbb P(L≤\theta≤U)=1-\alpha
$$
- where $\alpha$ is a (small) probability ($\alpha < 0.5$), and L, U are computed from a sample $X_1, X_2, \dots , X_n$.
- The interval $[L, U]$ is called a $100(1-\alpha)\%$ **two-sided** confidence interval for $\theta$.
- $(1-\alpha)$ is called the **confidence level**.
- Commonly used values of $\alpha$ include 0.1, 0.05 and 0.01. 0.05 is very common, resulting in a 95% confidence level.
- Let $z_{\alpha/2}=-\Phi^{-1}(\frac{\alpha}{2})$
- When $n$ is large (**or** for any $n$ if the distribution is normal), a $100(1-\alpha)\%$ **two sided confidence interval** for $\mu$ is given by
$$
[\bar{x}-z_{\alpha/2}\frac{\sigma}{\sqrt{n}}, \bar{x}+z_{\alpha/2}\frac{\sigma}{\sqrt{n}}]
$$
## One-sided confidence intervals
Note that it is $\alpha$ instead of $\alpha / 2$
- **Lower** $100(1 - \alpha)\%$ confidence interval: $\left[ \bar{x} - z_{\alpha} \frac{\sigma}{\sqrt{n}}, \infty \right)$
- **Upper** $100(1 - \alpha)\%$ confidence interval: $\left( -\infty, \bar{x} + z_{\alpha} \frac{\sigma}{\sqrt{n}} \right]$
## Student's t-distribution
- When n is not large, the distribution has been worked out with n-1 degrees of freedom

![image](ref/t%20distribution.png)
- $t_{n-1, \alpha / 2}$ is a value from the inverse cdf of the **t-distribution**
- Two-sided confidence interval for $\mu$, when $\sigma ^2$ is unknown
$$
\left[ \bar{x} - t_{n-1, \alpha/2} \frac{s_x}{\sqrt{n}},\ \bar{x} + t_{n-1, \alpha/2} \frac{s_x}{\sqrt{n}} \right]
$$
## Summary
| variance | distribution | n | outcome |
| --- | --- | --- | --- |
|known|normal|any|Z distribution|
|known|not normal|large|Z distribution|
|unknown|normal|any|t distribution|
|unknown|not normal|very large|t distribution|
