## Back to limits
- If limit exists, $f'(a) = \displaystyle\lim_{x \to a}\frac{f(x)-f(a)}{x-a} = \displaystyle\lim_{h \to 0}\frac{f(a+h)-f(a)}{h}$

$$ f(x) =
\begin{cases}
x^2 & \text{for } x \in [0, ∞) \\
-x & \text{for } x \in (-∞, 0)
\end{cases} $$
- If the limit does not exist, $f'(a)$ does not exist and $y=f(x)$ is not differentiable at $x=a$
- We can also say that 𝑓′(𝑎) is the instantaneous rate of change of 𝑓 at 𝑎.
> Example: Find an equation of the tangent line to the parabola $y = x^2 − 8x + 9$ at the point $(3, −6)$.
>
> *Method 1*:
> 	
> $$\begin{align*}
f(3) &= 9-24+9=-6\\
f'(3) &= \lim_{ x \to 3 } \frac{f(x) - f(3)}{x-3}\\
&=\lim_{ x \to 3 }\frac{x^2-8x+9-(-6)}{x-3}\\
&=\lim_{ x \to 3 }\frac{x^2-8x+15}{x-3}\\
&=\lim_{ x \to 3 }\frac{(x-3)(x-5)}{x-3}\\
&=\lim_{ x \to 3 }x-5\\
&=3-5\\
&=-2\\
\text{Equation:}\\
\frac{y+6}{x-3}&=2\\
y+6&=-2x+6\\
y&=-2x\\
\end{align*}$$
>
>*Method 2*:
>	
> $$\begin{align*}
f(3) &= 9-24+9=-5\\
f'(3) &= \lim_{ h \to 0 }\frac{f(3+h)-f(3)}{h} \\
&=\lim_{ h \to 0 }\frac{(3+h)^2-8(3+h)+9-(-6)}{h} \\
&=\lim_{ h \to 0 }\frac{9+6h+h^2-24-8h+15}{h} \\
&=\lim_{ h \to 0 } \frac{h^2-2h}{h} \\
&=\lim_{ h \to 0 }h-2 \\
&=-2
\end{align*}$$

- Using limits
	- For $x < 0$, $f'(x) = -1$
	- For $x > 0$, $f'(x) = 1$
	- For $x = 0$, $f'(x)$ is undefined
	- i.e $f'(x)$ is **discontinuous** at $x = 0$ and hence $f(x)$ is not **differentiable**
