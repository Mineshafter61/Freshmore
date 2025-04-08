## Momentum
- State of a system: **position** and **momentum** (both are fundamental)
- Momentum $\vec{p}=m\vec{v}$
- Can be represented as the product of mass and velocity
- Measures the quantity of the motion that obeys the conservation law
- Net force = time range of change of momentum
- $\vec{F}_{net}=\frac{d\vec{p}}{dt}=\frac{d(m\vec{v})}{dt}=\left( \frac{dm}{dt}\vec{v}+m\frac{d\vec{v}}{dt} \right)$
- Average force = $\vec{F}_{ave}=\frac{\int_{t_0}^{t_f} \vec{F} \, dt}{t_f-t_0}$
## Impulse
- Impulse = $\vec{I}=\int_{t_f}^{t_0} \vec{F} \, dt=\vec{F}_{ave}\cdot(t_f-t_0)$
- Area under curve of force-time graph (ref. [[8_Energy and Work Done#Work Done]])
- Impulse results in the **change** in momentum $Δ \vec{p}$
	- It is **not** momentum
## Momentum, Kinetic Energy and Work Done
- Kinetic energy and momentum are related by:
- $K=\frac{1}{2}mv^{2}=\frac{m^{2}v^{2}}{2m}=\frac{p^{2}}{2m}$
- Work-Kinetic Energy Theorem in terms of momentum:
- $W=\int_{\vec{r_{t_0}}}^{\vec{r_{t_f}}} \vec{F}\cdot d\vec{r}=Δ K=\frac{1}{2}mv_f^2-\frac{1}{2}mv_0^2=\frac{p_f^2}{2m}-\frac{p_0^2}{2m}$
- $Δ K \neq \frac{|Δ \vec{p}|^2}{2m}$
- Work‐Kinetic Energy theorem states that work done by a force is the change of kinetic energy of the system (**scalar**)
- Impulse is the change in momentum of a system (**vector**)
- Change in KE is **not** impulse since there is **direction** associated with impulse
## Internal forces
- All internal forces arise from a collection of objects interacting with each other.
- Sum of all internal forces is zero.
## Conservation of momentum
- The **momentum of a system is conserved** ($Δ \vec{p}_{sys} = 0$) if **either** of the conditions are true
	- the external force is 0 (in the direction of calculation); or
	- the interaction time with external forces is negligible
- Total initial momentum = total final momentum: $\sum p_0=\sum p_f$
- Vectors already contain information about direction, only apply the negative sign to scalars
	- e.g For a cart going left where right is defined to be positive
	- $\vec{v} = -v\hat{i}$
	- $-\vec{v} \neq -v\hat{i}$
- For conservation of momentum ($Δ p = 0$), **reference frame must consider all relevant objects as 1 system**
	- Usually from the "ground" perspective **outside** the system
	- **Cannot** be from the perspective of an object in the system
	- Recall relative velocity, where $v_{a,g}$ is velocity of $a$ with respect to the ground
$$v_{a,g} = v_{a,b} + v{b,g} \text{ where } b \text{ can be any other object in the system}$$
- Angle of velocities is also **different** for different reference frames since the cosine component of velocity is different for the same sine component if both reference frames only experience $Δ x$.
## Collisions
- If the net external force acting on a system is zero, or interaction time is negligible, then the momentum of the system is constant:
$$
\vec{I}_{net}=\int_{t_i}^{t_i} \vec{F}_{net} \, dt =0\implies Δ \vec{P}=\vec{0}
$$
- **Momentum is conserved for all collisions** if the conditions for [[9_Momentum and Impulse#Conservation of momentum|Conservation of Momentum]] are met
- **Elastic collisions**: 
	- Kinetic energy is **conserved**
	- $K_i = K_f$
	- $v_{1i}-v_{2i}=v_{2f}-v_{1f}$
	- If two objects of the **same mass** are travelling in the at the **same speed** in **opposite directions** collide, both objects come to a **stop**
	- If object $A$ travelling at velocity $\vec{v}$ collides with another object $B$ of the **same mass** at rest, object $A$ comes to a stop and **all** of its velocity $\vec{v}$ is **transferred** to object $B$
- **Super-elastic collisions**: 
	- **Initial** Kinetic Energy is **smaller** than **final** Kinetic Energy
	- $K_i < K_f$
- **Inelastic collisions**: 
	- **Initial** Kinetic Energy is **larger** than **final** Kinetic Energy
	- $K_i > K_f$
- **Perfectly elastic collisions**: 
	- All particles/objects **cluster** and stick together after collision: **only one body emerges**
### Energy Momentum Law
- Only applicable for **elastic** collisions
- **Both** momentum and kinetic energy are conserved
$$
\begin{align*}
p_{x,i}&=p_{x,f} \\
\implies m_{1}v_{1i}+m_{2}v_{2i}&=m_{1}v_{1f}+m_{2}v_{2f} \\
\implies m_{1}(v_{1i}-v_{1f})&=m_{2}(v_{2i}-v_{2f}) &(1) \\
K_{x,i}&=K_{x,f} \\
\implies \frac{1}{2}m_{1}v_{1i}^{2}+\frac{1}{2}m_{2}v_{2i}^{2}&=\frac{1}{2}m_{1}v_{1f}^{2}+\frac{1}{2}m_{2}v_{2f}^{2} \\
\implies m_{1}(v_{1i}^{2}-v_{1f}^{2})&=m_{2}(v_{2i}^{2}-v_{2f}^{2}) \\
\implies m_{1}(v_{1i}-v_{1f})(v_{1i}+v_{1f})&=m_{2}(v_{2i}-v_{2f})(v_{2i}+v_{2f}) &(2) \\\\
\text{Divide (2) by (1):} \\
v_{1i}-v_{2i}&=v_{2f}-v_{1f}\\
(v_{1i}-v_{2i})&=-(v_{1f}-v_{2f}) &
\end{align*}
$$
- Define relative velocities
$$
\begin{gather*}
v_{rel,i} = v_{1i} - v_{2i} \\
v_{rel,f} = v_{1f} - v_{2f}
\end{gather*}
$$
- Therefore
$$
v_{rel,i} = -v_{rel,f}
$$