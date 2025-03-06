# 5_1A_Polar Coordinate Systems

- Conversion:
  - $x=r\cos(θ)$
  - $y=r\sin(θ)$
  - $r=\sqrt{x^2+y^2}$
  - $θ=\arctan(\frac{y}{x})$
- To evaluate $\iint_R f(x,y)\,dA$, it is sometimes better to make a change of variables to polar coordinates, for instance when
  - the region R is a disk or a sector
  - the function $f$ contains terms like $x^2+y^2$.
- $dA = r\,dr\,dθ$
  - $r$: Jacobian
- Double integral over $R$ in polar coordinates is

$$
\iint_R f(x,y)\,dA = \iint_R f(r\cos(θ), r\sin(θ))\,r\,dr\,dθ
$$

- Example: area of a circle of radius a using double integration
  - Let R be the circular region defined by $x^2 + y^2 ≤ a^2$
  - Set $f$ to be **dimensionless**, i.e. $f=1$
  - Area given by $\iint_R 1\,dA$:
  $$ \begin{align*} \iint_R 1\,r\,dr\,dθ&=\int_0^{2π}\int_0^a r\,dr\,dθ\\ &=\int_0^{2π} \frac{1}{2} a^2\,dθ\\ &=πa^2 \end{align*} $$
- Remember to express the **limits of integration** in polar coordinates.
  - Express $x$ and $y$ in terms of $r$
  - Vertical line: $r=k\secθ$ where $x=k$
  - Horizontal line: $r=k\cscθ$ where $y=k$
