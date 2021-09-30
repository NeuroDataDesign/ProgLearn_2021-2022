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

pg 5/6 section 3.2 training and hyper param tuning 
