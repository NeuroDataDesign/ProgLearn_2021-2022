# Decision Trees: Abstract Forest Model
Created: 9/2/2021

Updated: 9/7/2021

Sources:
* [Decision Forests for Computer Vision and Medical Image Analysis](https://link.springer.com/book/10.1007/978-1-4471-4929-3), Chapter 3

**Tags**: #ml #trees #ndd #forest

Trees are good for lots of tasks, such as classificaiton, regression, density estimation, manifold learning, semi-supervised learning, active learning, and certainly more.

## 3.1 Decision Tree Basics
Trees are like graphs. Consider each node in a tree as if asking a successive question to partition.

## 3.2 Notation and definitions
* Data points = $v$
* Features of interest at a point in time are $\phi(v) = (x_{\phi_1}, ..., x_{\phi_{d'}}) \in \mathbb{R}^{d'}$ where $d$ and $d'$ are dimensions of feature space and feature subspace; $d' << d$ 
* Test functions, split functions, weak learners all mean the same thing: they are a **test function** at a split node $j$:
$$h(v, \theta_j) : \mathbb{R}^d \times \mathcal{T} \rightarrow \{0, 1\}$$
where 0 and 1 $\rightarrow$ false/true
	* $\theta_j \in \mathcal{T}$ denote split params at the jth node
	* Data point v sent L/R depending on result
* A set $S_i$ is some set of points, and we label nodes according to BFS
$$S_j = S^L_j \cup S^R_j$$
$$S^L_j \cap S^R_j = \emptyset$$
$$S^L_j = S_{2j+1}$$
$$S^R_j = S_{2j+2}$$

## 3.3 Randomly Trained Decision Trees
During **testing**, apply $h(\cdot, \cdot)$ to send $v$ right or left until leaf node w/ classifier/regressor. 

During **training**, select type and params for $h(v, \theta)$ via greedy optimization function. Goal: learn the function that best splits $S_j$ by maximizing objective function $I$
$$\theta_j = \underset{\theta \in T}{\mathrm{argmin}} I(S_j, \theta)$$
by searching over the set of possible params $\theta$. 

$I$ could be many things, but one example is purity. Regardless, apply procedure recursively to all nodes to yield:
1. Greedily optimize weak learners
2. Learn tree structure by constructing children until stopping criteria
3. A new set of training points at each leaf

### Weak Learner models
* $\phi = \phi(v)$ is some **feature selecter** from v
* $\psi$ is a **geometric primitive** for separation
* $\tau$ is a **param vector** to represent thresholds for inequalities

Linear Data Separation: $h(v, \theta) = [\tau_1 > \phi(v) \cdot \psi > \tau_2]$ where $[\cdot]$ is an indicator fnc.

Non-linear Data Separation example (2D conic section): $h(v, \theta) = [\tau_1 > \phi^T(v) \cdot \psi > \tau_2]$ where $\phi \in \mathbb{R}^{3x3}$ and using homogenous coords. 

Note that $\phi$ can sample $d>>2$ space into any dimension we want

### Energy Models
**Information gain**:
$$I = H(S) - \sum_{i\in \{L,R\}} \frac{S^i}{S}H(S^i)$$
where $|\cdot|$ is cardinality of set.

**Entropy of discrete distributions**:
$$H(S) = - \sum_{c \in C} p(c)\log(p(c))$$
c = Class label, C = set of all classes, $p(c)$ = emperical distribution as normalized histogram

**Entropy of discrete distributions**:
$$H(S) = -\int p(y)\log(p(y))dy$$

**Gaussian based** --> approx p(y) simply
$$H(S) = \frac12 \log((2\pi\epsilon)^2 \Lambda(S))$$

### Leaf prediction models
Each leaf has some training data, and we can use this to generate posterios (i.e. $p(c|v)$ or $p(y|v)$)

### Randomness Model
Goal: inject trandomness during training.
* **Bagging**: train each tree in the forest on different training subsets
* **Randomized Node Optimization**: 