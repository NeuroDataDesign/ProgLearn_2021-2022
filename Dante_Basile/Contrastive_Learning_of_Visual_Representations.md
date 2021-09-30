# A Simple Framework for Contrastive Learning of Visual Representations

Dante Basile

## Self-supervised contrastive learning
* Does not utilize specialized architectures of a memory bank
* Composition of data augmentations
* Introduced learnable non-linear transformation between representation and contrastive loss
* Greater benefit from increased batch size and training steps relative to supervised learning
* Benefits from deeper and wider networks similar to supervised learning

## Contrastive learning outperforms existing self and semi supervised methods on ImageNet

## Contrastive learning framework
* Uses contrastive loss to maximize agreement between the results of different augmentations
    * Loss function: $\mathcal{l}_{i, j} = -\log{ \frac{\exp{(\texttt{sim}(\textbf{z}_i, \textbf{z}_j) / \tau)}} {\sum_{k=1}^{2N}{\mathbb{I}_{[k \not{=} i]} \exp{\texttt{sim}(\textbf{z}_i, \textbf{z}_k) / \tau)}}} }$
    * $(i, j)$ is a positive pair. $z_i$ is the network's contrastive loss projection head output for sample $i$. $N$ samples with another $N$ augmentations, one for each sample, $2N$ data points total. $\tau$ is the temperature parameter.
    * The final loss is computed across all positive pairs $(i, j)$ and $(j, i)$ in a mini-batch
* Positive pair: two augmented images from the same sample
* Negative pair: two augmented images from different samples
* One positive pair (anchor), many negative pairs
* Train the network to detect positive pairs
* Vary batch size instead of using memory bank
* Aggregate batch normalization mean and variance over all devices

## Gains show translation to semi-supervised learning

## Transfer learning
* Outperforms baseline with hyperparameter tuning for each dataset