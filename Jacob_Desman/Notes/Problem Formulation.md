# Problem Formulation References
Created: 2022-02-21, 19:42

Edited: 2022-02-22

**Tags:**

**References:** 

## Interesting Papers Referencing Label Noise
### Learning with Noisy Labels
- https://proceedings.neurips.cc/paper/2013/file/3871bd64012152bfb53fdf04b401193f-Paper.pdf
	- https://papers.nips.cc/paper/2013/hash/3871bd64012152bfb53fdf04b401193f-Abstract.html
- Modifying a surrogate loss function leads to provable risk bounds where the risk is calculated on the loss of the clean distribution
- Uses cross validation to estimate the noise levels for their modeling
- 2 approaches
	1. Surrogate loss is an unbiased estimate of the loss function
	2. Minimizer of risk of risk under noisy distribution differs only where it thresholds $\eta = P(Y=1|X)$  

### Improving Robustness of Random Forest Under Label Noise
- https://ieeexplore.ieee.org/document/8658395
- Setup: label noise in training data may impact purity evaluation and degrade performance. 
	- [[Problem Formulation#Improving Robustness of Random Forest Under Label Noise|Another Paper]] makes the argument that decision trees and random forest are robust under **symmetric noise**, but not **asymmetric**
- Label noise model
	- **Class conditional random label noise**
- Their argument
	- RF minimizes classifier loss by greedily reducing uncertainty of training samples
	- They propose control over an overall classifier loss and its proper minimization
		- *Comment:* the reweighting of KDG might help with this? Also, pushing all samples through the trees may add this global notion of loss rather than the subsets via bagging
	- They claim their loss function is noise tolerant
	- However, doesn't their equation 13 rely on knowing the noise rates (equation (9))? How do they not need to be known in practice, as they say?
	- Also has a few more experiments. They use MNIST, CiFar10, letter, covtype, and usps with injected 
- Note: no theoretical results/proofs

### On The Robustness of Decision Tree Learning Under Label Noise
- https://arxiv.org/abs/1605.06296
- *Note*: One of the more theory heavy papers I can find on the topic
- Intro:
	- Dcision tree learning is better than SVM or LR w.r.t robustness to label noise, but naive Bayes is better than all of them
	- **Random noise model**
		- Their analysis assumes symmetric noise model because it is easier to analyze. 
- Goal:
	- Show in large sample limit, under symmetric or uniform label noise, the split rule that optimizes the objective function under noisy data is same as that under noise-free data
- RF are empirically robust to label noise
	- They note that most studies are empirical
	- "If noise rates are not known (and cannot be reliably estimated), it appears difficult to establish robustness of impurity based split criteria"

### Classification with Noisy Labels by Importance Reweighting
- https://arxiv.org/abs/1411.7718
- Intro
	- **Random classification noise model**, does not assume symmetry
	- Relies on finding a way to estimate the noisy distribution/the probabilities of flipping labels
- Related work
	- Some other works (which I have definitely seen, including the first paper on here), propose robust surrogate loss functions
	- Other works attempt to estimate the inversed noise rates 
- Setup
	- Corrupted labels, general RCN model given by ![[Pasted image 20220221201118.png]]
- Goal
	- Reweight the loss function by estimating properties of the corrupted label distribution

### Probabilistic Random Forest
- https://arxiv.org/abs/1811.05994
- Setup
- Notes
	- Determines probability for an object to propagate from the top node
	- Account for predictions given by all terminal nodes in final probability, then majority vote by the largest probability in the tree
- Has a few more types of noise experiments
	- Noise in the labels
		- **Uniform distribution/random classification noise** model
		- Shows that it beats RF
	- Noise in the features (a simple and complex version)
	- Different noise characteristics in the training and test sets

### Complete Random Forest Based Class Noise Filtering Learning for Improving the Generalizability of Classifiers
- https://ieeexplore.ieee.org/document/8481535


## Obeservations
- A few types of ways of handling noisy labels
	1.  Reducing label noise in the training data
	2. Determine the proportion of label noise in the sample and incorporate into classifier training/loss function
	3. Model structure is somehow designed with robustness to noise
- The extent of theory that most papers has is deriving a surrogate loss function