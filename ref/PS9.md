8.
(a)
$$
\begin{align}
s(t)&=t^3/3-5t^{2}+16t \\
s_{1\to7}&=7^3/3-(5)7^{2}+(16)7-1/3+5-16 \\
&=-30 \\
\end{align}
$$
(b)
$$
\begin{align}
(t-2)(t-8)&=t^{2}-10t+16 \\
d_{1\to7}&=d_{1\to2}+d_{2\to7} \\
&=\left|\frac{2^3}{3}-5(2^2)+16(2)-\frac{1}{3}+5-16\right|+\left|\frac{7^3}{3}-5(7^2)+16(7)-\frac{2^3}{3}+5(2^2)-16(2)\right| \\
&=\frac{110}{3}
\end{align}
$$
9
(a)
$$
\begin{align}
T&=\int_{0}^{a/2} \frac{1}{k(a-x)(b-x)} \, dx \\
 &=\frac{1}{k}\int_{0}^{a/2} \frac{1}{(a-x)(b-x)} \, dx \\
\frac{1}{(a-x)(b-x)}&=\frac{A}{(a-x)}+\frac{B}{(b-x)} \\
1&=A(b-x)+B(a-x)=Ab-Ax+Ba-Bx \\
1&=Ab+Ba \\
0&=-Ax-Bx \\
0&=A+B\implies B=-A \\
1&=Ab-Aa \\
A&=\frac{1}{b-a}, B=\frac{1}{a-b} \\
T&=\frac{1}{k}\int_{0}^{a/2} \frac{1}{(b-a)(a-x)}+\frac{1}{(a-b)(b-x)} \, dx \\
&=\frac{1}{k}[\ln|(b-a)(a-x)|+\ln|(a-b)(b-x)|]_{0}^{a/2} \\
&=\frac{1}{k}(\ln|(b-a)(a-a/2)|+\ln|(a-b)(b-a/2)|-\ln|(b-a)(a)|-\ln|(a-b)(b)|) \\
&=\frac{1}{k}\left( \ln\left|\frac{ab-a^2}{2}\right|+\ln\left|ab-b^2+\frac{ab-a^{2}}{2}\right|-\ln|ab-a^2|-\ln|ab-b^2| \right)
\end{align}
$$
(b)
$$
x_0\to a, \frac{1}{a-x}\to \frac{1}{0^+}=\infty, T\to \infty
$$
10
$$\begin{align}
\int(-75t^2+15t+98)\,dt&=-25t^3+7.5t^2+98t+c \\
\int 80\sin\left( 2t+\frac{\pi}{4} \right)\,dt&=-40\cos\left( 2t+\frac{\pi}{4} \right) \\
\int \frac{350}{16t+20}\,dt&=350\ln|16t+20|
\end{align}
$$
(a)
$$
HIC=0.015\left( \frac{1}{0.015}(-25(0.015)^3+7.5(0.015)^2+98(0.015)) \right)^{2.5}
$$
(b)
$$
HIC=0.015\left(\frac{1}{0.015}\left(-40\cos\left( 2(0.015)+\frac{\pi}{4} \right)\right)\right)^{2.5}
$$
(c)
$$
HIC=0.015\left( \frac{1}{0.015}(350\ln|16(0.015)+20|)-(350\ln|20|) \right)^{2.5}
$$
13.
(a)
$$
\begin{align}
\langle x \rangle&=\int_{0}^{a} \frac{2x}{a} \sin^{2}\left( \frac{\pi x}{a} \right) \, dx \\
&=a\sin^{2}a-\int_{0}^{a}\frac{\pi x^2}{a^2}2\sin\left( \frac{\pi x}{a} \right) \\
&=a\sin^{2}a+\int_{0}^{a} \frac{2x}{a}\cos\left( \frac{\pi x}{a} \right) \, dx \\
&=a\sin^{2}a+\left[ \frac{a}{\pi}\sin\left( \frac{\pi x}{a} \right) \right]-\int_{0}^{a} \frac{2}{\pi}\sin\left( \frac{\pi x}{a}\right) \, dx \\
&=a\sin^{2}a-\frac{4a}{\pi^{2}}
\end{align}
$$
(b)
$$
\begin{align}
\langle x^2 \rangle&=\int_{0}^{a} \frac{2x^2}{a} \sin^{2}\left( \frac{\pi x}{a} \right) \, dx \\
\sin^2\left( \frac{\pi x}{a} \right)&=\frac{\left( 1-\cos\left( \frac{\pi x}{a} \right) \right)}{2} \\
\therefore\langle x^2 \rangle&=\int_{0}^{a} \frac{2x^2}{a} \frac{\left( 1-\cos\left( \frac{\pi x}{a} \right) \right)}{2} \, dx \\
&=\int_{0}^{a}\frac{x^2}{a}-\frac{x^2\cos\left( \frac{\pi x}{a} \right)}{a}\,dx \\
&=\frac{1}{a}\int_{0}^{a}x^2\,dx-\frac{1}{a}\int_{0}^{a}x^2\cos\left( \frac{\pi x}{a} \right)\,dx \\
&=\frac{a^2}{3}-\frac{a^2}{\pi}+\frac{1}{a}\int_{0}^{a} 2x \frac{a}{\pi}\sin\left( \frac{\pi x}{a} \right) \, dx  \\
&=\frac{a^2}{3}-\frac{a^2}{\pi}+\frac{2a}{\pi^2}
\end{align}
$$
14
(a)
$$
\begin{align}
N_0\int_{0}^{T} e^{-\lambda t} \, dt &=N_0\left[ -\frac{1}{\lambda}e^{-\lambda t} \right]_0^T \\
&=N_0\left( \frac{1}{\lambda}-\frac{1}{\lambda}e^{-\lambda T} \right)
\end{align}
$$
(b)
$$
\begin{align}
\tau&=\frac{\displaystyle\int_{0}^{\infty} te^{-\lambda t} \, dt}{\displaystyle\int_{0}^{\infty} e^{-\lambda t} \, dt} \\
&=\frac{\displaystyle\lim_{ n \to \infty } \int_{0}^{n} te^{-\lambda t} \, dt}{\displaystyle\lim_{ n \to \infty } \int_{0}^{n} e^{-\lambda t} \, dt} \\
&=\frac{\displaystyle\lim_{ n \to \infty } \left[ \frac{t}{\lambda}-\frac{t}{\lambda}e^{-\lambda T} \right]_0^n-\displaystyle\lim_{ n \to \infty } \int_{0}^{n} e^{-\lambda t} \, dt}{\displaystyle\lim_{ n \to \infty } \int_{0}^{n} e^{-\lambda t} \, dt} \\
&=\frac{\infty}{\displaystyle\lim_{ n \to \infty } \int_{0}^{n} e^{-\lambda t} \, dt}-1 \\
&=\infty
\end{align}
$$