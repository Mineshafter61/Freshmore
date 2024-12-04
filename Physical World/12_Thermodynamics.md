## Heat
- Heat: Process of **energy transfer** that affects the agitation of atoms/molecules
- When heat transfers between matter and its surroundings, matter responds in one of the following ways
	- Increases (or decreases) the kinetic/potential energy of its constituent particles.
	- Changes the state of matter, e.g. solid to liquid or gas and vice versa.
- Symbol: Q; unit: Joule
## Heat capacity
- The amount of heat required $\Delta Q$ to raise the temperature of that body by $\Delta T$.
- Depends on the internal microscopic structure of atoms/molecules
$$
C=\frac{\Delta Q}{\Delta T}\implies \Delta Q = C\Delta T \text{or} dQ=CdT
$$
- If heat capacity $C(T)$ varies with temperature over the temperature interval $\Delta T$
$$
Q = \int_{T_i}^{T_f}C(T) \, dt
$$
- Symbol: C
### Specific heat capacity
- Heat capacity per unit mass
$$
c = \frac{1}{m}\frac{\Delta Q}{\Delta T} \implies \Delta Q = mc\Delta T
$$
- Symbol: c, unit: $J kg^{-1} K^{-1}$
## Phase Transition and Latent Heat
- Melting (fusion): solid → liquid
- Vaporization (condensation): liquid → vapour
- Sublimation: solid → vapour
- During a phase transition
  - Heat is involved in breaking or forming the bonds between molecules
  - Temperature remains **constant**
- This heat per unit mass is the latent heat $L$ for phase transition
$$Q = \pm mL$$
## Thermal equilibrium vs steady state
- A situation in which two bodies in thermal contact over time cease to exchange thermal energy. **No net** heat flows between them and they achieve **common temperature, T**.
- When two bodies are in thermal contact, heat can transfer between them via conduction, convection and/or radiation.
- Steady state: **constant** heat flow rate $\dot{Q}$ **in and out** of the system, $\dot{Q}_{net} = \dot{Q}_{in} + \dot{Q}_{out} = 0$, temperature stays constant w.r.t time
	- $\dot{Q} = \frac{dQ}{dt} = \text{power}$
## Temperature
- Temperature: **Measure of agitation** of atoms/molecules
- Celsius and Kelvin: $T_K = (T_C + 273.15) K$
## Mechanism of Heat Transfer
- Conduction occurs within the body or between two bodies in physical contact.
- Convection depends on motion of mass from one region of space to another. (usually fluids)
- Radiation is heat transfer by electromagnetic radiation (does not require a
medium between the two bodies).
### Conduction
- Heat transfer without the movement of material
- Main heat transfer process in solid material
- Thermal energy is mainly transferred by the vibrations of the atoms and lattice (phonon) along the substance.
- Movement of electrons also plays a role to transport heat in conductors/metals.
- Fourier's law of Heat Conduction: Rate of heat transfer $\Delta Q/\Delta t$ across a thin slab is proportional to the cross-sectional area A and the temperature gradient $\Delta T/\Delta x$ across that slab
 $$\dot{Q} = kA \frac{\Delta T}{\Delta x}$$
- Temperature gradient $\frac{\Delta T}{\Delta x}=\frac{T_2-T_1}{x_2-x_1}$
### Convection
- Energy transferred by the movement of a heated fluid substance
- Rate of heat convection: $$\dot{Q} = \frac{dQ}{dt} = hA\Delta T = hA(T_\infty - T_s)$$
	- $h$: Convection coefficient $\frac{W}{m^2 \cdot K}$
	- $T_\infty$: Temperature of ambient, usually a **constant**
	- $T_s$: Temperature of the system
### Radiation
- Energy transferred through the electromagnetic radiation (i.e. visible light, infrared, UV etc.) that is emitted from the surface of a body.
- EM waves travel at the speed of light $c$.
- Rate of which a surface radiates electromagnetic energy is proportional to the 4th power of its absolute temperature.
- Net heat flow rate from the body is
$$
\dot{Q}=\sigma Ae(T_\infty^4 - T_s^4)
$$
- $\sigma$: Stefan-Boltzmann Constant, $\sigma = 5.67\times 10^{-8}Wm^{-2}K^{-4}$
- $e$: Emissivity describes the ratio of energy energy an object radiates compared to the perfect emitter for a specific wavelength. It can take values of $0<e<1$.
### Extras
- Intensity $I=\frac{\dot{Q}}{A}$, therefore:
  - Conduction: $I = -k\frac{\Delta T}{\Delta x}$
  - Convection: $I = h\Delta T = h(T_\infty - T_s)$
  - Radiation: $I=\sigma e(T_\infty^4 - T_s^4)$
    - 2 faces: $I=\sigma 2e(T_\infty^4 - T_s^4)$
