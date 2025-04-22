# 13_Linear Transformations

A function $T:\mathbb{R}^n\rightarrow\mathbb{R}^m$ is called a **linear transformation** if for **all** vectors $\vec{u},\vec{v}\in \mathbb{R}^n$ and **all** scalars $c\in \mathbb{R}$,

- $T(\vec{u}+\vec{v})=T(\vec{u})+T(\vec{v})$ (closed under vector addition)
- $T(c\vec{u})=cT(\vec{u})$ (closed under scalar multiplication)
- Same property as subspaces
- $T$ is a *mapping* from all $\vec{u}$ to $T(\vec{u})$ (reference: functions)
- The number of dimensions can change (e.g. from $\mathbb{R}^3$ to $\mathbb{R}^2$ and vice versa)
- Example: $g:x\rightarrow 9x$ is a linear transformation (scalaing by 9)
- Example: $h:x\rightarrow x^2$ is a NOT a linear transformation
    - $h(x_1+x_2)=x_1^2+x_2^2+2x_1x_2$, not $x_1^2+x_2^2$ (general)
    - Let $x = 2$, $c = 3$. $h(cx)=h(6)=6^2=36\neq 3h(2)=3(4)=12$ (by counter-example)

## Transformation Matrix

If $A$is an $m\times n$ matrix, then $T(\vec{u}) := A\vec{u}$ is a linear
transformation, because
$$A(\vec{u}+\vec{v}) = A\vec{u}+ A\vec{v} and A(c\vec{u}) = cA\vec{u}$$
$A$ is called the **transformation matrix**.

- Constructing $A$:
$$\begin{align}T(x_1\vec{e}_1+x_2\vec{e}_2+\dots+x_n\vec{e}_n)&=T(x_1\vec{e}_1)+T(x_2\vec{e}_2)+\dots+T(x_n\vec{e}_n)\\&=x_1T(\vec{e}_1)+x_2T(\vec{e}_2)+\dots+x_nT(\vec{e}_n)\\&=\begin{bmatrix}T(\vec{e}_1)&T(\vec{e}_2)&\cdots&T(\vec{e}_n)\end{bmatrix}\begin{bmatrix}x_1\\x_2\\\vdots\\x_n\end{bmatrix}\end{align}$$
- $\begin{bmatrix}T(\vec{e}_1)&T(\vec{e}_2)&\dots&T(\vec{e}_n)\end{bmatrix}$ is the transformation matrix of $T$.
    - This matrix **may not be a square matrix**.
- $A$ consists of a combination of a few fundamental operations (scaling, rotation, reflection).
- Generally, the matrix $A$:

$$
A=
\begin{bmatrix}
T(\hat{i})_{x} & T(\hat{j})_{x} & T(\hat{k})_{x} & \cdots \\
T(\hat{i})_{y} & T(\hat{j})_{y} & T(\hat{k})_{y} & \cdots \\
T(\hat{i})_{z} & T(\hat{j})_{z} & T(\hat{k})_{z} & \cdots \\
\vdots & \vdots & \vdots & \ddots
\end{bmatrix}
$$

- where $T(\hat{i})_{x}$ is the **$x$-component of the transformation of the unit vector along the x-axis $\hat{i}$**.

## Composite linear transformations

Let $T:\mathbb{R}^n\rightarrow\mathbb{R}^m$ and $S:\mathbb{R}^n\rightarrow\mathbb{R}^r$ be linear transformations. Then the transformation matrix of the composite linear transformation $S\circ T: \mathbb{R}^n\rightarrow\mathbb{R}^r$ is $BA$, where $A$ is the $m\times n$ transformation matrix of $T$ and $B$ is the $r\times m$ transformation matrix of $S$.

## Rotations

### 2D

Consider a **counterclockwise** rotation (axis of rotation is $\hat{z}$) $R_θ$ by angle $θ$ in $\mathbb{R}^2$. The transformation matrix is given by
$$
A_\theta=\begin{bmatrix}
\cos \theta & -\sin \theta \\
\sin \theta & \cos \theta
\end{bmatrix}
$$
For a **clockwise** rotation, the transformation matrix is given by

$$
A_\theta=\begin{bmatrix}
\cos \theta & \sin \theta \\
-\sin \theta & \cos \theta
\end{bmatrix}
$$

### 3D

Consider a **counterclockwise** rotation $R_{y,\theta}$ by angle $\theta$ about the **y-axis** in $\mathbb{R}^3$. The transformation matrix is given by
$$
A_{y,\theta}=\begin{bmatrix}
\cos \theta & 0 & \sin \theta \\
0 & 1 & 0 \\
-\sin \theta & 0 & \cos \theta
\end{bmatrix}
$$
The transformation matrix of a **counterclockwise** rotation about the **x-axis** is
$$
A_{x,\theta}=\begin{bmatrix}
1 & 0 & 0 \\
0 & \cos \theta & \sin \theta \\
0 & -\sin \theta & \cos \theta
\end{bmatrix}
$$
The transformation matrix of a **counterclockwise** rotation about the **z-axis** is
$$
A_{z,\theta}=\begin{bmatrix}
\cos \theta & \sin \theta & 0 \\
-\sin \theta & \cos \theta & 0 \\
0 & 0 & 1
\end{bmatrix}
$$
For **clockwise**, replace all $\sin$ with $-\sin$

## Reflections

- About the $x$-axis in $\mathbb{R}^2$ (flip $y$)

$$
B = \begin{bmatrix}
1 & 0 \\
0 & -1
\end{bmatrix}
$$

- About the $y$-axis in $\mathbb{R}^2$ (flip $x$)

$$
B = \begin{bmatrix}
-1 & 0 \\
0 & 1
\end{bmatrix}
$$

- About the line $y=x$

$$
B = \begin{bmatrix}
0 & 1 \\
1 & 0
\end{bmatrix}
$$

## Scaling

- Eigenvalues are scaling factors
    - $A = PDP^{-1}$
    - Vectors in $D$ are the **scaling factors**
    - Vectors in $P$ are **bases (eigenbases) along which scaling is done**

## Connections with Determinants

- The determinant of the transformation matrix $A$ is the signed volume of the n-parallelotope (in 2D, area of the parallelogram) formed by the vectors of $A$.
- The absolute value of $\det(A)$ is the **volume scale vector** of of the transformation represented by $A$.
- The sign of $\det(A)$ indicates whether the transformation preserves orientation.
    - Positive: same orientation
    - Negative: opposite orientation

## Jacobian

- See [[5_2_Change of Variables]]
