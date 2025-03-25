2.
(a)
$f_x(2,1)=-1\cos(\pi y)=1$
$f_y(2,1)=x\cos(\pi y)+\pi xy\sin(\pi y)=2\pi$
$\text{Tangent plane}:z=2\cos(\pi)+2\pi(y-1)=2\pi(y-1)$
(b)
$f(2.1,1.05)≈0+0+2\pi(0.05)=0.1\pi$

3.
(a)
$$
\begin{align}
\nabla T&=\begin{bmatrix} 2x\\4y^3\\4z \end{bmatrix} \\
\text{At }(1,1,1), \\
\nabla T&=\begin{bmatrix} 2\\4\\4 \end{bmatrix} \\
\therefore \text{direction}&=\frac{\begin{bmatrix} 2\\4\\4 \end{bmatrix}}{\sqrt{2^2+4^2+4^2}}=\frac{1}{3}\begin{bmatrix} 1\\2\\2 \end{bmatrix}
\end{align}
$$
(b)
Instantaneous rate of change = $||\nabla T(1,1,1)||=\sqrt{2^2+4^2+4^2}=6$

4.
$$
\begin{align}
\frac{dA}{dt}&=\frac{\partial A}{\partial x} \frac{dx}{dt}+\frac{\partial A}{\partial y} \frac{dy}{dt}+ \frac{\partial A}{\partial \theta} \frac{d\theta}{dt} \\
\text{Parts:} \\
\frac{\partial A}{\partial x}&=\frac{1}{2}y\sin \theta\\
\frac{\partial A}{\partial y}&=\frac{1}{2}x\sin \theta\\
\frac{\partial A}{\partial \theta}&=\frac{1}{2}xy\cos \theta \\
\frac{dx}{dt}&=3 \implies x=3t+c_{1}\\
\frac{dy}{dt}&=-2 \implies y=-2t+c_{2}\\
\frac{d\theta}{dt}&=0.05 \implies \theta=0.05t+c_{3} \\
\therefore\frac{dA}{dt}&=\frac{1}{2}y\sin \theta(3)+\frac{1}{2}x\sin \theta(-2)+\frac{1}{2}xy\cos \theta(0.05) \\
&=\frac{1}{2}(50)\sin \left( \frac{\pi}{6} \right)(3)+\frac{1}{2}(40)\sin \left( \frac{\pi}{6} \right)(-2)+\frac{1}{2}(40)(50)\cos \left( \frac{\pi}{6} \right)(0.05) \\
&=37.5-20+25\sqrt{3} \\
&=\frac{35+50\sqrt{3}}{2}
\end{align}
$$
5.
$$
\begin{align}
f_x(x,y)&=-2xe^{-x^{2}-y^{2}}(x^2+2y^2)+2xe^{-x^{2}-y^{2}}=(2xe^{-x^{2}-y^{2}})(1-x^2+2y^2) \\
f_y(x,y)&=-2ye^{-x^{2}-y^{2}}(x^2+2y^2)+4ye^{-x^{2}-y^{2}}=(2ye^{-x^{2}-y^{2}})(2-x^2+2y^2) \\
\text{Critical points}: \\
\text{Let }(2xe^{-x^{2}-y^{2}})(1-x^2+2y^2)&=0 \\
\text{Let }(2ye^{-x^{2}-y^{2}})(2-x^2+2y^2)&=0 \\
x,y&=0,0 \\
\text{Set } x&=0: \\
(2ye^{-y^{2}})(2+2y^2)&=0 \\
2+2y^2&=0 \\
y&=1,-1 \\
\text{Set } y&=0: \\
(2xe^{-x^{2}})(1-x^2)&=0 \\
x^2&=1 \\
x&=1,-1 \\
\therefore \text{Critical points}&=(0,0),(0,-1),(0,1),(1,0),(-1,0) \\
x^2+y^2\leq 4 \text{ is a cylinder}&, \therefore \text{bounded region} \\
\text{Finding z-values}: \\
f(0,0)&=e^{-x^2-y^2}(x^2+2y^2)=0 \\
f(0,1)&=e^{0-1}(2)=2(0.37) \\
f(0,-1)&=e^{0-1}(0+2)=2(0.37) \\
f(1,0)&=e^{-1-0}(1+0)=0.37 \\
f(-1,0)&=e^{-1-0}(1+0)=0.37 \\
\text{Finding values along boundary}: \\
\text{Sub }x^2+y^2=4 &\text{ into } e^{-x^2-y^2}(x^2+2y^2) \\
f(x,y)&=e^{-4}(x^2+y^2+y^2) \\
&=e^{-4}(4+y^2) \\
\frac{\partial z}{\partial x}&=0\,\forall x\\
\text{At critical values, }\frac{\partial z}{\partial y}&=0 \\
\frac{\partial z}{\partial y}&=e^{-4}(2y) \\
e^{-4}(2y)&=0 \\
y&=0\implies x=2,-2 \\
\text{Sub into original equation}: \\
f(2,0)=e^{-4}(4)=4(0.018)\\
f(-2,0)=e^{-4}(4)=4(0.018)\\
\therefore \text{global maxima}&:(0,1),(0,-1)\\
\therefore \text{global minima}&:(0,0)
\end{align}
$$
6.
