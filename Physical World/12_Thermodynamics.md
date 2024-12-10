## Heat
- Heat: Process of **energy transfer** that affects the agitation of atoms/molecules
- When heat transfers between matter and its surroundings, matter responds in one of the following ways
	- Increases (or decreases) the kinetic/potential energy of its constituent particles.
	- Changes the state of matter, e.g. solid to liquid or gas and vice versa.
- Symbol: Q; unit: Joule
## Heat capacity
- The amount of heat required $Δ Q$ to raise the temperature of that body by $Δ T$.
- Depends on the internal microscopic structure of atoms/molecules
$$
C=\frac{Δ Q}{Δ T}\implies Δ Q = CΔ T \text{or} dQ=CdT
$$
- If heat capacity $C(T)$ varies with temperature over the temperature interval $Δ T$
$$
Q = \int_{T_i}^{T_f}C(T) \, dt
$$
- Symbol: C
### Specific heat capacity
- Heat capacity per unit mass
$$
c = \frac{1}{m}\frac{Δ Q}{Δ T} \implies Δ Q = mcΔ T
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
- Fourier's law of Heat Conduction: Rate of heat transfer $Δ Q/Δ t$ across a thin slab is proportional to the cross-sectional area A and the temperature gradient $Δ T/Δ x$ across that slab
 $$\dot{Q} = kA \frac{Δ T}{Δ x}$$
- Temperature gradient $\frac{Δ T}{Δ x}=\frac{T_2-T_1}{x_2-x_1}$
### Convection
- Energy transferred by the movement of a heated fluid substance
- Rate of heat convection: $$\dot{Q} = \frac{dQ}{dt} = hAΔ T = hA(T_\infty - T_s)$$
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
  - Conduction: $I = -k\frac{Δ T}{Δ x}$
  - Convection: $I = hΔ T = h(T_\infty - T_s)$
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
F_i = ma_i = m\frac{\vec{v}_f - \vec{v}_0}{Δ t} = m\frac{-v_x - v_x}{Δ t}\hat{i} = -\frac{2mv_x}{Δ t} = -\frac{2mv_x}{2d/v_x} = -\frac{mv_x^2}{d}
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
Δ E_{int}=Q-W
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
	- **For $N$ ideal gas particles at about room temperature, $T ≈ 300K$, $Δ E_{int}=f\times N\times \frac{1}{2}k_{B}Δ T=\frac{f}{2}nRΔ T$**
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
- Molar heat capacity at constant volume: $Q_V=nc_VΔ T$
- Molar heat capacity at constant pressure: $Q_p=nc_pΔ T$
- Heating a gas at constant volume does not produce mechanical work ($W=0$) since $dV=0$. The heat goes solely into raising the internal energy ($Δ E_{int}$) of the gas. 
$$
Q_V=nc_VΔ T=Δ E_{int}
$$
- Heating a gas at constant pressure *produces* mechanical work $W$. The heat goes into raising the internal energy of the gas + work done by gas ($W=pΔ V$).
$$
Q_p=nc_pΔ T=Δ E_{int}+pΔ V>Q_V
$$
### Isochoric (Isovolumetric) process
- Heating a gas at **constant volume**
- Does **not** produce mechanical work ($W = 0$) since $dV = 0, W = p Δ V = 0$
- Heat goes **solely** into **raising internal energy** $Δ E_{int}$ of the gas
- Molar heat capacity (from the First Law): $Q_V=nc_VΔ T=Δ E_{int}$
### Isobaric process
- Heating a gas at **constant pressure**
- Heat goes into **raising internal energy** $Δ E_{int}$ of the gas
- Heat goes into work done by the gas $W = p Δ V$
- Molar heat capacity: $Q_p=nc_pΔ T=Δ E_{int}+pΔ V>Q_V$
### Isothermal process
- Heating a gas at **constant temperature**
- **No change in internal energy** $Δ E_{int}$ for an ideal gas
- Heat goes **solely** into work done by the gas $W = p Δ V$
- Molar heat capacity: $Q_p=nc_pΔ T=Δ E_{int}+W>Q_V$
- Constant ratio $\frac{T}{V}$ in $pV = nRT$
### Adiabatic process
- **Does not allow heat exchange** between the system and its surroundings (i.e. $Q=0$). The system is isolated.
- $Q=0$
- Molar heat capacity: $W=-Δ E_{int}=-nc_{V}Δ T=nc_{V}(T_{i}-T_{f})$
- Adiabatic processes satisfies the **equation of state**, $pV^γ=k$ where $k$ is a constant and $\gamma=\frac{c_{p}}{c_{v}}$ is the **heat capacity ratio** which is temperature-dependant. 
	- For a monoatomic gas, $\gamma=\frac{5}{3}$
	- For a linear diatomic gas, $\gamma=\frac{7}{5}$
