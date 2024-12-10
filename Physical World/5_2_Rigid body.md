## Rigid Body
- Extended, non-deformable object in which the relative locations of all particles of which the object is composed remain **constant**
	- No shape change when forces are applied
### Translational Motion
- External force acts on center of mass (CM)
- The entire object moves
### Rotational Motion
- Object rotates about CM
- The entire object rotates
## Fixed Axis Rotation
- Axis of rotation always points in the same direction
	- No change in $\hat{k}$
	- Every part of the same body must have the same angular velocity and angular acceleration.
## Forces and torque law
- Consider a rigid body rotates with $\vec{\omega}$ and $\vec{\alpha}$. Each small element of mass ($Δ m_i$) is subjected to a force $\vec{F}_i$.
- By [[3_Forces#Second law of motion|Newton's Second Law]], $Δ m_i$ has an acceleration $\vec{a}_i$ that can be decomposed into the tangential $a_{θ i} \hat{θ}$ and radial $a_{ri} \hat{r}$ components with respect to an axis $\vec{S}$ passing perpendicularly through the plane of orbit.
- $\vec{F}_{i} = m_{i} \vec{a}_{i} = m_{i} (a_{θ i} \hat{θ} - a_{ri} \hat{r})$
- Let $\vec{r}_{i} = r_{i} \hat{r}$ be the position of point mass relative to $O$. The torque exerted on each $Δ m_{i}$ is

$$\begin{gather}
\vec{\tau}_i=\vec{r}_i\times \vec{F}_i=\vec{r}_i \times Δ m_i(a_{θ i}\hat{θ}+a_{ri}\hat{r}) \\
\implies \vec{\tau}_i=Δ m_ir_i\hat{r}\times(a_{θ i}\hat{θ}+a_{ri}\hat{r}) \\
\implies \vec{\tau}_i=mr_ia_{θ i}\hat{k}=mr_i^2\alpha \hat{k} \\\text{ where } a_{θ i}=r_{i}\alpha \text{ and } \hat{r} \times \hat{θ} = \hat{k}
\end{gather}$$

- Thus, total torque exerted on the rigid body is

$$\vec{\tau}=\sum \vec{\tau}_{i} = \sum_{i}Δ m_ir_i^2\alpha \hat{k} \implies \vec{\tau}=\left(\sum_{i}Δ m_ir_i^2\right)\vec{\alpha}$$
## Moment of Inertia
- Affected by **mass** and the **distribution of mass** from the axis of rotation
- The moment of inertia of a rigid body about $S$ is defined as the sum of all the small mass elements it is composed of:
$$
I_s=\sum_{i}Δ m_ir_i^2
$$
- Using continuous limits,
$$
\begin{gather*}
    Δ m_i \to dm \\
    r_i \to r \\
    \sum_{i} \to \underset{\text{body}}{\int}
\end{gather*}
$$
- Therefore, the moment of inertia of a continuous rigid body about S is
$$
I_s=\underset{\text{body}}{\int} r^2 \, dm
$$
- Unit is $kg \cdot m^2$
## Calculating Moment of Inertia
- For objects of **uniform density**
    - Volume density = $\frac{\text{mass}}{\text{volume}} \implies \rho = \frac{m}{V}$
    - Surface density = $\frac{\text{mass}}{\text{area}} \implies \sigma = \frac{m}{A}$
    - Linear density = $\frac{\text{mass}}{\text{length}} \implies \lambda = \frac{m}{L}$
- For **linear** objects of **non-uniform density**
    - e.g Density $\lambda$ is a function of length $x$, $\lambda(x) = Ax^2$
    - Density $\lambda(x)$ has to be individually calculated for each particle of mass $Δ m$ at distance $Δ x$ from the start of the function (start of rod) to the end of the function (end of rod)
    - $\lambda(x) = \frac{dm}{dx} \implies dm = \lambda(x) dx$
    - To get the constant $A$ which affects the "average" density of the whole rod, we integrate this equation and set the limits to the start and end of the rod
$$
\begin{gather*}
    M = \int_{0}^{L} \lambda(x) \, dx = \int_{0}^{L} Ax^2 \, dx = \frac{AL^3}{3} \\
    A = \frac{3M}{L^3} \text{ (This value is only for this specific example)}
\end{gather*}
$$
### Uniform Rod
- Given a linear object of length $L$ where the axis of rotation is at its CM,
    - Since the rod is uniform, density $\lambda(x) = \frac{M}{L}$ (constant, not a function of $x$)
    - Sub $dm = \lambda(x) dx$ derived above, to integrate w.r.t displacement $x$ instead of mass $m$
    - Top and bottom **integral limits** are the **leftmost** and **rightmost** end of the rod, calculated with the **axis of rotation** as the **origin**
    - The moment of inertia about the center of mass is: 
      $$I_{CM}=\int_{rod}r^2\,dm=\int_{-L/2}^{L/2}x^2\,dm=\int_{-L/2}^{L/2}\frac{x^2M}{L}\,dx=\frac{M}{3L}[x^3]_{-L/2}^{L/2}=\frac{ML^2}{12}$$
    - $I = \frac{1}{12}ML^2$ (rotating from midpoint)
    - $I = \frac{1}{3}ML^2$ (rotating from edge)
### Uniform Disk
- $I = \frac{1}{2}MR$ (spinning, axis of rotation through midpoint in the $z$-axis)
- $I = \frac{1}{4}MR$ (flipping, axis of rotation through midpoint in $x$-axis or $y$-axis)
### Uniform Cylinder
- $I = \frac{1}{2}MR^2$ (rotating through CM in the height axis)
## Parallel Axis Theorem
- Let the moment of inertia about axis through center of mass of the body be $I_{CM}$.
- Let the moment of inertia about parallel axis through Point S be $I_S$.
- Let the perpendicular distance between 2 parallel axes be $d_{S,CM}$
- **Parallel Axis Theorem**: $I_{S} = Md_{S,CM}^2+I_{CM}$
![[parallel axis theorem.png]]
