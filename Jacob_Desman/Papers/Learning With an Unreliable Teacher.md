# Learning With an Unreliable Teacher
Created: 2021-11-14, 14:51

Edited: 2021-11-14

**Tags**: #paper #ndd #ml

**References:** [Lugosi, G. (1991)](https://www.sciencedirect.com/science/article/pii/0031320392900087)

## Introduction
- Random variables paired with binary value (X, Y)
- Goal: find decision function so that error probability is minimal
- Optimal solution: Bayes decision

$$g^{*}(x) = \underset{0 \leq i \leq 1}{\operatorname{argmax}}  \mathbb{P}\{ Y = i | X=x \}$$
- Bayes error:
$$P^{B}(X, Y) = \mathbb{P}\{g^{*}(X) \neq Y\}$$

$$P^{B}(X, Y) = 1 - \mathbb{E} \{ \underset{i}{\operatorname{max}} p_i (X)\}$$

- Error probability of the decision:

$$P_g(X, Y) = \mathbb{P}\{g(X) \neq Y\}$$
$$P_g(X, Y) = 1 - \mathbb{E}\{p_{g(X)}(X)\}$$

- **Definition:** posterior probabilities:
$$p_i(x) = \mathbb{P}\{Y = i | X = x\} (i = 0,1)$$

- **Notation:** 
$$\xi_n = ((X_1, Y_1), ..., (X_n, Y_n))$$
$$\eta_n = ((X_1, Z_1), ..., (X_n, Z_n))$$

- **Error probability in training sequence:** $\mathbb{P}\{g_n(X, \xi_n) \neq Y\}$

And we use this to estimate Y in the form $g_n(X, \xi_n)$. However, for this case, we estimate Z --> the noisy labels.

- Regardless, there may be errors in the labels of the training data
- Purpose: investigate asymptotic behavior of
	- L1-consistent estimators of the a posteriori probabilities $\mathbb{P} \{Z = i, | X = x\}$
	- Nearest neighbor (1-NN) decision rule

### Key Lemmas
Define decision $g$ as $g(x, s) = \underset{x}{\operatorname{argmax}} q_i(x, s)$

#### Lemma 1.1
![[Pasted image 20211114150847.png|400]]
- The error probability of decision $g$ is very close to the Bayes risk if $q_i$ are good L1 apprxoimations of the a posteriori probabilities

#### Lemma 1.2
![[Pasted image 20211114150955.png|400]]
- Decisions based on maximization of measurable functions can be arbitarily approximated by approximating in the L1 sense

#### Lemma 1.3
![[Pasted image 20211114204019.png|400]]

## Classification with Estimating the a Posteriori Probabilities

This section investigates L1-consistent estimation of $q_i(x) = \mathbb{P}\{Z = i| X=x\}, x \in \mathbb{R}^d$.

- **Definition:** L1-consistency
$$\lim_{n \rightarrow \infty} \mathbb{E} \left( \sum^1_{i=0} |q_i(X) - q_{in}(X)| \right)$$

- In our case, we want to consider $g_n(x) = \underset{i}{\operatorname{argmax}} q_{in}(x)$ as an approximation of the decision $g(x)= \underset{i}{\operatorname{argmax}} q_i(x)$

#### Theorem 2.1
![[Pasted image 20211114153253.png|400]]
- If the error probability of training $\mathbb{P}\{Z \neq Y\}$ is small, then the error of $g(x)= \underset{i}{\operatorname{argmax}} q_i(x)$ will be small

### Discrete Memoryless Channel
- **Note:** I'm not really familiar with the idea of discrete memoryless channels but I have a hazy idea of what is going on  

#### If the channel is known/we know transition probabiltiies.
- If we know $q_i(x) = \mathbb{P}\{Z = i| X = x\}$, then we can determine the a posteriori probabilities and get Bayes decision
- Question: do we have $q_{in}$ instead of $q_i$?

##### Theorem 2.2 
- A proof shows that as long as the channel has non-zero capacity, then decision $f_n$ is asymptotically optimal
> "We can see from the result that the order of the rate of convergence is the same as that of estimation; the effect of the channel is expressed just in a constant factor: the noiser and more asymmetric the channel, the bigger the constant is"
- **Colloquially:** The factor at which the noisy estimation will converge is on the same order as the pure data, but more noise makes that constant larger

#### If the channel is not known
- Goal: investigate error probability of the decision $g_n(x) = \underset{i}{\operatorname{argmax}} q_in(x)$ 
- From [[Learning With an Unreliable Teacher#Theorem 2 1|Theorem 2.1]], small error probability in training --> decision is good approx of optimal
- Question: Can we get close to the Bayes decision *if error probability of training is not small*
##### Theorem 2.3
![[Pasted image 20211114201827.png|400]]
- **Colloquially:** the error of decision $g$ can be upper bounded by a constant times the Bayes risk $P^{B}(X, Y)$ if $p < \frac{1}{2}$

### Misprints in the training sequence
**Question:** what if $Z_i$ take arbitrary value with probability $p$ independent of $X_i, Y_i$. 
- Note: this is similar to the formulation in the NDD experiments
- $\beta_i \in \{0, 1\}$
- $\mathbb{P}\{\beta_i = 0\} = 1 - \mathbb{P}\{\beta_i = 1\} = p$
- $W_i$ are just some arbitrary random variables that can depend on $X_i, Y_i$, but are independent from all others

$$Z_i = \beta_i Y_i + (1 - \beta_i)W_i, (i = 1,2,...)$$

##### Theorem 2.5 
- The error probability $P_g(X, Y)$ can be obtained by maximization of the "wrong" a posteriori probabilities $q_i(x)$ and is upper bounded by:
![[Pasted image 20211114203238.png|400]]
$$r_i(x) = \mathbb{P}\{W_1 = i | X = x\}$$
$$q_i(x) = (1 - p)p_i(x) + pr_i(x)$$
- **Colloquially:** Once again, we see the decision error is upper bounded by the Bayes risk times some constant

### Consequently Lying Teacher
- Definition: lying such that $Z = h(X)$ where $h:\mathbb{R}^d \rightarrow \{0, 1\}$
- Using [[Learning With an Unreliable Teacher#Lemma 1 3|Lemma 1.3]], we see that the asymptotic error probability of decision $g_n$ is the error probability of training and **can never be less than that**
- **Remark:** consider a medical example where even physicians are incorrect sometimes in certain cases. This is a consequently lying teacher. If a large number label the symptoms, then [[Learning With an Unreliable Teacher#Theorem 2 3|Theorem 2.3]] says that the decision rule is asmpyotically optimal even if no physician knows the Bayes decision --> the machine can therefore be better than the expert

### Classification with Nearest Neighbor Rule
Until now, discussed decision rule $g_n(x) = \underset{i}{\operatorname{argmax}} q_{in}(x)$ with an L1-consitent estimator. 

Now, investigate the nearest neighbor (1-NN) decision.

- $\rho: \mathbb{R}^d \times \mathbb{R}^d \rightarrow \mathbb{R}$ for some norm $\rho(x,y) = \|x - y \|$ if $x, y \in \mathbb{R}^d$

TODO: finish, but section 2 is particularly relevant for NDD and producing an end of semester deliverable