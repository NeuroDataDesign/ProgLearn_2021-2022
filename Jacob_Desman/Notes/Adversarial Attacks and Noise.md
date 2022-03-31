# Adversarial Attacks and Noise
## Week of 3/14
**Goal**: refresh my memory on how adversarial attacks work, but more specifically for random forest since I once studied this in the CS Deep Learning course. In addition, see on adversarial noise (label noise specifically?)

### Code
- https://github.com/Trusted-AI/adversarial-robustness-toolbox
	- One repo that seems to be fairly popular as far as github stars and implements a number of the algorithms discussed below
	- Based on examples, could be compatible with KDG
- https://github.com/bethgelab/foolbox
	- Adversarial examples for neural networks

### Articles
#### Adversarial Machine Learning Applied to Intrusion and Malware Scenarios: A Systematic Review
https://ieeexplore.ieee.org/document/9001114 is a pretty good paper that states things colloquially, and is easy to follow

- Adversarial ML
	- Goal: trick ML models via deceptive input. 
	- Image recognition is a domain where this is often disucssed
	- The attack is a method to generate adversarial examples. 
	- Whitebox vs. blackbox
		- **Whitebox attack**: attacker has complete access to model (i.e. architecture and parameters)
		- **Blackbox attack**: attacker has no access to model, can only observe outputs
- How attacks "work"
	- **Poisoning attacks**: adversarial contamination of the training data
		- Note: this is basically the asymmetric noise case
		- Note: this could also be explored in the forward transfer cases that Tiffany is working on
	- **Evasion attacks**: 
		- "most prevalent and researched types of attacks"
		- Deceive previously trained classifiers
- Popular methods
	- Limited-memory BFGS (L-BFGS)
		- Find a small perturbation (minimize L2 distance) similar to a correct example that is incorrectly classified
		- Pros/Cons: generates good adversarial examples, but very computationally intensive
	- Fast Gradient Sign Method (FGSM)
		- Compute the gradient of loss w.r.t input and perturb each feature with the sign of the gradient
		- Pros/Cons: quick to compute, generally less effective at finding adversarial examples
	- Jacobian-based Saliency Map Attack (JSMA)
		- Compute saliency maps to determine how much features contribute to classification process. Then, perturb each by some value $\theta$ in order of decreasing contribution and stop when misclassification occurs.
		- Pros/Cons: more computationally intense than FGSM, but fewer features perturbed (samples look more similar to original input)
	- Deepfool
		- Minimize L2 distance betwene perturbed and original samples
		- Calculate a linear decision boundary that separtes samples into different classes, then perturb perpendicular to decision boundary. Since many boundaries are non-linear, add perturbations iteratively by attacking several times and finishing when adversary is found
		- Pros/Cons: generates samples with fewer perturbations than FGSM and JSMA and has a higher misclassification rate, but even more computationally intensive
	- Carlini & Wagner attack (C&W)
		- Based on L-BFGS attack
		- Proposes using a different loss function than the original used in training (ex. hinge loss instead of CE loss), and make the optimization problem easier to solve via some other methods
		- Pros/Cons: more efficient that L-BFGS at generating adversarial examples, could defeat SOA defenses
	- Zeroth-order optimization attack (ZOO)
		- Allow estimation of the gradient without access to the classifier -> good for black box attacks
		- Zeroth-order stochastic coordinate descent to optimize adversarial samples, iteratively adding perturbations to each feature
		- Doesn't require information on classifier nor training of substitute models
		- Pros/Con: similar performance to C&W, but requires a large amount of queries on the oracle

### Our goals
- Do we want to observe how KDG algorithms perform under adversarial attacks?
- Could this be interesting to explore with Tiffany's algorithm and the forward transfer?

