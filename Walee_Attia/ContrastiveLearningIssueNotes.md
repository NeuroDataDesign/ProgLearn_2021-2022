# Notes for Contrastive Learning Issue

Looking at Ronan Perry's comment on original issue:

The goal is to explicitly learn the network transformer in proglearn using constrastive loss.

Contrastive learning's goal is to learn an embedding space such that similar samples stay closer together than farther ones, enabling the transfromer to distinguish between different samples.

[Official Implementation](https://github.com/google-research/google-research/tree/master/supcon)

[Reference for supervised version](https://arxiv.org/abs/2004.11362)
[Reference for unsupervised version](https://arxiv.org/pdf/2002.05709.pdf)

The aim would be to implement contrastive learning and then validate by comparing accuracy and transfer efficiency to determine the best contrastive loss to use.

Ronan's prior [work](https://github.com/rflperry/ProgLearn/blob/contrast-loss/benchmarks/cifar_exp/fte_bte_exp.py) on this and [benchmarks](https://github.com/rflperry/ProgLearn/tree/contrast-loss/benchmarks/cifar_exp/result/figs)
