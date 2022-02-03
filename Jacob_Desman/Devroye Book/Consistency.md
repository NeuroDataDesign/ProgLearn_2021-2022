# Consistency
Created: 2022-01-31, 12:17

Edited: 

**Tags:** #book #chapter

**References:**  [[Probabilstic Theory of Pattern Recognition]]

## Universal Consistency
- Given a sequence of training data pairs, we want to achieve Bayes error probability $L^*$ on training data pairs $D_n$
- Can't usually get exact
- Can make a sequence of classification functions $\{g_n\}$ (classification rule) that gets close with error prob:
$$L_n = L(g_n) = P[g_n(X, D_n) \neq Y|D_n]$$
- Gets arbitrarily close to $L^*$ for most D_n

### Definition: Consistent
- If ![[Pasted image 20220202122246.png]], then a classification rule is consistent or *asymptotically Bayes-risk efficient*
- If $\lim_{n \rightarrow \infty} L_n = L^*$ with probability 1, then strongly consistent

**Colloquially**, convergence of expected value of L_n to L* is equivalent to the convergence of L_n to L* in probability since it is bound by L* and 1. This means that:

$$\lim_{n \rightarrow \infty} P[L_n - L^* > \epsilon] = 0$$

Using more data will make the error probability arbitrarily close to the optimum for every training seq. 

### Corollary 6.1:
$$L(g_n) - L^* \leq 2 \mathbb{E}[\eta(X) - \eta_n(X)||D_n]$$

### Definition: Universal Consistency
- A sequence of decision rules if universally (strongly) consistent if it is (strongly) consistent for any distribution of the pair (X, Y)

## Classification and Regression Estimation
An example of a decision rule can be a function $\eta_n(x)$, where $g_n(x) = 0$ if less than or equal to 1/2

The authors note that a key part of proving consistency of classification rules is writing the rules in a plug-in form, and then show the $L_1$ conergence of the approximation functions. 

## Partitioning Rules
- Many classifications partition $\mathbb{R}^d$ into disjoint cells, and then classify each cell according to a majority vote among the labels of $X_i$'s in those cells
	- ![[Pasted image 20220202123642.png]]
	- Note that partitions may change with $n$
- General consistency for these majority vote partitioning rules:
	1. Cells should be small enough so that local changes of distribution can be detected
	2. Cells should be large enough that averaging among labels is effective
-  Notation
	- diam(A) is related to the support
	- $N(x)$ denotes the number of $X_i$'s in the same cell as $x$