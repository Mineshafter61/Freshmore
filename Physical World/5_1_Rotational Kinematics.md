## Right hand curl rule
- Thumb points towards the direction of the vector
- Fingers point towards the direction of motion (tangential velocity)
## Angular displacement
- **Angle** about the origin
- Symbol: $\Delta \theta$
- Where angle is $\theta$
- Unit: $\text{rad}$
- Direction: $z$-axis ($\hat{k}$)
- Axis of rotation (use right hand rule)
## Angular velocity:
- Change in **angular displacement** per unit time
- Symbol: $\vec{\omega} = \frac{d\theta}{dt}\hat{k} = \omega_z\hat{k}$
- Unit: $\text{rad} \cdot s^{-1}$
- Direction:
	- $\vec{\omega}$ in $+\hat{k}$ when $\frac{d\theta}{dt} > 0$
		- Angle $\theta$ is increasing
		- Anticlockwise when viewed from the top
	- $\vec{\omega}$ in $-\hat{k}$ when $\frac{d\theta}{dt} < 0$
		- Angle $\theta$ is decreasing
		- Clockwise when viewed from the top
## Angular acceleration
- Change in **angular velocity** per unit time
- Symbol: $\vec{\alpha} = \frac{d\omega}{dt}\hat{k} = \alpha_z\hat{k}$
- Unit: $\text{rad} \cdot s^{-2}$
- Direction:
	- $\vec{\alpha}$ in $+\hat{k}$ when $\frac{d\omega}{dt} > 0$
		- Angular velocity $\omega$ is increasing
	- $\vec{\alpha}$ in $-\hat{k}$ when $\frac{d\omega}{dt} < 0$
		- Angular velocity $\omega$ is decreasing

- $\vec{v}=\vec{\omega}\times \vec{R}$
- $\vec{\alpha}=\vec{\alpha}\times \vec{R}+\vec{\omega}\times(\vec{\omega}\times \vec{R})$
## Kinematics Formulae (Circular Motion)
- Angular quantities $\theta, \omega_{z}, \alpha_{z}$ follows similar integral relations as the linear kinematics of one-dimensional motion.
- $\frac{d\theta(t)}{dt} = \omega_{z}(t)$
	- $\int^t_{t_{0}} \frac{d\theta(t)}{dt} dt = $
## Torque
- Cause of angular acceleration
- Symbol: $\tau$
- Formula: $\vec{r} \times \vec{F}$
- Moment of inertia: $I = mr^2$ (only true for point particles)
- Formula using moment of inertia: $\tau = I\vec{\alpha}$
- Direction: same direction as angular acceleration
## Rotational Dynamics of a Point Mass
### Torque Law & Moment of Inertia
- $\vec{\tau} = mr^2\vec{\alpha}\hat{k}$
- $\vec{r}\times \vec{F} = \vec{r} \times m(a_{\theta}\hat{\theta}+a_{r}\hat{r})$
- $\vec{\tau}=mr\hat{r} \times (a_{\theta}\hat{\theta}+a_{r}\hat{r})$
- $\vec{\tau}=mra_{\theta}\hat{k} \text{ where } \hat{r} \times \hat{\theta} = \hat{k}$
- $\vec{\tau}=mr^2\alpha \hat{k} \text{ where } a_{\theta} = r \alpha$
- $\vec{\tau}= mr^2 \vec{\alpha} \text{ angular acceleration vector } \vec{\alpha} = \alpha \hat{k}$

### Newton's 2nd Law
| Cause        | $\rightarrow$ | Effect             |     |
| ------------ | ------------- | ------------------ | --- |
| $\vec{F}$    | =             | $m\vec{a}$         |     |
| $\vec{\tau}$ | =             | $mr^2\vec{\alpha}$ |     |

| Linear Motion                                                     | Symbol                                 | Circular Motion                                                                 |
| ----------------------------------------------------------------- | -------------------------------------- | ------------------------------------------------------------------------------- |
| _**Force** changes the state of linear motion_                    | $\vec{F} \leftrightarrow \vec{\tau}$   | _**Torque** changes the state of rotation_                                      |
| _**Acceleration** measures the kinematic<br>effect of force_      | $\vec{a} \leftrightarrow \vec{\alpha}$ | _**Angular acceleration** measures the<br>kinematic effect of torque_           |
| _**Mass** is a measure of the inertia when<br>subject to a force_ | $m \leftrightarrow mr^2$               | _**Moment of inertia** is a measure of the<br>inertia when subject to a torque_ |
  
- $I = mr^2$ is the **moment of inertia** of a point mass $m$ at a perpendicular distance $r$ from a given axis