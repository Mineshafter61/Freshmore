# 6_2B_Divergence and Curl

- Divergence: scalar
    - $\nabla\cdot\vec{F}$
- Curl: vector
    - $\nabla\times\vec{F}$

## Vector differential operator

We denote the **vector differential operator** as
$$
\nabla =
\begin{bmatrix}
\frac{\partial}{\partial x} \\\frac{\partial}{\partial y} \\ \frac{\partial}{\partial z}
\end{bmatrix}
= \frac{\partial}{\partial x} \vec{e}_1 + \frac{\partial}{\partial y} \vec{e}_2 + \frac{\partial}{\partial z} \vec{e}_3
$$

This is an operator; it has to act on something to gain a meaning.

## Divergence

For a vector field $\vec{F}:\mathbb{R}^n\to \mathbb{R}^n$, the **divergence** of $\vec{F}$ is denoted by $\text{div} F$ or $\nabla\cdot \vec{F}$, and is defined in Cartesian coordinates by
$$
\nabla\cdot \vec{F}=\frac{\partial F_1}{\partial x_1}+\frac{\partial F_2}{\partial x_2}+\cdots+\frac{\partial F_n}{\partial x_n}
$$
which is a **scalar** field (i.e. function).

## Curl

For a vector field $\vec{F}:\mathbb{R}^3\to \mathbb{R}^3$, the **curl** of $\vec{F}$ is denoted by $\text{curl} F$ or $\nabla\times \vec{F}$, and is defined in Cartesian coordinates by
$$
\nabla\times \vec{F}=\begin{bmatrix}
    \frac{\partial F_3}{\partial y}-\frac{\partial F_2}{\partial z} \\ \frac{\partial F_1}{\partial z}-\frac{\partial F_3}{\partial x} \\ \frac{\partial F_2}{\partial x}-\frac{\partial F_1}{\partial y}
\end{bmatrix}
=\begin{bmatrix}
\frac{\partial}{\partial x} \\\frac{\partial}{\partial y} \\ \frac{\partial}{\partial z}
\end{bmatrix}\times
\begin{bmatrix}
F_1 \\ F_2 \\ F_3
\end{bmatrix}
$$

- Describes how much an object would **spin** when placed inside a vector field.
- Magnitude of the curl is related to the angular speed of rotation, and the direction is perpendicular to the plane of maximum rotation.
- **Parallel fluid flow** without shear has **0 curl**.

## Maxwell's Equations (Differential form)

- Gauss's Law for Electricity: $\nabla \cdot \vec{E} = \frac{\rho}{\epsilon_0}$
- Gauss's Law for Magnetism: $\nabla \cdot \vec{B} = 0$
- Faraday's Law: $\nabla\times \vec{E}=-\frac{\partial \vec{B}}{\partial t}$
- Ampère-Maxwell's Law: $\nabla\times \vec{B}=\mu_0\left(\vec{J}+\epsilon_0 \frac{\partial\vec{E}}{\partial t}\right)$
