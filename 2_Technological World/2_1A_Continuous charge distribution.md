# 2_1A_Continuous Charge Distribution

$$
\vec{E} = \int_{body} k_e \frac{dq}{|\vec{r}|^2} \hat{r} = \int_{body} k_e \frac{dq}{|\vec{r}_p - \vec{r}_s|^3}(\vec{r}_p - \vec{r}_s)
$$

- $\vec{r}_p$ is a constant point of interest
- $\vec{r}_s$ represents every single charge point in the body
- **It is the variable to be used in integration ($x$)**
- Similar to moment of inertia

## Charge Density

- Linear density = $\frac{\text{charge}}{\text{length}} \implies \lambda = \frac{Q}{L} \implies dq = \lambda dl$
- Surface density = $\frac{\text{charge}}{\text{area}} \implies \sigma = \frac{Q}{A} \implies dq = \sigma dA$
- Volume density = $\frac{\text{charge}}{\text{volume}} \implies \rho = \frac{Q}{V} \implies dq = \rho dV$

## Using the equation

1. From the continuous charge, choose a small $dq$. Identify the $dq$ position from the origin, $\vec{r}_s$.
2. Identify and relate $dq$ with geometry, $dq=\begin{cases}\lambda ds: 1D\\\sigma dA:2D\\\rho dv:3D\end{cases}$
   - Do note that in some cases, $\lambda ds$, $\sigma dA$ or $\rho dv$ may have to be rewritten again, e.g. for a ring, $\lambda ds=\lambda\,Rd\phi$.
3. Identify the position of $dq$, $\vec{r}_s=x$.
4. Identify the position of point of interest $P$, $\vec{r}_p=y$.
5. Calculate the distance from $dq$ to point $P$, $|\vec{r}_p-\vec{r}_s|=\sqrt{x^2+y^2}$
6. Electric field due to $dq$ is $dE=k_e \frac{\rho dv}{(x^2+y^2)^{3/2}}(\vec{y}-\vec{x})$
7. Identify the limits of the integral and integrate $E(\vec{r})=k_e \int\frac{\rho dv}{(x^2+y^2)^{3/2}}(\vec{y}-\vec{x})$
