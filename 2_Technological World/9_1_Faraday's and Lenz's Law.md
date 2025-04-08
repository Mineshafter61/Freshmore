# 9_1_Faraday's and Lenz's Law

- Changing magnetic flux across a conductor induces a current in the conductor
$$I_{\text{induced}}\propto\frac{d\Phi_{B}}{dt}$$

## Magnetic Flux through a Surface/Loop

- For uniform $\vec{B}$,
$$\Phi_{B}=B\perp A=B A\cos(\theta)={\vec{B}}\cdot{\vec{A}}$$
- For non-uniform $\vec{B}$ or irregular surface area,
$$\Phi_{B}=\iint_S{\vec{B}}\cdot d{\vec{A}}$$
- Rate of change of magnetic flux
$$I_{induced}\propto\frac{d\Phi_B}{dt}=\frac{d}{dt}\iint_S{\vec{B}}\cdot d{\vec{A}}$$

## Electromotive Force, $\epsilon$

- Current is due to moving charge accelerated by **electric field** in the space where magnetic flux is changing
- Work done per unit charge by the electric field, EMF is given by
$$\epsilon=\oint\vec{E}\cdot d\vec{s}$$
- EMF is caused by a **non-conservative field**, closed path integral is **not 0** unlike the electrostatic field.
- Therefore, Faraday’s law also states that the emf around a loop is proportional to the rate of change of magnetic flux coupled to the loop.
$$\oint\vec{E}\cdot d\vec{s}\propto\frac{d}{dt}\iint_S{\vec{B}}\cdot d{\vec{A}}$$

## Lenz's Law

- The EMF associated with changing magnetic flux around the loop is in direction that **opposes the change** in magnetic flux coupled to the loop.
$$\epsilon=-\frac{d\Phi_B}{dt}$$
- **Final law**
$$\oint\vec{E}\cdot d\vec{s}=-\frac{d}{dt}\iint_S\vec{B}\cdot d\vec{A}$$
- Directions of $d\vec{s}$ and $d\vec{A}$
    - If $d\vec{s}$ is chosen in the clockwise direction, $d\vec{A}$ is pointing into the page by the right hand rule.
    - Magnetic flux is **positive** if $\vec{B}$ is into the page, and **negative** if $\vec{B}$ is out of the page.
    - $-\frac{d}{dt}\iint_S\vec{B}\cdot d\vec{A}>0$ implies $\vec{E}$ and $d\vec{s}$ are in the **same direction**, otherwise $\vec{E}$ and $d\vec{s}$ are in the **opposite direction**.
    - Current induced by magnetic field is **opposite** to the cross product directions that give the magnetic field.
- Directions in terms of magnets: *Induced magnetic field* created by *induced current* always form poles that **oppose** the **change** in the original magnetic field
    - Pulling apart forms N-S to attract
    - Pushing together forms N-N or S-S to repel
    - Use right hand rule to determine current
