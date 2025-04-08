# 2_1B_Electric Field Lines and Flux

## Electric Flux

- Symbol: $\Phi_E$
- Unit: $N \cdot m^2/C$
- Time independent
- Recall that the electric field is proportional to the number of field lines per area
- Since there is no law to determine the proportionality constant above, we say that the electric field line density is equal to the magnitude of electric field.
- $\Phi_E=\vec{E}\cdot \vec{A}$ for **uniform electric field** and **flat surface**
- Can be negative if electric field is opposite direction to the area vector

## Non-uniform surfaces

- For non-uniform field $\vec{E}$ and a curved surface, we first divide the curved surface into many small pieces of area, $d\vec{A}$
- At a small specific area $d\vec{A}_i$, the electric field is a constant $\vec{E}_i$, such that the electric flux through each small piece is

$$
d\Phi_i = \vec{E}_i \cdot (d\vec{A})_i
$$

- The total flux through the curved surface is $\sum^N_{i=1} d\Phi_i$, given by

$$
\Phi_E = \iint_{surface} d\Phi_i = \iint_{surface} \vec{E} \cdot d\vec{A}
$$

- **Double integral** is required because of surface area
- *Example 1: Electric flux through a hemisphere*
    - By intuition, the area of a circle ("shadow" of hemisphere) is $πr^2$
    - Therefore, the flux is $E\cdotπr^2$
    - Math way: (uses [[0_Spherical Coordinate System|spherical coordinates]])

$$
\begin{align*}
\Phi_E&=\iint \vec{E}\cdot d\vec{A} \\
&=\iint \vec{E}\cdot R\,d\theta\,R\sin \theta\,d\phi \\
&=\iint \vec{E}\cdot R^2\sin \theta\,d\theta\,d\phi \\
\Phi_E&=\int_{0}^{π/2}\int_{0}^{2π} E\hat{k}\cdot R^2\sin \theta\,d\theta\,d\phi\,\hat{r} \\
\hat{k}\cdot \hat{r}&=|\hat{k}||\hat{r}|\cos \theta=\cos \theta \\
\Phi_E&=\int_{0}^{π/2}\int_{0}^{2π} ER^2\sin \theta \cos \theta\,d\phi\,d\theta \\
&=2π ER^2 \int_{0}^{π/2} \sin \theta \cos \theta \,d\theta \\
&=π ER^2 \int_{0}^{π/2} \sin 2\theta\,d\theta \\
&=π ER^2 \left[ \frac{-\cos2\theta}{2} \right]_{0}^{π/2} \\ \\
&=EπR^2
\end{align*}
$$
