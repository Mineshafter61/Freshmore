# 6_1_Magnetic Field and Force

## Magnetic Field and Field Lines

- Magnetic field ($B$) is a vector
- Unit: Tesla (T)
- Inside magnets, - Magnetic field lines must **connect** to form a circle
    - **Outside** the magnet, they point from North to South
    - **Inside** the magnet, they point from South to North magnetic field lines point **from south to north**.
- Maxwell's 2nd Equation states that **magnetic monopoles do not exist in isolation**, i.e. they are always **dipoles**.
    - Magnetic fields do not begin or end at any point
    - Number of B-field lines entering a closed surface = number of lines leaving the surface
- Magnets always rotates to orient with any external magnetic field.

## Gauss's Law for Magnetism

$$
\oiint\vec{B}\cdot d\vec{A}=0
$$

- Equation implies magnetic fields do not begin or end at any point.
- Number of B-field lines **entering a closed surface equals the number of lines leaving the surface**.
- The $0$ implies **no magnetic charge or magnetic monopole**.

## Magnetic Force on a Moving Charge (Lorentz Force)

$$
\vec{F}_{mag}=q\vec{v}\times \vec{B}
$$

- $\vec{F}_{mag}$ : **magnetic force**
- $q$ : charge
- $\vec{v}$ : velocity of the moving charge
- $\vec{B}$ : magnetic field
- Magnitude of the magnetic force on a charged particle:

$$
|\vec{F}_{mag}|=q|\vec{v}||\vec{B}|\sin \theta
$$

### Full Lorentz Force

- Electric force on charged particles in electric fields: $\vec{F}_{e}=q\vec{E}$
- Magnetic force on charged particles in electric and magnetic fields: $\vec{F}_{mag}=q\vec{v}\times \vec{B}$
- Putting it together, **Lorentz Force**:

$$
\vec{F}=q(\vec{E}+\vec{v}\times \vec{B})
$$

## Differences Between E-force and B-force

| Force | Direction | Motion | Work Done |
|---|---|---|---|
| Magnetic Force, $F_B$ | **Perpendicular** to magnetic field       | Acts only on **moving** charged particles                   | Steady state magnetic field does **no work** when a particle is displaced* |
| Electric Force, $F_E$ | **Along** the direction of electric field | Acts **regardless of state of motion** of charged particles | Does work in displacing a charged particle                                 |

- $F_B$ is perpendicular to the displacement
- When a charged particle moves with a velocity $v$ through a magnetic field, the field **can alter the direction of the velocity**, but **not the speed or the kinetic energy**.

## Magnetic Force on Current-Carrying Wire

- Magnetic force acting on a charge $dq$ : $d\vec{F}_{mag}=dq\vec{v}\times \vec{B}$
- Since $\vec{v}=\frac{d\vec{s}}{dt}$, $dq\vec{v}=dq\frac{d\vec{s}}{dt}=d\vec{s}\frac{dq}{dt}=d\vec{s}I$
- Hence, $d\vec{F}_{mag}=Id\vec{s}\times \vec{B}$

Thus, magnetic force acting on a current-carrying wire in a magnetic field, $d\vec{B}$ :
$$
\vec{F}_{mag}=\int Id\vec{s}\times \vec{B}
$$
If the wire is inside a uniform magnetic field, then
$$
\vec{F}_{mag}=I\left( \int_{wire} d\vec{s} \right)\times \vec{B}
$$
Note: **DO NOT** bring $\vec{B}$ outside if it is **not uniform**!

- If the wire is straight, the cross product of $\vec{B}$ and the unit vector along the wire is constant, hence we obtain

$$
\vec{F}_{mag}=I(\vec{L}\times \vec{B})
$$
where $\vec{L}$ is the length of the wire.

- **Important**: For a **closed current loop** in a **uniform magnetic field**, $\vec{F}_{mag}=0$
    - Only current perpendicular to the magnetic field contributes to the magnetic force
    - Vector sum of all magnetic forces cancel out

## Torque on a Current Loop

- For a loop of current, there is no net force by the magnetic field.
- However, there is torque (due to an imbalance of forces).
- The torque is calculated as follows:

$$
\vec{\tau}=I\vec{A}\times \vec{B}
$$

## Magnetic Dipole Moment, $\vec{\mu}$

- Formula:

$$
\vec{\mu}=I\vec{A}
$$

- Magnitude:

$$
|\vec{\mu}|=IA
$$

- Direction: The moment is perpendicular to the plane of the loop.
- Therefore, torque

$$
\vec{\tau}=\vec{\mu}\times \vec{B}
$$

- Torque tries to align the magnetic moment vector in the direction of the magnetic field.
- This dipole moment creates an electromagnet out of a loop of wire.
- **At equilibrium, $\vec{\mu}$ points in the direction of $\vec{B}$.**
