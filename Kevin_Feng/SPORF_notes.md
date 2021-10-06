# Sparse Projection Oblique Randomer Forests [SPORF](https://arxiv.org/pdf/1506.03410.pdf)
## Intro
What is an *axis-aligned* decision tree?
- trees that spli only along feature dimensions
What is and why is SPORF better than exisiting decision trees?
- SPORF uses very sparse random projections, significantly improves accuracy over existing algo's
- SPORF yields, improved performance over existing decision forests, while mitigating comp effieciency and scalability and maintaining interpretability 
- current oblique decision methods forfeit many desirable properties of axis-aligned trees

What does SPORF do differently?
- at each node of each tree, sporf searches for splits over a sample of very sparse random projections, rather than axis-aligned splits
- very sparse proj's preserve desirable properties of axis-aligned decision trees, while mitagating issues

Oblique extensions to Random forest
- introduce many different methods that all utilize some flavor of random projections 

### Random Projection

![image](https://user-images.githubusercontent.com/89429238/135372794-7b1b8328-ddc8-44ac-b4e9-22f555992096.png)

- commonly used as dimensionality reduction tool 

Gradient Boosted Trees (**GBTs**), another tree ensemble method used for regression and classification tasks
- unlike RF, GBTs are learned in an interative stage-wise manner by directly minimizing a cost function via gradient descent
- perform comparably to RF

## Methods
**Random Search for Splits**
- can identify good splits in many cases
- supervised procedures run risk of being overly greedy

**Flexible Sparsity**
- inducing an appropriate amount of sparsity in random projections increasese the probability of sampling discriminative projections

**Ease of Tuning**
- RF's work well out of box, existing oblique forests intro additional hyperparams to which they are sensitive to 

**Data Insight**
- Gini importance, comp eff way to assess the relative contribution/importance of each feature to the learned model, existing oblique forests do not lend themselves well to computation of GI

**Expediency and Scalability** 
- exisiting o forest algos involve exp computations to ID and select splits = less space and time eff than RF 

SPORF addresses all above
- \control over sparsity via \lambda, which is the only new hyperparam so easy to tune
- less sensitive to choice in \lambda than F-RC to choice in L
- GI computed in straightforward fashion cuz random projections sparse with only two discrete weightings of =/-1
- sparse raandom proj's cheap to computer

section 3.2 training and hyper param tuning 
- eaech algo uses 500 trees 
- split objective is to max reduction of Gini impurity
- trees fully grown, unpruned (nodes are split until pure)
- *d*, number of candidate split direstions evaluated at each split node, is the first param tuned
- SPORF and F-RC trained for d=p^2
- second hyperparam *\lambda*, the average sparsity of univariate projections sampled at each split node

**SPORF bridges the gap between RF and exisiting oblique methods**

SPORF and other oblique forests are proposed to be "more consistent" than Brieman's original RF
- results from their testing suggest that relaxing the constraint of axis-alignment of splits may allow oblique forests to be consisten across on a wider set of classification problems, also highlights why oblique forests are advantageous

### Simulated datasets
- perform variet of experiments on 3 simulated classifcation problems: **sparse parity**, **orthant**, and **trunk**
- **sparse parity:** miltivaraite generalization of the noisy XOR problem
- **orthant:** in R^p is a generalization of quadrant in R^2
- **trunk:** balanced two class problem in which each class is distributed as a p-dimensional multivariate gaussian with identity covariance matrices

SPORF performs as well or better than other algos on both sparse parity and orthant probs
- only method of the four that performs well on all the simulated data settings

SPORF is robust to hyperparameter selection

SPORF learns important features
- mean decrease of gini importance
- computed during training with minimal additional computation
- for a partifular feature, defined as the sum of the reduction in gini impurity over all splits of all trees made on that feature
- sporf learns features that are more important than any of the observed features and those features are interpretable, as they are sparse linear combinations of the observed features

![image](https://user-images.githubusercontent.com/89429238/136123938-bedefc89-832c-4b87-b264-8d477219f058.png)


### Real empirical data performance
sporf best overall classification performance on a large suite of benchmark datasets

![image](https://user-images.githubusercontent.com/89429238/136123920-b22e8883-bc5a-490a-9121-4982d70cd62b.png)

Identified default hyperparams: d = p, \lambda = 3/p

SPORF is robust to high dimensional noise

Time complexity similar to RF but can take longer if d > p

Space complexity is the same as RF

Storage complexity is similar to RF
