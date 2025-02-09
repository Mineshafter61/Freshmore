## Chain Rule
- For a function of one variable, the [[3_Derivatives#Chain Rule|chain rule]] states that
$$
\frac{dy}{dt}=\frac{dy}{dx} \frac{dx}{dt}
$$
### Type 1
- For $z = f(x, y)$, where $x = g(t)$ and $y = h(t)$ are both differentiable functions of $t$,
$$
\frac{dz}{dt}=\frac{\partial z}{\partial x} \frac{dx}{dt}+\frac{\partial z}{\partial y} \frac{dy}{dt}
$$
- Note that the formula contains both ordinary and partial derivatives
- *Example: Let $z=x^2y+y^2x$, where $x=t^2$ and y=$t^3$. Compute $\frac{dz}{dt}$.*
$$
\begin{align}
\frac{dz}{dt}&=(2xy+y^2)(2t)+(x^2+2yx)(3t^2) \\
&=(2t^5+t^6)(2t)+(t^4+2t^5)(3t^2) \\
&=7t^6+8t^7
\end{align}
$$
	- By substitution, $z=t^7+t^8$, therefore we can check the answer directly.
- *Example 2: Let $z=xy$, where $x=\sin(t)$ and $y=\cos(t)$. Compute $\frac{dz}{dt}$*
	- Direct substitution: 
$$
\begin{align}
z&=\sin(t)\cos(t) \\
&=\frac{1}{2}\sin(2t) \\
\frac{dz}{dt}&=\cos(2t)
\end{align}
$$
	- Chain rule: 
$$
\begin{align}
\frac{dz}{dt}&=y\cos(t)-x\sin(t) \\
&=\cos^2(t)-\sin^2(t) \\
&=\frac{1}{2}(1+\cos 2 t-1+\cos 2 t) \\
&=\cos 2 t
\end{align}
$$
#### Generalised Type 1
- For $z=f(w,x,y)$, the chain rule becomes 
$$
\frac{dz}{dt}=\frac{\partial z}{\partial w} \frac{dw}{dt}+\frac{\partial z}{\partial x} \frac{dx}{dt}+\frac{\partial z}{\partial y} \frac{dy}{dt}
$$
### Type 2
- For $z=f(x,y)$ where $x=g(u,v)$ and $y=h(u,v)$, we have
$$
\begin{align}
\frac{\partial z}{\partial u}=\frac{\partial z}{\partial x} \frac{\partial x}{\partial u}+\frac{\partial z}{\partial y} \frac{\partial y}{\partial u}\\
\frac{\partial z}{\partial v}=\frac{\partial z}{\partial x} \frac{\partial x}{\partial v}+\frac{\partial z}{\partial y} \frac{\partial y}{\partial v}
\end{align}
$$
- *Example: Let $z=f(x,y)$, where $x=x(r,\theta)=r\cos \theta,y=y(r,\theta)=r\sin \theta$*
	- Find the general expressions for $\frac{\partial z}{\partial r}$ and $\frac{\partial z}{\partial \theta}$ in terms of $\frac{\partial z}{\partial x}$, $\frac{\partial z}{\partial y}$, $r$ and $\theta$.
$$
\begin{align}
\frac{\partial z}{\partial r}&=\frac{\partial z}{\partial x}\frac{\partial x}{\partial r}+\frac{\partial z}{\partial y}\frac{\partial y}{\partial r} \\
&=\frac{\partial z}{\partial x}\cos \theta+\frac{\partial z}{\partial y}\sin \theta \\
\frac{\partial z}{\partial \theta}&=\frac{\partial z}{\partial x}\frac{\partial x}{\partial \theta}+\frac{\partial z}{\partial y}\frac{\partial y}{\partial \theta} \\
&=\frac{\partial z}{\partial y}r\cos \theta-\frac{\partial z}{\partial x}r\sin \theta
\end{align}
$$
	- Find $\frac{\partial z}{\partial r}$ and $\frac{\partial z}{\partial \theta}$ if $z=xy$. 
$$
\begin{align}
\frac{\partial z}{\partial x}&=y\\
\frac{\partial z}{\partial y}&=x \\
\frac{\partial z}{\partial r}&=y\cos \theta+x\sin \theta \\
\frac{\partial z}{\partial \theta}&=xr\cos \theta-yr\sin \theta
\end{align}
$$