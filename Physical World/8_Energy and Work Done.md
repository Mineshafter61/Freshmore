## Energy
- System: single object or a collection of objects
- State of system: position and momentum
- Energy: scalar quantity, not part of the state of the system
- Energy changes the characteristics of a system and/or affects the ability of the system to do work
- Energy can be transformed from one form to another
- Within an isolated system (first law of thermodynamics):
	- energy cannot be created or destroyed
	- energy can only be transformed from one form into another.
	- summing up all the changes in the energy forms that can be accounted for, the net change of total energy is zero.
	- $\displaystyle\sum_{i=1}^N \Delta E_i=\Delta E_1+\Delta E_2+\dots=0$
- Energy conservation problems
	1. Define the system properly, for which the total energy can be accounted for.
	2. Focus on the initial and final conditions and states of the system.
	3. Time is an invariant: total energy is a conserved quantity at each instant.
## Work-Kinetic Energy Theorem
- Work done $W$ by a constant force $F$, in displacing an object by $\Delta x$ is equal to $W=F\Delta x=\frac{1}{2}mv^2-\frac{1}{2}mu^{2}$ (**THIS IS TRUE FOR ALL PATHS**)
- **Linear kinetic energy**, $K=\frac{1}{2}mv^2=\frac{1}{2}m\vec{v} \cdot \vec{v}$
	- Reference frame-dependent
- **Work-Kinetic Energy Theorem** states that the work done by a net force in displacing ab object is equal to the change in kinetic energy of the object, i.e. $W=F_{net}\Delta x=\Delta K$
- **Rotational kinetic energy**, $K=\frac{1}{2}I\omega^2$
- Total work done by a variable force: $W=\int \vec{F}\,d\vec{r}$
- If $\vec{F}$ is a constant, $W=\vec{F}\cdot \int d\vec{r}=\vec{F}\cdot \Delta \vec{r}$
- In one dimension: $W=\int F\,dr$
- $W_{net}=\int \vec{F}_{net}\cdot d\vec{r}=\int\vec{F}_{1}\cdot d\vec{r}+\int\vec{F}_{2}\cdot d\vec{r}+\dots=\Delta K$
## Work Done
- Work Done is NOT a form of energy although its unit is Joules
- Transfer of energy into/out of a system.
- Force must be **continuously applied** for it to be considered work done
	- Pushing yourself from a wall is **not** work done by Normal contact force even if you get moved backwards
	- Jumping up is **not** work done by contact force of floor on your legs as it does not apply to you all the way up, it is momentum carrying you up
	- Gravity pulling you down **is** work done because it is continually applied on your way down
- Work done is the **area under a force-position graph** $$W = \lim_{ N \to \infty } \sum_{i=0}^{N} \vec{F}(\vec{r}_{i}) \cdot \Delta \vec{r}_{i}= \int_{\vec{r}_0}^{\vec{r}_f} \vec{F}(\vec{r}) \, d\vec{r}$$
- Note: $d\vec{r}=dx\hat{i}+dx\hat{j}=dr\hat{r}+rd\theta\hat{\theta}$
## Conservative Forces
- **Conservative Force**: If the work done by a force in **moving an object** from an initial point $\vec{r}_{i}$ to a final point $\vec{r}_{f}$ is **independent of the path**, then the force is called a **conservative force**. 
- Equivalently, net work done by a conservative force after going through a close path $(\vec{r}_{f}=\vec{r}_{i})$, i.e. $\oint \vec{F}_c \cdot d\vec{r}=0$
### Work Done by Conservative Force
- If the force is a **conservative force** $F_C$, the **change in potential energy** $\Delta U$, is the **negative** of the work done
$$
\Delta U=-W_C\implies U_B-U_A=-\int_{A}^{B}\vec{F}_C \cdot d\vec{r}\
$$
- Negative sign is required for potential energy due to the law of Conservation of Energy (C.O.E)
$$
\Delta W = \Delta K + \Delta U = 0
$$
### Work Done by Non-conservative Force
- Loss of mechanical energy (i.e heat loss due to **kinetic** friction)
$$
W_{net} = \int F_{net} \cdot d{\vec{r}} = \int (F_{C} + F_{NC}) \cdot d{\vec{r}} \\
\int F_{net} \cdot d{\vec{r}} = \int F_{C} \cdot d{\vec{r}} + F_{NC} \cdot d{\vec{r}} \\
\Delta K = -\Delta U + \int F_{NC} \cdot d{\vec{r}} \\
\Delta (K + U) = \int F_{NC} \cdot d{\vec{r}} \\
\Delta (K + U) = W_{NC}
$$
- $\Delta (K + U) = 0$ if there are **no** non-conservative forces (i.e no loss of mechanical energy)
### Solving Energy Problems
1. Identify **all sources** of energy in the **initial** state (GPE, KE, EPE, etc)
2. Identify **all sources** of energy in the **final** state
3. By C.O.E, $E_{initial} = E_{final} + |E_{loss}|$
### Conservative force and potential energy
- The conservative force is related to the potential energy function by $F_x=-\frac{dU}{dx}$
- 3D version: $\vec{F}=-\nabla U=\frac{\partial}{\partial x}\hat{i}+\frac{\partial}{\partial y}\hat{j}+\frac{\partial}{\partial z}\hat{k}$