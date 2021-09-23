---
alias:
---
# Regression Forests
## Metadata
- Date Created: [[2021-09-20]]
- Status: #status/in_progress
- Note Type: #note/topic_note 
- Topic: [[Machine Learning]], [[Random Forest]]
- Tags: 
---

Regression tasks aim to map unseen data points to a continuous output.
> ![[9781447149293 Decision Forests for Computer Vision and Medical Image Analysis#^b70f9d]]

Given a training point $(\mathbf{v}, \mathbf{y})$, a regressor seeks to find a relationship that maps $\mathbf{v}$ to $\mathbf{y} \in \mathbb{R}^n$.

As a decision forest is an ensemble of randomly trained decision trees, regression forests are an ensemble of randomly trained regression trees. Similar to decision forests, randomly generated regression forests generalize better than a single optimized regression tree.
> ![[9781447149293 Decision Forests for Computer Vision and Medical Image Analysis#^ed453c]]

## Models
How a regression forest structures itself and makes its decision depends on its model.

### Prediction Model

An input travels down a tree $t$ in a regression forest until it reaches a leaf which computes the posterior probability of observing $\mathbf{y}$ given $\mathbf{v}$ as $p_t (\mathbf{y}| \mathbf{v})$.

However, unlike decision forests, the labels given to a particular input are continuous to one another, so there needs to be a model that can demonstrate a relationship between all possible inputs with output. For this, there are polynomial and linear models that can represent this relationship by introducing weights and biases to the input and its powers.

### The Ensemble Model

The output of the overall forest is the average of the individual trees’ outputs.
$$
p(\mathbf{y}| \mathbf{v}) = \frac{1}{T} \sum_t^T p_t(\mathbf{y}|\mathbf{v})
$$

### Randomness Model

The randomized node optimization model controls how different nodes determine where in the training data space it forms decision boundaries. This is controlled by the parameter $\rho = |\mathcal{T}_j|$.

### Training Objective Function

Parameters for a split node $j$ $\boldsymbol{\theta}_j$ is determined by conducting the following optimization:
$$
\boldsymbol{\theta}_j = \arg\max_{\boldsymbol{\theta}\in\mathcal{T}_j} I(\mathcal{S}_j, \boldsymbol{\theta})
$$

Regression trees normally minimize for the last-squares or least-absolute error functions, but to generalize, information gain would be used instead as the the indicator function.
$$
I(\mathcal{S}_j, \boldsymbol{\theta}) = H(\mathcal{S}_j) - \sum_{i \in \{L, R\}} \frac{|\mathcal{S}_j^i|}{|\mathcal{S}_j|}H(\mathcal{S}_j^i)
$$
The entropy $H$ for a given subset $\mathcal{S}$ of training data $\mathcal{S}_0$ for univariate variables is:
$$
H(\mathcal{S}) = -\frac{1}{|\mathcal{S}|} \sum_{x \in \mathcal{S}}\int_y p(y|x)\log p(y|x)dy
$$
The conditional probability $p(y|x|)$ follows a Gaussian distribution:
$$p(y|x) = N(y; \bar{y}(x), \sigma^2_y(x))
$$
Substituting in the information gain equation:
$$
I(\mathcal{S}_j, \boldsymbol{\theta}) \propto \sum_{x\in\mathcal{S}_j}\log(\sigma_y(x)) - \sum_{i \in \{L,R\}} \left(\sum_{x \in \mathcal{S}^i_j} \log(\sigma_y(x))\right)
$$
Generalizing this equation to multivariate variables:
$$
I(\mathcal{S}_j, \boldsymbol{\theta}) = \sum_{\mathbf{v}\in\mathcal{S}_j}\log(|\boldsymbol{\Lambda}_\mathbf{y}(\mathbf{v})|) - \sum_{i \in \{L,R\}} \left(\sum_{\mathbf{v} \in \mathcal{S}^i_j} \log(\boldsymbol{\Lambda}_\mathbf{y}(\mathbf{v}))\right)
$$
where $\boldsymbol{\Lambda}_\mathbf{y}$ is the conditional covariance matrix computed from probabilistic linear fitting.

---
## Source
[[9781447149293 Decision Forests for Computer Vision and Medical Image Analysis|Decision Forests for Computer Vision and Medical Image Analysis]]