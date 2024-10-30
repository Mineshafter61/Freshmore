Suppose c is a constant and the limits $\displaystyle\lim_{ x \to a } f(x)$ and $\displaystyle\lim_{ x \to a } g(x)$ exist. Then:
1. $\displaystyle\lim_{ x \to a }[f(x)+g(x)] = \lim_{ x \to a }f(x)+\lim_{ x \to a }g(x)$
2. $\displaystyle\lim_{ x \to a }[f(x)-g(x)] = \lim_{ x \to a }f(x)-\lim_{ x \to a }g(x)$
3. $\displaystyle\lim_{ x \to a }[cf(x)] = c \lim_{ x \to a }f(x)$
4. $\displaystyle\lim_{ x \to a }[f(x)g(x)]=\lim_{ x \to a }f(x)\cdot \lim_{ x \to a }g(x)$
5. $\displaystyle\lim_{ x \to a }\frac{f(x)}{g(x)} = \frac{\displaystyle\lim_{ x \to a }f(x)}{\displaystyle\lim_{ x \to a }g(x)}$ if $\displaystyle\lim_{ x \to a }g(x)\neq 0$
6. $\displaystyle\lim_{ x \to a }[f(x)]^n = [\lim_{ x \to a }f(x)]^n$
7. $\displaystyle\lim_{ x \to a }c$
8. $\displaystyle\lim_{ x \to a }x=a$
9. $\displaystyle\lim_{ x \to a } x^n = a^n$ where n is a positive integer (only for finite numbers)
10. $\displaystyle\lim_{ n \to a } \root n \of{x} = \root n \of{a}$ where n is a positive integer (only for finite numbers)
11. $\displaystyle\lim_{ n \to a } \root n \of{f(x)} = \root n \of{\lim_{ n \to a } f(x)}$ where n is a positive integer (only for finite numbers)

For $\displaystyle\lim_{ x \to a } f(x)$ to exist, we must have $\displaystyle\lim_{ x \to a } f(x) = \displaystyle\lim_{ x \to a^- } f(x) = \displaystyle\lim_{ x \to a^+ } f(x)$.
However, if $\displaystyle\lim_{ x \to a } f(x) = \pm\infty$, the limit does not exist.

For a graph y=f(x):
- If $f(a) = \displaystyle\lim_{ x \to a } f(x)$, f(x) is continuous at x=a.
- If $f(a) \neq \displaystyle\lim_{ x \to a } f(x)$, x=a is a removable discontinuity.
- If $f(a)$ is undefined, x=a is a removable singularity.

## Piecewise function notation
- x approaches a from the left (left hand limit): $\displaystyle\lim_{ x \to a^- } f(x)$
	- $a^-$: value arbitrarily close to but smaller than a.
- x approaches a from the right (right hand limit): $\displaystyle\lim_{ x \to a^+ } f(x)$
	- $a^+$: value arbitrarily close to but larger than a.

## Limits of tangent
- $\displaystyle\lim_{ x \to \pi/2^+ } \tan(x) = -\infty$
- $\displaystyle\lim_{ x \to \pi/2^- } \tan(x) = \infty$

## Squeeze Theorem
- If $f(x) \leq g(x) \leq h(x)$ when x is near a (except possibly at x = a) and we have
$$\lim_{ x \to a }f(x) = \lim_{ x \to a }h(x) = L$$
then
$$\lim_{ x \to a } g(x) = L$$
- Commonly used to evaluate the limits:
	- $\displaystyle\lim_{\theta \to 0}\frac{\sin(\theta)}{\theta} = 1$
	- $\displaystyle\lim_{\theta \to 0}\cos(\frac{1}{\theta}) = 0$
	- $\displaystyle\lim_{\theta \to 0}\frac{\tan(\theta)}{\theta} = 1$
	- Useful: $\displaystyle\lim_{\theta \to 0^-}\frac{\sin(\theta)}{\theta} = \displaystyle\lim_{\theta \to 0^+}\frac{\sin(-\theta)}{-\theta}$