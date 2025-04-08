# 1_2_Level Curves and Partial Differentiation

## Level Curves

- The level curves of a two-variable function $f (x, y)$ are the curves with equation $f (x, y) = k$ where $k$ is a constant. ($k$ is the in the **range** of $f$.)
- Points on a given level curve have the same function value.
- Contour map: collection of level curves. A contour map can give a good idea of the shape of the graph in 3D-space.

## Partial Derivatives

- Partial derivative of $f(x,y)$ with respect to $x$ is

$$
\frac{\partial f}{\partial x}=\lim_{\Delta x \to 0} \frac{\Delta f}{\Delta x}=\lim_{\Delta x \to 0}\frac{f(x+\Delta x,y)-f(x,y)}{\Delta x}
$$

- Partial derivative of $f(x,y)$ with respect to $y$ is

$$
\frac{\partial f}{\partial y}=\lim_{\Delta y \to 0} \frac{\Delta f}{\Delta y}=\lim_{\Delta y \to 0}\frac{f(x,y+\Delta y)-f(x,y)}{\Delta y}
$$

- Alternative notations:
    - $\frac{\partial f}{\partial x}=f_x$
    - $\frac{\partial f}{\partial y}=f_y$
- Computations:
    - $\frac{\partial f}{\partial x}$: treat $y$ as a constant, then take the derivative of $f$ with respect to $x$.
    - $\frac{\partial f}{\partial y}$: treat $x$ as a constant, then take the derivative of $f$ with respect to $y$.
    - For a function $f(x_1,x_2,\dots ,x_n)$, the partial derivatives with respect to $x_i$ are similarly defined.

### Second order partial derivatives

- There are four second order partial derivatives:
    - $\frac{\partial}{\partial x}\frac{\partial f}{\partial x}=\frac{\partial^2f}{\partial x^2}=f_{xx}$
    - $\frac{\partial}{\partial y}\frac{\partial f}{\partial x}=\frac{\partial^2f}{\partial y\partial x}=f_{xy}$
    - $\frac{\partial}{\partial x}\frac{\partial f}{\partial y}=\frac{\partial^2f}{\partial x\partial y}=f_{yx}$
    - $\frac{\partial}{\partial y}\frac{\partial f}{\partial y}=\frac{\partial^2f}{\partial y^2}=f_{yy}$
    - The first operation is the one written closest to $f$.
- **Symmetry of Second Derivatives**: If $f_{xy}$ and $f_{yx}$ are continuous at a point, then they are **equal** at that point.
