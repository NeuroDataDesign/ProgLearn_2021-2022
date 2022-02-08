# [Lifelong Learning With a Task Oracle](https://arxiv.org/pdf/2011.04783.pdf)
Amanda Rios and Laurent Itti

## Abstract
- Supervised deep neural networks known to undergo sharp decline in accuracy of older tasks when new ones are learned = "catastrophic forgetting"
- current continual learning relies on biasing and/or parpartitioning a model to accommodate successive tasks incrementally. However, these methods largely depend on the availability of a task-oracle to confer task identities to each test sample, without which the models are entirely unable to perform.
- propose/compare task-assigning mappers which require little memory overhead
1. incremental unsupervised prototype using either nearest means, Gaussian mixture models, or fuzzy ART backbones
2. supervised incremental proto assignment with fast fuzzy ARTMAP
3. shallow perceptron trained via a dynamic coreset
- proposed model variants trained either from pre trained feature extractors or task-dependent feature embeddings of the main classifier network
- overall, methods perform close to a ground trouth oracle

## Learning without a task oracle
- major limiatation of task-dependent methods is inability to perform without task oracle
- determining task ID's is a learning procedure itself subject to catastrophic forgetting
- propose several task-mapper algo's to substitute the oracle input 
- models prio simplicity and low memory usage 
- to eval task mappers and baselines, use parameter superposition PSP with Beneficial Biases BD as standard state of the art task dependent backbone for fine grained classification 

![image](https://user-images.githubusercontent.com/89429238/152909184-c55ab8f8-0e89-418e-a726-42947b29811d.png)

### Incremental Unsupervised Task Mappers
