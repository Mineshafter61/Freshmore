# W2 - Open Systems and Enthalpy
## Conservation of Mass
- Mass flow rate, $\dot{m}$: mass of a substance which passes per unit time
- Mass balance (conservation of mass): $\frac{dm_{cv}}{dt}=\sum \dot{m}_{in}-\sum \dot{m}_{out}$
- Steady state (in terms of mass): $\frac{dm_{cv}}{dt}=0\implies\sum \dot{m}_{in}-\sum \dot{m}_{out}=0$
    - The same amount of mass flows in and out of the system per unit of time
## Conservation of Energy
Energy balance for **open system**
$$
\begin{align*}
\frac{dE_{sys}}{dt}&=\sum \dot{E}_{in}-\sum \dot{E}_{out}\\
&=(\dot{Q}_{in}-\dot{Q}_{out})+(\dot{W}_{in}-\dot{W}_{out})+(\dot{W}_{flow,in}-\dot{W}_{flow,out})+(\dot{E}_{flow,in}-\dot{E}_{flow,out})
\end{align*}
$$
- the **mass flowing through the system carries energy** ($\Delta \dot{E}_{flow}$)
- there is a new type of work – **flow work** ($\dot{W}_{flow,in}-\dot{W}_{flow,out}$)
### Flow work
- Work associated with the **fluid pressure** as **mass is introduced at the inlets and removed at the exits**
    - Power at the inlet $\dot{W}_i=P_i\dot{m}_iv_i$
    - Power at the outlet $\dot{W}_e=P_e\dot{m}_ev_e$
    - $P$ = pressure
    - $\dot{m}$ = mass flow rate
    - $v$ = specific volume ($\text{m}^{3}\text{/kg}$)
**Derivation (FYI)**
$$
\begin{align}
W&=F\times d \\
\dot{W}&=F\times \frac{d}{t}=F\times \mathrm v \\
&=P\times A\times \mathrm v \\
&=P\times \left( \frac{volume}{t} \right) \\
&=P\times \left( \frac{m}{t}\times \frac{1}{density} \right)\\
&=P\times \left( \frac{m}{t}\times v \right) \\
&=P\dot{m}v
\end{align}
$$
### Energy Carried by Inlet and Outlet
$$
\dot{E}_{flow,in}-\dot{E}_{flow,out}=\dot{m}_i\left( u_i+\frac{\mathrm v_i^2}{2}+gz_i \right)-\dot{m}_i\left( u_e+\frac{\mathrm v_e^2}{2}+gz_e \right)
$$
Note:
- $\mathrm v$: velocity
- $v$: specific volume
- The variables account for the **rate of internal, kinetic and potential** of entering and leaving the system

- By definition, specific enthalpy, $h = u + Pv$
- Hence we can combine the $\dot{W}_{flow}$ and $\dot{E}_{flow}$ equations to obtain the **rate of internal, kinetic and potential** of entering and leaving the system
$$
\begin{align*}
\frac{dE_{sys}}{dt}&=\sum \dot{E}_{in}-\sum \dot{E}_{out}\\
&=(\dot{Q}_{in}-\dot{Q}_{out})+(\dot{W}_{in}-\dot{W}_{out})+\dot{m}_i\left( h_i+\frac{\mathrm v_i^2}{2}+gz_i \right)-\dot{m}_e\left( h_e+\frac{\mathrm v_e^2}{2}+gz_e \right)
\end{align*}
$$
- Where
    - $\dot{m}_i =$ mass flow rate at **inlet** (kg/s)
    - $h_i =$ specific enthalpy at **inlet** (J/kg)
    - $v_i =$ velocity at **inlet** (m/s)
    - $z_i =$ elevation (height) at **inlet** (m)
    - $\dot{m}_e =$ mass flow rate at **outlet** (kg/s)
    - $h_e =$ specific enthalpy at **outlet** (J/kg)
    - $v_e =$ velocity at **outlet** (m/s)
    - $z_e =$ elevation (height) at **outlet** (m)
    - $g =$ acceleration due to gravity ($9.81~\mathrm{m/s^2}$)
#### Linear Gradient Interpolation

![[air property table.pdf]]

- Given a dataset, find the enthalpy at an unknown temperature
$$h = \frac{h_2-h_1}{T_2-T_1}(T_u - T_1) + h_1$$