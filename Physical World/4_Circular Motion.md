- Definition: special case of two-dimensional motion in which the object maintains a constant distance away from a fixed point.
- Position vector at any point in circular motion: $\vec{r}=R\hat{r}$
## Calculus
- Product rule: $\displaystyle\frac{d(uv)}{dt} = \frac{du}{dt}v+\frac{dv}{dt}u$
- Chain rule: $\displaystyle\theta(t), f(\theta): \frac{df}{dt} = \frac{df}{d\theta} \frac{d\theta}{dt}$
> $\displaystyle\sin \theta:  \frac{d \sin\theta}{dt} = \frac{d \sin \theta}{d\theta} \frac{d\theta}{dt} = \cos \theta \frac{d\theta}{dt}$
> $\displaystyle\cos \theta:  \frac{d \cos\theta}{dt} = \frac{d \cos \theta}{d\theta} \frac{d\theta}{dt} = -\sin \theta \frac{d\theta}{dt}$

> $\displaystyle\hat{r}=\cos \theta \hat{i}+\sin \theta \hat{j}$
> $\displaystyle\frac{d\hat{r}}{dt}=-\sin \theta \frac{d\theta}{dt} \hat{i} + \cos \theta \frac{d\theta}{dt} \hat{j}= \frac{d\theta}{dt}(-\sin \theta \hat{i}+\cos \theta \hat{j})$
> $\displaystyle\frac{d\hat{r}}{dt}=\frac{d\theta}{dt}\hat{\theta}$

> $\displaystyle\hat{\theta} = -\sin \theta \hat{i}+\cos \theta \hat{j}$
> $\displaystyle\frac{d\hat{\theta}}{dt}=-\cos \theta \frac{d\theta}{dt}\hat{i}-\sin \theta\frac{d\theta}{dt}\hat{j}= \frac{d\theta}{dt}(\cos \theta \hat{i}+\sin \theta \hat{j})$
> $\displaystyle\frac{d\hat{\theta}}{dt}=-\frac{d\theta}{dt}\hat{r}$

## Physics
- Position vector: $\vec{r} = R\hat{r}$
- Velocity vector: $\displaystyle\vec{v}=\frac{d\vec{r}}{dt}=\frac{d(R\hat{r})}{dt}=R \frac{d\hat{r}}{dt}= R \frac{d\theta}{dt}\hat{\theta}$
	- Direction of $\vec{v}$ is $\hat{\theta}$
	- Angular speed, $\displaystyle \omega:=\frac{d\theta}{dt}$
	- $\vec{v}=R\omega \hat{\theta}$, where $\displaystyle\omega=\frac{d\theta}{dt}$
- Acceleration $\displaystyle\vec{a}=\frac{d\vec{v}}{dt}=\frac{d}{dt}\left( R \frac{d\theta}{dt} \hat{\theta} \right)=R \frac{d}{dt}\left( \frac{d\theta}{dt} \hat{\theta} \right)$
	- $\displaystyle=R\left[ \frac{d}{dt}\left( \frac{d\theta}{dt} \right) \right]\hat{\theta}+R\frac{d\theta}{dt}\left( \frac{d\hat{\theta}}{dt} \right)$
	- $\displaystyle=R \frac{d^2\theta}{dt^2} \hat{\theta} + R\left( \frac{d\theta}{dt} \right)^2(-r^2)$
	- Tangential acceleration: $R \frac{d^2\theta}{dt^2} \hat{\theta}$
	- Centripetal acceleration: $R\left( \frac{d\theta}{dt} \right)^2(-r^2)$

### Accelerations
- Tangential acceleration, $\vec{a}_{\theta}$
	- Direction of $\vec{a}_{\theta}$ is $\hat{\theta}$
	- Increases/decreases the speed
	- Define angular acceleration $\alpha := \frac{d^2\theta}{dt^2} \text{or} \frac{d\omega}{dt}$; unit: $rad.s^-2$
- Centripetal acceleration, $\vec{a}_{r}$
	- Direction of $\vec{a}_{r}$ is $-\hat{r}$
	- Changes the direction of $\vec{v}$
	- $|\vec{a_{r}}| = R\left( \frac{d\theta}{dt} \right)^2 = R\omega ^2=\frac{v^2}{R}$
- $\vec{a}=\vec{a}_{\theta}+\vec{a}_{r}=R\alpha \hat{\theta} + R\hat{\omega}^2(-\hat{r})=\frac{v^2}{R}(-\hat{r})$

## Uniform circular motion
- In a **uniform circular motion**, there is **no tangential acceleration**.
- Centripetal acceleration is $\vec{a_{r}}=-|a_{r}|\hat{r}$, or
	- $\vec{a_{r}}=-v\omega \hat{r}=-\frac{v^2}{R}\hat{r}=-\omega^2R\hat{r}$
- Direction of velocity is constantly changing due to the **centripetal acceleration**.
## Nonuniform circular motion
- If the speed is time-varying, the motion is a nonuniform circular motion.
- Radial (centripetal acceleration is time-varying):
	- $\vec{a_{r}} (t) = -\frac{v^2(t)}{R}\hat{r}$
- There is also a tangential acceleration component $\hat{a_{\theta}}(t)$ that is **parallel** to the instantaneous velocity.
- Total acceleration:  $\vec{a}(t)=\vec{a_{r}}(t)+\vec{a_{\theta}}(t)$
## Summary of formulae
- Arc length and angular displacement: $s = R\theta$
- Tangential velocity and angular speed: $\vec{v}=\frac{d\vec{s}}{dt}=R \frac{d\theta}{dt} \hat{\theta} = R\omega \hat{\theta}$
- Tangential acceleration: $\vec{a}_{\theta}=\frac{d|\vec{v}|}{dt}\hat{\theta}=R \frac{d^2\theta}{dt^2}\hat{\theta}=R\alpha \hat{\theta}$
- Radial (centripetal) acceleration: $\vec{a}_{r}=-v\omega \hat{r}=-\frac{v^2}{R}\hat{r}=-R\omega^2\hat{r}$
- Angular speed: $\omega=\frac{d\theta}{dt}$
- Angular acceleration: $\alpha=\frac{d\omega}{dt}=\frac{d^2\theta}{dt^2}$
- Note : $\vec{a}_{r}$ has a negative sign since positive radial direction is defined as the direction pointing **away** from the center of the circular orbit.
## Dynamics of Uniform Circular Motion
- For an object in uniform circular motion, both its acceleration and the net force on it are directed towards the center of the circle.
- Acceleration is only centripetal.
- Net force on the particle: $\vec{F}_{\text{net}} = \sum \vec{F} = m\vec{a}$
## Centrifugal Force
- It is a **fictitious force** in an inertial frame of reference
- i.e The frame of reference is at a constant velocity (or $0$), from an observer **outside** of the circular motion
- The force is only required when **inside** the circular motion to explain the outwards push an object would experience inside
- This force points **outwards**, but should **not** be included in a free body diagram as its fictitious in the inertial frame of reference
## Useful Conversions
### Period $T$
- Time taken to complete 1 full circular orbit of $2\pi R$
- $T = \frac{\text{circumference}}{\text{speed}}$
### Revolutions per second $N$
- Each revolution covers an angle of $2\pi$
- $\omega = 2\pi N$
- $v = \omega R = 2\pi NR$
- Also, $N = \frac{1}{T}$