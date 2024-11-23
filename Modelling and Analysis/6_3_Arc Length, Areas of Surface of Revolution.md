## Arc Length
- For two points $(x_1, y_1)$ and $(x_2, y_2)$, the length $l$ between them is given by $l=\sqrt{(x_2-x_1)^2+(x_2-x_1)^2}$.
- If there are many segments on the line, arc length of each segment $\Delta s_i = \sqrt{(\Delta x)^2 + (\Delta y)^2}$ where $\Delta x$ is fixed while $\Delta y$ is kept variable to accommodate for vertical variations in the curve.
- The total length s of a continuous and differentiable curve $y=f(x)$ is defined over the interval $a ≤ x ≤ b$ is given by
$$\begin{align}s &= \lim_{n \to \infty} \sum_{i=1}^n \Delta s_i \\&= \lim_{n \to \infty} \sum_{i=1}^n \sqrt{(\Delta x)^2 + (\Delta y)^2} \\&= \lim_{n \to \infty} \sum_{i=1}^n \sqrt{1+\left(\frac{\Delta y}{\Delta x}\right)^2}\cdot \Delta x \\ &= \lim_{i=1} \sum_{i=1}^n \sqrt{1+(f'(x_i^*)^2}\cdot \Delta x \\&= \int_a^b \sqrt{1+[f'(x)]^2}\,dx\end{align}$$
- If the curve is expressed as $x=f(y)$, our formula for arc length is $\int_a^b \sqrt{1+[f'(y)]^2}\,dy$
### Trigonometric substitution
| Expression       | Substitution                              | Expression evaluation             |
| ---------------- | ------------------------------------ | ------------------------------------------ |
| $\sqrt{a^2-x^2}$ | $x=a\sin \theta, dx=a\cos \theta\,d\theta$              | $\sqrt{a^2-a^2\sin \theta}=a\cos \theta$  |
| $\sqrt{a^2+x^2}$ | $x=a\tan \theta, dx=a\sec^2 \theta\,d\theta$            | $\sqrt{a^2+a^2\tan^2 \theta}=a\sec \theta$ |
| $\sqrt{x^2-a^2}$ | $x=a\sec \theta, dx=a\sec^2 \theta \tan^2\theta\,d\theta$ | $\sqrt{a^2\sec^2\theta-a^2}=a\tan \theta$  |
> Example 1: Arc length of $y^2=x$ from $(0,0)$ to $(1,1)$
> $$
\begin{align}
g(y)&=y^2 \implies g'(y)=2y \\
\text{Arc length }s&=\int_{0}^{1} \sqrt{1+(2y)^2} \, dy\\
\text{Let } y &:= \frac{\tan\theta}{2}, dy := \frac{\sec^2\theta}{2}\,d\theta \\
\text{When }y=0, \tan \theta &= 0 \\
\theta_{1}&=0 \\
\text{When }y=0, \tan \theta &= 2 \\
\theta_{2}&=\tan^{-1} 2 \\\\
s&=\int_{y=0}^{y=1} \sqrt{1+\tan^2\theta}\left(\frac{\sec^2\theta}{2}\right)d\theta \\
&=\int_{y=0}^{y=1} \sec \theta\left( \frac{\sec^{2}\theta}{2} \right)d\theta \\
&=\frac{1}{2}\int_{y=0}^{y=1} \sec^3\theta\,d\theta \\
&=\frac{1}{2}\int_{y=0}^{y=1} \sec \theta \sec^2\theta\,d\theta \\
&=\frac{1}{2}\left(\sec \theta \tan \theta- \int_{y=0}^{y=1} \sec \theta \tan^2\theta\,d\theta\right) \\
&=\frac{1}{2}\left(\sec \theta \tan \theta- \int_{y=0}^{y=1} \sec \theta (\sec^2\theta-1)\,d\theta\right) \\
&=\frac{1}{2}\left(\sec \theta \tan \theta- \int_{y=0}^{y=1} \sec^3 \theta \,d\theta+ \int_{y=0}^{y=1} \sec \theta \,d\theta\right) \\
\int_{y=0}^{y=1} \sec^3\theta\,d\theta&=\frac{1}{2}[\sec \theta \tan \theta+\ln|\sec \theta+\tan \theta|]_{y=0}^{y=1} \\
 \\
\therefore s=\frac{1}{2}\int_{y=0}^{y=1} \sec^3\theta\,d\theta&=\frac{1}{4}[\sec \theta \tan \theta+\ln|\sec \theta+\tan \theta|]_{y=0}^{y=1} \\ \\
\text{Finding }\sec \theta: \\
\tan \theta&=2y \\
\sec^2\theta&=1+\tan^2\theta \\
&=1+4y^2 \\
\therefore \sec \theta&=\sqrt{1+4y^2} \\ \\
s&=\frac{1}{4}[\sqrt{1+4y^2}(2y)+\ln|\sqrt{1+4y^2}+2y|]_{y=0}^{y=1} \\
&=\frac{1}{4}[\sqrt{5}(2)+\ln|\sqrt{5}+2|]
\end{align}
$$

> Example 2: Length function of the arc of $y^2=x^3$ starting at $(1,1)$.
> $$
\begin{align}
y^{2}&=x^{3} \\
y&=x^{3/2} \\
\text{Let }f(x)&=x^{3/2} \\
f'(x)&=\frac{3}{2}x^{1/2} \\
s&=\int_{1}^{x} \sqrt{1+\left( \frac{3}{2}x^{1/2} \right)^{2}} \, dx\\
&=\int_{1}^{x} \sqrt{1+\frac{9}{4}x} \, dx \\
\text{Let }u&=1+\frac{9}{4}x \\
du&=\frac{9}{4}dx \\
dx&=\frac{4}{9}du \\
x=1&,u=\frac{13}{4} \\
x=x&,u=1+\frac{9}{4}x \\
\int_{1}^{x} \sqrt{1+\frac{9}{4}x} \, dx &= \int_{\frac{13}{4}}^{1+\frac{9}{4}x} u^{\frac{1}{2}} \left( \frac{4}{9} \, du \right) \\
&=\frac{4}{9}\int_{\frac{13}{4}}^{1+\frac{9}{4}x} u^{\frac{1}{2}} \, du \\
&=\frac{4}{9}\left[ \frac{2}{3}u^{\frac{3}{2}} \right]_{\frac{13}{4}}^{1+\frac{9}{4}x} \\
&=\frac{8}{27}\left[ \left( 1+\frac{9}{4}x \right)^{3/2}-\frac{13}{4}^{3/2} \right] \\
\therefore s(x)&=\frac{8}{27}\left[ \left( 1+\frac{9}{4}x \right)^{3/2}-\frac{13\sqrt{13}}{8} \right]
\end{align}
$$
## Areas of Surface of Revolution
- Formed when a curve is rotated about a line
- Formula for the surface area of the i-th band of the surface area is $$\begin{align}
S_i&=2πrl\\&=π\cdot r\cdot \Delta s_i\\&=2π\frac{(y_{i-1}+y_{i})}{2}\cdot\sqrt{1+(f'(x_i^*))^2}\,\Delta x\\&=π \cdot[2f(x_i^*)]\cdot\sqrt{1+(f'(x_i^*))^2}\,\Delta x
\end{align}$$ as when $n \to \infty, f(x_{i-1})=f(x_{i})$
- This is also the average radius of the approximating band. Thus, the surface area of the object is $$
\begin{align}
S&=\lim_{ n \to \infty } \sum_{i=1}^{n}S_{i} \\
&=\lim_{ n \to \infty } \sum_{i=1}^{n}π \cdot[2f(x_i^*)]\cdot\sqrt{1+(f'(x_i^*))^2}\,\Delta x \\
&=\int_{a}^{b} 2π\,f(x)\sqrt{1+[f'(x)]^{2}} \, dx  \\
&=\int 2πy\,ds \\
\text{where } y&=f(x), \\
s&=\int_{a}^{b}\sqrt{1+[f'(x)]^{2}} \, dx, \\
ds&=\sqrt{1+[f'(x)]^{2}}
\end{align}
$$
- Likewise, if the curve is described by $x=f(y)$, the formula is $S=\int_{a}^{b}2π\,f(y)\sqrt{1+[f'(y)]^{2}}\,dy=\int2πx\,ds$

> Example: The arc of the parabola $y=x^2$ from $(1,1)$ to $(2,4)$ is rotated about the y-axis. Find the resulting surface area.
> $$
\begin{align}
todo
\end{align}
$$