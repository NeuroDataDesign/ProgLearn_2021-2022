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
- Multi-task learning optimization easier than sequential task optimization. We want to mimic biological systems which optimize sequentially
	- **Catastrophic forgetting**  - classical machine learning systems have performance on prior tasks drop when training on new tasks (sequential learning)
- **Omnidirectional learning**
	- Builds on ProgNN (new tasks yield additional representational capacity)
		- Problems with ProgNN - fail to transfer backwards & require quadratic space and time complexity in sample size
	- **Proposal** - introduction of representation ensembling which enables omnidirectional transfer
	  - Uses "omni-voter" layer & reduces computational time and space to quasilinear  
  - Omnidirectional learning algorithms
	  - Omnidirectional Forests (Odif)
	  - Omnidirectional Networks (Odin)
### Results
#### A computational taxonomy of lifelong learning
- Fixed resources vs growing resources
  - Notation
    - Soft-O notation - quantifies complecity
    - *n* - sample size
    - *T* - number of tasks
	- Fixed resource lifelong learning methods are parametric - representational capacity does not depend on sample size and task number
		- Examples: EWC, Online EWC, SI, and LwF
	- Semi-parametric algorithm - representational capacity grows slower than sample size
	  - Examples: ProgNN
		  - ProgNN has quadratic space complexity due to lateral connections
	  - DFCNN improves on ProgNN - introduces knowledge base with lateral connections to each column (avoids pariwise connections)
- ODIN eliminates lateral connections between columsn of network (makes space complexity linear)
	- Also has linear time complexity - only non-parametric algorithm
### Illustrating Omnidirectional Learning with ODIF
- Omnidirectional learning in a simple environment
	- ODIF and RF have same generalization error on XOR when trained on XOR
	- When given XNOR data, RF performance gets worse on XOR (doesn't account for change in task) while ODIF improves
	- ODIF adjusts to classifying XNOR data well and improves with XNOR data
    - Demonstrates forward and backward transfer unlike RF which catastrophically forgets tasks
- Omnidirectional learning in adversarial environments
	- Suite of R-XOR examples with varied rotation angle
	- Amount of transfer can be a function of
		- Difficulty of learning good representation of each task
		- Relationship between the two tasks
		- Sample size of each
### Real Data Experiments
- Resource Growing Experiment
	- ODIF and ODIN compared to ProgNN and DF-CNN
	  - ODIF and ODIN have positive forward transfer for every task
	    - More robust to distributional shift than ProgNN and DF-CNN
	  - ODIF and ODIN demonstrate positive backwards transfer
      - ProgNN and DF-CNN do not show catastrophic forgetting but also don't show backwards transfer
	  - ODIF and ODIN have positive final transfer efficiency for all tasks 
      - ProgNN and DF-CNN have negative final transfer efficiency for at least one task
## Discussion
- ODIF and ODIN have possibility of achieving both forward and backward transfer (due to leveraging resources learned from other tasks)
- ODIF and ODIN store old data to vote on newly learned transformers to achieve backwards transfer
	- Storing data does not increase computational complexity - remains quasilinear
	- Can't achieve backwards transfer without storing all past data (computation time becomes quadratic)
	  - Extension - use generative model to obviate need to store all data
- Omnidirectional algorithms mature particular skills using rich representer dictionary
