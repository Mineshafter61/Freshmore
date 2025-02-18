## Electric field
- 'Mediator' of the electric forces between charges
- Electric force per unit charge
- The electric field at a point $P$ due to a source point charge $q_s$ is the force acting on a test point charge $q_t$ at the point $P$, divided by the charge $q_t$:
	- $\displaystyle\vec{F}_{st}(P)=q_t\vec{E}_s(P)= k_e \frac{q_{s}q_{t}}{r^2_{st}}\hat{r}_{st}$
	- $\displaystyle\implies\vec{E}_s(P)=\frac{1}{q_t} k_e \frac{q_sq_t}{r_{st}^2}\hat{r}_{st}$
	- $\displaystyle\implies\vec{E}_s(P)=k_e \frac{q_s}{r_{st}^2}\hat{r}_{st} = k_e \frac{q_s}{r_{st}^3}\vec{r}_{st}$
## Superposition Principle
- Since electric field is linear to the charge, the electric field due to a collection of $N$ point charges is the vector sum of the individual electric fields due to each charge.
	- $\displaystyle\vec{E}_i(P)=k_e \frac{q_i}{r_{iP}^2} \hat{r}_{iP}$
	- $\displaystyle\vec{E}(P)=\sum_{i=1}^{N}\vec{E}_{i}(P)=\sum_{i=1}^{N}k_e \frac{q_i}{r_{iP}^2} \hat{r}_{iP}$
- If there is a point charge $q$ at point $P$, the point charge experiences a force of
	- $\displaystyle q\vec{E}(P)=\sum_{i=1}^{N}q\vec{E}_{i}(P)=\sum_{i=1}^{N}k_e \frac{q\,q_i}{r_{iP}^2} \hat{r}_{iP}$
## Electric field lines
- We can construct electric field lines by joining the electric field vectors at each location in space to form smooth lines.
- The direction of $\vec{E}$ at any point is tangent to the field lines
- The field lines **begin on positive charges** (or at infinity) and **terminate on negative charges** (or at infinity)
	- Positive charges (**sources**) have field lines spreading outward.
	- Negative charges (**sinks**) have field lines converging in on themselves.
- The denser the line, the greater the magnitude of $\vec{E}$
- No two field lines can cross each other
- Field lines do not indicate the motional trajectory of a charge
- It shows the direction of **acceleration** at any point in time
## Electric dipole
- Two equal but opposite charges separated in space
- Electric dipole moment: $$\vec{P}\equiv qr\,\hat{r}=q\vec{r}=q(\vec{r}_{2}-\vec{r}_{1})=q\vec{r}_{2}-q\vec{r}_{1}=q_{2}r_{2}+q_{1}r_{1}=\sum_{i=1}^{2}q_i\vec{r}_i$$
	- $\vec{r}_{1}$ : distance between an arbitrary point and the negative charge
	- $\vec{r}_{2}$ : distance between an arbitrary point and the positive charge
- If there are N charges in a neutral charge body, the dipole moment is $$\vec{P}=\sum_{i=1}^{N}q_i\vec{r}_i$$
- $\vec{P}$ points from negative to positive charge
- Unit: mC
## Electric Field Pattern of an Electric Dipole
- Onion ring-shaped pattern
- Field is due to the superposition of the electric fields contributed by the positive and negative charge in the dipole.
- For the far field region, a dipole can be approximated as a point dipole.
- Electric field at point $P$, $\vec{E}_P=\frac{k_eqd}{x^3}(-\hat{j})=\frac{k_eP}{x^3}(-\hat{j})$
- TODO: Proof of Point Dipole Approximation (1st order Taylor series expansion) ![[TW_point dipole approximation.png]]
## Force & Torque on Electric Dipole in Electric Field
- Force in a uniform field
	- Let $\vec{E}=E\hat{i}$
	- $\vec{r} \equiv 2a (\cos \theta \hat{i}+\sin \theta \hat{j})$
	- $\vec{p}\equiv \vec{r}q=2qa(\cos \theta \hat{i}+\sin \theta \hat{j})$
	- Total net force in a uniform field: $\vec{F}_{net}=\vec{F}_{+}+\vec{F}_{-}=q\vec{E}+(-q)\vec{E}=0$
- Torque on Dipole (w.r.t. to negative charge $-q$)
	- $\vec{\tau}=\vec{r}\times \vec{F}=\vec{r}\times q\vec{E}=q\vec{r}\times \vec{E}=\vec{p}\times \vec{E}$
- Force in a non-uniform field
	- Dipole experiences a force
### Continuous charge distribution
$$
\vec{E} = \int_{body} k_e \frac{dq}{|\vec{r}|^2} \hat{r} = \int_{body} k_e \frac{dq}{|\vec{r}_p - \vec{r}_s|^3}(\vec{r}_p - \vec{r}_s)
$$
- $\vec{r}_p$ is a constant point of interest
- $\vec{r}_s$ represents every single charge point in the body
- **It is the variable to be used in integration ($x$)**
- Similar to moment of inertia
### Charge Density
- Linear density = $\frac{\text{charge}}{\text{length}} \implies \lambda = \frac{Q}{L} \implies dq = \lambda dl$
- Surface density = $\frac{\text{charge}}{\text{area}} \implies \sigma = \frac{Q}{A} \implies dq = \sigma dA$
- Volume density = $\frac{\text{charge}}{\text{volume}} \implies \rho = \frac{Q}{V} \implies dq = \rho dV$