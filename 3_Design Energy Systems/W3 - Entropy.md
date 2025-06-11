# W3 - Entropy

- Entropy is generated when there are **irreversibilities**
    - $\dot{\sigma}_\text{gen, cv} > 0$
  1. Heat transfer through a finite temperature difference
  2. Unrestrained expansion of a gas or liquid to a lower pressure
  3. Spontaneous chemical reaction
  4. Spontaneous mixing of matter at different compositions or states
  5. Friction – sliding friction as well as friction in the flow of fluids
  6. Electric current flow through a resistance
  7. Magnetization or polarization with hysteresis
  8. Ineleastic deformation
- For ideal/reversible processes, no entropy is generated
    - $\dot{\sigma}_\text{gen, cv} = 0$

## Entropy rate balance for Open System

$$
\frac{dS_{sys}}{dt}=\sum_{i=1}^W\frac{\dot{Q}_{in, i}}{T_i}-\sum_{j=1}^W\frac{\dot{Q}_{out, j}}{T_j}+\sum_{k=1}^y\dot{m}_{in,k}s_{in,k}-\sum_{l=1}^z\dot{m}_{out,l}s_{out,l}+\dot{\sigma}_{gen,cv}
$$

- Where:
    - $\frac{dS_{sys}}{dt}$: rate of entropy change
    - $\sum_{i=1}^W\frac{\dot{Q}_{in, i}}{T_i}-\sum_{j=1}^W\frac{\dot{Q}_{out, j}}{T_j}$: rate of entropy transfer due to heat
    - $\sum_{k=1}^y\dot{m}_{in,k}s_{in,k}-\sum_{l=1}^z\dot{m}_{out,l}s_{out,l}$: rate of entropy transfer accompanying mass flow in and out of control volume
        - Read entropy values from entropy table
    - $\dot{\sigma}_{gen,cv}$: rate of entropy production
- **Entropy can be created but cannot be destroyed**
    - Any equation which results in $\dot{\sigma}_\text{gen, cv} < 0$ is not possible
- **At steady state, entropy of the system does not change with time**

## Reading Entropy from Table

### Incompressible Substances

- Change in specific entropy of an **incompressible** substance (specific volume does not change with T),

$$
\Delta s=\int_{T_1}^{T_2} \frac{c_{p(T)}}{T} \, dT
$$

- Where:
    - $c_{p(T)}$ is the specific heat at constant pressure.
- To determine specific entropy ($s^o$), we set the absolute zero as the reference temperature:

$$
s^o(T)=\int_{0}^{T} c_p(T') \, \frac{dT'}{T'}
$$

- According to this definition, $s^o$ is a function of T only.

### Ideal Gas

To find the change in the specific entropy we need to add the correction due to changing pressure (from the ideal gas formula $PV = nRT$):

$$
\Delta s = s_2^0 - s_1^0 - \frac{R}{M_W} \ln \frac{P_2}{P_1}
$$

- Where:
    - $s_1^0$ and $s_2^0$ are the values of the specific entropy corresponding to temperatures $T_1$ and $T_2$ (from table),
    - $R = 8.314 \, \frac{J}{K \cdot \text{mol}}$ is the ideal gas constant,
    - $M_W$ is the molar weight of the substance in $\frac{kg}{\text{mol}}$,
    - $r = \frac{R}{M_W}$ is the gas constant $(J/kg \cdot K)$
    - $P_1$ and $P_2$ are the pressures of the gas at temperatures $T_1$ and $T_2$ respectively.

## Efficiency

- Efficiency, $\eta=\frac{\dot{W}_{out}}{\dot{Q}_{h}}=\frac{\dot{Q}_{h}-\dot{Q}_{c}}{\dot{Q}_{h}}=1-\frac{\dot{Q}_{c}}{\dot{Q}_{h}}$
- Coefficient of Performance for refrigerator, $\text{COP}=\frac{\dot{Q}_{c}}{\dot{W}_{in}}=\frac{\dot{Q}_{c}}{\dot{Q}_{h}-\dot{Q}_{c}}=\frac{T_{c}}{T_{h}-T_{c}}$
- Coefficient of Performance for heat pump, $\text{COP}=\frac{\dot{Q}_{h}}{\dot{W}_{in}}=\frac{\dot{Q}_{h}}{\dot{Q}_{h}-\dot{Q}_{c}}=\frac{T_{h}}{T_{h}-T_{c}}$
