## Local Extrema

- $f$ has a **local maximum** at the point $(x_0, y_0)$ if $f(x, y) \leq f(x_0, y_0)$ for all points $(x, y)$ near $(x_0, y_0)$
- $f$ has a **local minimum** at the point $(x_0, y_0)$ if $f(x, y) \geq f(x_0, y_0)$ for all points $(x, y)$ near $(x_0, y_0)$
- At local extrema $(x_0, y_0)$ where it is differentiable, then $\nabla f(x_0, y_0) = \vec{0}$
  - That is, $f_x(x_0, y_0) = 0$ and $f_y(x_0, y_0) = 0$
- Local extrema can also have an **undefined gradient**.

## Critical Points

- $\nabla f(x_0, y_0) = \vec{0}$, **or** if one of the partial derivatives $f_x$, $f_y$ does not exist ($\nabla f(x_0, y_0)$ is undefined)

## Saddle Points

- "Inflection point"
- $\nabla f(x_0, y_0) = \vec{0} \text{ or undefined}$
- Not a local maximum or minimum
- Can be local minimum in one direction and local maximum in another direction

## Second Derivative Test

- Define $D(x_0,y_0)=f_{xx}(x_0,y_0)f_{yy}(x_0,y_0)-f_{xy}(x_0,y_0)f_{yx}(x_0,y_0)$
  - $D<0$, then $(x_0,y_0)$ is a saddle point
  - $D>0$ and $f_{xx}>0$, then $(x_0,y_0)$ is a **local minimum**
  - $D>0$ and $f_{xx}<0$, then $(x_0,y_0)$ is a **local maximum**
  - $D=0$, then this test is inconclusive and another method is required to determine the nature of the critical point.
- *Example: Find all critical points of $f(x,y)=x^2+y^3-6xy$, and classify them as either local maxima, local minima, or saddle points.*

$$
\begin{gather}
f_x(x,y)=2x-6y \\
f_y(x,y)=3y^2-6x \\
2x-6y=0;3y^2-6x=0 \\
x=3y; y^2=2x \\
y^2=6y \implies y=0,y=6 \\
\implies x=0,x=18 \\
\therefore \text{Critical points are }(0,0) \text{ and }(18,6)\\
D(0,0)=(2)(0)-(6)(6)=-36<0\\
D(18,6)=(2)(36)-(6)(6)=36>0\\
f_{xx}(18,6)=2\\
\therefore (0,0) \text{ is a saddle point and }(18,6)\text{ is a minimum point}
\end{gather}

$$
