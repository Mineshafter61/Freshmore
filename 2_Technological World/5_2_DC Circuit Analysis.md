# 5_2_DC Circuit Analysis

## Current

- Average current $I_{av}=\frac{\Delta Q}{\Delta t}$
- Instantaneous current $I=\frac{dQ}{dt}$
- Unit of current: Ampere (A)
- Direction of current: **opposite** to the direction that negative charges (e.g. electrons) flow.
- **Scalar**

## Current Density, $\vec{J}$

- Current passing through an infinitesimal cross-sectional area divided by that area.
- Given by

$$
\vec{J}=\frac{dI}{dA_n}
$$

- where the direction of $A_n$ is parallel to the current flow.
- Integration notation:

$$
I=\iint \vec{J}\cdot \hat{n}dA=\iint \hat{J}\cdot d\vec{A}
$$

- $d\vec{A}$ is the unit surface area of interest. It is not necessary the same direction as $\hat{J}$.

## Current Enclosed

- Flux of the current density through an **open surface** (i.e. not a Gaussian surface) $S$ bounded by the closed path.
- Given by

$$
I_{enc}=\iint_{S} \vec{J}\cdot \hat{n}dA=\iint_{S} \hat{J}\cdot d\vec{A}
$$

## Microscopic Ohm’s Law

- Class of conductor for which the current density $\vec{J}$ that flows through it is proportional to the electric field applied $\vec{E}$.
- Electrical resistivity $\rho$.
- Electrical conductivity $\sigma$.
- Relations:

$$
\begin{gather*}
\sigma=J/E\\\rho=E/J\\\sigma=1/\rho
\end{gather*}
$$

- $\rho$ and $\sigma$ depend only on the microscopic properties of the material, not on its shape.
- Ability of current to flow depends on density of charges and rate of scattering (collisions)

## Microscopic Ohm’s Law, $\Delta V=IR$

$$
\begin{gather*}
\Delta V=V_b-V_a=-\int_a^b \vec{E}\cdot d\vec{s}=El\\
J=\frac{E}{\rho}=\frac{\Delta V/l}{\rho}, J=\frac{I}{A}
\implies \Delta V=I\left(\frac{\rho l}{A}\right)\equiv IR
\end{gather*}
$$

- Resistance
$$R=\rho l/A$$
- where $l$ is length and $A$ is cross-sectional area

## Resistance and Temperature

- Over a limited temperature range, the resistivity of a conductor varies approximately linearly with the temperature:

$$
\rho=\rho_0(1+\alpha(T-T_0))
$$

- $\rho_0$ is the resistivity at some reference temperature $T_0$.
  - $T_0$ is usually taken to be $20˚C$.
- $\alpha$ is the temperature coefficient of resistivity
- Notes: Not all materials behave in such a way.
  - Resistance of intrinsic semiconductor materials decrease with increasing temperature.

## Electrical Symbols

![image](https://img.freepik.com/premium-vector/simple-electrical-electronic-symbols-flat-design_496334-22.jpg?w=2000)

## Electromotive Force (EMF)

- **Not a force**
- Potential energy per unit charge supplied by a battery or any electrical energy source.
- Symbol: $\varepsilon$, unit: V
- Let $\vec{F}_s$ be the force produced by the energy source. EMF is:

$$
\varepsilon=\int_-^+ \frac{\vec{F}_s}{q}\cdot d\vec{s}=\int_-^+ \vec{f}_s\cdot d\vec{s}=\int_-^+ \frac{-\vec{F}_E}{q}\cdot d\vec{s}
$$

- The energy source needs to produce force/energy to move charges against the internal electric field of the source.

## Resistors In Series

- The same current $I$ must flow through both resistors.
- Potential difference is **cumulative** in series
  - $\Delta V = \Delta V_1 + \Delta V_2$
- $\Delta V=IR_1+IR_2=I(R_1+R_2)=IR_{eq}$
- $R_{eq}=R_1+R_2$

## Resistors In Parallel

- Potential difference across 2 points in parallel is **constant**
  - $\Delta V = \Delta V_1 = \Delta V_2$
- $I=I_1+I_2$
- $\Delta V=\Delta V_1=\Delta V_2=I_1R_1=I_2R_2=IR_{eq}$
- $I=I_1+I_2=\frac{\Delta V}{R_1}+\frac{\Delta V}{R_2}=\frac{\Delta V}{R_{eq}}$
- $\implies \frac{1}{R_{eq}}=\frac{1}{R_1}+\frac{1}{R_2}$

### Potential Divider Law

$$
V_{out} = V_{in}\left(\frac{R_2}{R_1+R_2}\right)
$$

### Current Divider Law

## Power

- Change in energy per unit time

$$
dU = Pdt = dq\Delta V
$$

- Power to move current through circuit elements:

$$
P=\frac{dq}{dt}\Delta V=I\Delta V
$$

- Moving across a resistor in the direction of current **decreases** the potential.
- Resistors **always dissipate** power.

$$
P_{dissipated}=I|\Delta V|=I^2R=\frac{\Delta V^2}{R}
$$
