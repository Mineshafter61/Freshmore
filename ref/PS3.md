1a.
$$
\begin{gather}
N_{t+1}=f(N_{t})\\
f(N_{t})=N_{t+1}\\
f(f(N_{t}))=f(N_{t+1})=N_{t+2}
\end{gather}
$$
1b.
$$
f^{-1}(N_{t+1})=N_{t}
$$
3.
a=11: a approaches an infinite sequence of 2s and 1s.
a=25: a approaches an infinite sequence of 2s and 1s.
Conjecture: a approaches an infinite sequence of 2s and 1s for all a.
4.
$$
\begin{align}
a_{0} &= \frac{1}{9};\\
a_{n+1}&=a_{n}+\frac{1}{9}(1-a_{n}) \\
&=\frac{1}{9}+\frac{8}{9}a_{n}\\
L =\lim_{ n \to \infty } a_{n}&=\lim_{ n \to \infty } \frac{1}{9}+\frac{8}{9}a_{n-1}\\
&=\frac{1}{9}+\frac{8}{9} \lim_{ n \to \infty } a_{n-1} \\
L&=\frac{1}{9}+\frac{8}{9}L \\
\frac{1}{9}L&=\frac{1}{9} \\
L&=1, qed
\end{align}
$$
5.
(a) L
(b) L
(c) L
6.
(a)
$$
\begin{align}
\lim_{ n \to \infty } \frac{8n^2-3\sqrt{ n }}{1-n-5n^2}&=\lim_{ n \to \infty }\frac{8-3n^{-1.5}}{n^{-2}-n^{-1}-5} \\
&=\frac{8-0}{0-0-5} \\
&=-\frac{8}{5}
\end{align}
$$
(b)
$$
\begin{align}
\lim_{ n \to \infty } \frac{(-3)^n+2^n}{5^n}&=\lim_{ n \to \infty } \frac{(-3)^n}{5^n}+\lim_{ n \to \infty }\frac{2^n}{5^n} \\
&=\lim_{ n \to \infty }\left( \frac{-3}{5} \right)^n+\lim_{ n \to \infty }\left( \frac{2}{5} \right)^n \\
&=0+0 \\
&=0
\end{align}
$$
(c)
$$
\begin{align}
\lim_{ n \to \infty } \frac{3n^3-4n^4}{2^n}&=0
\text{ since the largest power dominates}
\end{align}
$$
(d)
$$
\begin{align}
\lim_{ n \to \infty } \sqrt{ \frac{9(n!)+3^{n+2}+7^{n-1}}{n!+3^n} }&=\sqrt{ \lim_{ n \to \infty } \frac{9(n!)+3^{n+2}+7^{n-1}}{n!+3^n} } \\
&=\sqrt{ \lim_{ n \to \infty } \frac{9+\frac{3^{n+2}}{n!}+\frac{7^{n-1}}{n!}}{1+\frac{3^n}{n!}} } \\
&=\sqrt{ \lim_{ n \to \infty } \frac{9+0+0}{1+0} } \\
&=\sqrt{ 9 } \\
&=3
\end{align}
$$
7.
(a)
$$
\begin{gather}
\text{Assume that } (x_{n}+y_{n})_{n=1}^\infty \text{ is convergent. This implies that} \lim_{ n \to \infty } x_{n}+y_{n} \text{ exists. Let this limit be } L.\\
\text{Since }(x_{n})_{n=1}^\infty \text{ is convergent, }\lim_{ n \to \infty } x_{n} \text{ exists. Let this limit be } M.\\
\text{As }(y_{n})_{n=1}^\infty \text{ is divergent, }\lim_{ n \to \infty } y_{n} \text{ should not exist.}\\
\lim_{ n \to \infty } y_{n}=\lim_{ n \to \infty } x_{n}+y_{n}-\lim_{ n \to \infty } x_{n}=L-M\\
\text{thus contradicting the statement.}
\end{gather}
$$
(b)
$$
\begin{gather}
\text{Let } \lim_{ x \to a }(f(x)+g(x))=M\\
\lim_{ x \to a }g(x)=\lim_{ x \to a }(f(x)+g(x))-\lim_{ x \to a }f(x)=L-M\\
\text{Therefore }\lim_{ x \to a }(f(x)+g(x)) \text{ should not exist, thus contradicting the statement.}\\\\
\lim_{ x \to 0 } \cos x=1\\
\lim_{ x \to 0 } \cos \frac{1}{x}=\text{undefined}\\
\end{gather}
$$
Using the result from the previous part, the limit of the addition of two functions, one of which does not exist, results in a nonexistent function. Therefore, $\displaystyle\lim_{ x \to 0 }\cos x+\cos\frac{1}{x}$ does not exist.
9.
(a)
$$
\begin{align}
\lim_{ \frac{v}{c} \to 0 } \frac{KE}{E_{K}}&=\frac{\frac{1}{2}mv^2}{mc^2\left( \frac{1}{\sqrt{ 1-\frac{v^2}{c^2} }}-1 \right)}\\
&=\frac{\frac{v^2}{c^2}}{2\left( \frac{1}{\sqrt{ 1-\frac{v^2}{c^2} }}-1 \right)} \\
&=\frac{1}{2}\times\frac{\frac{v^2}{c^2}\sqrt{ 1-\frac{v^2}{c^2} }}{1-\sqrt{ 1-\frac{v^2}{c^2}}} \\
&=\frac{1}{2}\times\frac{\frac{v^2}{c^2}\sqrt{ 1-\frac{v^2}{c^2} }}{1-\sqrt{ 1-\frac{v^2}{c^2}}}\times\frac{1+\sqrt{ 1-\frac{v^2}{c^2}}}{1+\sqrt{ 1-\frac{v^2}{c^2}}} \\
&=\frac{1}{2}\times\frac{\frac{v^2}{c^2}\sqrt{ 1-\frac{v^2}{c^2} }+\frac{v^2}{c^2}\left( 1-\frac{v^2}{c^2} \right)}{1-\left( 1-\frac{v^2}{c^2} \right)} \\
&=\frac{1}{2}\times\frac{\frac{v^2}{c^2}\sqrt{ 1-\frac{v^2}{c^2} }+\frac{v^2}{c^2}\left( 1-\frac{v^2}{c^2} \right)}{\frac{v^2}{c^2}} \\
&=\frac{1}{2}\times\left( \sqrt{ 1-\frac{v^2}{c^2} }+\left( 1-\frac{v^2}{c^2} \right) \right) \\ \\
&=\frac{1}{2}\times (1+1)=1
\end{align}
$$
(b) As the speed of an object approaches 0, its kinetic energy approaches its relativistic kinetic energy.
