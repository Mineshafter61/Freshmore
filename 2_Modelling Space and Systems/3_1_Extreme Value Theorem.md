## Region
- A region in $\mathbb{R}^n$ is **bounded** if it is contained in some ball.
- A bounded region is **finite**, i.e. does not stretch to infinity in any direction.
## Boundary
- A point $(x_0, y_0)$ is a **boundary point** of $R$ if, for every $r > 0$, the circular disk with centre $(x_0, y_0)$ and the radius $r$, contains **both** points which are **in** $R$ and points which are **not in** $R$.
- The collection of ALL the boundary points is the **boundary** of R.
- **Note that the point $(x_0, y_0)$ can be a boundary point of region $R$ without belonging to $R$.**
## Open and Closed Region
- A region is **closed** if it contains **ALL** its boundary.
	- If constrains have only $≤$, $≥$ or $=$, it is a closed region.
- A region is **open** if it **does not contain any part** of its boundary.
	- If constrains have only $<$ or $>$, it is an open region.
- A region is **neither closed nor open** if it contains only **part** of its boundary.
- $\mathbb{R}^n$ and the empty set $∅$ are both open and closed.
- **Note, 'bounded' and 'containing the boundary' (i.e. closed) are completely different concepts**
	- There are closed regions that is not bounded, for example $[0, ∞)$ in $\mathbb{R}$
	- There are bounded regions that are not closed, for example $(0, 1)$ in $\mathbb{R}$
## Intersection of Closed Sets
- The intersection of any number of closed sets is closed.
- This is not true for infinite unions, but true for finite unions.
## Extreme Value Theorem
- If $f(x, y)$ is a **continuous** function on a **closed and bounded** region $R$, then $f(x, y)$ has a global maximum at some point $(x_0, y_0)$ in $R$ and a global minimum at some point $(x_1, y_1)$ in $R$.
### General Procedure
1. Check if the region (if any) of interest is closed and bounded, and whether the function is continuous within the region.
	- If the region is closed and bounded, AND if the function is continuous, EVT applies.
	- Otherwise, use [[3_2_Unbounded Regions]]
2. Find all critical points of the function $f$ in the interior of the region.
	- $\nabla f=\vec{0}$
	- $\nabla f \text{ is undefined}$
3. Compute the values of $f$ at these critical points.
	- Largest value = global maxima, smallest value = global minima
4. Find the extreme values of $f$ along the boundary of the region.
5. Compare the values of $f$ found in step 3 and 4. The largest values are the global maxima and the lowest values are the global minima.