## Oscillations
- When moved away from an equilibrium, the object stores PE.
- A **restoring force** arises to pull it back towards equilibrium.
- Picks up KE as it approaches equilibrium
- Overshoots and travels to the other side
- Stops, and pulled back to equilibrium
- Repeat
### Variables
- Amplitude, $A$: maximum displacement from equilibrium (related to energy)
- Period, $T$: time taken for one cycle (s)
- Frequency, $f$: the number of cycles in a unit of time (Hz)
	- $T = 1/f, f = 1/T$
- Angular frequency, $ω$: rate of change of an angular quantity (rad/s)
	- 1 cycle = $2π$
	- $ω=2πf=2π/T$
	- Similar to $ω=vR$
### Simple Harmonic Motion
- Simple: the simplest kind of oscillation possible
- Harmonic: Property of a wave where **frequency components of the signal is an integer multiple of the fundamental frequency**
	- $A \cos (ω_0t)$
	- $B \sin (ω_0t)$
- Motion: when the restoring force is **directly proportional** to the displacement from equilibrium, the oscillation motion is SHM.
- e.g. Ideal spring: $F_x=-kx$. Negative sign is important for the restoring nature of the force.
## Simple Harmonic Motion Characteristics
- Given $x = A\cos(\omega_{0}t)$:
$$
\frac{d^{2}x}{dt^{2}}=-\omega_0^2A\cos(\omega_0t)=-\omega_0^2x
$$
- Also works for $x = A\sin(\omega_{0}t)$:
$$
\frac{d^{2}x}{dt^{2}}=-\omega_0^2A\sin(\omega_0t)=-\omega_0^2x
$$
- Therefore, $\text{SHM} \Leftrightarrow \frac{d^{2}x}{dt^{2}}=-\omega_0^2x$
- Linear Acceleration is **directly proportional** to the **displacement from equilibrium**, with **negative** constant of proportionality.
	- Negative sign shows the restoring force.
## General Solution of SHM
- Possible solutions (aka *ansätze*, sing. *ansatz*)
1. $x(t)=A\cos(\omega_0t + \phi)$, where $A$ is the amplitude and $\phi$ is the phase shift
2. $x(t) = C\cos(\omega_0t) + D\sin(\omega_0t)$, where $C$ is the initial position $x_0$ and $D$ is $\frac{v_0}{\omega_{0}}$.
	- Obtained from $\cos(A+B) = \cos A\cos B - \sin A\sin B$
- Converting between the two forms:
	- $\phi=\tan^{-1}\left( -\frac{v_0}{\omega_0x_0} \right)$
	- $A=\sqrt{x_0^2+\frac{v_0^2}{\omega_0^2}}$
## Energy
- Given the max energy in a system to be $E_t$
	- Spring potential energy $U(x)$ is the area **below** a curve $E=U(x)$
	- Kinetic energy $K(x)$ is the area **between** the curve $E=U(x)$ and the line $E=E_t$
	- $E = K(x) + U(x)$
### Definitions (Energy Method)
- Kinetic Energy
$$
K(t) = \frac{1}{2}mv_x^2(t) = \frac{1}{2}m\omega_0^2A^2\sin^2(\omega_0t + \phi)
$$
- Potential Energy
$$
U(t) = \frac{1}{2}k_x^2(t) = \frac{1}{2}m\omega_0^2A^2\cos^2(\omega_0t + \phi)
$$
- Mechanical Energy
$$
E = K(t) + U(t) = \frac{1}{2}m\omega_0^2A^2 = \frac{1}{2}kA^2 + \frac{1}{2}mv_{x,max}^2
$$
- Period of energy graphs are half that of position, velocity, and acceleration.
### Spring-Mass System (Energy method)
$$
\begin{align}
E_t&=K+U\\
C &= \frac{1}{2}m\left( \frac{dx}{dt} \right)^{2}+\frac{1}{2}kx^{2} \\
0 &= \frac{1}{2}m 2 \frac{dx}{dt}\frac{d^{2}x}{dt^{2}}+\frac{1}{2}k 2x\frac{dx}{dt} \\
0 &= \frac{dx}{dt}(m \frac{d^{2}x}{dt^{2}} + kx) \\
0 = \frac{dx}{dt} (\text{trivial}) &\text{ or } 0 = m \frac{d^{2}x}{dt^{2}} + kx \\
\frac{d^{2}x}{dt^{2}} &= -kx \therefore \text{SHM}
\end{align}
$$