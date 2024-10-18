## Rigid Body
- Extended, nondeformable object in which the relative locations of all particles of which the object is composed remain **constant**
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
- Consider a rigid body rotates with $\vec{\omega}$ and $\vec{\alpha}$. Each small element of mass ($\Delta m_i$) is subjected to a force $\vec{F}_i$.
- By Newton's second law, $\Delta m_i$ has an acceleration $\vec{a}_i$ that can be decomposed into the tangential $a_{\theta i}\hat{\theta}$ and radial $a_{ri}\hat{r}$ components with respect to an axis $\vec{S}$ passing perpendicularly through the plane of orbit.
- $\vec{F}_{i} = m_{i}\vec{a}_{i} = m_{i}(a_{\theta i} \hat{\theta} - a_{ri}\hat{r})$
- Let $\vec{r}_{i}=r_{i}\hat{r}$ be the position of point mass relative to $O$. The torque exerted on each $\Delta m_{i}$ is
$$
\begin{gather}
\vec{\tau}_i=\vec{r}_i\times \vec{F}_i=\vec{r}_i \times \Delta m_i(a_{\theta i}\hat{\theta}+a_{ri}\hat{r}) \\
\implies \vec{\tau}_i=\Delta m_ir_i\hat{r}\times(a_{\theta i}\hat{\theta}+a_{ri}\hat{r}) \\
\implies \vec{\tau}_i=mr_ia_{\theta i}\hat{k}=mr_i^2\alpha \hat{k} \\\text{ where } a_{\theta i}=r_{i}\alpha \text{ and } \hat{r} \times \hat{\theta} = \hat{k}
\end{gather}
$$
- Thus, total torque exerted on the rigid body is
$$
\vec{\tau}=\sum \vec{\tau}_{i} = \sum_{i}\Delta m_ir_i^2\alpha \hat{k} \implies \vec{\tau}=\left(\sum_{i}\Delta m_ir_i^2\right)\vec{\alpha}
$$
## Moment of Inertia of a Continuous Rigid Body
- Total torque exerted on the rigid body $$
\vec{\tau}=\left(\sum_{i}\Delta m_ir_i^2\right)\vec{\alpha}
$$
- The moment of inertia of a rigid body about $S$ is defined as (sum over all mass elements)
$$
I_s=\sum_{i}\Delta m_ir_i^2
$$
- Therefore, the moment of inertia of a continuous rigid body about S:
$$ \begin{gather*} I_s=\int_{\text{body}}r^2dm \\ \vec{\tau}=I_s\vec{\alpha} \end{gather*} $$

- Volume density: $\frac{\text{mass}}{\text{volume}} = \rho$
- Surface density: $\frac{\text{mass}}{\text{area}} = \sigma$
- Linear density: $\frac{\text{mass}}{\text{length}} = \lambda$
## Parallel Axis Theorem
- Let the moment of inertia about axis through center of mass of the body be $I_{CM}$.
- Let the moment of inertia about parallel axis through Point S be $I_S$.
- Let the perpendicular distance between 2 parallel axes be $d_{S,CM}$
- **Parallel Axis Theorem**: $I_{S} = Md_{S,CM}^2+I_{CM}$
