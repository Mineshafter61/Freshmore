## Conditions for Static Equilibrium
- Translational Equilibrium
	- the vector sum of the external forces acting on the rigid body is zero
	- $\vec{F_{total}}=\vec{F_1}+\vec{F_2}+\cdots=\vec{0}\implies\vec{a_{CM}}=\vec{0}$
- Rotational Equilibrium
	- the vector sum of the torques about any point $S$ in a rigid body is zero
	- $\vec{\tau_{s, \text{total}}}=\vec{\tau_{s,1}}+\vec{\tau_{s,1}}+\cdots=\vec{0}\implies\vec{\alpha_{s}}=\vec{0}$
- **Static Equilibrium** (special case of dynamic equilibrium)
	- the rigid body is in translational and rotational equilibrium, and it is at rest relative to the observer
	- $v_{CM}=0 \text{ and } \omega=0$
### Problem Solving Strategy
- **Part 1: Force**
	1. Choose a coordinate system
	2. Draw free body diagrams for all relevant objects
	3. Write down the equations of motion for *translational equilibrium*: **sum of forces is a zero vector**, i.e. $\sum \vec{F}=\vec{0}$. 
- **Part 2: Torque**
	1. **Choose an arbitrary point about which the torques are to be analysed.**
	2. Choose a sign convention for torque
	3. For each force, calculate torque **about that point** (note the sign!)
	4. Write down the equation for rotational equilibrium condition: **sum of torques about that point is a zero vector**, i.e. $\sum \vec{\tau}=\vec{0}$.
## Rotational Dynamics
[[5_1_Rotational Kinematics#Rotational Dynamics of a Point Mass]]
- **Moment of inertia** (found experimentally): $I_{cm}=mR^2\left( \frac{gt_{1}^2}{2s}-1 \right)$
- In a system with a massive pulley, the **tension in the string is not the same throughout the string**.
### Problem Solving Strategy
1. Draw a simplified diagram of the system clearly indicating all forces and their point of action. For each force, draw the vector, $\vec{r}$, pointing from $S$ to where $\vec{F}$ acts. (Torque diagram)
2. Draw a free body diagram.
3. Use right hand rule to determine the direction for angular acceleration. Set this direction as the positive rotation direction and indicate it in the torque diagram, e.g. ↺+
4. Indicate the point about which you are calculating the torques in the torque diagram.
5. Set up the dynamical equations using **[[3_Forces#Second law of motion|Newton's Second Law]]** and the **[[5_1_Rotational Kinematics#Torque Law & Moment of Inertia|Torque Law]]**. 
6. Look out for **constraint condition** between rotational acceleration and linear acceleration (if any).
7. Solve for the quantities of interest.
## Rotational and Translational Motion
- Translational Motion (Newotn's 2nd Law): $\vec{F}_{CM}=m\vec{a}_{CM}$
- Rotational Motion (Torque Law): $\vec{\tau}=I_{CM}\vec{\alpha}$
- For linear motion, things rotate about a fixed axis (always poining in k direction) and the center of mass translates constantly such that $\vec{a}_{CM}=\vec{0}$
### Relative velocities
- $\vec{v}_{a,b} = \vec{v}_{a,c} + \vec{v}_{c,b}$
  - Where $c$ is the "middleman"
### Rolling Wheel
- Distance traveled in the center of mass reference frame by point P (a point on the rim) in time $\Delta t$: $\Delta s=R \Delta \theta = R \omega_{CM} \Delta t$
- Distance traveled in the reference frame fixed to ground by center of mass in time $\Delta t$: $\Delta X_{CM}=V_{CM}\Delta t$

| Circular Motion (W4) | Rotational Dynamics (W6D1) | Rotational Motion (W6D2) |
|---|---|---|
| $V=R\omega$, where vV is tangential speed | $V_{cm}=R\omega$ | $V_{cm}=R\omega$, where V is the speed of the center of mass of rolling object |
| $a_{\theta}=R\alpha$, where a is tangential acceleration | $a_{cm}=R\alpha$, where a is linear acceleration of falling object | $a_{cm}=R\alpha$, where a is acceleration of rolling object (ONLY TRUE FOR PURE ROLLING) |

- Cylinder Rolling Without Slipping Down an Inclined Plane: $v(t)=\sqrt{\frac{2mR^2}{I_{CM}+mR^2}gh}=\sqrt{\frac{2gh}{\frac{I_{CM}}{mR^2}}+1}$
- Velocity of objects rolling down a hill is **independent** of mass and radius (Since $I = \sum \Delta m \Delta r^2$)


