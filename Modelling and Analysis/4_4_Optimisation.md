- Finding the optimal outcome
- Steps:
	1. Create an equation that relates the variable to be found to the independent variables.
	2. Differentiate the above equation.
	3. Find out where the equation from Step 2 is 0.
	4. Check whether the value found in Step 3 is a maximum/minimum using the first/second derivative test.
> **Example:**
> Let $2x + y = 2400$, $A = xy$. Find the maximum A.
> $$
2x+y=2400 \implies y=2400-2x \implies A=xy=x(2400-2x)=2x(1200-2x)
$$
> We need to find the critical numbers of this expression.
> $$
\begin{gather*}
\text{Let } A(x)=2x(1200-x)>0 \implies 0 < x < 1200\\
A(x)=2x(1200-x)\\A'(x)=2(1200-x)+2x(-1)=2400-4x\\
\text{When }A'(x)=0,\\
x=600, y=2400-1200=1200\\A(600)=2(600)(1200-600)=720000\end{gather*}$$
> Check using Second Derivative Test:
> $$A''(x)=2400-4x=-4<0$$
> hence the graph is concave and A is a maximum.