# W4 - Exergy Analysis

## Exergy and the Dead State

### Carnot engine efficiency

$$\eta_{rev}=1-\frac{T_c}{T_h}=\frac{\dot{W}_{rev}}{\dot{Q}_{in}}$$

- $\dot{W}_{rev}$ is the **useful work potential** of a system at the specified state
    - It is the **maximum amount of useful work** for a system producing work
    - It is the **minimum required work** for a system that requires work
    - Maximised when entropy generation $\dot{\sigma}_{gen} = 0$
    - Usually a theoretical value

### Exergy

Exergy ($X$) is the **maximum theoretical work obtainable** from an overall setup consisting of a system and the environment (dead state)

- $\phi$ is the specific exergy (exergy per unit mass)

$$
X[kJ] = (U - U_0) + P_0(V - V_0) - T_0(S - S_0) + \frac{mv^2}{2} + mgz \\
\phi[\frac{kJ}{kg}] = \frac{X}{m} = (u - u_0) + P_0(v - v_0) - T_0(s - s_0) + \frac{v^2}{2} + gz
$$

| Symbol        | Description                                 | Unit                         |
|---------------|---------------------------------------------|------------------------------|
| $\phi$        | Specific exergy                             | $\text{kJ/kg}$               |
| $X$           | Total exergy                                | $\text{kJ}$                  |
| $m$           | Mass                                         | $\text{kg}$                  |
| $u$           | Specific internal energy                    | $\text{kJ/kg}$               |
| $v$           | Specific volume                             | $\text{m}^3/\text{kg}$       |
| $s$           | Specific entropy                            | $\text{kJ/kg K}$             |
| $v$ (in $\frac{v^2}{2}$) | Velocity of the fluid or object            | $\text{m/s}$                 |
| $g$           | Gravitational acceleration                  | $\text{m/s}^2$               |
| $z$           | Elevation above reference level             | $\text{m}$                   |

- $X_{heat/in/out} = \dot{W}_{rev/in/out}$
    - It is a **measure of the departure of the state of a system from that of the environment**.
    - It is an **attribute of the system and environment together**.
    - BUT once the environment is specified, a value can be assigned to exergy in terms of property values for the system only, so exergy **can be regarded as a property of the system**.
    - Exergy is an **extensive** property.
    - Exergy is **not conserved** – it is **destroyed by irreversibilities**.
    - It can be **transferred to and from the systems**
    - Exergy analysis allows us to **find where exergy is destroyed and lost**

### Dead State

- A system is said to be in the **dead state** when:
    - it is in **thermodynamic equilibrium** with its environment - a system has the same temperature and pressure as its environment
    - **No KE or PE relative to the environment** (zero velocity and zero elevation above a reference level);
    - **Does not react with the environment** (chemically inert).
    - No **unbalanced magnetic, electrical and surface tension** effects between the system and its environment.
- The properties of a system in the dead state are denoted by the subscript zero e.g. $P_0, T_0, h_0, u_0, s_0$
- If system is in the dead state – there is no potential for developing work.
- **Dead state has zero exergy**

### Irreversibility & Reversible Work

Irreversibility $I$ is the difference between reversible work $W_{rev}$ and work $W$
$$
I=W_{rev,out}-W_{out} \text{ for a power producing device} \\
I=W_{in}-W_{rev,in} \text{ for a power consuming device}
$$

- Irreversibility is equivalent to the **exergy destroyed**
    - Wasted work potential, or lost opportunity to do work

### Exergy Balance for Closed Systems

- Recall that **entropy** can be generated, but cannot be destroyed

$$
\Delta S_{system} = S_{in} - S_{out} + \sigma_{gen}
$$

- But **exergy** can be destroyed, but cannot be generated

$$
\Delta X_{system} = X_{in} - X_{out} + X_{destroyed}
$$
$$
X_{\mathrm{destroyed}}\left\{\begin{array}{l l}{{>0}}&{{\mathrm{Ireversible~process}}}\\ {{=0}}&{{\mathrm{Reversible~process}}}\\ {{<0}}&{{\mathrm{Impossible~process}}}\end{array}\right.
$$

- Exergy destroyed is **proportional to the entropy generated**

$$
X_{destroyed} = T_0\sigma_{gen}
$$
