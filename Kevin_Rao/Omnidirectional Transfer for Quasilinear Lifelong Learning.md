# Omnidirectional Transfer for Quasilinear Lifelong Learning
## Metadata
- Author: [[Joshua T. Vogelstein]], [[Jayanta Dey]], [[Hayden S. Helm]], [[Will LeVine]], [[Ronak D. Mehtra]], [[Ali Geisa]], [[Gido M. van De Ven]], [[Emily Chang]], [[Chenyu Gao]], [[Weiwei Yang]], [[Bryan Tower]], [[Jonathan Larson]], [[Christopher M. White]], [[Carey E. Priebe]]
- Date Created: [[2021-09-01]]
- Date Published: [[2021-08-20]]
- Status: #status/complete 
- Source: https://arxiv.org/abs/2004.12908
- Source Type: #source/paper 
- Note Type: #note/literature_note
- Topic: [[Machine Learning]], [[Lifelong Learning]]
- Tags: 
---
## Summary
## Highlights
### Introduction
- Training machine learning systems multiple different tasks is harder sequentially than simultaneously
	- **Catastrophic forgetting** occurs during sequential learning, causing performance on prior tasks to drop upon training to do new tasks.
- Approaches to overcome catastrophic forgetting
	- Algorithm with fixed resources reallocates resources to incorporate new knowledge (adulthood)
	- Algorithm adds new resources as new data comes in (neurogenesis, neuroplasticity)
	- Both approaches embody continual/lifelong learning: learn new tasks without forgetting the old ones
	- Many algorithms cannot transfer knowledge forward and none can transfer knowledge backward
		- What does this mean by transfering knowledge forward and backward? #question/unanswered
	- Inability to transfer knowledge omnidirectionally is a key limitation of artificial intelligence
- **Omnidirectional learning**
	- Builds on ideas from Progressive Neural Networks
		- New tasks increase representational capacity
		- Can only transfer forward.
		- Require quadratic space and time complexity in sample size.
	- Uses an "omni-voter" layer for omnidirectional transfer
		- Reduces computational time and space to quasilinear (linear up to polylog terms)
- Omnidirectional learning algorithms
	- Omnidirectional Forests (Odif)
	- Omnidirectional Networks (Odin)
	- Resource building but leverages prior representations
	- Converts "juvenile" resource building to "adult" resource building while maintaining omnidirectional learning capability and efficiency
### Results
#### A computational taxonomy of lifelong learning
- Fixed resources vs growing resources
	- [[Soft-O notation]] ($\tilde{O}$)
		- $n$ -- sample size
		- $T$ -- number of tasks
		- $f(n, t) = \tilde{O})g(n,T))$ when $|f|$ bounded above asymptotically by a function $g(n, T)$ up a constant factor and polylogarithmic terms,
	- Fixed resource lifelong learning methods are parametric -- representational capacity does not depend on sample size and task number
		- $\tilde{O}(1)$
	- Semi-parametric algorithm -- representational capacity grows slower than sample size
		- ProgNN $\tilde{O}(T^2)$ space complexity due to lateral connections.
			- Scales quadratically with $n$ when $n\propto T$.
		- Algorithmed implemented as Total Replay
		- DFCNN improves on ProgNN by introducing a knowledge base with lateral connections to each column, avoiding pariwise connections.
- ODIN removes lateral connections between columsn of network, reducing space complexity to $\tilde{O}(T)$.
	- Stores data to enable backwards transfer but linear time complexity.
	- Representational capacity naturally increases with complexity of task.
### Illustrating Omnidirectional Learning with ODIF
- Omnidirectional learning in a simple environment
	- ODIF and random forest have same generalization when trained on XOR
	- Random forest does not account for change in task, so its performance worsened when XNOR data introduced
	- ODIF can adjust to classifying XNOR data well and improves with additional data, demonstrating positive forward and backward transfer unlike random forest
- Omnidirectional learning in adversarial environments
	- A task $t$ is adversarial with respect to task $t’$ if the true joint distribution of task $t$ without any domain adaptation impedes performance on task $t’$.
		- E.g. Gassuan XOR is adversarial for Gaussian XOR rotated  by $45^\degree$ (R-XOR)
	- For ODIF, imperfect discriminant boundaries can improve performance for R-XOR when trained on XOR, producing positive forward transfer.
	- Both forward and backward transfer is negative for RF
	- Amount of transfer can be a function of
		- Difficulty of learning good representation of each task
		- Relationship between task
		- Sample size of each
### Real Data Experiments
- Vision and language modalities tested
- CIFAR 100 challenge
	- 50000 training and 10000 testing samples
	- 32x32 RGB image of common object with 100 possible classes
	- 10x10 divides data into 10 tasks with 10 classes
- Compared ODIF and ODIN to deep lifelong learning algorithms
- Under lifelong learning framework, learning agent sequentially trained on sequential tasks in constrained capacity and computation time.
- Resource Growing Experiment
	- ODIF and ODIN compared to ProgNN and DF-CNN
	- ODIF and ODIN have positive forward transfer for every task; more robust to distributional shift than ProgNN and DF-CNN
	- ODIF and ODIN demonstrate positive backwards transfer, indicating that performance on prior tasks increase with new task. ProgNN and DF-CNN do not, but no catastrophic forgetting.
	- ODIF and ODIN have positive transfer efficiency for all task while ProgNN and DF-CNN have negative final transfer efficiency for at least one task.
- Aversarial experiments
	- Transfer efficiency of both ODIF and ODIN invariant to rotation angle while other approaches more sensitive to rotation angle.
## Discussion
- ODIF and ODIN have possibility of achieving both forward and backward transfer from leveraging resources learned from other tasks.
- Forest-based representation can add new resources when appropriate
- ODIF and ODIN store old data to vote on newly learned transformers to achieve backwards transfer.
	- Storing data does not increase computational complexity
	- Not obvious how to achieve backward transfer with bounded and space complexity even by allowing storage of all past data since it would make computational time quadratic.
	- Extension could be storing data using generative model
- Paradigm of ensembling representations besides learners can be applied more generally.
	- Federated learning central in artificial intelligence due to importance in differential privacy
- Representation ensembling resembles constructivist view of brain development.
	- Brain progressive elaboration of neural circuit resulting in augmented cognitive representation while maturing in a certain skill
	- Omnidirectional algorithms mature particular skills using rich representer dictionary.
## Further References
-    Andrei A Rusu, Neil C Rabinowitz, Guillaume Desjardins, Hubert Soyer, James Kirkpatrick, Koray Kavukcuoglu, Razvan Pascanu, and Raia Hadsell. [[Progressive neural networks]]. arXiv preprint arXiv:1606.04671, 2016.
---
## See Also:
- 