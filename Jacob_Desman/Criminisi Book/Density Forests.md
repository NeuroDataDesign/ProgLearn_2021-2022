# Density Forests
Created: 9/12/2021

Updated: 9/13/2021

Sources:
* [Decision Forests for Computer Vision and Medical Image Analysis](https://link.springer.com/book/10.1007/978-1-4471-4929-3), Chapter 6

**Related**: [[Abstract Forest Model]]

**Tags**: #ml #ndd #trees #forest #textbook #unsupervised

## 6.2 Specializing the Forest Model for Density Estimation

**Goal:** estimate the pdf from which a set of unlabeled observations was generated.

What is a *density* forest? - A collection of trees which cluster through simple prediction models.
- Involves deterministic clustering
- Forest posterior is combination of tree posteriors; each input data point explained by multiple clusters (one per tree)
	- TODO(jacob): I don't understand this

### The Objective Function
Referring back to the classic [[Abstract Forest Model#Energy Models|optimization equation]]:

$$\theta_j = \underset{\theta \in T_{j}}{\mathrm{argmax}} I(S_j, \theta)$$

$$I(S_k, \theta) = H(S_j) - \sum_{i\in \{L,R\}} \frac{|S^i_j|}{|S_j|}H(S^i_j)$$

*Unsupervised* entropy can be shown as:

$$H(S) = \frac{1}{2} \log\left((2\pi e)^d \right) |\Lambda(S)|$$

$$I(S_j, \theta) = \log(|\Lambda(S_j)|) - \sum_{i\in\{L, R\}} \frac{|S^i_j|}{S_j} \log(|\Lambda(S^i_j)|)$$

- Note that $| \cdot |$ is the determinant for matrix args and cardinality for set args
- Determinant of covariance matrix --> volume of ellipsoid for cluster --> maximizing $I$ compacts clusters

### Prediction Model

$$l(v): \mathbb{R}^d \leftarrow \mathcal{L} \subset \mathbb{N}$$
- $l(v)$ = leaf l reached by input point v
- $\mathcal{L}$ = set of all leaves in tree t

Describing the statistics of a training point arriving at a leaf node:

$$p_t(v) = \frac{\pi_{l(v)}}{Z_t} \mathcal{N}(v; \mu_{l(v)}, \Lambda_{l(v)})$$
- $\mu_l$ = mean of all points reaching leaf l
- $\Lambda_l$ = associated covariance matrix of points reaching leaf l
- $\pi_l$ = proportion of all training points reaching leaf l, $\pi_l = \frac{S_l}{S_0}$

Note that any given Gaussian is truncated by a partition cell. The probability is normalized following the exact or approximated functions:

$$Z_t = \int_v \pi_{l(v)} \mathcal{N}(v; \mu_{l(v)}, \Lambda_{l(v)})dv$$

$$Z_t = \Delta \cdot \sum_i \pi_{l(v_i)} \mathcal{N}(v; \mu_{l(v_i)}, \Lambda_{l(v_i)})$$

- $v_i$ generated on finite grid with spacing $\Delta$

**Quick note to self:** Basically, the tree output is given by a domain-bounded Gaussian. This means that the parameters of a leaf are used to define this ROI

### The Ensemble Model

$$p(v) = \frac{1}{T} \sum^T_{t=1}p_t(v)$$

## 6.3 Effect of Model Params

### Tree Depth

Deeper trees create more splits with smaller Gaussians, overfitting to noise of training data

![[Pasted image 20210913091124.png|400]]

### Forest Size

- Even if individual trees over-fit, further trees produce smoother densities. 
	- D compromises between output smoothness and capture of structural details
- Practically, more trees T is better since it produces better results.

## 6.4 Complexity Comparison
- GMM = T x K x G
	- T = # random restarts, K = # Gaussian components, G = cost of evaluating v for each Gaussian
- Density forest = T x (D x B + G)
	- B is cost of binary test in split node
	- Can be computationally efficient

## 6.5 Sampling from Generative Model
- Generate D random numbers from uniform distributions for branch, then randomly generate d-dimensional vector from domain-bounded Gaussian
- N x (2J + K) efficiency
	- J = cost of randomly generating number $t\in \{ 1,..., T\}$

## 6.6 Quantitative Analysis

Goal: given the sampled points from a density only, reconstruct pdf which is as close as possible to the original.

Density reconstruction error:

$$E = \sum_v \left( p(v) - p_{\mathrm{gt}}(v)\right)^2$$