# Contrastive learning transformer for PL Network

## Issue
Documented [here](https://github.com/neurodata/ProgLearn/issues/426)

### Background
* Current loss function is softmax
* Contrastive may be better for subsequent kNN
* Official implementation [here](https://github.com/google-research/google-research/tree/master/supcon) with
[unsupervised](https://arxiv.org/pdf/2002.05709.pdf) and [supervised](https://arxiv.org/abs/2004.11362) papers

### Requested features
* Validate by comparing accuracy and transfer efficiency
* Determine the best form of contrastive loss to use

### Prior experiments
* Proveded example of attempted implementation [here](https://github.com/rflperry/ProgLearn/blob/contrast-loss/benchmarks/cifar_exp/fte_bte_exp.py)
with [benchmarks](https://github.com/rflperry/ProgLearn/tree/contrast-loss/benchmarks/cifar_exp/result/figs)