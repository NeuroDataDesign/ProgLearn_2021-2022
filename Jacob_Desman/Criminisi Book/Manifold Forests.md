# Manifold Forests
Created: 9/12/2021

Updated: 9/13/2021

Sources:
* [Decision Forests for Computer Vision and Medical Image Analysis](https://link.springer.com/book/10.1007/978-1-4471-4929-3), Chapter 7

**Related**: [[Abstract Forest Model]]

**Tags**: #ml #ndd #trees #forest #textbook #unsupervised

Here, the main task lies in:
- Learning the structure of **high dimensional data** and 
- mapping it onto a lower dimensional space while
- preserving spatial relationships between data points

Similar to dimensionality reduction and embedding. Can think about the ways a hyperplane might make for a complex higher dimensional representation, but a lower dimensional representation in other ways. 

## 7.1 Manifold Learning and Dimensionality Reduction in the Literature
- PCA and isometric feature mapping (IsoMap) are popular to preserve geodesic distances between point pars
- All point pairs may be *intractable*. 
- Laplacian eigenmaps used here to preserve *local* pairwise point distances
	- Think spectral clustering

## 7.2 Specializing the Forest Model for Manifold Learning
**Goal:** given a set of k unlabeled observations $\{v_1, v_2, ..., v_i, ..., v_k\}$ with $v_i \in \mathbb{R}^d$, we wish to find smooth mapping $f: \mathbb{R}^d \leftarrow \mathbb{R}^{d'}$ that **approximately** preserves the observations relative geodesic distances with d' << d

![[Pasted image 20210913094535.png|400]]

In the above figure, some function $f(\cdot)$ maps points into d' = 1.

#### What Are Manifold Forests?

Collections of clustering trees, but with extra components:
1. Used to efficiently infer the $k \times k$ affinity matrix W between all pairs of input data
2. Given W, dimensionality reduction (ex. via Laplacian eigenmaps)

### The Training Objective Function ([[Abstract Forest Model#3 3 Randomly Trained Decision Trees|See Abstract Forest Model]] & [[Density Forests#The Objective Function|See Density Forests]])
$$\theta_j = \underset{\theta \in \mathcal{T}_{j}}{\mathrm{argmax}} I(S_j, \theta)$$

$$I(S_j, \theta) = \log(|\Lambda(S_j)|) - \sum_{i\in\{L, R\}} \frac{|S^i_j|}{|S_j|} \log(|\Lambda(S^i_j)|)$$

### The Predictor Model ([[Density Forests#Prediction Model|See Density Forests]])
Again, we use the single multivariate Gaussian to describe the training points at each leaf node.

$$p_t(v) = \frac{\pi_{l(v)}}{Z_t} \mathcal{N}(v; \mu_{l(v)}, \Lambda_{l(v)})$$

### The Affinity Model
Need notion of affinity/similarity/**distance**.

Compute affinity matrix $W$ for a clustering tree via:

$$W_{ij}^t = e^{-Q^t(v_i, v_j)}$$

Q can be defined in multiple ways, sucha as the **binary affinity**:
$$ Q^t(v_i, v_j)
\begin{cases} 
	0 & l(v_i) = l(v_j)\\
	\infty & \mathrm{otherwise} \\
\end{cases}
$$

"Given a tree t and two points, we assign perfect affinity (affinity = 1, distance = 0) if they end up in the same cluster (leaf) and null afinity (infinite distance) otherwise"

### The Ensemble Model
$$W = \frac{1}{T} \sum^T_{t=1} W^t$$

### Estimating the Embedding Function
Laplacian matrix:

$$L = I - \Upsilon^{-\frac{1}{2}} W \Upsilon^{-\frac{1}{2}}$$

Where $\Upsilon_ii = \sum_j W_{ij}$. Called the **normalizing diagonal matrix** or **degree matrix**.

Find eigenvalue decomposition of L, and order solutions $e_0, e_1, ..., e_{k-1}$ be solutions in increasing order of eigenvalues. 
- Ignore $e_0$ (degenerate)
- Choose some d << d' eigenvectors to construct a k x d' matrix E:

$$
E = 
\begin{pmatrix}
| & ... & | & ... & | \\
e_1 & ... & e_j & ... & e_{d'} \\
| & ... & | & ... & |
\end{pmatrix}
$$

Map a point  $v_i \in \mathbb{R}^d$ simply by reading the ith row of E. This is how we use the function **f**.

### Mapping Previously Unseen Points
Interpolate based on previously existing points and a trained manifold corest. Compute point $v'$ by:

$$v' = \frac{1}{T} \sum_t \frac{1}{\eta^t} \sum_i \left( e^{-Q^t(v,v_i)}f(v_i) \right)$$

where $\eta^t = \sum_i e^{-Q^t(v, v_i)}$ is a normalizing constance and $Q^t(\cdot, \cdot)$ applies the $t$th tree onto $v$.

### Properties and Advantages
#### 1. Distance Estimation
Defines pairwise distances from the tree structure itself. For example, a forest could determine that forest-beach images are a closer pair than distinct metropolis from a city-beach pair.

#### 2. Choosing the Feature Space
Rather than crafting how to represent the data, can define generic *family* of features (ex. gradients, wavelet, filter banks). Tree training --> select discriminative features and parameters associated, greedily optimize information gain.

Ex. Avg within a rectangle. Position and size of rectangles automatically selected in training.

#### 3. Computational Efficiency
Eigen-system can be difficult to solve, but is independent from forest size T. 

#### 4. Estimating Target Intrinsic Dimensionality
Can pick the d' eigenvalues using the **elbow method** --> useful for spectral clustering as well

## 7.3 Experiments and Effects of Model Params
### Forest Size
Ensembling makes *forest* affinity matrix W smoother since multiple trees enable different point pairs to exchange infrmation. *No longer binary!* --> like averaging affinity matrices together.

More trees T better approximates W.

![[Pasted image 20210914144726.png|400]]

### Manifold Learning in Higher Dimensions
3D --> 2D functions similarly to 2D --> 1D case

### Discovering the Manifold Instrinsic Dimensionality
Since we wish to choose a small d', how small can we pick it without losing "too much" information?

If we make an elbow plot of the sorted eigenvalues, we can search for a sharb elbow in the curves. Informs a choice of dimensionality.



