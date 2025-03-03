# 4_2_Capacitance

- Conductor
  - Charges are free to move
  - Electrons are weakly bound to the atoms
- Insulator
  - Charges are not free to move
  - Electrons are strongly bound to atoms

## Capacitor

- Fundamental electrical component with two isolated conductors and an insulator
- Conductors are deposited with equal and opposite charges $\pm Q$
- Used to store charge and electrical energy
- If the potential difference between the two conductors is $\Delta V$, a constant called the capacitance $C$ is defined as the **ability to store charge**,

$$C=\frac{Q}{|\Delta V|}=\frac{\varepsilon_0A}{d}$$

- Units: Coulomb per Volt or Farad (F)
- $C$ is always **Positive**

## Parallel Plate Capacitor

- Simplest form of capacitor
- Usually assumed that the dimensions of the plates are very long as compared to the distance $d$ between the plates.
- Using gaussian surfaces, between the 2 plates

$$
E = 2 \cdot \frac{\rho}{2\varepsilon_0} = \frac{Q}{A\varepsilon_0}
$$

- Thus, potential difference between the 2 plates can be derived

$$
\Delta V = - \int^{\text{top}}_{\text{bottom}} \vec{E} \cdot d\vec{s} = Ed = \frac{Q}{A\varepsilon_0}d
$$

- Therefore, capacitance is

$$
C = \frac{Q}{|\Delta V|} = \frac{\varepsilon_0 A}{d}
$$

- Capacitance $C$ is only dependent on **geometric factors**
	- This means that $C$ may not be $\frac{\varepsilon_{0}A}{d}$ for other geometries, e.g. cylindrical (as seen below)
  - In this case, $A$ and $d$ for a parallel plate capacitor
  - $\varepsilon_0$ can be a different value with the use of **electrolytic capacitors**
    - Insulators (dielectrics) between the 2 plates instead of vacuum

### When disconnected from a battery

- We increase the separation distance $d$
- Charge $Q$ remains constant regardless of $d$
- As $d$ increases, $V = Ed$ increases

### When connected to a battery

- We increase the separation distance $d$
- Potential $V$ between the plates is constant (potential difference of battery)
- By $V = Ed$, $E \propto Q$, $E$ and $Q$ decreases

## Cylindrical Capacitor

- Length of capacitor: $L$
- Inner conductor's radius: $a$
- Outer conductor's radius: $b$

1. Choose our Gaussian surface to be a coaxial cylinder with length $\ell<L$ and radius $r$, $a<r<b$.
2. Using Gauss's law, we have $E=\frac{\lambda \ell}{2π\varepsilon_0r\ell}=\frac{\lambda}{2π\varepsilon_0r}$ (from [[3_1_Conductor at Equilibrium#Cylindrical symmetry]])
3. Potential difference $\Delta V=V_b-V_a=-\int_{a}^{b} E \, dr=-\int_{a}^{b} \frac{\lambda}{2π\varepsilon_{0}r} \, dr$
4. Since $\lambda$, $2π$ and $\varepsilon_0$ are all constants, the integration simplifies to $-\frac{\lambda}{2π\varepsilon_0}\int_{a}^{b} \frac{1}{r} \, dr=-\frac{\lambda}{2π\varepsilon_0}\ln\left( \frac{b}{a} \right)$.
5. Calculate capacitance $C=\frac{Q}{|\Delta V|}=\frac{\lambda L\,2π\varepsilon_0}{\lambda \ln(b/a)}=\frac{2π\varepsilon_0L}{\ln(b/a)}$

- For non-parallel plate capacitors, **always** derive the final formula from potential difference (by integration) and charge.
