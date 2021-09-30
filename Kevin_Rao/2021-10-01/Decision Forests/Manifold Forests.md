# Manifold Forests
## Metadata
- Date Created: [[2021-09-29]]
- Status: #status/in_progress
- Note Type: #note/permenant_note
- Topic: [[Random Forest]]
- Tags: 
---

Manifold forests are a type of decision forest that aims to find a smooth mapping that approximately preserves observed data points’ geometric distances in a reduced number of dimensions.
Unlike density forests, manifold forest have consider the affinity between data points and an algorithm for estimating the mapping function.

> ![[9781447149293 Decision Forests for Computer Vision and Medical Image Analysis#^91eb9a]]

## Training Objective Function
Manifold forests follow randomized node optimization for the $j$th node’s parameters $\boldsymbol{\theta}_j$:
$$
\boldsymbol{\theta} = \arg\max_{\boldsymbol{\theta}} I(\mathcal{S}_j, \boldsymbol{\theta})
$$
With I defined as for density forests
$$
I(\mathcal{S}_j, \boldsymbol{\theta}) = \log|\Lambda (\mathcal{S}_j) - \sum_{i \in \{L, R\}} \frac{|\mathcal{S}_j^i|}{|\mathcal{S}_j|}\log|\Lambda(\mathcal{S}_j^i)|
$$

## Predictor Model
The predictor model of each leaf follows single multivariate Gaussian
$$
p_t(\mathbf{v}) = \frac{\pi_{l(\mathbf{v})}}{Z_t}\mathcal{N}(\mathbf{v}; \boldsymbol{\mu}_{l(\mathbf{v})}, \Lambda_{l(\mathbf{v})})
$$

## Affinity Model
The affinity model aims to preserve distances between points after the mapping. This is accomplished by computing an affinity matrix for clustering tree $t$ whose elements are defined
$$
W_{ij}^t = e^{-Q^t(\mathbf{v}_i, \mathbf{v}_i)}
$$
Where $Q$ is a function that computes distance which can be defined in different ways defined using $\mathbf{d}_{ij} = \mathbf{v}_i-\mathbf{v}_j$:

### Mahalanobis affinity
$$
Q^t(\mathbf{v}_i, \mathbf{v}_j) = \begin{cases}
\mathbf{d}_{ij}^T(\Lambda^t_{l(\mathbf{v}_i)})^{-1} \mathbf{d}_{ij} & l(\mathbf{v}_i) = l(\mathbf{v}_j)\\
\infty & \text{otherwise}
\end{cases}
$$

### Gaussian affinity
$$
Q^t(\mathbf{v}_i, \mathbf{v}_j) = \begin{cases}
\frac{\mathbf{d}_{ij}^T\mathbf{d}_{ij}}{\varepsilon^2} & l(\mathbf{v}_i) = l(\mathbf{v}_j)\\
\infty & \text{otherwise}
\end{cases}
$$

### Binary Affinity
$$
Q^t(\mathbf{v}_i, \mathbf{v}_j) = \begin{cases}
0 & l(\mathbf{v}_i) = l(\mathbf{v}_j)\\
\infty & \text{otherwise}
\end{cases}
$$
Binary affinity is the simplest and most interesting as it can be seen as a special case where $\varepsilon \to \infty$. It states that perfect affinity can be assigned to a pair of points if they are on the same cluster (leaf).

A problem in manifold learning is how to define appropriate neighborhoods that give good approximation of distances. Manifold forests perform a maximization of unsupervised information objective function that creates natural neighborhoods with pairwise similarities.

## Ensemble Model
Individual random decision trees do not produce affinities representative of airwise point similarities, especially with binary models. This is not the case with a forest ensemble model where a smoother affinity matrix can be defined even with a binary model. For a forest of $T$ trees, the afinity matrix is defined as
$$
W = \frac{1}{T} \sum_{t=1}^T W^t
$$

## Embedding Function
Given an affinity matrix $W$, a Lapacian matrix can be defined
$$
L = I - T^{-\frac{1}{2}}WT^{-\frac{1}{2}}
$$
where $T$ is a normalizing diagonal matrix such that $T_{ii} = \sum_{j} W_{ij}$ and is often called the degree matrix.

A mapping function $\mathbf{f}$ can be computed by eigen-decomposition of $L$.
Let $\mathbf{e}_0,\ldots, \mathbf{e}_{k-1}$ be the solutions in increasing order of eigenvalues.
$$
L \mathbf{e}_i=\lambda_i\mathbf{e}_i
$$
The first eigenvector $\mathbf{e}_0$ corresponds to the generate solution, so the remaining eigenvectors are used to constract a matrix $E$:
$$
E = \begin{pmatrix}
\mathbf{e}_1 & \mathbf{e}_1 & \ldots & \mathbf{e}_{d'}
\end{pmatrix}
$$
So, a point $\mathbf{v}_i \in \mathbb{R}^d$ can be mapped to a corresponding point $\mathbf{v}_i’ \in \mathbb{R}^{d’}$ by reading the $i$th row of $E$.
$$
\mathbf{v}_i' = \mathbf{f}(\mathbf{v}_i) = \begin{pmatrix}
E_{i1} & \ldots & E_{id'}
\end{pmatrix}^T
$$
By this approach, there is no need to tune a length parameter or neighborhood size.

## Mapping Previouly Unseen Points

Given an unseen point $\mathbf{v}$ and an already trained manifold forest, the corresponding point $\mathbf{v}‘$ can be computed:
$$
\mathbf{v}' = \frac{1}{T}\sum_t \frac{1}{\eta^t}\sum_i\left( e^{-Q^t(\mathbf{v}, \mathbf{v}_i)}\mathbf{f}(\mathbf{v}_i)} \right)
$$
where $\eta^t = \sum_{i}e^{-Q^t(\mathbf{v}, \mathbf{v}_i)$ as a normalizing constant.

---
## Source
[[9781447149293 Decision Forests for Computer Vision and Medical Image Analysis|Decision Forests for Computer Vision and Medical Image Analysis]]