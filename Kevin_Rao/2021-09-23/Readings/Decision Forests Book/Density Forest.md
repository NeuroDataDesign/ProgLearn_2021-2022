# Density Forest
## Metadata
- Date Created: [[2021-09-21]]
- Status: #status/in_progress
- Note Type: #note/permenant_note
- Topic: 
- Tags: 
---

The density estimation task involves computing the probability density function of a given input, trained off of unlabeled training data.
> ![[9781447149293 Decision Forests for Computer Vision and Medical Image Analysis#^509b9a]]

Density forests are an ensemble of randomly trained clustering trees. Tree leaves use generalized Gaussian mixture models that partition data clusters. The forest posterior probability is also explained as a combination of individual tree posteriors.

## Training Objective Function
For a collection of data points $\mathcal{S}_0 = \{v\}$, the parameters for node $j$ $\boldsymbol{\theta}_j$ is optimized as:
$$
\boldsymbol{\theta} = \arg\max_{\boldsymbol{\theta}\in\mathcal{T}_j} I(\mathcal{S}_j, \boldsymbol{\theta})
$$
Information gain $I$ is defined as:
$$
I(\mathcal{S}_j,\boldsymbol{\theta}) = H(\mathcal{S}_j) - \sum_{i=\{L,R\}}\frac{|\mathcal{S}_j^i|}{|\mathcal{S}_j|}H(\mathcal{S}_j^i)
$$
Since the data points have no labels, unsupervised entropy is used to compute the entropy of a $d$-dimensional Gaussian:
$$
H(\mathcal{S}) = \frac{1}{2}\log\left((2\pi e)^d |\Lambda(\mathcal{S})|\right)
$$
where $\Lambda$ is a $d\times d$ covariance matrix.
The information gain model simplifies to:
$$
I(\mathcal{S}_j,\boldsymbol{\theta}) = \log\left( |\Lambda(\mathcal{S})|\right) - \sum_{i=\{L,R\}}\frac{|\mathcal{S}_j^i|}{|\mathcal{S}_j|}\log\left( |\Lambda(\mathcal{S}^i_j)|\right)
$$
[[202109211403 - Density forest information gain optimize for compact cluster sizes.|Density forest information gain optimize for compact cluster sizes.]]

## Prediction Model
For the $t$th tree in a forest, which leaf an input data point $\mathbf{v}$ reaches is deterministic. The output of the this tree is determined by maximum likelihood esimation using a single multivariate Gaussian distribution:
$$
p_t(\mathbf{v}) = \frac{\pi_{l(\mathbf{v})}}{Z_t}\mathcal{N}(\mathbf{v};\boldsymbol{\mu}_{l(\mathbf{v})}, \Lambda_l(\mathbf{v}))
$$
Where $\pi_{l(\mathbf{v})} = \frac{|\mathcal{S}_l|}{|\mathcal{S}_0|}$ is the proportion of all training points that reach the leaf data point $\mathbf{v}$ reaches.
$Z_t$ is the partition function that normalizes the probability:
$$Z_t = \int_\mathbf{v} \sum_l \pi_l \mathcal{N}(\mathbf{v};\boldsymbol{\mu}_l,\Lambda_l)p(l|\mathbf{v})d\mathbf{v}
$$
Since in a density each data point reaches exactly each tree once, the conditional probability simplifies to a delta function $p(l|\mathbf{v}) = \delta(l=l_\mathbf{v})$, so the partition function simplifies to:
$$Z_t = \int_\mathbf{v}  \pi_l \mathcal{N}(\mathbf{v};\boldsymbol{\mu}_l,\Lambda_l)p(l|\mathbf{v})d\mathbf{v}
$$
Computing this for multidimensional data can be difficult and has no closed form solution. For smaller weak learners, this term can be approximated as
$$
Z_t \approx \Delta \cdot \sum_i \pi_{l(\mathbf{v}_i)}\mathcal{N}(\mathbf{v};\boldsymbol{\mu}_{l(\mathbf{v}_i)},\Lambda_{l(\mathbf{v}_i)}
$$
where $\mathbf{v}_i$ is are points in a finite space and $\Delta$ is the volume of the space.

## Ensemble Model
The classification of a density forest is the average of all tree densities:
$$
p(\mathbf{v}) = \frac{1}{T} \sum_{t=1}^Tp_t(\mathbf{v})
$$
---
## Source
[[9781447149293 Decision Forests for Computer Vision and Medical Image Analysis|Decision Forests for Computer Vision and Medical Image Analysis]]