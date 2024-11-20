## L'Hôpital's Rule
- Only works with fractions
- Suppose $f$ and $g$ are differentiable and $g'(x) ≠ 0$ near $a$ (except possibly at $a$)
	- $\displaystyle\lim_{x \to a}f(x) = 0$ **and** $\displaystyle\lim_{x \to a}g(x) = 0$, **OR**
	- $\displaystyle\lim_{x \to a}f(x) = ±∞$ **and** $\displaystyle\lim_{x \to a}g(x) = ±∞$
- We have the **intermediate form** $\frac{0}{0}$ or $\frac{∞}{∞}$, then
$$
\lim_{x \to a}\frac{f(x)}{g(x)} = \lim_{x \to a}\frac{f'(x)}{g'(x)}
$$
- If the limit on the right side exists (or is $±∞$)
- This is **not** quotient rule
- **If the equation is in the form $\displaystyle\lim_{ x \to ∞ }f(x)\cdot g(x)$, where $\displaystyle\lim_{x \to a} f(x) = 0$ and $\displaystyle\lim_{x \to a} g(x) = ± ∞$, convert the equation to a quotient to apply the rule.**
## Comparing Rates of Growth
$$
\lim_{x \to ∞} \frac{f(x)}{g(x)} =
\begin{cases}
0 & \text{if } g(x) > f(x) \\
∞ & \text{if } g(x) < f(x)
\end{cases}
$$
- At the point where $f(x) = 0$ and $g(x) = 0$
	- If we zoom in far, the graphs would start to look linear
	- Their ratio would be the ratio of their gradient (or derivatives)
	- This is a visual argument to justify L'Hôpital's Rule
- **Steps to solve problems comparing growth:**
	1. Let the two functions being compared be f(x) and g(x)
	2. Calculate their ratio using the limit function above
	3. The answer should be $0$ or $∞$. Use the conditions to the right to figure out whether g(x) < f(x) or otherwise.

> **Example of L'Hôpital's Rule:** 
> 
> $$\begin{align}
\lim_{ x \to ∞ } (e^x-x)&=\lim_{ x \to ∞ } x\left( \frac{e^x}{x}-1 \right) \\
&=\lim_{ x \to ∞ }x \cdot \left(\lim_{ x \to ∞ } \frac{e^x}{x}-1\right)\\
\text{By L'H\^opital's Rule:}\\
&=∞ \cdot \left(\lim_{ x \to ∞ } \frac{e^x}{1}-1\right) \\
&=∞ \cdot (∞-1) \\ \\
&=∞
\end{align}$$