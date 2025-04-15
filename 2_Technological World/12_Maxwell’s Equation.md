# 12_Maxwell’s Equation

- Applying Ampere’s Law to Capacitor (at charging state)
    - Source of emf is connected across a parallel-plate capacitor so that a time-dependent current $I$ develops in the wire. During the transient-state of charging a capacitor:
    - Using Ampere’s Law to calculate the magnetic field around path $P$,

$$
\oint_P \vec{B}\cdot d \vec{s}=\mu_0I_{enc}=\mu_0\iint_S \vec{J}\cdot d\vec{A}
$$

## Displacement Current

- There is a **changing $E$ field** between the two plates of a capacitor:

$$
\begin{align}
E=\frac{\sigma}{\epsilon_0}&=\frac{Q}{A\,\epsilon_0}\\
\epsilon_0 \frac{dE}{dt}A&=\frac{dQ}{dt} \\
\epsilon_0 \frac{d\Phi_E}{dt}&=\frac{dQ}{dt}=I_{dis}
\end{align}
$$

- $I_{dis}$ is **NOT** a flow of charges, but a quantity proportional to **changing electric flux**.
    - Same unit as current (ampere)
- If a gaussian surface $S$ encloses **all** the electric flux due to a charged plate, then it is equal to the conduction current
 $$I_\text{dis} = \epsilon_0\frac{d}{dt}\iint_S \vec{E} \cdot \, d\vec{A} = I_\text{con}$$

- Therefore, the Maxwell-Ampere's Law is given by

 $$\begin{align}
\oint_{C}\vec{B}\cdot d\vec{s}&=\mu_0\iint\vec{J}\cdot d\vec{A}+\mu_0\varepsilon_0\frac{d}{d t}\iint\vec{E}\cdot d\vec{A} \\
&= \mu_0I_\text{enc}+\mu_0\varepsilon_0{\frac{d\Phi_{E}}{d t}} \\
&= \mu_0(I_\text{enc} + I_\text{dis})
\end{align}
$$

- **The presence of a magnetic field in the space between the capacitor plates, implies a changing electric field, changing flux and hence changing current**
    - Current direction is determined by right hand rule
- Inside a **conductor**, the displacement current is **negligible**
- **Note: $E = \frac{V}{l}$ for long straight wire**
