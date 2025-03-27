# 9_2A_Self Inductance of an Inductor

- Inductance Symbol: $L$
- Unit: Henry (H), $1 \text{H} = 1 \frac{\text{V s}}{\text{A}}$
- "Self flux", $\Phi_B\equiv LI\implies L=\frac{\Phi_B}{I}$.
- Faraday's Law,
$$\epsilon_{induced}=-\frac{d\Phi_B}{dt}=-L\frac{dI}{dt}$$
- Similar to capacitance

## Calculating self inductance

1. Assume a current $I$ is flowing in the device.
2. Calculate the $B$ field due to the $I$ assumed.
3. Calculate the magnetic flux $\Phi_B$ due to the $B$ field.
4. Calculate the self inductance (divide $\Phi_B$ by $I$).

*Example:* Self-inductance L of a solenoid (n turns per unit length, total length l, radius R)

- Assume length l is relatively large as compared to radius R.
- Assume B-field outside solenoid is 0.
- B-field inside is parallel
- Define closed loop through the solenoid wires. L is the displacement between the two points in the loop passing through the turns.
- By Ampere's Law, $\oint \vec{B}\cdot d\vec{s}=\mu_0(nL)I\implies B=\mu_0nI$
- Magnetic flux across each turn $\Phi_{B/\text{turn}}=\iint \vec{B}\cdot d\vec{A}=BA=\mu_0nI\pi R^2$
- Total magnetic flux for N turns $\Phi_B=N\Phi_{B/\text{turn}}=N\mu_0nI\pi R^2=\mu_0n^2I\pi R^2l$
- Therefore, inductance $L=\mu_0n^2\pi R^2l$

*Example:* Self-inductance L of a toroid (inner radius $a$, outer radius $b=a+h$, height $h$, number of turns $N$, current $I$)

We define r as an arbitrary radius between the centre of the toroid and a point between a and b.
$$
\begin{align}\int_0^{2\pi} \frac{1}{\mu_0} B(r) r d\theta &= NI\\
\implies 2\pi r \frac{B(r)}{\mu_0} = NI \implies B(r) &= \frac{\mu_0 NI}{2\pi r}\\
\Phi &= N \int_a^b B(r) h\,dr\\
\implies \Phi = \int_a^b \frac{\mu_0 N^2 I}{2\pi r} h\,dr &= \frac{\mu_0 N^2 I h}{2\pi} \ln \frac{b}{a}\\
L = \frac{\Phi}{I} &= \frac{\mu_0 N^2 h}{2\pi} \ln \frac{b}{a}\end{align}
$$

## Inductor Behaviour and Back EMF

- By Faraday's and Lenz's law,
$$\epsilon_{induced}=-\frac{d\Phi_B}{dt}=-L\frac{dI}{dt}$$

- Inductor with constant current does nothing.

- Induced EMF opposes **change** of $I$
  - **Create an imaginary battery that creates a current that opposes the change**

![image](TW_inductionBehaviour.png)
