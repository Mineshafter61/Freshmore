- Centre of Mass: A point where the **total mass of a system of objects or a continuous body appear to concentrate at**.
- The position of the centre of mass of a system can be described as the **average position** of the system's mass.
## Symmetrical objects
- Homogenous
- Symmetric object
- Centre of Mass is in its **geometric centre**
## Discrete bodies
- Total mass for collection of discrete bodies (system): $M_{sys}=\sum_{i=1}^{N}m_{i}$
- Position of centre of mass: $\vec{R}_{cm}=\frac{1}{M_{sys}}\sum_{i=1}^{N}m_{i}\vec{r}_{i}$
- Expression for the centre of mass can be interpreted as mass-weighted average.
- Split into $\hat{i}$ and $\hat{j}$ components
- Recall: Moment about CM is $0$ given no external forces
## Continuous bodies
- Similar to [[5_2_Rigid body#Calculating Moment of Inertia]]
- Position of centre of mass
$$
\begin{gather}
\vec{R}_{cm} = \frac{1}{M_{sys}}\int_{body}\vec{r} \, dm \\
\text{ where } dm =
\begin{cases}
\rho dV \text{ where } \rho \text{ is volume density, } dV \text{ is volume element} \\
\sigma dA \text{ where } \sigma \text{ is area density, } dA \text{ is area element} \\
\lambda ds \text{ where } \lambda \text{ is line density, } ds \text{ is length element} \\
\end{cases}
\end{gather}
$$
## Motion of centre of mass
$$
\begin{gather}
\vec{V}_{cm} = \frac{d\vec{R}_{cm}}{dt} = \frac{1}{M_{sys}}\sum_{i=1}^N m_i\vec{v}_i = \frac{1}{M_{sys}}\int_{body} \vec{v} \, dm \\
\vec{p}_{sys} = \sum_{i=1}^N m_i\vec{v}_i = \int_{body} \vec{v} \, dm \\
\vec{A}_{cm} = \frac{d\vec{V}_{cm}}{dt} = \frac{1}{M_{sys}}\sum_{i=1}^N m_i\vec{a}_i = \frac{1}{M_{sys}}\int_{body} \vec{a} \, dm
\end{gather}
$$
### Force on a N-body system
- Force on a system of particles is the **external force** because the internal force is $0$. $$\vec{F}_{total} = \vec{F}_{ext} + \vec{F}_{int} = \vec{F}_{ext} + 0 = \vec{F}_{ext}$$
- When a body is acted upon by external forces, the CM moves as though all mass were **concentrated**
- **Linear acceleration** of **CM** is **same** no matter what point the force is applied
### Extras
- If $\vec{F}_{ext}=0$, when an object splits into two, $m_{1}x_{1}=m_{2}x_{2}$
- $\int_{body}$ refers to $\int_{0}^{L}$ where L is the length of the rod for a 1D case.