---
alias: "Density forest information gain optimize for compact cluster sizes."
---
# Density forest information gain optimize for compact cluster sizes.
## Metadata
- ID: 202109211403
- Date Created: [[2021-09-21]]
- Status: #status/in_progress
- Note Type: #note/permanent_note
- Topic: [[Density Forest]], [[Machine Learning]]
- Tags: 
---

The unsupervised entropy information gain of a multivariate Gaussian Mixture Model for a density forest is
$$
I(\mathcal{S}_j,\boldsymbol{\theta}) = \log\left( |\Lambda(\mathcal{S})|\right) - \sum_{i=\{L,R\}}\frac{|\mathcal{S}_j^i|}{|\mathcal{S}_j|}\log\left( |\Lambda(\mathcal{S}^i_j)|\right)
$$
where $\mathcal{S}$ is the training data and $\Lambda$ is the covariance matrix.

The determinant of the covariance matrix is a function of the ellipsoid surrounding a cluster. So, the maximization of the information optimizes for the splitting of data points into compact clusters, with the centers of the clusters located in areas of high density and the boundaries between clusters located near areas of low density.
> ![[9781447149293 Decision Forests for Computer Vision and Medical Image Analysis#^b9feeb]]

---
## Source
[[9781447149293 Decision Forests for Computer Vision and Medical Image Analysis|Decision Forests for Computer Vision and Medical Image Analysis]]