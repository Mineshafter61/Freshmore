If $\displaystyle\lim_{ x \to \infty } f(x) = L$ an $\displaystyle\lim_{ x \to \infty }g(x) = M$ and $c$ and $d$ are constants, then:
- $\displaystyle\lim_{ x \to \infty }[f(x) \pm g(x)] = \lim_{ x \to \infty } f(x) \pm g(x) = L \pm M$
- $\displaystyle \lim_{ x \to \infty } c f(x) = c \lim_{ x \to \infty } f(x) = cL, \lim_{ x \to \infty } c = c$
- $\displaystyle\lim_{ x \to \infty }[f(x) \cdot g(x)] = \lim_{ x \to \infty } f(x) \cdot g(x) = L \cdot M$
- $\displaystyle\lim_{ x \to \infty } \frac{f(x)}{g(x)} = \frac{\displaystyle\lim_{ x \to \infty }f(x)}{\displaystyle\lim_{ x \to \infty }g(x)} = \frac{L}{M}, M \neq 0$
- $\displaystyle\lim_{ x \to \infty }[f(x)]^p = [\lim_{ x \to \infty }f(x)]^p, p>0 \text{ and } f(x) > 0$
- $\displaystyle\lim_{ x \to \infty } \frac{1}{x^p} = 0, p > 0$
Exponential function limits:
$$\lim_{x \to \infty}b^x =
\begin{cases}
0 & \text{for } 0 < b < 1 \\
\text{undefined} & \text{for } b = 1 \\
\infty & \text{for } b > 1
\end{cases} $$

$$\lim_{x \to -\infty}b^x =
\begin{cases}
\infty & \text{for } 0 < b < 1 \\
\text{undefined} & \text{for } b = 1 \\
0 & \text{for } b > 1
\end{cases} $$
## Techniques for evaluating limits
- Substitution
	- Replace all variables with limits
	- Will result in indeterminate forms most of the time
- Factorisation
	- Factorise the $x$ term out
- Conjugate
	- Meaning $\displaystyle\sqrt{x}-x \cdot \frac{\sqrt{x}+x}{\sqrt{x}+x}$
	- Uses $\displaystyle(a + b)(a - b) = a^2 - b^2$
	- Useful to remove the $x$ term from the **numerator** and move it to the **denominator**
- Divide by the highest power term (for fractions)
	- Commonly used for rational functions (or fractions)
	- Useful because $\displaystyle\lim_{x \to \infty} \frac{n}{x} = 0$
- L'Hôpital's rule (for fractions)
	- Covered in `Week 6`
## Indeterminate forms
- $\frac{0}{0}$
- $\frac{\infty}{\infty}$
- $\infty-\infty$
- $0^0$
- $1^\infty$
- $\infty^0$
