- Definition: special case of two-dimensional motion in which the object maintains a constant distance away from a fixed point.
- Position vector at any point in circular motion: $\vec{r}=R\hat{r}$
## Calculus
- Product rule: $\displaystyle\frac{d(uv)}{dt} = \frac{du}{dt}v+\frac{dv}{dt}u$
- Chain rule: $\displaystyleθ(t), f(θ): \frac{df}{dt} = \frac{df}{dθ} \frac{dθ}{dt}$
> $\displaystyle\sin θ:  \frac{d \sinθ}{dt} = \frac{d \sin θ}{dθ} \frac{dθ}{dt} = \cos θ \frac{dθ}{dt}$
> $\displaystyle\cos θ:  \frac{d \cosθ}{dt} = \frac{d \cos θ}{dθ} \frac{dθ}{dt} = -\sin θ \frac{dθ}{dt}$

> $\displaystyle\hat{r}=\cos θ \hat{i}+\sin θ \hat{j}$
> $\displaystyle\frac{d\hat{r}}{dt}=-\sin θ \frac{dθ}{dt} \hat{i} + \cos θ \frac{dθ}{dt} \hat{j}= \frac{dθ}{dt}(-\sin θ \hat{i}+\cos θ \hat{j})$
> $\displaystyle\frac{d\hat{r}}{dt}=\frac{dθ}{dt}\hat{θ}$

> $\displaystyle\hat{θ} = -\sin θ \hat{i}+\cos θ \hat{j}$
> $\displaystyle\frac{d\hat{θ}}{dt}=-\cos θ \frac{dθ}{dt}\hat{i}-\sin θ\frac{dθ}{dt}\hat{j}= \frac{dθ}{dt}(\cos θ \hat{i}+\sin θ \hat{j})$
> $\displaystyle\frac{d\hat{θ}}{dt}=-\frac{dθ}{dt}\hat{r}$

## Physics
- Position vector: $\vec{r} = R\hat{r}$
- Velocity vector: $\displaystyle\vec{v}=\frac{d\vec{r}}{dt}=\frac{d(R\hat{r})}{dt}=R \frac{d\hat{r}}{dt}= R \frac{dθ}{dt}\hat{θ}$
	- Direction of $\vec{v}$ is $\hat{θ}$
	- Angular speed, $\displaystyle \omega:=\frac{dθ}{dt}$
	- $\vec{v}=R\omega \hat{θ}$, where $\displaystyle\omega=\frac{dθ}{dt}$
- Acceleration $\displaystyle\vec{a}=\frac{d\vec{v}}{dt}=\frac{d}{dt}\left( R \frac{dθ}{dt} \hat{θ} \right)=R \frac{d}{dt}\left( \frac{dθ}{dt} \hat{θ} \right)$
	- $\displaystyle=R\left[ \frac{d}{dt}\left( \frac{dθ}{dt} \right) \right]\hat{θ}+R\frac{dθ}{dt}\left( \frac{d\hat{θ}}{dt} \right)$
	- $\displaystyle=R \frac{d^2θ}{dt^2} \hat{θ} + R\left( \frac{dθ}{dt} \right)^2(-r^2)$
	- Tangential acceleration: $R \frac{d^2θ}{dt^2} \hat{θ}$
	- Centripetal acceleration: $R\left( \frac{dθ}{dt} \right)^2(-r^2)$

### Accelerations
- Tangential acceleration, $\vec{a}_{θ}$
	- Direction of $\vec{a}_{θ}$ is $\hat{θ}$
	- Increases/decreases the speed
	- Define angular acceleration $\alpha := \frac{d^2θ}{dt^2} \text{or} \frac{d\omega}{dt}$; unit: $rad.s^-2$
- Centripetal acceleration, $\vec{a}_{r}$
	- Direction of $\vec{a}_{r}$ is $-\hat{r}$
	- Changes the direction of $\vec{v}$
	- $|\vec{a_{r}}| = R\left( \frac{dθ}{dt} \right)^2 = R\omega ^2=\frac{v^2}{R}$
- $\vec{a}=\vec{a}_{θ}+\vec{a}_{r}=R\alpha \hat{θ} + R\omega^2(-\hat{r})=\frac{v^2}{R}(-\hat{r})$

## Uniform circular motion
- In a **uniform circular motion**, there is **no tangential acceleration**.
- Centripetal acceleration is $\vec{a_{r}}=-|a_{r}|\hat{r}$, or
	- $\vec{a_{r}}=-v\omega \hat{r}=-\frac{v^2}{R}\hat{r}=-\omega^2R\hat{r}$
- Direction of velocity is constantly changing due to the **centripetal acceleration**.
## Nonuniform circular motion
- If the speed is time-varying, the motion is a nonuniform circular motion.
- Radial (centripetal acceleration is time-varying):
	- $\vec{a_{r}} (t) = -\frac{v^2(t)}{R}\hat{r}$
- There is also a tangential acceleration component $\hat{a_{θ}}(t)$ that is **parallel** to the instantaneous velocity.
- Total acceleration:  $\vec{a}(t)=\vec{a_{r}}(t)+\vec{a_{θ}}(t)$
## Summary of formulae
- Arc length and angular displacement: $s = Rθ$
- Tangential velocity and angular speed: $\vec{v}=\frac{d\vec{s}}{dt}=R \frac{dθ}{dt} \hat{θ} = R\omega \hat{θ}$
- Tangential acceleration: $\vec{a}_{θ}=\frac{d|\vec{v}|}{dt}\hat{θ}=R \frac{d^2θ}{dt^2}\hat{θ}=R\alpha \hat{θ}$
- Radial (centripetal) acceleration: $\vec{a}_{r}=-v\omega \hat{r}=-\frac{v^2}{R}\hat{r}=-R\omega^2\hat{r}$
- Angular speed: $\omega=\frac{dθ}{dt}$
- Angular acceleration: $\alpha=\frac{d\omega}{dt}=\frac{d^2θ}{dt^2}$
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