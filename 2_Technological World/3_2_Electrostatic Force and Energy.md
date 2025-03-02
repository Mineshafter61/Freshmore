## Work Done by Electrostatic Force
- Work done by electrical force moving $q_t$ from point A to B is
$$
W_e=\int_A^B \vec{F}_{st}\cdot d\vec{s}=\int_A^B k_e \frac{q_sq_t}{r_{st}^2}\hat{r}_{st}\cdot d\vec{s}
$$
- If $\vec{F}$ is in the same direction as the displacement $d\vec{s}$, W is positive and vice versa.
- The direction of displacement $d\vec{s}$ is determined by the limits of the integral.
	- Recall: For polar coordinates, $ds = dr\,\hat{r} + r\,d\theta\,\hat{\theta}$
## Electrostatic Potential Energy and Configuration Energy
### Gravity vs Electrostatics
| Mass M | Charge q |
| --- | --- |
| $\vec{g}=-G \frac{M}{r^2}\hat{r}$ | $\vec{E}=k_e \frac{q_s}{r^2}\hat{r}$ |
| $\vec{F}_g=-G\frac{Mm}{r^2}\hat{r}=m\vec{g}$ | $\vec{F}_E=k_e \frac{q_sq_t}{r^2}\hat{r}=q\vec{E}$ |
| $\Delta U_g=-\int_{A}^{B} \vec{F}_g\cdot d\vec{s}$ | $\Delta U_E=-\int_{A}^{B} \vec{F}_E\cdot d\vec{s}$ |
| $\Delta V_g=-\int_{A}^{B} \vec{g}\cdot d\vec{s}$ | $\Delta U_E=-\int_{A}^{B} \vec{E}\cdot d\vec{s}$ |
- $\vec{g}$ is gravitational acceleration, equivalent to gravitational field. (analogous to electric field)
- $V_E$ is the **electric potential** while $U_E$ is the **electric potential energy**
### Work done, Kinetic and Potential Energy
- The work done by the electric field is
$$
W=q \int_A^B \vec{E} \cdot d\vec{s}
$$
- As this work is done by the field, the change of kinetic energy must be equal to W.
$$
W=\Delta K
$$
- If the total energy of the system is conserved, $\Delta U+\Delta K=0$, thus we have the change of potential energy equal to
$$
\begin{gather*}
\Delta U=-\Delta K=-W\\
\Delta U=-q \int_A^B \vec{E} \cdot d\vec{s}
\end{gather*}
$$
### Potential Energy Difference $\Delta U$
- In polar coordinates,
$$
\Delta U = U_B - U_A = -W = -\int^B_A \vec{F}_{st} \cdot d\vec{s} = k_eq_sq_t(\frac{1}{r_B} - \frac{1}{r_A})
$$
- At $r = \infty$, $U(\infty) = 0$
### Configuration Energy
- The potential energy stored in any configuration of charged objects is the sum of its **potential energy $\Delta U$**
	- Kinetic energy $\Delta K$ is 0 as the process is **time independent**
	- $t = \infty \implies v = s/t = 0 \implies \Delta K = 0$
- Configuration energy is the potential energy stored in a configuration of charged objects. It is also the energy needed to form such a configuration.
1. Start from infinity, choose $U(\infty) = 0$, bring in the first charged object. Because there is no external electric field,
$$
\Delta U_1 = 0
$$
2. Bring in the second charged object. It will be affected by field created by the first charged object
$$
\Delta U_2 = U_{12} = \frac{k_eq_1q_2}{r_{12}}$$
3. Bring in the third charged object. It will be affected by **both** the fields created by the first and second charged objects
$$
\Delta U_3 = U_{12} = \frac{k_eq_1q_2}{r_{12}}$$