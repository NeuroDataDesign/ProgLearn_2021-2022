# Tomia 2015 - Sparse Projection Oblique Randomer Forests
Created: 2021-09-20, 18:33

Edited: 2021-09-22

**Tags**: #ml #forest #paper #ndd

**References:** [Tomia et al.](https://arxiv.org/abs/1506.03410)

## Introduction
* Random Forests and XGBoost are popular ensembles of **axis-aligned trees**.
	* Requires deep-trees with step-like decision boundaries --> overfitting and variance
* Forest-RC (Breiman) splits on linear combinations of coords rather than individual coords --> **oblique**
* Canoncial Correlation Forests and Random Rotation Random Forests perform well on some problems, but perform worse on problems which axis-aligned splits would work well for. 
	* Also inefficient, difficult to tune, and sensitivite to noisey inputs
* Sparse Projection Oblique Randomer Forests (SPORF)
	* At each node, SPORF searches for splits over a sample of very sparse random projections rather than axis-aligned splits

## Background and related work
### Random Forests
* Splits based on information gain, i.e. reduction in Gini impurity:
$$I(\mathcal{S}) = \sum^K_{k=1} f_k(1 - f_k)$$
$$f_k = \frac{1}{\mathcal{S}} \sum_{i \in \mathcal{S}} I[y_i = c_k]$$
* Let $\theta = (j, \tau)$ index a dimension and represent splitting threshold. Left and right partitions made based on threshold. 
* Sample a random subset of $p$ features, evaluate objective function. 
* Recursively split nodes until stopping (max depth, min number observations in node, purity, etc.)

$$\hat{y} = \underset{c_k \in \mathcal{Y}}{\mathrm{argmax}} \sum_{t=1}^T I[\hat{y}^{(t)} = c_k]$$

### Oblique Extensions to Random Forest
* Relax the axial restriction of RF --> oblique to the coordinate axes
* Various approaches have implemented this in the past
	* Breiman F-RC
	* Random Rotation Random Forest - rotate data prior to making trees
	* Canonical Correlation Forests - correlation analysis to correlate with class labels

### Random Projections
- Project using matrix $A \in \mathbb{R}^{p \times d}$:
$$\tilde{X} = XA \in \mathbb{R}^{n \times d}, d << \min(n,p)$$
- If random entries $a_{ij}$ are iid with zero mean and constant variance, then $\tilde{X}$ presevres pairwise distances of X
- Construct $a_{ij}$ following:

![[Pasted image 20210922211617.png]]

### Gradient Boosted Trees
- Unlike RF, GBTs are learned iteratively by minimizing a cost function via gradient descent
- Accurate over a wide range of settings --> widely used and successful

## Methods
### Sparse Projection Oblique Randomer Forests
- Let $X \in \mathbb{R}^{n \times p}$ be a feature matrix of n samples at a split note, sample matrix $A \in \mathbb{R}^{p \times d}$ from distribution $f_A$. Project the feature matrix as in [[Tomia 2015 - Sparse Projection Oblique Randomer Forests#Random Projections|Random Projections]].
- Search for best split in the dimensions of projected space $\tilde{X} \in \mathbb{R}^{n \times d}$, d--> dimensionality of projected space (by choice?)
- Default projection distirbution based on:
	- Random search for splits - can identify good splits, such as success to RF
	- Flexibile sparsity - consider the case of highly uninformative features or a high dimensionsal space with only a few informative features. Appropriate amount of sparsity needed
	- Ease of tuning 
	- Data insight - existing oblique forests don't lend themselves well to Gini importance
	- Scalability
- SPORF summary: sample $\lambda pd$ numbers from {-1, 1} with equal probabilities. $\lambda \in ( 0, 1\}$ is density (fraction of non-zeros) of A, [] ceiling function (nearest interger)
	- $\lambda$ is the only hyperparameter to tune

### Training and Hyperparameter Tuning
- Nodes are split until pure but averaging over many uncorrelated trees tends to alleviate overfitting
	- Tune $d$, number of candidate split directions at each node (cannot be $d>p$)
	- Tune $\lambda$, average sparsity of univariate projections at each split node
	- These values are optimized in the authors' experiments over certain ranges

## Simulated Data Emperical Performance
- SPORF is robust to hyperparameter selection and performs better than F-RC in the orthant and sparse parity simulations
- Feature importances can be computed (Gini importance) in comparison to other oblique forests

## Computational Efficiency and Scalability
- RF has average time complexity of $\mathcal{O}(Tdn \log^2n)$ while SPORF has $\mathcal{O}(Tdnlog^2n + Tdnp\lambda)$.  
	- $d > p$ may result in longer SPORF training times, but $d > p$ often results in improved classification performance
- Space complexity of RF and SPORF are $\mathcal{O}(T(np + c))$

## Conclusion
- Version that attempts to preserve nice properties of RF while gaining the performance benefits of oblique splitting --> statistically robust, computationally efficient, scalable, and interpretable. 