### Relationship
- **More energy** is required to raise the temperature of a gas by $Δ T$ at **constant pressure**
- Some energy is needed to do work since volume increases
- The internal energy of both gases is the **same** since $E_{int}\propto T$
## Heat Engine Cycles
- Convert heat into useful mechanical work
1. Heat is input $Q_h > 0$ into the working substance and raises its thermal energy
2. Part of the heat is converted into work to give net work output $W$
3. The balance of the heat is output $Q_c < 0$ which returns the working substance to its initial state
4. The cycle is repeated
- Net heat **absorbed** per cycle
$$Q_{\mathrm{net}} = Q_h - Q_c$$
- Since there is no change in internal energy $\Delta E_{int} = 0$ for a cyclic process
$$W_{\mathrm{net}} = Q_{\mathrm{net}}$$
- The **thermal efficiency** $e_{th}$ of the cycle is the ratio of $W$ to $Q_h$ over 1 cycle
$$e_{\mathrm{th}}:={\frac{|W_{\mathrm{net}}|}{|Q_{h}|}}={\frac{|Q_{h}|-|Q_{c}|}{|Q_{h}|}}=1-{\frac{|Q_{c}|}{|Q_{h}|}}$$
### Stirling Engine
- Work done by the gas during the isothermal process is given by $nRT\ln\left( \frac{V_{f}}{V_{i}} \right)$
	- $W_{1\to2}=nRT_h\ln \left( \frac{V_{2}}{V_{1}} \right)>0$ (Equation 1)
	- $W_{3\to4}=nRT_c\ln \left( \frac{V_{4}}{V_{3}} \right)<0$ (Equation 2)
- Since $V_{2}=V_{3}$ and $V_{1}=V_{4}$, taking Equation 2/Equation 1:
	- $\displaystyle\frac{W_{3\to4}}{W_{1\to2}}=\frac{T_{c}\ln(V_{4}/V_{3})}{T_{h}\ln(V_{2}/V_{1})}$
- Since $\frac{\ln(V_{4}/V_{3})}{\ln(V_{2}/V_{1})}=-1$, we can rewrite the above equation as
	- $\displaystyle W_{3\to4}=-\frac{T_{c}}{T_{h}}W_{1\to2}$
- From the 1st law, $Q_{1\to2}=W_{1\to2}=nRT_h\ln(V_{2}/V_{1})>0$
- Zero work done by the gas during isochoric process, $W_{2\to3}=W_{4\to1}=0$.
- $\displaystyle W_{net}=W_{1 \to 2}+W_{3 \to 4}=\left( 1-\frac{T_{c}}{T_{h}} \right)W_{1 \to 2}$
- $\displaystyle e_{th}=\frac{W_{net}}{Q_{h}}=\frac{1T_c/T_{h}W_{1 \to 2}}{Q_{1\to2}}=1-\frac{T_c}{T_h}$
- Carnot Theorem: No heat engine can be more efficient that $1-\frac{T_c}{T_h}$