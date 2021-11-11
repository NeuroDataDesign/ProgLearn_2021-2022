# Geodesic Forests

Dante Basile

## Motivation
* Want to use KNN for Kernel function on $x$. However, $x$ is a noisy measurement of $\tilde{x}$. We want to learn to understand distances on the underlying manifold of the true distribution.
* Unsupervised: learn only on the features of $x$. Ignore labels $y$.
* Dimensionality reduction when dimansionality $p$ is larger than sample size $N$
* Approximation algorithms when $N$ is very large

## Geodesic Distance
* Shortest path between two points in a Riemannian manifold
* Learning: estimate geodesic distances between pairs of points in a data corpus
* Use manifold learning algoriths to learn latent structure of data, then estimate distances in estimated latent space

## Geodesic Forest Method
* Achieve near linear space and time complexity
* Approximate the true latent geodesic distances

## Implementation
* Based on Random Forest
* New splitting criteria: Fast-BIC
    * Do not split points in original feature space
* 2-GMM Splitting with Fast-BIC

## Drosophila example