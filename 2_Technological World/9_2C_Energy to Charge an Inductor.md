# 9_2C_Energy to Charge an Inductor

1. Start with uncharged inductor
2. Gradually increase current, must do work
$$ dW = Pdt = \epsilon I dt = L\frac{dI}{dt} = LI\, dI $$
3. Integrating to find total work done,
 $$ U_L = W = \int dW = \int_0^I LI \, dI = \frac{1}{2}LI^2 $$

## Energy density

- Magnetic energy density is given by
 $$ u_b = \frac{B^2}{2\mu_0} $$

- Recall, electric energy density
 $$ u_E = \frac{\varepsilon E^2}{2} $$

- Energy in inductors is stored in the **magnetic field** only
- In general, to find the total energy stored in a field,
 $$ U = \int_{\text{all space}} u\, dV $$

## Energy stored in a solenoid

- Length $l$, radius $R$, turns per length $n$, current $I$

$$
\begin{align}
B&=\mu_0nI \\
L&=\mu_0n^2πR^2l \\
U_B&=\frac12LI^2=\frac12 (\mu_0n^2πR^2l)I^2 \\
U_B&=\frac{B^2}{2\mu_0}πR^2l
\end{align}
$$

- Energy density = $\frac{B^2}{2\mu_0}$
- Volume = $πR^2l$

This implies that indeed the energy to charge up a solenoid/inductor is stored in the magnetic field $B$.

## Energy stored in a toroid

- Inner radius $a$
- Outer radius $b=a+h$
- Height $h$
- $N$ square windings
- Current $I$

$$
\begin{align}
B(r)&=\frac{\mu_0NI}{2πr} \\
u_B(r)=\frac{B^2}{2\mu_0}&=\frac{\mu_0N^2I^2}{8π^2r^2} \\
\text{Let }dV&=2πrh\,dr \\
dU&=u_B(r)\,dV \\
&=\frac{\mu_0N^2I^2}{8π^2r^2}2πrh\,dr \\
&=\frac{\mu_0N^2I^2h}{4πr}dr \\
U=\int dU&=\int_a^b\frac{\mu_0N^2I^2h}{4πr}dr \\
&=\frac{\mu_0N^2I^2h}{4π}\ln\frac{b}{a} \\
\text{Since }U&=\frac{1}{2}LI^2, \\
\frac{1}{2}LI^2&=\frac{\mu_0N^2I^2h}{4π}\ln\frac{b}{a} \\
\implies L&=\frac{\mu_0N^2h}{8π}\ln\frac{b}{a}
\end{align}
$$
