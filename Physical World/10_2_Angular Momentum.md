## Angular momentum
- In analogy with Newton's second law, torque can be expressed by $\vec{\tau}_{s}=\frac{d(\vec{r}_{s}\times \vec{p})}{dt}$.
- We shall define **angular momentum** with respect to point s: $\vec{L}_{s}=\vec{r}_{s}\times \vec{p}$
- There is **no motion** in the direction of angular momentum
- Angular momentum always points towards the **axis of rotation**, perpendicular to $\vec{r}+s$
- Torque is defined by $\vec{\tau}_s = \frac{d\vec{L}_s}{dt}$
### ... of a point mass
- By the cylindrical coordinate system, the momentum is $\vec{p}=mR\omega \hat{\theta}$
- The position vector is $\vec{r}_s = h\hat{k} + R\hat{r}$
- The angular momentum with respect to point S is $$\vec{L}_{s}=\vec{r}_{s}\times \vec{p}=(h\hat{k}+R\hat{r})\times(mR\omega\hat{\theta})=-hmR\omega \hat{r}+mR^2\omega \hat{k}$$
- If the reference point is at the centre of orbit, the angular momentum will be in the $\hat{k}$ or $-\hat{k}$ direction.
### ... of a point mass in circular motion about a fixed axis
- Angular velocity: $\vec{\omega}=\omega_{z}\hat{k}$
- Velocity: $\vec{v}=R\omega_{z}\hat{\theta}$
- Angular momentum about point S: $$\vec{L}_{s}=\vec{r}_{s}\times \vec{p}=(R\hat{r})\times(mR\omega_{z}\hat{\theta})=(mR^{2}\omega _{z})\hat{k}=(mR^2)\vec{\omega}$$
### ... of fixed axis rotation
- The magnitude and direction of the angular momentum of mass $m_i$ about the point $S$: $\Delta L_{s,i}=\vec{r}_{i}\times (m_{i}\vec{v}_{i})=(r_{i,\parallel}+r_{i,\perp}\hat{r}_{i})\times m_{i}r_{i,\perp}\omega_{z}\hat{\theta}_{i}$
- The component of the angular momentum along the fixed rotation axis ($\hat{k}$) is given by the 2nd term: $(\Delta \vec{L}_{s,i})_{z}=m_{i}r_{i,\perp}^{2}\omega_{z}\hat{k}$
- Therefore, for the rigid body, $$(\vec{L}_{s})_{z}=\lim_{ N \to \infty }\sum_{i}^{N}(m_{i}r_{i,\perp}^{2})\omega_{z}\hat{k}=\left( \int_{body}r_{\perp}^{2}\,dm \right)\omega_{z}\hat{k}=I_{z}\omega_{z}\hat{k}=I_{z}\vec{\omega}$$
	- where $I_z$ is the moment of inertia **only** about the $z$ axis.
		- For symmetrical objects of uniform density spinning about it's CM, $I = I_z$ as all $I_r$ component of a point is cancelled by that of the opposite point
	- $I_{z}\omega_{z}\hat{k}=I_{z}\vec{\omega}$ refers to the rigid body spinning about a fixed axis.
## Angular impulse
- Angular impulse is given by $$\vec{J}_{s}=\Delta \vec{L}_{s}=(\vec{\tau}_{s})_{ave}(\tau_f-\tau_i)=\int_{t_{0}}^{t_{f}} \vec{\tau}_{s} \, dt$$
## Conservation of angular momentum
- Change in angular momentum $\Delta\vec{L}_s$ is **zero** if
	- There is no net external torque **or**
	- The interaction time is short
- Angular momentum is constant w.r.t time
- Take all interacting bodies as **1 system**
## 2D Rotation and Translation
- Angular momentum for a translating and rotating object is given by $$\vec{L}_{s}^{tot}=\sum_{i=1}^{N}\vec{r}_{s,i}\times m_{i}\vec{v}_{s,i}=\vec{R}_{s,cm}\times \vec{p}_{sys}+\sum_{i=1}^{N}\vec{r}_{cm,i}\times m_{i}\vec{v}_{cm,i}$$
- The first term is the angular momentum arising from the **translation** of the centre of mass (a point) w.r.t the fixed reference point $S$ (called orbital motion), $$\vec{L}_{s,cm}^{tr}=\vec{R}_{s,cm}\times \vec{p}^{sys}$$
- The second term is the angular momentum arising from **rotation** (spinning motion) about the centre of mass, $$\vec{L}_{cm}^{rot}=\sum_{i=1}^{N}\vec{r}_{cm,i}\times m_{i}\vec{v}_{cm,i}$$
## Kinetic Energy of Rotating Rigid Body
For a spinning ice skater
$$
K_{rot} = \frac{1}{2}I_z(\omega_z)^2 = \frac{(L_z)^2}{2I_z}
$$
- Rotational momentum $L_z$ is always **conserved**
- Rotational KE $K_{rot}$ is **not conserved**
	- When pulling her arms in, $K_{rot}$ is **increased** due to WD by muscles (somehow considered external) being added to the system
	- Since angular momentum $L_z$ is conserved and $I_z$ in the denominator decreases ($r$ decreases as she pulls her arms in), $K_{rot}$ increases
## Fixed Axis Rotation of Rigid Body
- Torque of rigid body about an axis: $$\vec{\tau}_{s}=\frac{d\vec{L}_{s}}{dt}=I_s \frac{d\vec{\omega}}{dt}=I_s\vec{\alpha}$$
- If there is no resultant torque about the $z$-axis: $$
\vec{\tau}_{s}=0 \implies \frac{d\vec{L}_{s}}{dt}=I_{s}\vec{\alpha}=\vec{0}
$$
- Therefore, angular momentum is constant: $$\begin{align}
\vec{L}_{s,f}&=\vec{L}_{s,i}\\
I_{z,f}\omega_{z,f}&=I_{z,i}\omega_{z,i}
\end{align}$$