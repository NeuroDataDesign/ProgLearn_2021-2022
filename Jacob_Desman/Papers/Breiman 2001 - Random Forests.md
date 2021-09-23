# Breiman 2001 - Random Forests
Created: 2021-09-20, 22:55

Edited: 2021-09-21

**Tags**: #ml #forest #paper 

**References:** [Breiman 2001](https://link.springer.com/content/pdf/10.1023/A:1010933404324.pdf)

**Related:**

## Commentary
This seems to be a pretty involved paper. As this is my first go, I intend to write a blurb for each section with a high level overview and major takeaways from the paper. In the future, I might take a second pass with more notes on the path, although I am reading through those parts as well to ensure I have a basic understanding of what is going on. 

## Random Forests
* General Random Forest Procedure
	* kth tree, generate random vector $\Theta_k$, independent of past vectors. Design random vector *somehow*
	* **Bagging**: take a random subset of data $\Theta_k$ for a tree
* **Random forests**: A classifier consisting of a collection of tree-structured classifiers $\{h(x, \Theta_k), k=1,...\}$, where the $\{\Theta_k\}$ are iid random vectors and each tree casts a unit vote for the most popular class at input x.

## Characterizing the Accuracy of Random Forests
* Margin equation - measures the extent to which average number of votes at X, Y for the right class exceeds the average vote for any other class. 
* Generalization error - converges as more trees are added --> random forests do not overfit as more trees are added.
	* Depends on:
		1. Strength of individual classifiers in the forst
		2. Correlation between them into terms of margin functions
	* c/s2 ratio: correlation / square of strength --> smaller is better. 
		* Lower correlation or higher strength --> better for accuracy
	* Overall: Strong Law of Large Numbers and tree structure --> "As number of trees increases, surely all sequences converge to \[equation\]"

## Using Random Features
* "Adaboost" works better than the pre-2000 algos. --> What is AdaBoost (Adaptive Boosting)?
* 2 reasons for bagging
	* Enhance accuracy when random features used (decrease correlation)
	* Give ongoing estimates of generalization error (estimates are out-of-bag)

## Random forests using random input selection
* Random input selection has the advantage of being much faster than AdaBoost or Bagging in data sets with many variables.

## Random forests using linear combinations of inputs
* Forest-RC: using linear combinations of a number of input variables --> create more features
	* Works better than AdaBoost on synthetic data
* Encode categrical variables using dummy variables 0 and 1
* F must be relatively high (about int($\log_2 M + 1$)) to get enough strength to provide good accuracy 
	* Low F --> low correlation and low strength

## Empirical results on strength and correlation
* Better random forests (lower generalization error) have lower correlation between classifiers and higher strength
* Randomness must be down sucht aht it aims to decrease the correlation between trees while maintaing reasonable strength

## Conjuecture: Adaboost is a random forest
* I'm a bit confused as to the relationship between random forest and AdaBoost. 
	* I think the idea is that we can set up a random forest classifier such that we have $K$ sets of weights, and probabilities for $p(K)$ with outcome $|Theta$. If $\Theta = k$, then we grow a classifier $h(x, \Theta)$with $w(k)$ weighting the training set. 
* AdaBoost determines weights on the training set for the input to next classifier based on the prior step's misclassifications
	* Note that noise in the classification labels will cause AdaBoost to overfit to noise, warping the output space

## The effects of output noise
* Random alteration of some output labels --> decrease AdaBoost accuracy.
	* Makes sense given the points from [[Breiman 2001 - Random Forests#Conjuecture Adaboost is a random forest|the previous section]]
* Bagging and random split selection are more robust to noise. 

## Data with many weak inputs
* Weak input: a single feature or group of inputs that cannot distinguish between the classes. Difficult for neural nets and trees. 
	* Ex. Frequent problem in medical cata circa 2001. 
* Author notes as F increases, the goal to increase strength while maintaining low correlation is achieved.
* *Forests can work with very weak classifiers as long as their correlation is low*

## Exploring the random forest mechanism
* Interpretability is important - medical experiments needs to be able to understand variable interactions
* One idea: out of bag testing, but $m$th variable is randomly permuted and out-of-bag data run down that tree. The $m$th variable with noise is compared with the true class label to give misclassification rule. 
	* Goal: determine the percent increase in misclassification rate (out of bag modified vs. out of bag variables intact)
* Various experiments

## Random forests for regression
* Instead of class labels, tree predictor $h(x, \Theta)$ outputs numerical values rather than class labels
* Keep in mind minimizing the mean squared error

## Empricial results in regression
* Regression forests, in addition to bagging (training data), use random feature selection.
	* More features --> lower PE*(tree) but higher correlation.  

## Remarks and conclusions
* Random forests are effective in prediction 
* Does not overfit because of the Law of Large Numbers
* Type of randomness matters
* "Their accuracy indicates they act to reduce bias. The mechanism for this is not obvious"