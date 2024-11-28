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
- $\dot{Q} = kA \frac{\Delta T}{\Delta x}$
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
