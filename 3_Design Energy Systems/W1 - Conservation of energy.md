# W1 - Conservation of energy

## System and Surrounding

![image](ref/system%20surroundings.png)

- **System**: Defined region that contains energy and/or matter and is isolated from its surroundings by an arbitrarily imposed wall or boundary
- **Boundary**: an arbitrary closed surface through which energy and mass can enter or exit the system
- **Surroundings**: everything that can interact with the system, exerting an influence on its behavior and properties

### Properties

- **Extensive property** – its value for a whole system is the **sum of its values** for the parts into which the system is divided. They depend on the size or extent of a system.
    - Example: mass, volume, energy, ...
- **Intensive property** – its value is independent of the size or extent of a system. They are **all the same** when the system is divided into parts
    - Example: density, pressure, temperature, ...

### Energy of a System

- Sum of all the kinetic, potential and *internal energy* of a system
    - Internal energy, $U_S$, is an umbrella term for all other types of energy inside the system
        - It is the kinetic energy of **molecules** and potential energy due to **interactions between molecules**
        - It is **NOT the same as $KE_S$ and $PE_S$ of the whole system**

### State and Path Functions

- **State function**: Property of the system that depends only on the initial and final states, not the path taken
    - Examples: energy, temperature, pressure, volume, enthalpy, entropy, ...
- **Path function**: Property whose value depends on the path taken to reach a particular state
    - Examples: work and heat **only**
    - Recall the area under p-V graph

## Conservation of Energy

- Change of energy during time interval $\Delta t$ = energy transferred into the system across the boundary $E_{in}$ in time $\Delta t$ - energy transferred out of the system across the boundary $E_{out}$ in time $\Delta t$
- Hence, the change of energy in the system is $\Delta E_s = \Delta KE_s + \Delta PE_s + \Delta U_s$
- **Rate of change of energy of the system**

$$
\frac{dE_s}{dt}=\sum \dot{E}_{in} - \sum \dot{E}_{out} = (\dot{Q}_{in} - \dot{Q}_{out}) + (\dot{W}_{in} - \dot{W}_{out})
$$

- Where $\dot{E}$ is the rate of change of $E$, $\frac{dE}{dt}$
- All RHS values are **positive** by convention
![image](ref/closed%20conservation%20of%20energy.png)

## Open and Closed Systems

![image](ref/open%20closed%20system.png)

- Through the boundary, the system and surrounding can exchange:
    - For a **Closed** system, **energy** only
    - For a **Open** system, **energy and mass**

### System's Internal Energy

- The KE and PE of a system depends on the **speed** and **height of the centre of mass** of the system
- In a **closed** and **stantionary** system, $KE_S = PE_S = 0$
    - The rates of change of these energies are also 0.
    - Therefore,

$$
E_S = U_S \\
\frac{dE_{sys}}{dt} = \frac{dU_S}{dt}
$$

## Heat Transfer Modes

| Mode        | Description                                                                                         | Equation                                               |
|-------------|-----------------------------------------------------------------------------------------------------|--------------------------------------------------------|
| Conduction  | Transfer of energy from more energetic particles to adjacent, less energetic particles due to interactions between particles | $\dot{Q}_{\text{cond}} = -\kappa A \dfrac{T_h - T_c}{L}$ |
| Convection  | Energy transfer due to diffusion and bulk movement of fluid | $\dot{Q}_{\text{conv}} = h A (T_h - T_c)$ |
| Radiation (FYI) | Transfer of energy from a point of higher temperature to a point of lower temperature by electromagnetic radiation | $\dot{Q}_{\text{rad}} = \varepsilon \sigma A (T_h^4 - T_c^4)$ |

**Symbols:**

- $\dot{Q}$ = heat transfer (W or J/s)
- $\kappa$ = thermal conductivity (W/m·K)
- $h$ = heat transfer coefficient (W/m²·K)
- $A$ = heat transfer area (m²)
- $\varepsilon$ = emissivity (0 < $\varepsilon$ < 1)
- $\sigma$ = Stefan-Boltzmann constant = $5.67 \times 10^{-8}$ W/m²·K⁴
- $L$ = thickness or distance (m)
- $T_h$ = temperature of the hot region (K)
- $T_c$ = temperature of the cold region (K)
- $\frac{T_h - T_c}{L} = \frac{dT}{dx}$ = temperature gradient in the $x$ direction ($K/m$)
- Note the negative sign in $\dot{Q}_{\text{cond}}$ as it must be positive, and $dT$ & $dx$ are always in opposite directions

## Steady State

- Conduction = Convection + Radiation (no change in system energy over time)
$$\therefore \frac{dE_{sys}}{dt}=\sum\dot{E}_{in}-\sum\dot{E}_{out}=0$$

### Thermal Resistance (only for Conduction and Convection)

There exists an analogy between the diffusion of heat and electrical charge.

**Resistance**: ratio of a driving potential to the corresponding transfer rate.

- $\dot{Q}_{cond}=\frac{\kappa A}{L}(T_h-T_c)\implies R_{cond}=\frac{T_h-T_c}{\dot{Q}_{cond}}=\frac{L}{\kappa A}$
- $\dot{Q}_{conv}=h\cdot A(T_h-T_c)\implies R_{conv}=\frac{T_h-T_c}{\dot{Q}_{conv}}=\frac{1}{h\cdot A}$

Useful identity: $\dot{Q}R=(T_h-T_c)$