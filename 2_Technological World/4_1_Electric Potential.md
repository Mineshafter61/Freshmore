## Electric Potential Difference, $\Delta V$
- Change in potential energy per unit test charge moving from point A to B:
$$\Delta V\equiv\frac{\Delta U}{q_t}=-\int_{A}^{B} \frac{\vec{F}}{q_t} \, d\vec{s}= -\int_{A}^{B} \vec{E} \, d\vec{s}$$
	- Units: Joules/Coulomb = Volts
	- The negative sign is important. It exists from the definition, $\Delta U=-W_e$
	- Potential difference is a scalar quantity.
	- It tells you the potential energy difference of a charge $q_t$ between 2 points.
	- Also known as voltage.
- Force on a charged particle $q$ by electric field $\vec{E}$: $\vec{F}=q\vec{E}$
- Potential energy change of $q$ when it is moved over a displacement of electric potential $\Delta V$: $\Delta U=q\Delta V$.
- If there is no external force acting on the particle over the displacement, kinetic energy change $\Delta K=-\Delta U$.
- If there is an external force acting on the system, $\Delta K+\Delta U=W_{ext}$, where $W_{ext}$ is the work done by the external force.
	- Total energy of the system is increased due to $W_{ext}$.
- If the kinetic energy remains over the displacement, $W_{ext}=\Delta U=q\Delta V$.
	- Work done by the external force converts to the potential energy stored in the system.
- $\Delta V$ does not depend on $q_t$
## Electric Potential Field of a Continuous Charge Body
### Continuous charge distributions
1. Break the continuous charge distribution into infinitesimal charged elements, each of charge $dq$. Electric potential difference between infinity and $P$ due to $dq$.
2. $dV\equiv V_{dq}(P)-V_{dq}(\infty)=k_e \frac{dq}{r}$
3. Note: $r$ is the distance from $dq$ to the point of interest, $P$.
4. By superposition principle: $V(P)-V(\infty)=k_e \int \frac{dq}{r}$
5. We usually set the infinity as the reference point to have zero potential: $V(\infty)=0$
6. Thus, the potential at point $P$ due the continuous charge body: $V(P)=k_e \int \frac{dq}{r}$

#### For calculations:
1. Choose $V(\infty)=0$
2. From the continuous charge, choose a small $dq$. Identify the $dq$ position from the origin, $\vec{r}_s$.
3. Identify and relate $dq$ with geometry, $dq=\begin{cases}\lambda ds: 1D\\\sigma dA:2D\\\rho dv:3D\end{cases}$
4. Identify the position of point of interest $P$, $\vec{r}_p$.
5. Calculate the distance from $dq$ to point $P$, $|\vec{r}_p-\vec{r}_s|$
6. Electric potential due to $dq$ is $dV=k_e \frac{dq}{|\vec{r}_p-\vec{r}_s|}$
7. Identify the limits of the integral and integrate $V(\vec{r})=k_e \int \frac{dq}{|\vec{r}_p-\vec{r}_s|}$
### Electric Potential Difference from Electric Field (Gauss’s Law)
- If the charge distribution is highly symmetric, we can use Gauss’s Law to calculate the electric field first. 
- Then, we calculate the electric potential $V$ using this relation:
$$V_B-V_A=-\int_A^B \vec{E}\cdot d\vec{s}$$
- Useful for highly symmetrical charge distributions
- **Unlike for electric field, there cannot be a discontinuity in electric potential**
## Properties of equipotential lines
- E field lines point from high to low electric potential.
- E field lines is always perpendicular to equipotential lines.
- E field has no component along equipotential lines.
	- No E field implies equipotential!
- The electrostatic force does zero work to move a charged particle along an equipotential line.
- Conductors are equipotential surfaces
## Deriving E from V
- Where $A = (x,y,z)$, $B = (x + \Delta x,y,z)$ and $\Delta \vec{s} = \Delta x\hat{i}$,
$$
\Delta V = -\int^B_A \vec{E} \cdot d\vec{s}
$$
- Therefore,
$$
E_x = -\frac{\Delta V}{\Delta x} = -\frac{\partial V}{\partial x}
$$
- Combining all directions together,
$$
\begin{align*}
\vec{\nabla}&\equiv \frac{\partial}{\partial x}\hat{i}+\frac{\partial}{\partial y}\hat{j}+\frac{\partial}{\partial z}\hat{k} \\
\vec{E}&=-\left(\frac{\partial}{\partial x}\hat{i}+\frac{\partial}{\partial y}\hat{j}+\frac{\partial}{\partial z}\hat{k}\right)V=-\vec{\nabla}V
\end{align*}
$$
- Electric field is the **negative** gradient of electric potential
	- Cannot be derived from electric potential from only one point