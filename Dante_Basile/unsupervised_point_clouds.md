# Unsupervised Multi-Task Feature Learning on Point Clouds

Dante Basile

## Problem Space
* Point clouds: sparse order-invariant sets of interacting points defined in a coordinate spaceand sampled from object surfaces
* spatial-semantic information

## Approach
* Self-supervised learning: define pretext task using only info present in data (surrogate supervisory signal)
    * Define encoder to map samples into a latent space
    * Use clustering, classification, decoding