## L'Hôpital's Rule
- Suppose $f$ and $g$ are differentiable and $g'(x) \neq 0$ near $a$ (except possibly at $a$)
	- $\displaystyle\lim_{x \to a}f(x) = 0$ **and** $\displaystyle\lim_{x \to a}g(x) = 0$, OR
	- $\displaystyle\lim_{x \to a}f(x) = \pm\infty$ **and** $\displaystyle\lim_{x \to a}g(x) = \pm\infty$
- We have the **intermediate form** $\frac{0}{0}$ or $\frac{\infty}{\infty}$, then
$$

\lim_{x \to a}\frac{f(x)}{g(x)} = \lim_{x \to a}\frac{f'(x)}{g'(x)}

$$
- If the limit on the right side exists (or is $\pm\infty$)
- This is **not** quotient rule


$$
\begin{gather}
y=x^4-4x^3\\
y'=4x^3-12x^2\\
y''=12x^2-24x
\end{gather}
$$
### Comparing Rates of Growth
$$

\lim_{x \to \infty} \frac{f(x)}{g(x)} =

\begin{cases}

0 & \text{if } g(x) \to \infty \text{ quicker than } f(x) \to \infty\\

\infty & \text{if } g(x) \to \infty \text{ slower than } f(x)\to \infty

\end{cases}

$$
- At the point where $f(x) = 0$ and $g(x) = 0$
	- If we zoom in far, the graphs would start to look linear
	- Their ratio would be the ratio of their gradient (or derivatives)
	- This is a visual argument to justify L' Hospital's Rule