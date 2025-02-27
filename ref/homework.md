# TW 2
### Problem 3
(b) $\vec{E}=0$
$\begin{align}\text{(c) }\vec{E}&=\int \rho_{0}\left( 1-\frac{4r}{3R} \right)4\pi r^2\,dr \\ &=4\pi\rho_{0}\int r^2-\frac{4}{3R}r^3\,dr \\ &=4\pi\rho_{0}\left( \frac{r^3}{3}-\frac{r^4}{3R} \right)\end{align}$
(d) GRAPH of above function until R, then 0.

### Problem 4
(a)
$$
\begin{align}
F_{13}&=F_{23} \\
k_e \frac{(0.1)(0.001)}{(1+x)^2}&=k_e \frac{(0.05)(0.001)}{(1-x)^2} \\
0.0001(1-2x+x^2)&=0.005(1+2x+x^2) \\
2-4x+2x^2&=1+2x+x^2 \\
1-6x+x^2&=0 \\
x&=\frac{6\pm \sqrt{6^2-4}}{2} \\
&=\frac{6\pm 4\sqrt{2}}{2} \\
\text{Since }x\leq 1, \\
x&=3-2\sqrt{2} \\
\theta&=\arctan\left( \frac{3-2\sqrt{2}}{10} \right) \\
&=0.983\degree
\end{align}
$$
(b)
$$
\begin{align}
\text{Since capacitance }\propto \text{ radius}: \\
\frac{C_{1}}{C_{2}}&=\frac{R_{1}}{R_{2}}=2 \\
\text{When the metallic spheres are brought into contact,}&\text{ their } \Delta V\text{ becomes } 0. \\
\text{Hence,} \\
\frac{q_{1}}{q_{2}}&=\frac{C_{1}}{C_{2}}=2 \\
\text{Total charge }q_{total}&=150\text{ mC} \\
q_{total}&=q_{1}+q_{2} \\
&=3q_{2}\\
\therefore q_{2}&=50\text{ mC},q_{1}=100\text{ mC} \\
F_{13}&=F_{23} \\
k_e \frac{(0.1)(0.001)}{(1+x)^2}&=k_e \frac{(0.05)(0.001)}{(1-x)^2} \\
0.0001(1-2x+x^2)&=0.005(1+2x+x^2) \\
2-4x+2x^2&=1+2x+x^2 \\
1-6x+x^2&=0 \\
x&=\frac{6\pm \sqrt{6^2-4}}{2} \\
&=\frac{6\pm 4\sqrt{2}}{2} \\
\text{Since }x\leq 1, \\
x&=3-2\sqrt{2} \\
\theta&=\arctan\left( \frac{3-2\sqrt{2}}{10} \right) \\
&=0.983\degree
\end{align}
$$
### Problem 5
(a)
$$
\begin{align}
\text{At initial}: \\
E&=K+U \\
&=\frac{1}{2}(0.0015)(22)^2+\frac{9\times 10^{9}(-2.80\times 10^{-6})(-7.80\times 10^{-6})}{0.800} \\
&=0.6087\text{ J} \\
\text{At final}&\text{ (let }v\text{ be final speed)}: \\
E&=\frac{1}{2}(0.0015)v^2+\frac{9\times 10^{9}(-2.80\times 10^{-6})(-7.80\times 10^{-6})}{0.400} \\
&=7.5\times10^{-4}v^2+0.4914\text{ J} \\
&\text{By conservation of energy,} \\
0.6087&=7.5\times10^{-4}v^2+0.4914 \\
0.1173&=7.5\times10^{-4}v^2 \\
v^2&=156.4 \\
v&=12.506 \text{ m/s}
\end{align}
$$
(b)
$$
\begin{align}
\text{At the minimum distance, }&v=0\implies K=0\implies E=U \\
0.6087&=\frac{9\times 10^{9}(-2.80\times 10^{-6})(-7.80\times 10^{-6})}{r} \\
r&=\frac{9\times 10^{9}(-2.80\times 10^{-6})(-7.80\times 10^{-6})}{0.6087} \\
&=0.323\text{ m}
\end{align}
$$
### Problem 6
(a)
$$
\begin{align}
r≤a,\\
\vec{E}(r)&=\nabla V \\
&=\frac{dV}{dr} \\
&=\frac{\rho_{0}a^2}{18\epsilon_{0}}\left[ -\frac{6r}{a^2}+\frac{6r^2}{a^3} \right] \\
&=\frac{\rho_{0}}{3\epsilon_{0}}\left( \frac{r^2}{a}-r \right) \\
r>a, \\
\vec{E}(r)&=0
\end{align}
$$
(b)
$$
\begin{align}
\text{Let V be the volume of a sphere.} \\
V&=\frac{4}{3}\pi r^3 \\
dV&=4\pi r^2\,dr\\
\vec{E}(r)&=\int k_e \frac{\rho 4\pi r^2\,dr}{r^2} \\
&=\int k_e\rho 4\pi\,dr \\
&=\rho k_e2\pi r \\
\rho&=\frac{\vec{E}(r)}{k_e2\pi r} \\
r≤a, \\
\rho(r)&=\frac{\frac{\rho_{0}}{3\epsilon_{0}}\left( \frac{r^2}{a}-r \right)}{k_e2\pi r} \\
&=\frac{\frac{\rho_{0}}{3\epsilon_{0}}\left( \frac{r^2}{a}-r \right)}{\frac{2\pi r}{4\pi\epsilon_{0}}} \\
&=\frac{2\rho_{0}}{3}\left( \frac{r}{a}-1 \right) \\
r>a, \\
\rho(r)&=0
\end{align}
$$
(c)
We set up a spherically symmetric Gaussian surface with radius a enclosing the charge.

$$
\begin{align} \\
\text{For all }r,\\
E(r)&=\frac{Q}{4\pi\epsilon_{0}r^2} \\
r=a,\\
E(r)&=\frac{Q}{4\pi\epsilon_{0}a^2} \\
\frac{\rho_{0}}{3\epsilon_{0}}\left( \frac{a^2}{a}-a \right)&=\frac{Q}{4\pi\epsilon_{0}a^2} \\
\frac{\rho_{0}}{3\epsilon_{0}}(a-a)&=\frac{Q}{4\pi\epsilon_{0}a^2} \\
0&=\frac{Q}{4\pi\epsilon_{0}a^2} \\
Q&=0 \\
r>a, \\
E(r)&=\frac{Q}{4\pi\epsilon_{0}r^2} \\
0&=\frac{Q}{4\pi\epsilon_{0}r^2} \\
\implies Q&=0
\end{align}
$$