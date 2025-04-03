# Vectors

## Dot product

$\vec{A} \cdot \vec{B} = AB \cos{θ}$
$\vec{A} \cdot \vec{B} = \displaystyle\sum_{i=1}^{n}a_ib_i= a_1b_1+a_2b_2+\dots+a_nb_n$

- Pure scalar
- Commutative ($\vec{A} \cdot \vec{B} = \vec{B} \cdot \vec{A}$)
- Distributive
- **Graphical interpretation**: for two vectors, the dot product gives the component of one vector in another vector (projection of one vector on another vector)
- Used when having the same direction carries meaning
- $\vec{A}\cdot \vec{B}=0\leftrightarrow \vec{A}\perp \vec{B}$

## Norm of vectors

- The length or **norm** of a vector $\vec{v}$ is given by $||\vec{v}||=\sqrt{v_1^2+v_2^2+\dots+v_n^2}=\sqrt{\vec{v} \cdot \vec{v}}$

## Cross product

$\vec{A} \times \vec{B} = AB \sin{θ}\,\hat{n}$
$\begin{bmatrix}s_{x}\\ s_{y}\\ s_{z}\end{bmatrix} = \begin{bmatrix}a_{y}b_{z}-a_{z}b_{y}\\ a_{z}b_{x}-a_{x}b_{z}\\ a_{x}b_{y}-a_{y}b_{x}\end{bmatrix}$

- Vector
- **Anti-commutative**
- Distributive
- Not associative
- Defined **only for** $\mathbb{R}^3$
- The cross product of two vectors gives a vector perpendicular to both vectors.
- **Graphical interpretation**: Area of the parallelogram formed by vectors A and B.

## Expressing Vectors

- Vector $\vec{v}$ in $\mathbb{R}^{3}$ can be expressed as $v_{1}\vec{e}_{1}+v_{2}\vec{e}_{2}+v_{3}\vec{e}_{3}$ where
$$\begin{align}\vec{e}_{1} = \begin{bmatrix}1\\0\\0\end{bmatrix}=\hat{i}\\\vec{e}_{2} = \begin{bmatrix}0\\1\\0\end{bmatrix}=\hat{j}\\\vec{e}_{3} = \begin{bmatrix}0\\0\\1\end{bmatrix}=\hat{k}\end{align}$$
- $\vec{e}_{1}, \vec{e}_{2},\vec{e}_{3}$ are unit vectors.

## Linear combinations

- A vector $\vec{v}$ can be expressed as a linear combination of $\vec{v}_{1}$, $\vec{v}_{2}$, $\dots$, $\vec{v}_{n}$ if it can be expressed as
$$\vec{v}=α_1\vec{v}_1+α_2\vec{v}_2+···+α_n\vec{v}_n$$

## Lines and Planes

### Lines

- Normal form of the equation of a line in $\mathbb{R}^2$ is $$\vec{n}\cdot(\vec{r}-\vec{r}_{0})=0$$
    - $\vec{r}_{0}$ is the position vector of a specific point on the line
- General form of the equation of a line in $\mathbb{R}^2$ is $$ax+by=c$$
    - $\vec{n}=\begin{bmatrix}a\\b\end{bmatrix}$ is a normal vector of the line
- Vector form of the equation of a line in $\mathbb{R}^2$ and higher dimensions is
$$\vec{r}=\vec{r}_0+t\vec{d}\,\,\,,\,\,\,\forall\, t∈\mathbb{R}$$
>
> - $\vec{r}_{0}$ is the position vector of a specific point on the line
> - $\vec{d}\neq\vec{0}$ is a direction vector of the line (vector parallel to the line)
>
- $\vec{n}\perp \vec{d},\vec{n}\cdot \vec{d}=0$

### Planes

- Normal form of the equation of a plane in $\mathbb{R}^3$ is
$$\vec{n}\cdot(\vec{r}-\vec{r}_{0})=0$$
>
> - $\vec{r}_{0}$ is the position vector of a specific point on the plane
> - $\vec{n}=\begin{bmatrix}a\\b\end{bmatrix}$ is a normal vector of the plane
>
- General form of the equation of a plane in $\mathbb{R}^3$ is >
$$ax+by+cz=d$$
>
> - $\vec{n}=\begin{bmatrix}a\\b\\c\end{bmatrix}$ is a normal vector of the plane
> - $d$ is the dot product of the normal vector and a specific point on the plane.
>
- Vector form of the equation of a plane in $\mathbb{R}^3$ and higher dimensions is
$$\vec{r}=\vec{r}_0+s\vec{u}+t\vec{v}\,\,\,,\,\,\,\forall\, s,t∈\mathbb{R}$$
>
> - $\vec{r}_{0}$ is the position vector of a specific point on the plane
> - $\vec{u}\ne\vec{0}$ and $\vec{v}\ne\vec{0}$ are direction vectors of the plane
> - $\vec{u}$ and $\vec{v}$ are parallel to the plane but NOT parallel to each other.