## Definition of Derivatives
- $f'(a) = \displaystyle\lim_{x \to a}\frac{f(x)-f(a)}{x-a} = \displaystyle\lim_{Δ x \to 0}\frac{Δ y}{Δ x} = \frac{dy}{dx} = \frac{d}{dx}(y)$
- Higher order derivatives
	- $f''(x) = f^{(2)}(x) = \frac{d}{dx}(\frac{dy}{dx}) = \frac{d^2y}{dx^2}$
	- $f'''(x) = f^{(3)}(x) = \frac{d}{dx}(\frac{d^2y}{dx^2}) = \frac{d^3y}{dx^3}$
- Note: $\frac{d^2y}{dx^2} ≠ (\frac{dy}{dx})^2$
### Differentiability
- Differentiable: the derivative exists for every value in the function's domain
	- A Differentiable function implies a Continuous function (but not vice versa)
	- Polynomials are differentiable and continuous
	- Sharp changes in gradient means the function is not differentiable
> Example: Where is f = |x| differentiable?
> 	
> 	$$f(x) = |x| =
\begin{cases}
x & \text{for } x ≥ 0 \\
-x & \text{for } x < 0
\end{cases}$$
> 	
> Transition point: x = 0
> 
> If x = 0 is differentiable:
> $$\lim_{ h \to 0^+ } \frac{f(x+h)-f(x)}{h} = \lim_{ h \to 0^- } \frac{f(x+h)-f(x)}{h}$$
> 	
> 	Finding limit when $x ≥ 0$:
> $$\lim_{ h \to 0^+ } \frac{f(x+h)-f(x)}{h} 
= \lim_{ h \to 0^+ } \frac{f(h)-f(0)}{h}
= \lim_{ h \to 0^+ } \frac{h-0}{h}
= \lim_{ h \to 0^+ } \frac{h}{h} = 1$$
> 	
> 	However, when $x < 0$:
> $$\lim_{ h \to 0^- } \frac{f(x+h)-f(x)}{h} 
= \lim_{ h \to 0^- } \frac{f(h)-f(0)}{h}
= \lim_{ h \to 0^- } \frac{-h-0}{h}
= \lim_{ h \to 0^- } \frac{-h}{h} = -1$$
### Derivatives and the graph
- $f'(x) > 0$ means gradient is **positive** and $f(x)$ is increasing
- $f'(x) < 0$ means gradient is **negative** and $f(x)$ is decreasing
- $f'(x) = 0$ means that the gradient is **zero** and this defines a local **maxima** or **minima** on the graph
	- You can tell if its a maximum or minimum point by comparing $f'(x^-)$ and $f'(x^+)$
- $f''(x) ≥ 0$ for all x: convex / concave upwards.
- $f''(x) \leq 0$ for all x: concave / concave downwards.

- The derivative of an even function is an odd function.
- The derivative of an odd function is an even function.
> Proof:
> 	
> $$\begin{align*} \\
\text{Odd function definition: } f(-x) &= -f(x)  \\
\text{Derivative definition: } f'(x) &= \lim_{ h \to 0 } \frac{f(x+h)-f(x)}{h} \\
f'(-x) &= \lim_{ h \to 0 } \frac{f(-x+h)-f(-x)}{h} \\
&= \lim_{ h \to 0 } \frac{f[-(x-h)]-[-f(x)]}{h} \\
&= \lim_{ h \to 0 }\frac{-f(x-h)+f(x)}{h} \\
&= \lim_{ h \to 0 } \frac{f(x)-f(x-h)}{h} \\
&= f'(x) \\\\
f'(x)&=\lim_{ h \to 0 } \frac{f(x+h)-f(x)}{h} \\
&=\lim_{ h \to 0 } \frac{f(x)-f(x-h)}{x-(x-h)} \\
&=\lim_{ h \to 0 } \frac{f(x)-f(x-h)}{h} \\
&= f'(x)\\
\text{Therefore: } f'(x) = f'(-x) \text{, hence even function}
\end{align*}$$
## Basic Differentiation Formula
- Constant functions: $\frac{d}{dx}(c) = 0$
- Power functions: $\frac{d}{dx}(x^n) = n \cdot x^{n-1}$
- Constant multiple rule: $\frac{d}{dx}(c\cdot f(x)) = c \frac{d}{dx}(f(x))$
- Sum and difference rule: $\frac{d}{dx} (f(x) ± g(x)) = \frac{d}{dx} f(x) ± \frac{d}{dx} g(x)$
- Exponential functions: $\frac{d}{dx} b^{f(x)} = b^{f(x)} \ln(b) \cdot f'(x)$
	- Special case: $\frac{d}{dx} e^x = e^x$
- Logarithmic functions: $\frac{d}{dx} \log_b(x) = \frac{f'(x)}{\ln(b)\cdot f(x)}$
	- Special case: $\frac{d}{dx} \ln(x) = \frac{1}{x}$
- Trigonometric functions: 
	- $\frac{d}{dx} \sin (f(x)) = \cos (f(x)) \cdot f'(x)$
	- $\frac{d}{dx} \cos(f(x)) = -\sin (f(x)) \cdot f'(x)$
	- $\frac{d}{dx} \tan (f(x)) = \sec^2 (f(x)) \cdot f'(x)$
	- $\frac{d}{dx} \cot (f(x)) = \csc^2 (f(x))\cdot f'(x)$
	- $\frac{d}{dx} \sec (f(x)) = \sec (f(x))\tan (f(x))\cdot f'(x)$
	- $\frac{d}{dx} \csc (f(x)) = -\csc (f(x))\cot (f(x))\cdot f'(x)$
- Inverse trigonometric functions:
	- $\frac{d}{dx} \sin^{-1}(f(x))=\frac{f'(x)}{\sqrt{1-(f(x))^{2}}}$
	- $\frac{d}{dx} \cos^{-1}(f(x))=\frac{-f'(x)}{\sqrt{1-(f(x))^{2}}}$
	- $\frac{d}{dx} \tan^{-1}(f(x))=\frac{f'(x)}{1+(f(x))^{2}}$
	- $\frac{d}{dx} \cot^{-1}(f(x))=\frac{-f'(x)}{1+(f(x))^{2}}$
	- $\frac{d}{dx}\sec^{-1}(f(x))=\frac{f'(x)}{|f(x)|\sqrt{(f(x))^{2}-1}}$
	- $\frac{d}{dx}\csc^{-1}(f(x))=\frac{-f'(x)}{|f(x)|\sqrt{(f(x))^{2}-1}}$
## Chain Rule
- $\frac{d}{dx} f(g(x)) = f'(g(x)) \cdot g'(x)$
- $\frac{d}{dx}[\ln f(x)]=\frac{f'(x)}{f(x)}$
## Product Rule
- $\frac{d}{dx} \left[ f(x) g(x) \right] = f'(x) g(x) + f(x) g'(x)$
## Quotient Rule
- $\frac{d}{dx} \left[ \frac{f(x)}{g(x)} \right] = \frac{f'(x)g(x) - f(x)g'(x)}{g(x)^2}$
## Implicit Differentiation
- $y = log_bx \implies b^y = x$
- Differentiate on both sides w.r.t $x$
	- $\frac{d}{dx}b^y = \frac{d}{dx}x$
	- $b^yln(b) \cdot \frac{dy}{dx} = 1$
	- $\frac{dy}{dx} = \frac{1}{b^yln(b)} = \frac{1}{xln(b)}$
## Derivative of rational functions with products
1. Apply the natural logarithm to both sides of the equation:

$$\begin{align*}
\text{Let } y &= \frac{\frac{x^3}{4}\sqrt{ x^2+1 }}{(3x+2)^5} \\
\ln(y) &= \ln \left( \frac{\frac{x^3}{4}\sqrt{ x^2+1 }}{(3x+2)^5} \right) \\
&= \ln\left( x^\frac{3}{4} \right)+\ln(\sqrt{ x^2+1 })-\ln[(3x+2)^5] \\
&= \frac{3}{4}\ln x+\frac{1}{2}\ln(x^2+1)-5\ln(3x+2) \\
\end{align*}$$

2. Differentiating implicitly w.r.t. x:

$$\begin{align*}
\frac{1}{y}\cdot \frac{dy}{dx}&=\frac{3}{4x}+\frac{1}{2(x^2+1)}\cdot 2x-\frac{5}{3x+2}\cdot 3 \\
\frac{dy}{dx}&=y \cdot \frac{3}{4x}+\frac{x}{(x^2+1)}-\frac{15}{3x+2} \\
&= \frac{ \frac{x^3}{4} \sqrt{ x^2+1 }}{(3x+2)^5} \cdot \frac{3}{4x}+\frac{x}{(x^2+1)}-\frac{15}{3x+2} \\
\end{align*}$$
## Related rates
1. Make a sketch to organise the given information.
2. Write one or more equations that express the basic relationships among the variables.
3. Introduce rates of change by differentiating the appropriate equations with respect to time t.
4. Substitute the known values and solve the desired quantity. Check that units are consistent and the answer is reasonable.
## Linear Approximations, Taylor Polynomials
### Linear Approximations
- We can use the tangent line at $(a, f(a))$ as an approximation to the curve $y = f(x)$ when $x$ is **near** $a$
- This is because a curve lies very close to its tangent line near the point of tanegency
- Given that $f'(a) = \frac{f(x)-f(a)}{x-a}$
- $y = f(x) = f(a) + f'(a) \cdot (x-a) = L(x)$
- $L(x)$ is the **linearization** of the function $f$ at $a$
### Taylor Polynomials
- A better approximation than a linear one is a second-degree (quadratic) approximation $P(x)$
- When $x \to a$
	- $P(a) = f(a)$
	- $P'(a) = f'(a)$
	- $P''(a) = f''(a)$
- Second order polynomial $P(x) = A + B(x-a) + C(x-a)^2$
	- $P(a) = f(a) \rightarrow A = f(a)$
	- $P'(a) = f'(a) \rightarrow B = f'(a)$
	- $P''(a) = f''(a) \rightarrow 2C = f''(a) \rightarrow C = \frac{f''(a)}{2}$
- Higher order polynomial approximations are more accurate than preceding ones
- For the approximation to be accurate, $T_n(x), n \to ∞$

$$\begin{gather*}
T_n(x) = f(a) + f'(a)(x - a) + \frac{f''(a)}{2!}(x - a)^2 + \cdots + \frac{f^{(n)}(a)}{n!}(x - a)^n\\
\text{ where } n \text{ is a positive integer and } n! = n(n−1)(n−2) \cdots (3)(2)(1)\\
T_n(x) = \sum_{k=0}^{n} \frac{f^{(k)}(a)}{k!}(x - a)^k
\end{gather*}$$
- **Maclaurin Series**: Taylor polynomials when $a=0$