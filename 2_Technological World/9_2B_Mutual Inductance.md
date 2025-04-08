# 9_2B_Mutual Inductance

Current $I_2$ in coil 2 generates magnetic flux $\Phi_{12}$ in coil 1. This magnetic flux in coil 1 is proportional to the current in coil 2. The constant of proportionality is called the mutual inductance $M_{12}$.
$$\Phi_{12}\equiv M_{12}I_{2}$$
$$\epsilon_{12}\equiv-\frac{d\Phi_{12}}{dt}=-M_{12}\frac{dI_{2}}{dt}$$

- It also determines the **EMF induced in coil 1** due to the **change of current** $\frac{dI_{2}}{dt}$ in **coil 2**.
- It can be shown that $M_{12} = M_{21} = M$
- It implies that if we passes through the same current change in coil 1, the same amount of EMF can be induced in coil 2.

*Example:* An infinite straight wire carrying current I is placed displacement s the left of a rectangular loop of wire with width w and length l. What is the mutual inductance of the system?
$$
\begin{align}
\oint \vec{B}\cdot d \vec{s}&=µ_{0}I_{enc} \\
\implies B(r)2πr&=µ_0 \\
\implies B(r)&=\frac{µ_0I}{2πr}\\
d\Phi_B&=B\,dA \\
&=\frac{µ_0I}{2πr}l\,dr \\
\Phi_B=\int d\Phi_B&=\int_{s}^{s+w} \frac{µ_0Il}{2πr} \, dr \\
&=\frac{µ_0Il}{2π}\ln\frac{s+w}{s} \\
M&=\frac{\Phi_B}{I} \\
&=\frac{µ_0l}{2π}\ln\frac{s+w}{s}
\end{align}
$$
