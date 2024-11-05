## Indefinte integrals
- Integration: process of finding the antiderivative
- General expression of antiderivatives: $\int f(x) dx = F(x)+c \implies F'(x)=f(x)$
- Integration is the inverse of differentiation:
	- $\frac{d}{dx} e^x = e^x\implies\int \frac{d}{dx} e^x \mathop{dx} = \int e^x \mathop{dx} \implies \int e^x dx=e^x+c$
	- $\frac{d}{dx}\sin x=\cos x \implies \int\frac{d}{dx}\sin x\mathop{dx}=\int\cos x\mathop{dx} \implies \sin x=\int \cos x \mathop{dx}$
- Constant of integration C **must be included in solution**.
## Standard formulae
- $\int[f(x)\pm g(x)]\,dx=\int f(x)\,dx\pm\int g(x)\,dx$
- $\int k f(x) \mathop{dx} = k \int f(x)\mathop{dx}$
- $\int x^{n}dx=\frac{x^{n+1}}{n+1}+C; n \neq -1$
- $\int \frac{1}{x} \mathop{dx} = \ln |x| +C$ (NOTE: **Absolute symbol MUST be included**)
- $\int e^{x} \mathop{dx}=e^{x}+C$
- $\int e^{kx} \mathop{dx}=\frac{1}{k}e^{kx}+C$
- $\int a^x \mathop{dx}=\frac{a^x}{\ln a}+C$
- $\int \sin x \mathop{dx}=-\cos x+C$
- $\int \cos x \mathop{dx}=\sin x+C$
- $\int \sec^{2} x \mathop{dx}=\tan x+C$
- $\int \csc^{2} x \mathop{dx}=-\cot x+C$
- $\int \sec x\tan x \mathop{dx}=\sec x+C$
- $\int \csc x\cot x \mathop{dx}=-\csc x+C$
- $\int \frac{1}{x^2+1}\,dx=\tan^{-1}x+C$

- Examples:
	- $\int\left( 2x^3-6x+\frac{3}{x^2+1} \right)\,dx=\frac{x^4}{2}-3x^2+3\tan^{-1}x+C$
	- $\int \frac{2t^2+t^{2}\sqrt{t}-1}{t^{2}}\,dx=\int 2+\sqrt{t}-\frac{1}{t^{2}}\,dx=2t+\frac{2t^{3/2}}{3}+\frac{1}{t}+C$
	- $\int[\cos x-\sin x]\,dx=\sin x+\cos x+C$
## Definite integrals
- Definition: Given a **continuous function** $f(x)$ on an interval $[a,b]$, the definite integral from $a$ to $b$ can be defined by **dividing the interval into $n$ subintervals of width** $\Delta x=\frac{b-a}{n}$, and **selecting $x^*_i$ in each subinterval the following way**: $$\int_{a}^{b} f(x) \, dx =\lim_{ n \to \infty } \sum_{i=1}^{n} f(x_i^*) \Delta x$$ if the limit exists.
- **Signed area** of the region bounded by the graph of $f(x)$, the x axis, and the vertical lines $x=a$ and $x=b$
- Can be negative if large portions of the graph are under the x axis.
- Area under graph can be **approximated** by splitting it into rectangles (also known as the [Riemann sum](https://en.wikipedia.org/wiki/Riemann_sum))
$$
\text{Area } \approx \Delta x f(x_0) + \Delta x f(x_1) + \cdots + \Delta x f(x_{n-1})
$$
### Rules
- $\int_{a}^{b} f(x) \, dx = -\int_{b}^{a} f(x) \, dx$
- $\int_{a}^{a} f(x) \, dx = 0$
- $\int_{a}^{b} c \, dx = c(b-a)$
- $\int_{a}^{b} f(x) \pm g(x) \, dx = \int_{a}^{b} f(x) \, dx \pm \int_{a}^{b} g(x) \, dx$
- $\int_{a}^{b} cf(x) \, dx = c\int_{a}^{b} f(x) \, dx$
- $\int_{a}^{b} f(x) \, dx = \int_{a}^{c} f(x) \, dx + \int_{c}^{b} f(x) \, dx$
### Comparison theorem
- If $f(x)\geq g(x)$ for $a \leq x \leq b$, then $$\int_{a}^{b} f(x) \, dx\geq \int_{a}^{b} g(x) \, dx$$
- If $m\leq f(x)\leq M$ for $a\leq x\leq b$, then $$m(b-a)\leq \int_{a}^{b} f(x) \, dx\leq M(b-a)$$
### Evaluation theorem
- Let $f(x)$ be continuous on an interval $[a,b]$, then $$\int_{a}^{b} f'(x) \, dx = f(x)|_a^b = (f(b) + C) - (f(a) + C) = f(b) - f(a)$$
## Finding constant c
- Constant can be determined by the initial conditions in the question
## Finding integral from Riemann sum (//todo)
- $\displaystyle\lim_{ n \to \infty }\sum_{k=1}^{n}f(c_k)\Delta x=\int_{a}^{b} f(x) \, dx$
- Example: $\displaystyle\lim_{ n \to \infty }\sum_{k=1}^{n}-c\left( 2+\frac{8k}{n} \right) \frac{8}{n}$
	- We know that $\displaystyle\Delta x=\frac{b-a}{n}$ and $\displaystyle c_{k}=x_{k}=a+k\Delta x$
	- From $\displaystyle\lim_{ n \to \infty }\sum_{k=1}^{n}-c\left( 2+\frac{8k}{n} \right) \frac{8}{n} \implies \Delta x=\frac{8}{n} \implies b-a=8$
	- Therefore, $f(x)=-c\left( 2+\frac{8k}{n} \right) \implies c_{k}+\frac{8}{n}k=a+k(\Delta x) \implies a=2 \text{ and } b=8+a=10$
	- Hence, $\displaystyle\int_{a}^{b} F(x) \, dx=\lim_{ n \to \infty }\sum_{k=1}^{n}-c\left( 2+\frac{8k}{n} \right) \frac{8}{n}=$