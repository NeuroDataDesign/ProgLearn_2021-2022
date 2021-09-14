# Regression Forests
Created: 9/12/2021

Updated: 9/12/2021

Sources:
* [Decision Forests for Computer Vision and Medical Image Analysis](https://link.springer.com/book/10.1007/978-1-4471-4929-3), Chapter 5

**Related**: [[Abstract Forest Model]]

**Tags**: #ml #ndd #trees #forest #textbook #regression


## 5.2 Specializing the Decision Forest Model for Regression
The goal is to map an input to a **continuous** output, that is given $v$, estimate a pdf $p(y|v)$ for $y \in \mathbb{R}^n$. A regression forest is a collection of randomly trained regression trees. 

### The Prediction Model
The simplest generic polynomial model corresponds to:
$$y(x) = \sum^n_{i=0}w_i x^i$$
* Leaf output for a single tree is $p_t(y|v)$.
	* Pdf is good since we can get confidence over $y$

![[Pasted image 20210912162249.png|400]]

**Note: Think of it like this - if we use a linear model, the split notes basically partition the region that uses a certain function learner by a weak learner.**

![[Pasted image 20210912165022.png |400 ]]

### The Ensemble Model

Output is average of all tree outputs, as usual: $p(y|v) = \frac{1}{T} \sum^T_t p_t(y|v)$

### The Randomness Model

Again, use $\rho = \mathcal{T}_j$ to denote a random selection of split parameters, hence randomized node optimization model.

### The Training Objective Function ([[Density Forests#The Objective Function|See Density Forests]])
Objective function (same as classification):

$$\theta_j = \underset{\theta \in \mathcal{T}_{j}}{\mathrm{argmax}} I(S_j, \theta)$$

However, the $I$ objective function can change. Some methods use minimization of least squares, but the book uses a Gaussian density model.

$$I(S_k, \theta) = H(S_j) - \sum_{i\in \{L,R\}} \frac{|S^i_j|}{|S_j|}H(S^i_j)$$

Note that the book derives the regression gain. The derivation is simple (pages 51-52) and the 1d input/output along with general form are shown below:

$$I(S_j, \theta) \propto \sum_{x \in S_J} \log(\sigma_y(x)) - \sum_{x \in \{L, R\}} \left(\sum_{x \in S^i_j} \log \left(\sigma_y(x)\right)\right)$$

$$I(S_j, \theta) \propto \sum_{x \in S_J} \log(\Lambda_y(v)) - \sum_{x \in \{L, R\}} \left(\sum_{x \in S^i_j} \log \left(\Lambda_y(v))\right)\right)$$

Where $\sigma_y^2$ is the variance and $\Lambda_y$ is the conditional covariance matrix from linear fitting.

Energy Function:

$$\sum_{v \in S_j} (y-\bar{y_j})^2 - \sum_{x \in \{L, R\}}\left( \sum_{v\in S_j^i} (y-\bar{y}^i_j)^2 \right)$$

### The Weak Learner Model

Weak learners are trained as usual through $h(v, \theta_j) \in \{0, 1\}$ as like classification.

## 5.3 Effect of Model Parameters
### Forest Size

Smoothness of interpolating curve controlled through forest size $T$

### Tree Depth
* D = 1 is like linear regression
* D = 5 begins to overfit

### Spatial Smoothness and Testing Uncertainty
* Gaps in the regression forst successful capture multi-modal priors

