# 3_1_Conductor at Equilibrium

## Conductors

- Ideal conductor: infinite supply of mobile charge carriers
- All charge carriers move without resistance

## Electric Fields & Conductors

- If an electric field is present inside a conductor, free charges will move around
  - Not an electrostatic condition
- The free charges in a conductor will redistribute themselves and stop moving
  - External and internal electric fields cancel each other
  - Now the conductor is in electrostatic equilibrium
  - The **net** electric field in a conductor is **zero**

## Electrostatic Equilibrium

- Tangential component of $\vec{E}$ is **zero** on the surface of the conductor
  - Otherwise, charges will move tangentially along the surface which is a non-static condition
- $\vec{E}$ can only be **normal** to the surface outside the conductor
  - Due to the different density of positive and negative charges at different points

1. No $\vec{E}$ field inside conductor
2. No net charge
3. $\vec{E}$ must be perpendicular to the surface
4. Net charge can only be on the surface

## Symmetrical Charge Distribution

- Simplified way to find $\vec{E}$ under **symmetric conditions**

### Conditions

1. Surface must be **perpendicular** to $\vec{E}$
2. Ensure $|\vec{E}| = E$ is **uniform** on the surface

- Gauss's Law simplifies to

$$
\oiint_{\text{G.S}} \vec{E} \cdot d\vec{A} = \pm EA_\perp = \pm\frac{Q_{\text{enclosed}}}{\varepsilon_0}
$$

#### Dipole

- No Gaussian surface
- E Field (outside) Strength: Falls off by $1/r^3$

#### Spherical Symmetry

- Gaussian surface: Concentric Sphere
- E Field (outside) Strength: $\vec{E} = k_e\frac{Q}{r^2}\hat{r}$
- Rotational symmetry about any axis through the centre of the charge sphere
- **Inside** the sphere, $Q \propto r^3$
- **Outside** the sphere, $Q \propto \frac{1}{r^2}$

$$
\begin{align*}
\oiint \vec{E}\cdot d\vec{A}&=\frac{Q_{enclosed}}{\varepsilon_0} \\
\implies \iint E(r)\,dA&=\frac{Q}{\varepsilon_0} \\
\implies E(r)\iint dA&=\frac{Q}{\varepsilon_0} \\
\implies E(r)\,4πr^2&=\frac{Q}{\varepsilon_0} \\
\implies E(r)&=\frac{Q}{4π\varepsilon_0 r^2}=k_e \frac{Q}{r^2} \\
\end{align*}
$$

#### Cylindrical symmetry

- Gaussian surface: Coaxial Cylinder
- E Field (outside) Strength: $\vec{E} = k_e\frac{\lambda}{2\pi\varepsilon_0r}\hat{r}$
- Rotational symmetry about the axis of the cylinder
- Translational symmetry along the axis of the cylinder
- Reflection symmetry about a perpendicular plane

$$
\begin{align*}
\oiint\vec{E}\cdot d\vec{A}&=\frac{Q_{enclosed}}{\varepsilon_0}\\
\implies E(r)2πrl&=\frac{Q_{enclosed}}{\varepsilon_0}\\
E(r)&=\frac{Q_{enclosed}}{\varepsilon_02πrl}
\end{align*}
$$

#### Planar symmetry

- Gaussian surface: Gaussian 'pillbox'
- E Field (outside) Strength: $\vec{E} = \pm\frac{\rho}{2\varepsilon_0}\hat{i}$ (Constant)
- Translational symmetry along any straight path
- Rotational symmetry about any axis perpendicular to the plane
- Reflection symmetry about the planar charged plane.

$$
\begin{align*}
\oiint\vec{E}\cdot d\vec{A}&=\frac{Q_{enclosed}}{\varepsilon_0}\\
\implies E(r)(2A_\perp)&=\frac{Q_{enclosed}}{\varepsilon_0}\\
\implies E(r)&=\frac{Q_{enclosed}}{\varepsilon_0 2A_\perp}
\end{align*}
$$
