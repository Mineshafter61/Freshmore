# W13D2 - Maximum Likelihood

- Purpose: estimate parameters
- Transforms parameter estimation into an optimisation problem
- Maximise the probability of observing the data

## Likelihood function

Given a probability distribution, let $\theta$ stand for the **parameter** to be estimated, and denote the probability mass/density function to be $f(x|\theta)$.

If we have a random sample of size $n$ drawn from the distribution, and the observed values are $x_1, x_2, \dots, x_n$, the **likelihood function** $L(\theta)$ is

$$L(\theta)=f(x_1|\theta) \times f(x_2|\theta) \times \cdots \times f(x_n|\theta)$$

Note that $L(\theta)= \mathbb P(\text{observing } x_1, x_2, \dots, x_n)$, and $f(x_i|\theta)=\mathbb P(\text{observing } x_i)$.

**We think of $L$ as a function of $\theta$ only, and treat the $x_i$'s as fixed.**

## Maximum likelihood estimate (MLE)

If the **maximum** of $L(\theta)$ occurs at a point $\hat{\theta}$, $\hat{\theta}$ is the parameter value for which the observed data is most likely to have been generated, so we use it for our estimate for $\theta$.

- $\hat{\theta}$ is the **maximiser** of $L(\theta)$.
- To find $\hat{\theta}$, we can equivalently **maximise $\ln(L(\theta))$ instead**; this simplifies calculations (maximum of $L$ and $\ln(L)$) occur at the same point.)
- We can find $\hat{\theta}$ by solving $\frac{d}{d\theta}\ln(L(\theta))=0$
- **Show that the stationary point is a global maximum**: check that $\frac{d^2}{d\theta^2}\ln(L(\theta)) < 0$
