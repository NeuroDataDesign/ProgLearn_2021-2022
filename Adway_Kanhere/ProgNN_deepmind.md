# Progressive Neural Networks

[![arXiv](https://img.shields.io/badge/arXiv-2004.12908-red.svg?style=flat)](https://arxiv.org/abs/1606.04671)

## A 1 minute summary:

Main topic: Proposes a novel approach to learning that is immune to forgetting and can leverage prior knowledge

- The model is organized such that they allocate a new column for each task (sequence of fully connected layers)
- The progressive network starts with a single column for a task. When switching to the second task, the parameters of the previous tasks are "frozen" and a new column with parameters is instantiated via lateral connections.
- Introduces adapters: NN layers are augmented with non-linear lateral connections. This is done to improve inital conditioning and perform dimensionality reduction
- The paper discusses several experiments performed by PNNs on a sequence of RL based tasks.
- The paper also discusses the model's limitations
    - Model grows linearly as tasks increase
    - It does not work under fixed memory and compute conditions
    - The task labels need to be provided during testing
