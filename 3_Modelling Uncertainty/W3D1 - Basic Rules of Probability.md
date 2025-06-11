# W3D1 - Basic Rules of Probability
## Set theory
- A **set** is a well-defined collection of distinct objects. Usually, a set is written as a list of objects between curly braces, for instance $\{1, 2, 3, 4, 5, 6\}$.
- If an object $x$ belongs to a set $A$, then $x$ is called an element of $A$. This is denoted by $x \in A$.
- A set $B$ is called a subset of a set $A$, if all elements of $B$ are also elements of $A$. This is denoted by $B \subseteq A$.
- The number of elements in a set $A$ is called the size (or the cardinality) of $A$, and is denoted by $|A|$.
- The empty set is denoted by $\emptyset$ or $\{\}$.
**Key terms in probability**
- An **experiment** is a process whose **outcomes are random** (that is, not predictable with certainty), but whose set of all possible outcomes is known.
- The set of all possible outcomes of an experiment is called the **sample space** of the experiment, and is often denoted by $\mathcal S$. So each outcome of an experiment is an element of the sample space.
- Any subset of the sample space is known as an **event**. So an event is a set of some possible outcomes of an experiment.
- An event $E$ is said to **occur** if the outcome of an experiment is an element of $E$.
- $U$ is called a **universal set** if all sets under consideration are subsets of $U$ . In probability, $U$ is usually the sample space $\mathcal S$ of an experiment.
- The **complement** of a set $A$ is the set of all elements in $U$ that are **not** in $A$. It is denoted by $A^c$ .
- The **union** of sets $A$ and $B$, denoted by $A\cup B$, is the set whose elements are in $A$ **or** in $B$ (or in both). (Note: in set theory, ‘or’ is always inclusive; $A \cup B$ is the same as $B \cup A$.)
- The **intersection** of sets $A$ and $B$, denoted by $A ∩B$, is the set whose elements are in both $A$ **and** $B$. If $A ∩B= ∅$, then $A$ and $B$ are said to be **disjoint** (or mutually exclusive).
## Axioms of probability
1. $\mathbb P(E)\geq 0$
2. $\mathbb P(\mathcal S)=1$
3. For any **infinite sequence** of disjoint events $E_{1},E_{2},E_{3},\dots$, $\mathbb P(E_{1}\cup E_{2}\cup E_{3}\cup\dots)=\mathbb P(E_{1})+\mathbb P(E_{2})+\mathbb P(E_{3})+\dots$
## Extras
$\mathbb P(E) = \frac{|E|}{|S|}$