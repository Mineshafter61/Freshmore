23.
(a)
$$
\begin{align}
\lim_{ x \to 0 } \frac{\sin(ax)}{x}&=\lim_{ x \to 0 } \frac{a\sin(ax)}{ax} \\
&=a\lim_{ x \to 0 } \frac{\sin(ax)}{ax} \\
&=a
\end{align}
$$
(b)
$$
\begin{align}
\lim_{ x \to 0 } \frac{\sin(3x)}{\tan(5x)}&=\lim_{ x \to 0 } \frac{\sin(3x)\cos(5x)}{\sin(5x)} \\
&=\lim_{ x \to 0 } \frac{\sin(3x)}{\sin(5x)} \lim_{ x \to 0 } \cos(5x) \\
&=\lim_{ x \to 0 } \frac{3x 5x \sin(3x)}{3x 5x \sin (5x)} \\
&=\lim_{ x \to 0 } \frac{3x}{5x} \lim_{ x \to 0 } \frac{\sin(3x)}{3x} \lim_{ x \to 0 } \frac{\sin(5x)}{5x} \\
&=\lim_{ x \to 0 } \frac{3}{5}=\frac{3}{5}
\end{align}
$$
24.
$$
\begin{align}
b=\lim_{ v \to 10^+ } -5v^2=-500 \\
-500=\lim_{ v \to 10^- } -av \implies a=5
\end{align}
$$
25.
(a)
$$
\lim_{ x \to 0 } \frac{\sin(3x)}{x}=3\lim_{ x \to 0 } \frac{\sin(3x)}{3x}=3
$$
(b)
$$
\begin{align}
\lim_{ x \to 0 } \frac{\sin(4x)}{\sin(6x)}&=\lim_{ x \to 0 } \frac{4x6x\sin(4x)}{4x6x\sin(6x)} \\
&=\lim_{ x \to 0 }\frac{\sin(4x)}{4x}\cdot\lim_{ x \to 0 }\frac{6x}{\sin(6x)}\cdot\lim_{ x \to 0 } \frac{4x}{6x} \\
&=\frac{4}{6}
\end{align}
$$
(c)
$$
\begin{align}
\lim_{ t \to 0 } \frac{\tan(6t)}{\sin(2t)}&=\lim_{ t \to 0 } \frac{\sin(6t)}{\cos(6t)\sin(2t)} \\
&=\lim_{ t \to 0 } \frac{1}{\cos(6t)} \cdot\frac{\sin(6t)}{\sin(2t)} \\
&=\lim_{ t \to 0 } \frac{\sin(6t)}{\sin(2t)} \\
&=\frac{6}{2}=3
\end{align}
$$
(d)
$$
\begin{align}
\lim_{ t \to 0 } \frac{\sin^2(3t)}{t^2}&=\lim_{ t \to 0 } \frac{\sin(3t)}{t}\cdot\lim_{ t \to 0 } \frac{\sin(3t)}{t}=3\cdot 3=9
\end{align}
$$
(e)
$$
\begin{align}
\lim_{ x \to 0 } \frac{\sin x}{x+\tan x}&=\frac{\frac{\sin(x)}{x}}{1+\frac{\tan(x)}{x}} \\
&=\frac{1}{1+1}=\frac{1}{2}
\end{align}
$$
(f)
$$
\begin{align}
\lim_{ x \to 0 } x\cot x&=\lim_{ x \to 0 } \frac{x}{\tan x} \\
&=\lim_{ x \to 0 } \frac{1}{\frac{\tan x}{x}} \\
&=\frac{1}{1}=1
\end{align}
$$
26.
$$
\begin{align}
\lim_{ x \to -2 } \frac{3x^2+ax+a+3}{x^2+x-2}&=\lim_{ x \to -2 } \frac{15-a}{4}
\end{align}
$$
a can be any number.

27.
Let $n=n^3+1$
$0=n^3-n+1$
$n=-1.32472$
Therefore yes.

28.
If $\displaystyle f(x)=\begin{cases}x^4 \sin \frac{1}{x} &\text{if }x \neq 0\\0 &\text{if }x = 0\end{cases}$ is continuous, $\displaystyle\lim_{ x \to 0 }x^4\sin \frac{1}{x} = 0$ must be true.
$\displaystyle\lim_{ x \to 0 }x^4\sin \frac{1}{x} = \lim_{ x \to 0 }x^4 \lim_{ x \to 0 }\sin \frac{1}{x}=0\lim_{ x \to 0 }\sin \frac{1}{x}$
Since the range of sin(x) is $[-1, 1]$, sin(1/x) cannot be infinity, therefore the limit is determinate and is 0. Thus the function is continuous.

29.

| x | f(x) |
|---|---|
| -3 | -11 |
| -2 | 3 |
| -1 | 5 |
| 0 | 1 |
| 1 | -3 |
| 2 | -1 |
| 3 | 13 |
The roots are between -3 and -2, 0 and 1, and 2 and 3.

31.
(a) The particle is moving forwards but decelerating.
(b) Positive: 0 < t < 5; negative: 5 < t ≤ 6; zero: t = 5
(c) Negative: 0 ≤ t ≤ 6
(d) t = 5
(e) t = 2.5

32.
Let f(t) be the distance from the monastery as a function of the time from 7am on the first day. Let g(t) be the distance from the monastery as a function of the time from 7am on the second day. If the distance to the top of the mountain is x, f(x) must have endpoints 0 and x and be in the domain $[0,x]$, and likewise, g(x) must have endpoints 0 and x and be in the domain $[0,x]$. By the intermediate value theorem, these two functions must have at least 1 point in common, and this point is where the monk passes through at the same time on each day.