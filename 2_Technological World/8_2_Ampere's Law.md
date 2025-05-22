# 8_2_Ampere's Law

Consider a closed path of a circle of radius $r$ around a long current carrying wire. For an infinite wire with current $I$, the magnetic field is
$$
\begin{align*}
\vec{B} &= \frac{\mu_0I}{2\pi R}\hat{\theta} \\ \implies \oint \vec{B}\cdot d\vec{s} &= \oint \frac{\mu_0I}{2\pi R}\hat{\theta} \cdot rd\theta\hat{\theta} \\&= \oint \frac{\mu_0I}{2π} d\theta \\&=\frac{\mu_0I}{2π}(2π) \\&= \mu_0I
\end{align*}
$$

For a more complicated closed path where $\oint \vec{B}\cdot d\vec{s}=\int_{ab} \vec{B}\cdot d\vec{s}=\int_{bc} \vec{B}\cdot d\vec{s}=\int_{cd} \vec{B}\cdot d\vec{s}=\int_{da} \vec{B}\cdot d\vec{s}$,

- Radial path $ab$: $\int_{ab} \vec{B}\cdot d\vec{s}=0$
- Radial path $cd$: $\int_{cd} \vec{B}\cdot d\vec{s}=0$
- Circular arc path $bc$: $\int_{bc} \vec{B}\cdot d\vec{s}=\frac{\mu_0I}{2π} \theta$
- Circular arc path $bc$: $\int_{da} \vec{B}\cdot d\vec{s}=\frac{\mu_0I}{2π} (2π-\theta)$
- Total path: $\oint \vec{B}\cdot d\vec{s}=\mu_0I$
- **Insight (Ampere's Law): all closed paths (Amperian loop) result in $\oint \vec{B}\cdot d\vec{s}=\mu_0I_{enc}$**
- $I_{enc}$ is positive by the **Right-Hand Rule**

Note: Even though Ampere’s Law is always true, it is only useful to find a magnetic field when a system possesses certain symmetry:

- infinitely long straight wire
- infinitely large sheet
- infinite solenoid
- toroid

## Current density and current

- Current density $\vec{J}$ is a **vector** but current $I$ is a **scalar**.
- Current density $\vec{J}$: amount of equivalent positive charge passing through a unit perpendicular area per unit time
- If the perpendicular surface area that the uniform current density $J$ is passing through is $A$, then the total current is $I=\pm JA$.
- For uniform current density $\vec{J}$ flowing through an arbitrary plane $\vec{A}$, current is $I=\vec{J}\cdot\vec{A}$, or $I=JA\cos\theta$.
- If current density is not uniform,
$$I=\iint \vec{J}\cdot d\vec{A}$$
- Therefore, Ampere's law becomes
$$\oint \vec{B}\cdot d\vec{s}=\mu_0\iint_{\text{open surface}} \vec{J}\cdot d\vec{A}$$
- Calculating $B$ field:
    - $\oint d\vec{s}=2πr$
    - $\iint dA = \int 2\pi r dr$, express $dA$ in terms of $dr$
    - Perform integration to express $B$ in terms of $r$ and $J$
- Note: an open surface is always bounded by a closed boundary.
- Use right hand rule to determine sign of current
    - If the direction of $\vec{J}$ (fingers) and the normal $\hat{n}$ (thumb) to the plane $\vec{A}$ are in the **same direction**, the current is **positive**.
    - If the directions are **opposite**, the current is **negative**.

## Magnetic field of ideal solenoid

- Infinitely long solenoid, no way for magnetic field to loop back
- All magnetic field is within the solenoid, where $n = \frac{N}{L}$ which is the # of turns per unit length

$$
\begin{align}
\oint \vec{B}\cdot d\vec{s}&=\mu_0I_{\text{enc}} \\
Bl &= \mu_0 nlI \\
B &= \mu_0nI
\end{align}
$$

## Magnetic field of a toroid

Toroid: a coil wound into a torus.
$$
\oint \vec{B}\cdot d\vec{s}=\oint B\,ds=B\oint ds=B(2πr)=\mu_0I=\mu_0 NI
$$
Therefore,
$$
B=\frac{\mu_0 NI}{2πr}
$$
