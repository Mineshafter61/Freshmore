# W5 - Exergy in an Open System
## Second Law (Exergetic) Efficiency, 𝜀
The ratio of actual thermal efficiency to the maximum possible (reversible/ideal) thermal efficiency under the same conditions.
$$
𝜀 = \frac{\eta}{\eta_{rev}}=\frac{COP}{COP_{rev}}=\frac{\text{exergy recovered}}{\text{exergy supplied}}=1-\frac{\text{exergy destroyed}}{\text{exergy supplied}}
$$
- Ranges from a value of 0 to a value of 1.
- For power producing devices, $𝜀 = \frac{W_{out}}{W_{rev,out}}$
- For power consuming devices, $𝜀 = \frac{W_{rev,in}}{W_{in}}$
$${\frac{dX_{system}}{dt}}=\bigl(\dot{X}_{heat,in}-\dot{X}_{heat,out}\bigr)+\bigl(\dot{X}_{work,in}-\dot{X}_{work,out}\bigr)+\sum_{in}\dot{m}\psi-\sum_{out}\dot{m}\psi-\dot{X}_{destroyed}$$
- **Note: For water property table, take $\Delta s$ without the correction term $r \ln\frac{P_2}{P_1}$ as that is for ideal gas**
## Summary
$$
\frac{dX_{\text{system}}}{dt} =
\underbrace{(\dot{X}_{\text{heat,in}} - \dot{X}_{\text{heat,out}})}_{\text{Exergy transfer via heat}} +
\underbrace{(\dot{X}_{\text{work,in}} - \dot{X}_{\text{work,out}})}_{\text{Exergy transfer via work}} +
\underbrace{\sum_{\text{in}} \dot{m} \psi - \sum_{\text{out}} \dot{m} \psi}_{\text{Exergy with mass flow}} -
\underbrace{\dot{X}_{\text{destroyed}}}_{\text{Irreversibility losses}}
$$
1. $\frac{dX_{\text{system}}}{dt}$
    - = 0 at steady state
2. $\dot{X}_{heat} = \dot{W}_{rev} = (1−\frac{T_0}{T})\dot{Q} \text{ , also applies for } X/W_{in} \text{ and } X/W_{out}$
    - When heat is transferred reversibly from a **reservoir** at temperature $T$ to a system at ambient temperature $T_0$​, and we want to know the maximum work that can be extracted from that heat
    - $\dot{Q} = \dot{m}\Delta h$
3. $\dot{X}_{work}$
    - Mechanical or electrical work, assuming no loss
4. $\psi = (u - u_0) + P_0(v - v_0) - T_0(s - s_0) + \frac{v^2}{2} + gz$
    - Exergy entering or leaving due to mass flow
    - $\psi=\Delta h−T_0​\Delta s$
5. $\dot{X}_{destroyed} = T_0\dot{\sigma}_{gen}$
    - Exergy destroyed due to irreversibilities, related to entropy generation
- **Note: For water property table, take $\Delta s$ without the correction term $r \ln\frac{P_2}{P_1}$ as that is for ideal gas