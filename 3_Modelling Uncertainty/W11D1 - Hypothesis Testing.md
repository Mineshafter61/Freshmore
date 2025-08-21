# W11D1 - Hypothesis Testing
**Steps**:
1. Set up two **hypotheses**
2. Choose a **significance level**, $\alpha$
3. Collect data
4. Perform computation on the data
5. Probability is applied to test the hypotheses and to reach a conclusion.
$$
\begin{gather}
\text{Claim: }\frac{\bar{x} - \mu_0}{\sigma/\sqrt{n}} \\ \\
\text{Actual: (From table)}
\end{gather}
$$
## Two competing hypotheses
- **Default claim (null hypothesis)**, $H_0$
  - claim of no difference, no improvement or no effect; the default/current/conservative stance.
- **Counter claim (alternative hypothesis)**, $H_1$ or $H_A$
  - claim that contradicts $H_0$
  - Usually, $H_1$ is the claim that there is a difference or effect; a change from a well-accepted current practice.
- $H_0$ and $H_1$ are usually written as **equalities** or **inequalities** concerning a fixed parameter of interest, $\theta$.
- $H_1$ is usually written in the form of $\theta\neq\theta_0$ (2-sided alternative), $\theta>\theta_0$, or $\theta<\theta_0$ (1-sided alternatives), where $\theta_0$ is a fixed constant that can be determined from the research question.
- $H_0$ is usually written as $\theta=\theta_0$

![image](ref/hypothesis%20test.png)
## 'Proof' by contradiction
- Assume $H_0$ to be true
- Perform a calculation to determine whether the data contradicts this assumption beyond reasonable doubt
- If Yes, we **reject $H_0$ in favour of $H_1$**
- If No, we **do not reject $H_0$**. Note that **we do not accept either hypothesis.**
## Types of errors
- **Type I** (false positive): probabilities denoted by $\alpha$
- **Type II** (false negative): probabilities denoted by $\beta$
## Unknown variance or small $n$
1. Replace population stdev $\sigma$ with sample stdev $s_x$
2. Replace standard distribution with t distribution, $z_{\alpha/2}$ with $t_{n-1,\alpha/2}$ and $z_{\alpha}$ with $t_{n-1,\alpha}$
## Terminology
- Correct:
  - *reject $H_0$ in favour of $H_1$*
  - *do not reject $H_0$*
- Incorrect:
  - *reject $H_1$*
  - *accept $H_0$*