## Ideal Gases
- Law: $$pV=nRT$$
- Assumptions: 
- **Large number** of **identical** particles in **random motion**
	- Statistical average can be used to model particle behaviour
- **Negligible particle volume** (dilute) and **negligible inter‐particle force**
	- No force exerted on each other except during collision
- Classical **elastic collisions**
	- Momentum and KE are conserved
	- Relative speed of approach = relative speed of separation
- Gas pressure and volume relation: $pV=\frac{2}{3}N\langle K_{tr}\rangle=\frac{Nm}{3}\langle v^{2}\rangle$ where $K_{tr}$ is translational kinetic energy
- Average force on wall per particle
$$
F_i = ma_i = m\frac{\vec{v}_f - \vec{v}_0}{\Delta t} = m\frac{-v_x - v_x}{\Delta t}\hat{i} = -\frac{2mv_x}{\Delta t} = -\frac{2mv_x}{2d/v_x} = -\frac{mv_x^2}{d}
$$
### Degrees of Freedom
- Translational kinetic energy: $K_{tr}=\frac{1}{2}mv^2$
- Translational kinetic energy: $K_{tr}=\frac{1}{2}Iω^2$
- Potential energy: $U=\frac{1}{2}kx^2$ (for diatomic particles vibrating along the molecular axis. Only considered for high temperature)
### Theorem of Equipartition of Energy
- Each degree of freedom with quadratic energy dependence averagely contributes $\frac{1}{2}k_{B}T$ to the system's energy, where $k_{B}$ is Boltzmann's constant and $T$ is temperature in Kelvin.
- For any ideal gas particles, where $f=3$, average translational KE is $$\langle K_{tr} \rangle=\frac{1}{2}m\langle v^2\rangle=\frac{3}{2}k_{B}T$$
- By the Ideal Gas Law, $$
pV=\frac{2}{3}N\langle  K_{tr}\rangle=Nk_{B}T
$$
## First Law of Thermodynamics
- The **change in the internal energy** of a **closed system** is equal to the heat $Q$ acquired by the system minus the work done **BY** the system, $W$: $$
\Delta E_{int}=Q-W
$$
- Polarity matters:
	- If $Q$ is positive, heat is added to the system
	- If $Q$ is negative, heat is removed from the system
	- If $W$ is positive, the system is doing work.
	- If $W$ is negative, work is being done on the system.
- Internal energy of a system is the **microscopic energy** internal to the system when viewed from a **reference frame at rest** w.r.t the object
	- Includes translational, rotational, vibrational energies of the particles
	- Includes inter-particle potential energy, energy of electrons and nuclei
	- Does **not** include macroscopic K.E and P.E of the body (i.e gravitational field)
	- **For $N$ ideal gas particles at about room temperature, $T ≈ 300K$, $\Delta E_{int}=f\times N\times \frac{1}{2}k_{B}\Delta T=\frac{f}{2}nR\Delta T$**
### Quasi-Equilibrium Process
- Quasistatic expansion: 
### Work done
- Work done is area under the graph of a p-V diagram.
$$W=\int_{V_{i}}^{V_{f}} p \, dV$$
- If gas **expands**, $W > 0$
- If gas **contracts**, $W < 0$
- Work done is **process-dependent**
	- Work done is not consistent even though initial and final states of $p$ and $V$ are the same
	- Heat engines can do work in a cyclical process because of this
## Heat in a Thermodynamic Process
- Molar heat capacity at constant volume: $Q_V=nc_V\Delta T$
- Molar heat capacity at constant pressure: $Q_p=nc_p\Delta T$
- Heating a gas at constant volume does not produce mechanical work ($W=0$) since $dV=0$. The heat goes solely into raising the internal energy ($\Delta E_{int}$) of the gas. 
$$
Q_V=nc_V\Delta T=\Delta E_{int}
$$
- Heating a gas at constant pressure *produces* mechanical work $W$. The heat goes into raising the internal energy of the gas + work done by gas ($W=p\Delta V$).
$$
Q_p=nc_p\Delta T=\Delta E_{int}+p\Delta V>Q_V
$$
### Isochoric process
- Heating a gas at **constant volume**
- Does **not** produce mechanical work ($W = 0$) since $dV = 0, W = p \Delta V = 0$
- Heat goes **solely** into **raising internal energy** $\Delta E_{int}$ of the gas
- Molar heat capacity: $Q_V=nc_V\Delta T=\Delta E_{int}$
### Isobaric process
- Heating a gas at **constant pressure**
- Heat goes into **raising internal energy** $\Delta E_{int}$ of the gas
- Heat goes into work done by the gas $W = p \Delta V$
- Molar heat capacity: $Q_p=nc_p\Delta T=\Delta E_{int}+p\Delta V>Q_V$
### Relationship
- **More energy** is required to raise the temperature of a gas by $\Delta T$ at **constant pressure**
- Some energy is needed to do work since volume increases
- The internal energy of both gases is the **same** since $E_{int}\propto T$