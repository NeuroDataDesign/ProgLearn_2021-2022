# Semi-supervised Classification Forests
## Metadata
- Date Created: [[2021-09-29]]
- Status: #status/in_progress
- Note Type: #note/permenant_note
- Topic: 
- Tags: 
---

Semi-supervised classification forests associate a class label to unlabeled “test” data points that are used during the training phase. This is typically done in discrete categories. There are two types of data: labeled $\mathbf{v}^l \in \mathcal{L}$ and unlabeled $\mathbf{v}^u \in \mathcal{U}$. Semi-supervised forests aim to optimize an objective function for a supervised and unsupervised component.

## Training Objective Function
$$\boldsymbol{\theta}_j = \arg\max{\boldsymbol{\theta}\in \mathcal{T}_j} I(\mathcal{S}_j, \boldsymbol{\theta})
$$
Unlike other forest types, the objective function must separate labeled training data and separate high density regions from one another. This can be done so by defining it as
$$
I(\mathcal{S}_j, \mathbf{\theta}) = I^u(\mathcal{S}_j, \mathbf{\theta}) + \alpha I^S(\mathcal{S}_j, \mathbf{\theta}) 
$$
where $I^S$ is the supervised term that depends on labeled data points and $I^U$ is the unsupervised term that depends on all data points. Parameter $\alpha$ specifies weight.

Using information gain defined over a discrete class distribution, $I^S$ is defined
$$
I^S(\mathcal{S}_j, \mathbf{\theta}) = H(\tilde{\mathcal{S}}_j)- \sum_{i \in \{L, R\}} \frac{|\tilde{\mathcal{S}}|}{|\tilde{\mathcal{S}}_j^i|}H(\tilde{\mathcal{S}}_j^i)
$$
Where $\tilde{\mathcal{S}} = S \cup \mathcal{L}$ and $H(\tilde{\mathcal{S}}) = -\sum_c p(c)\log p(c)$ where $c$ are the ground truth class labels of points in $\tilde{\mathcal{S}}$.

Unsupervised gain $I^u$ is defined with differential entropy of a multivariate Gaussian density:
$$
I^U(\mathcal{S}_j, \mathbf{\theta}) = \log|\Lambda(\mathcal{S}_j) - \sum_{i \in \{L, R\}} \frac{|\mathcal{S}_j^i|}{|\mathcal{S}_j|}\log|\Lambda (\mathcal{S}_j^i)|
$$
## Transduction Trees for classifying Already Available Data
Label transduction from labeled data to unlabeled data can occur via the following minimization
$$
c(\mathbf{v}^u) = c\left( \arg\min_{\mathbf{v}^l \in \mathcal{L}} Q(\mathbf{v}^u, \mathbf{v}^l) \right)
$$
Where $c$ returns a class index associated with a point. The generic geodesic distance $Q$ is defined
$$
Q(\mathbf{v}^u, \mathbf{v}^l) = \min_{\boldsymbol{\Gamma} \in \mathcal{G}} \sum_{i=0}^{|\boldsymbol{\Gamma}| - 1} d(\mathbf{s}_i, \mathbf{s}_{i+1})
$$
where $d$ are local symmetric Hahalanobis distances



---
## Related