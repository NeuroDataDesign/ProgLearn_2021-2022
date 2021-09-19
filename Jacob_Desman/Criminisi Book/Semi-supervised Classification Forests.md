# Semi-supervised Classification Forests
Created: 9/19/2021

Updated: 9/19/2021

Sources:
* [Decision Forests for Computer Vision and Medical Image Analysis](https://link.springer.com/book/10.1007/978-1-4471-4929-3), Chapter 9

**Related**: [[Abstract Forest Model]]

**Tags**: #ml #ndd #trees #forest #textbook #unsupervised

* Small set of labeled training, large set of unlabeled
* **Transductive** learning: keep different known labels in different regions, make sure boundaries go through areas of low data density

## 8.1 Semi-supervised Learning in Literature
* Transductive SVM (TSVM)

## 8.2 Specializing the Decision Forest Model for Semi-Supervised Classification
* **Goal**: given labeled and unlabeled data points, associate label to already available unlabeled data points
	* "Test" data available during training
	* $v^l \in \mathcal{L}$ is labeled, $v^u \in \mathcal{U}$ is unlabeled

![[Pasted image 20210919105444.png|400]]

Good when traditional classification would produce a suboptimal surface (i.e. a vertical line in the figure above)

### The Training Objective Function ([[Abstract Forest Model#3 3 Randomly Trained Decision Trees|See Abstract Forest Model]]])
$$\theta_j = \underset{\theta \in \mathcal{T}_{j}}{\mathrm{argmax}} I(S_j, \theta)$$

Objective function must encourage the sepration of labeled training data and separating different high-density regions from one other. The mixed information gain:

$$I(S_j, \theta) = I^U(S_j, \theta) + \alpha I^S(S_j, \theta)$$
- $I^S$ is supervised (depends on labeled points)
- $I^U$  is unsupervised (depends on labeled and unlabeled points)\
- $alpha$ is a weighting term

$$I^S(S_j, \theta) = H(\tilde{S_j}) - \sum_{i\in \{L,R\}} \frac{|\tilde{S_j^i}|}{|\tilde{S_j}|}H(\tilde{S_j^i})$$
- $\tilde{S_j} = S \cap \mathcal{L}$

$$I^U(S_j, \theta) = \log(|\Lambda(S_j)|) - \sum_{i\in\{L, R\}} \frac{|S^i_j|}{|S_j|} \log(|\Lambda(S^i_j)|)$$
- Same Gaussian density as in [[Manifold Forests#The Training Objective Function Abstract Forest Model 3 3 Randomly Trained Decision Trees See Abstract Forest Model Density Forests The Objective Function See Density Forests|Manifold Forests]]
- $S_j \subseteq S \cap \mathcal{L}$

## 8.3 Transduction Trees for Classifying Already Available Data
Label trasductionfrom annotated to unannotated data can be achieved via a minimization of the geodesic distance comparison between labeled and unlabeled data, for the unlabeled data:

$$c(v^u) \rightarrow c(\underset{v^l \in \mathcal{L}}{\mathrm{argmin}}Q(v^u, v^l)) \forall v^u \in \mathcal{U}$$
- $Q$ is generic geodesic distance function
- Local distances $d(\cdot, \cdot)$ are [symmetric Mahalanobis distances](https://stats.stackexchange.com/questions/62092/bottom-to-top-explanation-of-the-mahalanobis-distance/62147#:~:text=Mahalanobis%20distance%20is%20defined%20as,dependent%2C%20%CE%A3%20is%20positive%20definite.)
	- ![[Pasted image 20210919111819.png|200]]
	- Effectively, this prevents paths from cutting across regions of **low data density** by this sort of revisualization of the space based on the data density (see picture)
- Note that all leafs associated with the same Gaussian, so geodesic distances can be taken w.r.t the cluster centroids to speed up computation (approximately)

![[Pasted image 20210919112113.png|400]]

Each tree produces a distribution $p_t^u(c|v^u)$, akin to $p_t^u(c = c_k|v^u) \in \{0, 1\}$

### Transductive Ensemble
Simply average:
$$p^u(c|v^u) = \frac{1}{T}\sum_t^T p_t^u(c|v^u)$$

## 8.4 Inductive from Transduction
Previously, we saw labeled --> unlabeled available data. Now, unlabeled --> unavailable unlabeled.

Instead of computiong $T$ shortest path operations for all new points $v$, make an inductive posterior from existing partitions of the feature space. 

### Inductive Ensemble
The *inductive* forest class posterior has form:

$$p(c|v) = \frac{1}{T} \sum_{t=1}^T p_t(c|v)$$

Recall that information gain has already been maximized on mix of unsupervised and supervised data.

![[Pasted image 20210919113828.png]]


### Discussion:
This is not *self-training*. That would involves training a supervised classifier, classifying the unlabeled data, and using the newly classified data to train a new classifier. Proceed iteratively.

## 8.5 Examples, Comparisons, and Effect of Model Parameters
### Additional Supervision and Active Learning
- Getting more data in low-confidence regions signficiantly increases the confidence of the prediction. 

### Comparison with Transductive SVMs
- Captures uncertainty unlike SVMs (can help reflect noise)

### Handling Multiple Classes
- Regions of low data density appropriately assigned low confidence unlike SVM hard classification

![[Pasted image 20210919165531.png|400]]

### Tree Depth
- Unsurprisingly, increased depth imrpvoes results (more accurate and confident)



