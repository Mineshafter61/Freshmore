## Displacement
- difference of 2 positions in space
- vector quantity [[1_Vectors]]
- Displacement vector: difference between two position vectors
- Always smaller than or equal to distance
## Velocity
- Change in displacement over time
- Average velocity: $\frac{\Delta\vec{r}}{\Delta t} = \frac{\vec{r}(t_2) - \vec{r}(t_1)}{t_2 - t_1}$
- Instantaneous velocity: $\frac{d\vec{r}(t)}{dt}$
- Constant velocity: average velocity = instantaneous velocity
## Acceleration
- Change in velocity over time
- Average velocity: $\frac{\Delta\vec{v}}{\Delta t} = \frac{\vec{v}(t_2) - \vec{v}(t_1)}{t_2 - t_1}$
- Instantaneous velocity: $\frac{d\vec{v}(t)}{dt}$
- Constant acceleration: average acceleration = instantaneous acceleration
### Graphs and equations
- Area under acceleration vs time curve is the CHANGE in velocity:
> (t' is a dummy variable)
> $\frac{dv(t)}{dt} = a(t)$
> $\implies \int_{t_0}^t \frac{dv(t')}{dt'} dt' = \int_{t_0}^t a(t') dt'$
> $\implies \int_{t_0}^t dv(t') = \int_{t_0}^t a(t') dt'$
> $\implies v(t) - v_0 = \int_{t_0}^t a(t') dt'$

- Area under velocity vs time curve is the CHANGE in displacement:
> (t' is a dummy variable)
> $\frac{ds(t)}{dt} = v(t)$
> $\implies \int_{t_0}^t \frac{ds(t')}{dt'} dt' = \int_{t_0}^t v(t') dt'$
> $\implies \int_{t_0}^t ds(t') = \int_{t_0}^t v(t') dt'$
> $\implies s(t) - s_0 = \int_{t_0}^t v(t') dt'$
## Reference Frames
Let:
- $\vec{R}$ be relative displacement
- $\vec{V}$ be relative velocity
- $\vec{A}$ be relative acceleration
- $\vec{r_1}$ be the distance from Reference Frame 1 to the object
- $\vec{r_2}$ be the distance from Reference Frame 2 to the object
- $\vec{v_1}$ be the velocity of the object with respect to Frame 1
- $\vec{a_1}$ be the acceleration from reference frame 1 to the object
From the vector triangle:
> $\vec{R} = \vec{r_1} - \vec{r_2}$
- $\vec{r}_{a, b}$ is  the displacement vector of Frame $a$ w.r.t Frame $b$ (reference point)
### Law of Velocity Addition (Galilean Transformation)
- Observers in different reference frames will measure different velocities for an object if the relative velocities of the frames $\vec{V} = \frac{d\vec{R}}{dt}$ is **not zero**.
	- In other words, if two reference frames are moving with respect to (collinear) to each other, the measured velocity of the object will be different.

- By differentiating the original relative position equation by $t$, we obtain:
> $\vec{V} = \vec{v}_1 - \vec{v}_2$ (first derivative)
> $\vec{A} = \vec{a}_1 - \vec{a}_2$ (second derivative)

- If the relative velocity $\vec{V}$ between 2 reference frames is **constant**, relative acceleration
> $\vec{A} = \frac{d\vec{V}}{dt} = \frac{d^2\vec{R}}{dt^2} = 0$

- These 2 frames are known as **inertial reference frames**

> Tip: always start with the position vector triangle

## Kinematics Equations
**General Equations:** 
- Only works for **constant** acceleration
- **Take integral for non-constant acceleration**
- No acceleration $a$ given: $s = \frac{v + u}{2}t$
- No displacement $s$ given: $v = u + a\Delta t$
- No final velocity $v$ given: $s = ut + \frac{1}{2}at^2$
- No initial velocity $u$ given: $s = vt - \frac{1}{2}at^2$
- No time $t$ given: $v^2 = u^2 + 2as$

**Projectile Motion:**
- Acceleration in the x direction is 0
> $a_x=0$
> $\implies \frac{dv_x(t)}{dt} = 0$
> $\implies \int_{t_0}^t \frac{dv_x(t')}{dt'} dt' = 0$
> $\implies \int_{v_{x0}}^{v_x(t)} dv_x = 0$
> $\implies v_x(t)=v_{x0}$

> $v_x(t)=v_{x0}$
> $\implies \frac{dx(t)}{dt} = v_{x0}$
> $\implies \int_{t_0}^t \frac{dx(t')}{dt'} = \int_{t_0}^t v_{x0} dt'$
> $\implies \int_{x_0}^{x(t)} dx = \int_{t_0}^t v_{x0} dt'$
> $\implies x(t) = x_0 + v_{x0}(t-t_0)$

- Acceleration in the y direction is -g
> $a_y = -g$
> $\implies \frac{dv_y(t)}{dt} = -g$
> $\implies \int_{t_0}^t \frac{dv_y(t')}{dt'} dt' = \int_{t_0}^t -gdt'$
> $\implies \int_{v_{y0}}^{v_y(t)} = \int_{t_0}^t -gdt'$
> $\implies v_y(t)=v_{y0}-g(t-t_0)$

> v_y(t)=v_{y0}-g(t-t_0)
> $\implies \frac{dy(t)}{dt} = v_{y0} -g(t-t_0)$
> $\implies \int_{t_0}^t \frac{dy(t')}{dt'} dt' = \int_{t_0}^t [v_{y0} -g(t'-t_0)]$
> $\implies \int_{y_0}^{y(t)} dy = \int_{t_0}^t [v_{y0} -g(t'-t_0)]$
> $\implies y(t) = y_0 + v_{y0} (t-t_0) - \frac{g}{2}(t-t_0)^2$
- The above two equations implies the following:
> $v_y^2 = v_y0^2 - 2 g (y - y_0)$

- At a projectile's maximum height, the magnitude of its velocity is at the minimum (but not zero).

