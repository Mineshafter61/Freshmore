$\newcommand{\oiint}{{\subset\!\supset} \mathllap{\iint}}\newcommand{\oiiint}{{\Large{\subset\!\supset}} \mathllap{\iiint}}$
(above line is for Obsidian.md to render oiint correctly)
## Closed surfaces
- Closed surface contains a volume 
- It can be made up of many open surfaces
- The direction of the normal area vector $\hat{n}$ points from **inside out**
$$\Phi_E = \oiint_{surface} d\Phi_i = \oiint_{surface} \vec{E} \cdot d\vec{A}$$

- $\oiint$ means **closed surface integral**
- $d\Phi_E > 0$ if $\vec{E}$ points **outwards**
- $d\Phi_E < 0$ if $\vec{E}$ points **inwards**
## Gauss's Law, Gaussian Surface and Charge Enclosed
- **First Maxwell Equation**: The total flux for all **closed surfaces** is given as
$$
\Phi_{E}=\oiint_{\text{closed surface}}\vec{E} \cdot d\vec{A}=\frac{Q_\text{enclosed}}{\varepsilon_0}
$$
- The total flux passing through **any closed surface** is equal to the **charged enclosed inside** divided by the **permittivity of free space** (constant $\varepsilon_0$) 
  - The shape of the enclosed surface **does not matter** as the total electric field lines passing through the enclosed surface is constant
  - **No net flux** for any **closed surface** placed in an **external** electric field (electric field in cancels electric field out)