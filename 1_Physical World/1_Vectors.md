## Vectors
- Scalar: magnitude only
- Vector: magnitude + direction

Example:
> Displacement: $\vec{s}$
> Distance (magnitude of displacement): $|\vec{s}|$

- Vectors can be represented by an arrow: 
	- length : magnitude ($|\vec{A}|$ -> A)
	- arrow head : direction of the vector ($\frac{\vec{A}}{A}=\hat{A}$ "A hat", magnitude = 1)
	- Hence, $\vec{A}$ = $|\vec{A}|\cdot \hat{A}$

- 2 vectors are identical if their magnitude and direction are the same.

### Operations of Vectors
- Addition (tip-to-tail or parallelogram methods)
- Subtraction (tip-to-tail or parallelogram methods) -> use $\vec{A} + (-\vec{B})$ 
- **Angle between vectors: angle between the vectors' tails**

### Cartesian coordinates
- Define î = 1 unit in the x-axis and ĵ = 1 unit in the y-axis
- Position vector of a point P (x, y) is the displacement vector from the origin $\vec{r} = xî + yĵ$
> Addition and subtraction:
> $\vec{r_{1}} = x_{1}î + y_{1}ĵ$
> $\vec{r_{2}} = x_{2}î + y_{2}ĵ$
> $\vec{r_{1}}+\vec{r_{2}} = (x_{1}+x_{2})î + (y_{1}+y_{2})ĵ$

> Magnitude: $\vec{r} = xî + yĵ \implies |\vec{r}| = \sqrt{x^{2}+y^{2}}$
> Direction (with respect with x-axis): $\arctan{\frac{y}{x}}$

### Polar coordinates
- Described with (r, θ)
- Unit vector $\hat{r}$: away from the origin
- Unit vector $\hat{θ}$: tangentially in the anti-clockwise direction
- $\hat{r}$ and $\hat{θ}$ are *position dependent* (function of angle θ)

Conversion between the two coordinate systems:
$x = r \cos θ$
$y = r \sin θ$
$\hat{r} = \cos{ θ\cdot\hat{i}} + \sin{ θ\cdot\hat{j}}$
$\hat{θ} = -\sin{ θ\cdot\hat{i}} + \cos{ θ\cdot\hat{j}}$

Position vector r of point P:
$\vec{r}$ = $x\hat{i} + y\hat{j}$
$\vec{r}$ = $r\hat{r}$
### Dot product
$\vec{A} \cdot \vec{B} = AB \cos{θ}$
$\vec{A} \cdot \vec{B} = a_{1}b_{1}+a_{2}b_{2}+a_{3}b_{3}$
- Pure scalar
- Commutative ($\vec{A} \cdot \vec{B} = \vec{B} \cdot \vec{A}$)
- Distributive
- **Graphical interpretation**: for two vectors, the dot product gives the component of one vector in another vector (projection of one vector on another vector)
- Used when having the same direction carries meaning

Example:
> Work done: $W = \vec{F}\cdot\vec{S}$
### Cross product
$\vec{A} \times \vec{B} = AB \sin{θ}.\hat{n}$
$\begin{bmatrix}s_{x}\\ s_{y}\\ s_{z}\end{bmatrix} = \begin{bmatrix}a_{y}b_{z}-a_{z}b_{y}\\ a_{z}b_{x}-a_{x}b_{z}\\ a_{x}b_{y}-a_{y}b_{x}\end{bmatrix}$
- Vector
- **Not commutative**
- Distributive
- **Graphical interpretation**: Area of the parallelogram formed by vectors A and B.
Example:
> Torque: $\vec{\tau} = \vec{r}\times\vec{F}$