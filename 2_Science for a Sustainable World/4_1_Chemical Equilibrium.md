# 4_1_Chemical Equilibrium

- **Dynamic** equilibrium in which the **rates of forward** and **reverse reactions are equal** and there is no net change in composition.
- For a reversible reaction: aA+bB⇄cC+dD
- **No macroscopic** evidence of change
- Reached through a **spontaneous** process
- **Dynamic balance** of forward and reverse processes
- Equilibrium can be reached **regardless of direction of approach** (forward or backward)
- Equilibrium constant, $K_c$:

$$
K_c=\frac{[C]_{eq}^c[D]_{eq}^d}{[A]_{eq}^a[B]_{eq}^b}
$$

- subscript $c$: concentration
- subscript $eq$: equilibrium

## Equilibrium constant, $K$

- Relative amount of products and reactants at equilibrium
- Constant for a particular reaction that is at equilibrium at a **specified temperature**. (i.e. depends on temperature)
- Allows for determination of whether the mixture is at equilibrium and the extent of reaction.
- Take note that **solids** and **liquids** do not appear in $K_c$ as their effective concenrations remain constant throughout the reaction.
- For the reaction $aA+bB⇄cC+dD$,

| Solution                                                | Gaseous                                                         |
| ------------------------------------------------------- | --------------------------------------------------------------- |
| $K_c=\frac{[C]_{eq}^c[D]_{eq}^d}{[A]_{eq}^a[B]_{eq}^b}$ | $K_P=\frac{[P_C]_{eq}^c[P_D]_{eq}^d}{[P_A]_{eq}^a[P_B]_{eq}^b}$ |
| $[]$: concentration in mol/L                            | $P$: partial pressure in atm                                    |

## RICE table

- Given K and initial [], calculate [] at equilibrium.
- Components
    - **Reaction (R)**: Write the balanced chemical equation for the reaction.
    - **Initial (I)**: List the initial concentrations or pressures of the reactants and products.
    - **Change (C)**: Indicate the changes in concentrations or pressures as the system moves towards equilibrium.
    - **Equilibrium (E)**: Calculate the equilibrium concentrations or pressures.
- Example 1: $2NO_2$ (g) $⇄$ $2NO$ (g) $O_2$ (g); Initial pressure of $NO_2$ = 0.75 atm; $K_P=5.9\times10^{-13}@25˚C$

| -   | Reactant        | $⇄$ | Product 1 | Product 2 |
| --- | --------------- | --- | --------- | --------- |
| R   | $2NO_2$ (g)     | $⇄$ | $2NO$ (g) | $O_2$ (g) |
| I   | $0.75$ atm      | $⇄$ | 0         | 0         |
| C   | $-2x$ atm       | $⇄$ | $+2x$     | $+x$      |
| E   | $0.75 - 2x$ atm | $⇄$ | $2x$      | $x$       |

$$
K_P=\frac{ (P_{2NO})_{eq}(P_{O_2})_{eq} }{ (P_{2NO_2})_{eq}}=5.9\times10^{-13}\implies \frac{2x^2}{0.75-2x}=5.9\times10^{-13}
$$

- Example 2:

| -   | Reactant 1 |            | $⇄$ | Product 1     | Product 2   |
| --- | ---------- | ---------- | --- | ------------- | ----------- |
| R   | $H_2O$ (l) | $H_2O$ (l) | $⇄$ | $H_3O^+$ (aq) | $OH^-$ (aq) |
| I   | -          | -          | $⇄$ | 0             | 0           |
| C   | -          | -          | $⇄$ | $+x$          | $+x$        |
| E   | -          | -          | $⇄$ | $x$           | $x$         |

$$
K_w=[H_3O^+]_{eq}[OH^+]_{eq}=1.0\times10^{-14}\implies xx=1.0\times10^{-14}\implies x=1.0\times10^{-7}
$$

## Reaction Quotient, $Q$

- Reaction Quotient are the concentrations/partial pressures of the reactants and products at non-equilibrium conditions
- For a gas reaction, $Q=\frac{(P_C)^c(P_D)^d}{(P_A)^a(P_B)^c}$
- $Q$ can be used to predict the direction of the reaction.
    - $Q < K$: reaction shifts to right
    - $Q = K$: equilibrium ➔ no shift
    - $Q > K$: reaction shifts to left

## Disturbing an Equilibrium System

- **Le Châtelier’s Principle**:
  – A system in equilibrium that is **subjected to stress** will react in a way that **tends to minimise the effect of the stress**.
  – Predicts qualitatively the **direction of change of a system under an external perturbation**.

### Three Common Disturbances to Equilibrium

- Change in concentration (**does not alter K**)
    - To minimise the disturbance, the reaction goes forward to reduce the disturbed reactant (thus producing more products).
    - Q decreases when the concentration of a reactant increases
- Change in temperature (**alters K**)
    - Exothermic reaction ($\Delta H_{rxn}^{0}>0$)
        - Increase temperature, T₂ > T₁:
            - equivalent to adding more heat (i.e. adding products)
            - to remove heat, reaction moves backward
            - $P_A$ and $P_B$ increase and $P_C$ decreases → K₂ decreases
            - K₂ < K₁
        - Decrease temperature, T₂ < T₁:
            - equivalent to removing heat (i.e. removing products)
            - to replenish heat, reaction moves forward
            - $P_A$ and $P_B$ decrease and $P_C$ increases → K₂ increases
            - K₂ > K₁
    - Endothermic reaction ($\Delta H_{rxn}^{0}<0$)
        - Increase temperature, T₂ > T₁:
            - equivalent to adding more heat (i.e. adding products)
            - to remove heat, reaction moves forward
            - $P_A$ and $P_B$ decrease and $P_C$ increases → K₂ increases
            - K₂ > K₁
        - Decrease temperature, T₂ < T₁:
            - equivalent to removing heat (i.e. removing products)
            - to replenish heat, reaction moves backward
            - $P_A$ and $P_B$ increase and $P_C$ decreases → K₂ decreases
            - K₂ < K₁
- Adding an inert (constant pressure or constant volume)
    - Not covered in this course
