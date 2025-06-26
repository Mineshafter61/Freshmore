# W2D1 - Linear Regression
Aim: When there appears to be a **linear** relationship in a scatter plot, the line which 'best' models the data is

$$\hat{y}=\hat{\beta}_0+\hat{\beta}_1x$$

where

- $\hat{\beta}_1=\frac{s_{xy}}{s_x^2}$
- $\hat{\beta}_0=\bar{y}-\hat{\beta}_1\bar{x}$

Observation: The ‘best’ line can be found simply using the sample mean, variance, and covariance from the data.

## Simple linear regression
For simple linear regression, the domain of $y_i$ (response/outcome/dependent variable) is all real numbers (**cannot be categorical**)
- Simple: one explanatory (independent) variable

### Least squares method
- Let $e_i=y_i-\hat{y}_i=y_i-\hat{\beta}_0+\hat{\beta}_1x_i$
- Least squares: $f:=\sum e_i^2$

Aim: find $(\beta_0,\beta_1)$ such that $f$ is minimised
This becomes an optimisation problem where the independent variables are $\beta_0$ and $\beta_1$. Therefore, we compute:
- $\frac{\partial f}{\partial \beta_0}$
- $\frac{\partial f}{\partial \beta_1}$

We equate them to 0 and solve for $\beta_0$ and $\beta_1$.

After some algebra, we find that
- $\hat{\beta}_1=\frac{s_{xy}}{s_x^2}$
- $\hat{\beta}_0=\bar{y}-\hat{\beta}_1\bar{x}$
### Coefficient of determination, $r^2$
- Defined as
$$r^2=\frac{\sum_{i=1}^n(\hat{y}_i-\bar{y})^2}{\sum_{i=1}^n(y_i-\bar{y})^2}$$
- proportion of the variance in $Y$ that can be accounted for by the regression, as such, $r^2$ is used as a measure of how successful the regression is; higher is better.
- always between 0 and 1
- can be shown that $r^2=r_{xy}^2=\frac{s_{xy}^2}{s_{x}^2s_{y}^2}$
### Data transformation
If there is a non-linear relationship between $x$ and $Y$, sometimes an appropriate **transformation** may be used to make the  relationship linear, which would allow subsequent application of simple linear regression.
## Multiple Linear Regression
- If we believe that there is a linear relationship of the form $Y= β_0 + β_1 x_1 + β_2 x_2$, then multiple linear regression is a method to estimate $β_0$, $β_1$ and $β_2$.
- More generally, suppose we have $k$ independent (or predictor) variables $x_1, x_2, \dots, x_k$. (A data set for this would consist of $k$ columns corresponding to the $x_i$’s, and 1 column for $Y$.) Then multiple linear regression aims to produce a ‘best’ model of the form
$$\hat{y}=\hat{\beta}_0+\hat{\beta}_1x_1+\hat{\beta}_2x_2+\dots+\hat{\beta}_kx_k$$
### $r^2$ for multiple linear regression
- Defined the same as in simple linear regression, namely
$$r^2=\frac{\sum_{i=1}^n(\hat{y}_i-\bar{y})^2}{\sum_{i=1}^n(y_i-\bar{y})^2}$$
- Note that $r^2$ no longer equals $\frac{s_{xy}^2}{s_{x}^2s_{y}^2}$