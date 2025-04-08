# 10_1A_Kirchhoff Voltage and Current Law

- **No magnetic field coupling in circuit, i.e. no inductors in circuit**
- Electric field is **conservative**, i.e. path independent.

## Kirchhoff's Current Law or Kirchhoff's Junction Rule

- **Junction**: multiple current paths intersect
- The sum of all the currents **entering any junction** in a circuit **must be equal** to the **sum of currents leaving that junction**.
$$\sum I_{in}=\sum I_{out}$$

## Kirchhoff's Voltage Law or Kirchhoff's Loop Rule

- By the conservative nature of electrostatic field, the **sum of the potential differences**, $\Delta V$, across **all elements** around **any closed-circuit loop** must be zero.
$$\sum_i\Delta V_i = \pm\oint \vec{E}_{static}\cdot d\vec{s}=0$$
- Note the negative sign

### Sign Conventions

- KVL direction is arbitrary
- Label higher potential region across component as ($+$), lower potential region as ($-$)
- Across **Battery**:
    - KVL travels from low potential to high potential: $+\epsilon$
    - KVL travels from high potential to low potential: $-\epsilon$
- Across **Resistor**
    - Where current **enters**: High potential
    - Where current **exits**: Low potential
    - KVL travels from high potential to low potential: $-IR$
    - KVL travels from low potential to high potential: $+IR$
- Across **Capacitor**
    - Plate with positive charges: High potential
    - Plate with negative charges: Low potential
    - KVL travels from low potential to high potential: $+\frac{Q}{C}$
        - Discharging, acts as a battery
    - KVL travels from high potential to low potential: $-\frac{Q}{C}$
        - Charging, acts like a battery

### Circuit Analysis

1. Assign current direction in the circuit for every loop (can be arbitrary)
2. Determine sign of potential based on sign convention for each components
3. Assign an analysis loop direction (can be arbitrary)
4. Based on KCL, write down junction equations (1 per junction)
    - $\epsilon + IR + \cdots = 0$
5. Based on KVL, write down loop equations (1 per loop)
    - $I_1 + I_2 = I_3$
6. Solve simultaneous equations for the unknowns.

- **Tips:**
    1. Junction equations needed if there is a junction in the circuit.
    2. You need N equations to solve N unknowns.
