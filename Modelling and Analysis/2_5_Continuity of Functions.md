A function is continuous if there are no discontinuities. That is,
$$f(a) \text{ is defined and } \displaystyle\lim_{ x \to a } f(x) = \displaystyle\lim_{ x \to a^- } f(x) = \displaystyle\lim_{ x \to a^+ } f(x) = f(a)$$
## Common continuous functions
- Polynomials in their domains
- Trigonometric functions in their domains
- Exponential functions in their domains
- Logarithmic functions in their domains
- the sum, subtraction, product or quotient of the above functions, when they are properly defined.

## Continuous piecewise functions
- Given $f(x) =\begin{cases} g(x) & \text{for } x < n \\h(x) & \text{for } x \geq n\end{cases}$
- Check if range is defined for both components of a piecewise function $g(x)$ and $h(x)$
	- Where a single function is defined, it will also be continuous
- Prove that $\displaystyle\lim_{x \to n}g(x) = \displaystyle\lim_{x \to n}h(x)$ by showing $\displaystyle\lim_{x \to n^-}g(x) = \displaystyle\lim_{x \to n^+}h(x)$ at the **transition point** $n$

## Intermediate value theorem
- Only true for continuous functions
- Suppose that $f$ is continuous on the closed interval $[a, b]$.
- Let N be any number between $f(a)$ and $f(b)$.
- There exists a number $c$ in $[a, b]$ such that $f(c) = N$.
- The existence of $c$ such that $f(c) = N$ does not mean that it is unique. There can be multiple values of c that satisfy $f(c) = N$.