## Week of 3/28
### Papers and brainstorming
- [Adversarial Robustness with Non-uniform Perturbations](https://arxiv.org/abs/2102.12002)
	- Fig 1: X axis perturbation size, y axis error. Can bound the norm of the perturbations and so that the x-axis is consistent, and can compare across RF vs. KDF and KDN vs. NN.
		- This would tell us if KDG is more robust to small perturbations than the algorithms' counterparts
	- Code available online
	- But this is adversarial training - we would want to do an evasion attack most likely
- Ashwin discussed a PGD experiment that he did with KDCNN
	- However, this is a white-box attack
	- The "easiest" method would be to do some sort of black-box attack
- Idea 1
	- If picking an attack method with a chosen perturbation size ($\epsilon$), then can create a figure where the x-axis is $\epsilon$ and the y-axis is average accuracy or error. 
		- Compare KDF vs RF and KDN vs NN
	- See [Adversarial Robustness with Non-uniform Perturbations](https://arxiv.org/abs/2102.12002) Fig. 1 for an example of this
		- ![[Pasted image 20220328175017.png]]
- Idea 2
	- Report average $l_2$ and/or $l_{\infty}$ norm of the generated attack samples. The idea that if one method is more robust, than the norms of the generated samples should be larger.
	- Could investigate on both simulated and in the OpenML data
	- Papers
		- [Robust Decision Trees Against Adversarial Examples](https://arxiv.org/abs/1902.10660)
			- They report avg $l_{\infty}$ distance for their "robust" method and "natural" method
			- ![[Pasted image 20220328175001.png]]
- Idea 3
	- X-axis as number of images successfully attacked and y-axis as a constraint on the norm. Shows how robust to perturbation the samples are?
	- Papers
		- [Adversarial Robustness Assessment: Why both L0 and L_infity Attacks are Necessary](https://arxiv.org/abs/1906.06026)
		- ![[Pasted image 20220328174938.png]]

### Papers
#### How to compare adversarial robustness of classifiers from a global perspective
- https://arxiv.org/abs/2004.10882
- Intro
	- Must understand what a small pertubration is. Needs 1) a distance function and 2) choice of scale to create the **threat model** under which a model is robust
	- Often use $lp$ norms, like l1, l2, and $l_{\infty}$. Perturbation threshold $\epsilon$
	- To show superiority of a new method, typically compare accuracies for a handful of threat models and datasets (ex. l_infinity eps = 0.1 and l2 eps = 0.3 )
- Experiments
	- Note that this is for adversarial training. They show the risk at a number of perturbation threshold $\epsilon$

#### Adversarial Robustness Assessment: Why both L0 and L_infity Attacks are Necessary
- https://arxiv.org/abs/1906.06026
- Intro
	- Formalize 4 problems
	1. Model agnostic quality assessment
	2. Insufficient evaluation - several types of adversarial samples and attack variations, but each has own bias. Quality assessment needs few but sufficient tests to provide in-depth analysis
	3. False adversarial samples - need for inspection of adversarial samples should not be necessary
	4. Perturbation dependent results - varying amount of perturbation -> varying adversarial accuracy. Different networks may differ in sensitivity to attacks given a varied amount of perturbation -> can result in double standards or hide important information
	- Addressing P1: **black-box** attacks are desirable for model agnostic evaluation. 
	- Addressing P2 and P3: propose using attacks based on L0 and L_infty to avoid creating adversarial attacks not correctly classifier by humna beings after modifications
		- ???
	- Addressing P4: define robustness in terms of a contrainst threshold in this paper
- Some notes
	- Few pixel attack: L0 black-box attack
	- Threshold attack: L_infty black-box attack
- Results
	- Shows adversarial accuracy results for L0 and L_infty attacks over a variety of thresholds. 
		- Adversarial accuracy: "corresponds to the accuracy of the adversarial attack to create adversarial samples to fool neural networks"
		- "Without knowing anything aboutt he learning system and in a constrained setting, black-box attacks are still able to reach more than 80% accuracy"
	- Shows **number of samples successfully attacked vs. the threshold**
		- Gives an idea of how difficult it is to fool a network

#### ZOO: Zeroth Order Optimization based Black-box Attacks to Deep Neural Networks without Training Substitute Models
- https://arxiv.org/abs/1708.03999
- Intro
	- General sketch of method: needs model confidence score as the output. Goal is to optimize the important features first by seeing how much they chance the confidence
- Results
	- Benchmarks their method using a $L_2$ norm

#### Imperceptible Adversarial Attacks on Tabular Data
- https://arxiv.org/abs/1911.03274
- https://github.com/axa-rev-research/LowProFool
	- Note that this is what they introduce as a better metric, but this is a white box attack
- After Tuesday OH, Jayanta wanted to know how relevant adversarial attacks are on tabular data. The hot topic in adversarial attacks is largely for images. Therefore, this paper is good to look at 
- Introduction
	- Consider bank customer applying for  aloan. A ML model is used to make the decision regarding the acceptance, which is based on tabular data. However, it is intuitively possible to perturb the data such that the data crosses the decision boundary. This is show in Fig. 1
	- ![[Pasted image 20220330150938.png]]
- Imperceptible attacks
	- **Imperceptibility** is still a subject of debate
	- Defining adversarial attacks: colloquially, some say
		- Adversarial examples are close to nautral inputs but classified incorrectly
		- That the perurbation must be *imperceptible*
		- Some allow it to be visible, but confined to a small patch of image
		- Others generate a discernible adversarial patch to always classify as one class
	- Commonly, some $l_p$ norm is used, but this may not be sufficient to measure perceptual similarity between images

#### Adversarial Attacks for Tabular Data: Application to Fraud Detection and Imbalanced Data
- https://arxiv.org/abs/2101.08030
- Main contributions
	- novel approach to adapt adversarial attack algorithms that are **used in the image domain to tabular data**
		- **Class balance**: Balance of samples between classes is different sometimes in the binary case. In theirs, it is. They introduce the concept of a decision thrsehold within the attack algorithms 
		- **Value range**: feature ranges can assume different scales. 
		- **Imperceptibility**: they assume imperceptibility is related to the number and entity of changes, and use it in the context of fraud
- Algorithm modifications
	- Basically used a custom loss function for ZOO from the adversarial robustness toolbox (ART)