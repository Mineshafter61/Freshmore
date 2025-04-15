# 11_LC and Undriven RLC Circuits

## LC Circuit Equation

$$\frac{d^2Q}{dt^2}+\frac{1}{LC}Q=0\text{ OR } \frac{d^2Q}{dt^2}=-\frac{1}{LC}Q$$

- $Q$: charge
- $L$: inductance
- $C$: capacitance
- This is a **Simple Harmonic Motion (SHM)** differential equation.
- Analogous to mechanical mass on a spring system.

### LC Circuit Solution

- General solution:
$$Q(t)=Q_0\cos(\omega_0t+\phi); I(t)=Q_0\omega\sin(\omega_0t+\phi)$$
    - $Q_0$: Amplitude of charge oscillation
    - $\phi$: Phase (time offset)
    - $\omega_0=\frac{1}{\sqrt{LC}}$: Oscillation angular frequency
    - $I_0=Q_0\omega$
- $Q_0$ and $𝜙$ can be determined from the initial conditions given.
- $I=-\frac{dQ}{dt}=Q_0\omega_0\sin(\omega_0t+\phi)$

## Energy point of view

- Energy stored in Capacitor, $U_E=\frac{Q^2}{2C}=\left( \frac{Q_0^2}{2C} \right)\cos^2\omega_0t$
- Energy stored in Inductor, $U_B=\frac12LI^2=\frac12LI_0^2\sin^2\omega_0t=\left( \frac{Q_0^2}{2C} \right)\sin^2\omega_0t$
- Note: $\frac12LI_0^2=\frac12\frac{Q_0^2}C$ ($U_{max}$ in inductor L = $U_{max}$ in capacitor C)
- Thus, $U_{total}=U_E+U_B=\frac{Q_0^2}{2C}=\text{constant}$

## Undriven RLC Circuits

![[TW_rlcCircuit.png]]
- From KVL, we obtain
$$
\frac{Q}{C} - IR - L \frac{dI}{dt}
$$
- For discharging, relationship between $I$ & $Q$ is $I = -\frac{dQ}{dt}$
$$
{\frac{Q}{C}}-\left(-{\frac{d Q}{d t}}\right)R-L{\frac{d}{d t}}{\biggl(}-{\frac{d Q}{d t}}{\biggr)}=0 \\
{\frac{Q}{C}}+R{\frac{d Q}{d t}}+L{\frac{d^{2}Q}{d t^{2}}}=0
$$
### RLC vs LC circuit
- Depending on value of $R$, the damping oscillation differential equation can be solved with 3 possible scenarios
1. **Overdamping**: $R$ is large and no oscillations occur (exponential decay only)
2. **Critical Damping**: $R$ is just nice that the behavior is neither oscillatory not exponential decay
3. **Underdamping**: $R$ is small enough and oscillations are still present
![[TW_rlcDamping.png]]