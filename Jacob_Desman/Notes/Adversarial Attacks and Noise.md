# Adversarial Attacks and Noise
**Goal**: refresh my memory on how adversarial attacks work, but more specifically for random forest since I once studied this in the CS Deep Learning course. In addition, see on adversarial noise (label noise specifically?)

## Code
- https://github.com/Trusted-AI/adversarial-robustness-toolbox
	- One repo that seems to be fairly popular as far as github stars and implements a number of the algorithms discussed below
	- Based on examples, could be compatible with KDG

## Articles
### Adversarial Machine Learning Applied to Intrusion and Malware Scenarios: A Systematic Review
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

## Our goals
- Do we want to observe how KDG algorithms perform under adversarial attacks?
- Could this be interesting to explore with Tiffany's algorithm and the forward transfer?
