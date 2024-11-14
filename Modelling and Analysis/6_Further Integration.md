## Improper integrals
- Definite integral when the **interval** is **infinite**
	- **Convergent** if the corresponding (final value) limit exists
	- **Divergent** if the corresponding (final value) limit does not exist
1. Provided that this limit exists (i.e. a finite number), if $\int_{a}^{b} f(x) \, dx$ exists for every number $b ≥ a$, then $$ \int_{a}^{\infty}f(x)\,dx=\lim_{b\to \infty}\int_{a}^{b}f(x)\,dx $$
2. Provided that this limit exists (i.e. a finite number), if $\int_{a}^{b} f(x) \, dx$ exists for every number $a ≥ b$, then $$ \int_{-\infty}^{b}f(x)\,dx=\lim_{a\to -\infty}\int_{a}^{b}f(x)\,dx $$
3. If the improper integrals $\int_{a}^{\infty} f(x) \, dx$ and $\int_{-\infty}^{a} f(x) \, dx$ are convergent, then we define the sum $\int_{-\infty}^{\infty} f(x) \, dx$ to also be convergent, where $a$ is any real number

> Example:
> $$\begin{align}\int_{-\infty}^{\infty} \frac{1}{1+x^2} \, dx&=\int_{-\infty}^{0}\frac{1}{1+x^2}\,dx+\int_{0}^{\infty}\frac{1}{1+x^2}\, dx \\
&=\lim_{ b \to -\infty }\int_{b}^{0}\frac{1}{1+x^2}\,dx+\lim_{ b \to \infty } \int_{0}^{b} \frac{1}{1+x^2}\,dx \\
&=\lim_{ b \to -\infty }[\tan^{-1}x]_{b}^{0}+\lim_{ b \to \infty }[\tan^{-1}x]_{0}^{b} \\
&=\lim_{ b \to -\infty }[\tan^{-1}0-\tan^{-1}b]+\lim_{ b \to \infty }[\tan^{-1}b-\tan^{-1}0] \\
&=-\tan^{-1}(-\infty)+\tan^{-1}(\infty) \\
&=-\left( -\frac{\pi}{2} \right)+\frac{\pi}{2} \\
&=\pi\end{align}
$$
### Finding convergence/divergence
- Find integral for edge case
- Find integral for non-edge case
- Determine the $<$ and $>$ between the edge cases

> Example: For what values of $p$ is $\int_{1}^{\infty} \frac{1}{x^p} \, dx$ convergent?
> $$\begin{gather}
p=1: \int_{1}^{\infty} \frac{1}{x^{p}} \, dx=\lim_{ b \to \infty } \int_{1}^{b} \frac{1}{x}\,dx=\lim_{ b \to \infty }[\ln(x)]_1^b=\lim_{ b \to \infty } [\ln b-1]=\infty \\
p\neq1: \int_{1}^{\infty} \frac{1}{x^{p}} \, dx=\lim_{ b \to \infty } \int_{1}^{b} \frac{1}{x^p}\,dx=\lim_{ b \to \infty } \left[\frac{x^{-p+1}}{-p+1}\right]_1^b=\lim_{ b \to \infty } \frac{1}{1-p}\left[ \frac{1}{b^{p-1}}-1 \right]\\
p>1\implies(p-1)>0\implies \lim_{ b \to \infty } b^{p-1}=\infty \implies \lim_{ b \to \infty } \frac{1}{b^{p-1}}=0\\\implies \lim_{ b \to \infty } \frac{1}{1-p}\left[ \frac{1}{b^{p-1}}-1 \right]=-\frac{1}{1-p}=-\frac{1}{p-1}\\
p<1 \implies (p-1)<0 \implies\lim_{ b \to \infty } b^{p-1}=0 \implies \lim_{ b \to \infty } \frac{1}{b^{p-1}}=\infty\\
\implies\lim_{ b \to \infty } \frac{1}{1-p}\left[ \frac{1}{b^{p-1}}-1 \right]=\infty\\
∴ \int_{1}^{\infty} \frac{1}{x^{p}}\,dx \text{ converges when } p>1 \text{ and diverges when } p≤1
\end{gather}$$
### Discontinuity in f(x)
1. If $f$ is continuous on $[a,b)$ and is discontinuous at $b$, then $\displaystyle\int_{a}^{b} f(x) \, dx =\lim_{ t \to b^- } \int_{a}^{t} f(x) \, dx$ if this limit exists.
2. If $f$ is continuous on $(a,b]$ and is discontinuous at $a$, then $\displaystyle\int_{a}^{b} f(x) \, dx =\lim_{ t \to a^+ } \int_{t}^{b} f(x) \, dx$ if this limit exists.
3. If $f$ has a **discontinuity** at $c$, where $a < c < b$, and both $\int_a^c f(x) \, dx$ and $\int_c^b f(x) \, dx$ are convergent, then we define $\displaystyle\int_{a}^{b} f(x) \, dx=\int_{a}^{c} f(x) \, dx+\int_{c}^{b} f(x) \, dx$

> Example:
> $$\begin{align}
\int_{0}^{\pi/2}\sec(x)\,dx &=\lim_{t\to\pi/2^-}\int_{0}^{t} \sec(x)\,dx \\
&=\lim_{t\to\pi/2^-}[\ln|\sec x+\tan x|]_0^t \\
&=\lim_{t\to\pi/2^-}[\ln|\sec t+\tan t|-\ln|\sec 0+\tan 0|] \\
&=\lim_{t\to\pi/2^-}[\ln|\sec t+\tan t|-\ln(1+0)] \\
&=\lim_{t\to\pi/2^-}[\ln|\sec t+\tan t|] \\
&=\ln|\sec (\pi/2^-)+\tan (\pi/2^-)| \\
&=\infty
\end{align}
$$
## Laplace Transform
- If $f(t)$ is continuous for $t \geq 0$, then the *Laplace transform* of the function $F$ is defined by
$$
F(s) = \int_0^\infty f(t)e^{-st}dt
$$
and the domain of $F$ is the set consisting of all numbers $s$ for which the integral converges