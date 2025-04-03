# 10_1B_RC Circuit Analysis

- Resistor + capacitor in a circuit

## Charging

- External battery charges capacitor, max current at $t=0$ decreases to $0$ gradually as capacitor charges and charges accumulated on plate produces an opposing current
- $I=+\frac{dQ}{dt}$
    - Positive sign means that the charge in the capacitor is increasing

## Discharging

- External battery is removed and capacitor acts as a battery, max current at $t=0$ decreases to $0$ gradually as capacitor discharges and there is no longer any difference in charge between the 2 plates
- $I=-\frac{dQ}{dt}$
    - Negative sign means that the charge in the capacitor is decreasing

## Solving $Q(t)$, as a function of time

1. Substitute $I = \pm \frac{dQ}{dt}$ based on charging/discharging condition
2. Formulate $\sum_i \Delta V_i = \cdots = 0$ equation
3. Using separation of variable, bring variable $Q$ and $dQ$ to 1 side and $dt$ to the other side
$$f(Q)\, dQ = f(t)\, dt$$
4. At $t=0$, $Q=0$ in the capacitor. At $t=t_1$, $Q = Q(t_1)$. Apply integration and the limits for both sides
$$\int_0^{Q(t_1)} f(Q)\, dQ = \int_0^{t_1} f(t)\, dt$$
