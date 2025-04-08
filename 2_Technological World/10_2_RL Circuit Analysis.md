# 10_2_RL Circuit Analysis

- **Inductor**: a passive electronic component which is capable of storing energy in a magnetic field when electric current flows through it.
- $\Phi_B=LI$ and EMF $\epsilon=-\frac{d}{dt}\Phi_B=-L\frac{d}{dt}I$

## Faraday’s and Lenz’s Law

$$\oint \vec{E}\cdot d \vec{s}=-\frac{d\Phi_B}{dt}$$

- $\vec{E}$ in a circuit with **magnetic flux coupling (i.e. with an inductor)** is no longer just a conservative electrostatic field. Thus, the path integration of $\vec{E}$ around a closed loop **is not zero**.
    - $\vec{E}=\vec{E}_{\text{conservative}}+\vec{E}_{\text{non-conservative}}$
- Consider an electric circuit that is coupled to a magnetic field that varies with time. The negative path integral of the electric field around the loop with $n$ circuit elements (excluding inductors in the loop) is the sum of all voltages dropped,
$$-\oint \vec{E}\cdot d \vec{s}=\sum_{i=1}^{n}\Delta V_i$$
- Thus, Faraday's and Lenz's law applied on the circuit becomes
$$-\oint \vec{E}\cdot d \vec{s}=\frac{d\Phi_B}{dt}\implies\sum_{i=1}^{n}\Delta V_i=\frac{d\Phi_B}{dt}$$
- If the magnetic field coupled to the circuit is concentrated around the inductor $L$ in the circuit, then
$$\Phi_B=LI\implies \frac{d\Phi_B}{dt}=L \frac{dI}{dt}$$
- Therefore,
$$\sum_{i=1}^{n}\Delta V_i=L \frac{dI}{dt}$$
    - $\sum_{i=1}^{n}\Delta V_i$ is the sum of the **electric potential** of all the **non-inductive components** on the loop.
    - $L \frac{dI}{dt}$ is the **EMF across the inductor** to **oppose current** passing through

## Inductor Sign Conventions

- When the KVL path moves across an inductor **in the direction of current**, the EMF across an inductor **decreases (negative)**.
- When the KVL path moves across an inductor **opposite to the direction of current**, the EMF across an inductor **increases (positive)**.
- Analogous to resistor

## RL Circuit

|                               | **$t = 0^+$**<br>Right after the switch is closed                                                             | **$t = \infty$**<br>After the switch is closed for a long time |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| **Current, $I(t)$**           | Current is *zero*,<br>$I(0^+) = 0$                                                                            | Current is *steady*,<br>$I(\infty) = \text{const.}$            |
| **Rate of change of current** | $\dfrac{dI(t)}{dt} > 0$                                                                                       | $\dfrac{dI(t)}{dt} = 0$                                        |
| **Behaviour of the inductor** | Inductor induces a *back emf* (like a battery in opposite direction of the current) to **oppose** the current | Inductor *does nothing* and looks like a wire                  |
| **Behaviour between a and b** | Looks like an *open circuit* momentarily between a and b                                                      | Looks like a *short circuit* between a and b                   |

### Current Buildup

Applying KVL to a circuit of 1 inductor, 1 resistor and 1 battery,
$$ \epsilon-IR-L \frac{dI}{dt}=0\implies \frac{dI}{dt}=-\frac{R}{L}\left( I-\frac{\epsilon}{R} \right) $$

At $t=0$,
$$\frac{dI}{dt}=-\frac{R}{L}\left( I-\frac{\epsilon}{R} \right)\implies I(t)=\frac{\epsilon}{R}(1-e^{-t/(L/R)})$$

We can set $\tau=\frac{L}{R}$, the time constant of the LR circuit
$$ I(t)=\frac{\epsilon}{R}(1-e^{-t/\tau}) $$

### Current Decay

- Find current as a function of time. Circuit: 1 inductor L connected to 1 resistor R in a loop.

$$
\begin{align}
\text{One loop}:-L\frac{dI}{dt}-IR&=0 \\
\frac{dI}{dt}&=-\frac{R}{L}I \\
\int_{\epsilon/R}^{I(t)} \frac{dI}{I}&=\int_{0}^{t}-\frac{R}{L}dt \\
\ln \frac{I(t)}{\epsilon/R}&=-\frac{R}{L}t \\
I(t)&=\frac{\epsilon}{R}e^{-\frac{R}{L}t} \\
\end{align}
$$

## Capacitor vs Inductor

|                | Capacitor                        | Inductor                                                    |
| -------------- | -------------------------------- | ----------------------------------------------------------- |
| **Empty**      | $Q=0, V=0$; Short circuit        | $I=0$; Open circuit                                         |
| **Full**       | $Q_{max}, V_{max}$; Open circuit | $\frac{dI}{dt}=0,\epsilon=-L\frac{dI}{dt}=0$; Short circuit |
| **Continuity** | **Voltage** continuity           | **Current** continuity                                      |
