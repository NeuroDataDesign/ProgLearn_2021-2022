### Introduction: The Abstract Forest Model
Unified model of decision forests - classification, regression, density estimation, manifold learning, semi-supervised learning, and active learning

Prototypical machine learning problems --> general model   (different parameterizations)

Pro: only need to implement once and make small modifications in applications

### 3.1 Decision Tree Basics

Decision Tree - a collection of nodes and edges organized in a hierarchical fashion (circles and squares)

![alt text](https://github.com/NeuroDataDesign/ProgLearn_2021-2022/blob/main/Mordred_Yuan/Week%201/Screen%20Shot%202021-09-09%20at%2010.16.10%20AM.png)

Key:
1. the tests associated with each internal node 
2. the decision-making predictors associated with each leaf

### 3.2 Mathematical Notation and Basic Definitions
Concepts:
1. Data point - v = (x1, x2, . . . , xd ) ∈ Rd
2. Feature - xi
3. Dimensionality - d
4. Features of interest - φ(v) = (xφ1, xφ2, . . . , xφd) ∈ Rd'
5. split function / test function / weak learner - h(v, θj ) : Rd × T → {0, 1} --> get binary output at a split node j
6. Training points - data point for which the attributes we are seeking for may be known and used to compute tree parameters
7. Training sets - S0 - a collection of different training data points


### 3.3 Randomly Trained Decision Trees
#### Function:
* Off-line phase - training 
   * test function h(· , ·) to v
   * to the left or right child
   * leaf node - predictor/estimator
   * output
   
* On-line phase - testing
   * θj = argmax I (Sj , θ)   θ∈T
   * Left and right sets : ![alt text](https://github.com/NeuroDataDesign/ProgLearn_2021-2022/blob/main/Mordred_Yuan/Week%201/Screen%20Shot%202021-09-09%20at%2010.52.32%20AM.png)
   * Tree Structure - stopping criteria
   * Afterwards:
      * the (greedily) optimum weak learners (split functions) associated with each node
      * a learned tree structure,and 
      * a different set of training points at each leaf.

#### Weak Learner Models (θ = (φ, ψ, τ))
1. Linear Data Seperation - h(v, θ) = [τ1 > φ(v) · ψ > τ2]
   * axis-aligned weak learners - decision stumps
2. Non-linear Data Separation - h(v, θ) = [τ1 > φ^T (v) ψ φ(v) > τ2]
   * low-dimensional weak learners of this type can be used even for data that originally reside in a very high dimensional space (d >> 2)

![alt text](https://github.com/NeuroDataDesign/ProgLearn_2021-2022/blob/main/Mordred_Yuan/Week%201/Screen%20Shot%202021-09-09%20at%2011.20.46%20AM.png)

#### Energy Models
Energy Models --> weak learners --> determines the prediction and estimation behavior of a decision tree

* Entropy - H - a measure of the uncertainty associated with the random variable we wish to predict
  * discrete probability distributions - Shannon entropy
  * continuous-valued labels and continuous distributions - differential (continuous) entropy
* Information Gain 
  * ![alt_text](https://github.com/NeuroDataDesign/ProgLearn_2021-2022/blob/main/Mordred_Yuan/Week%201/Screen%20Shot%202021-09-09%20at%2011.40.22%20AM.png)
  * Maximizing the information gain - select the split parameters which produce the highest confidence (lowest uncertainty) in the final distributions

#### Leaf Prediction Models
conditional distributions - p(c|v) or p(y|v)
Maximum A-Posteriori (MAP) estimate

#### The Randomness Model

* Random Training Set Sampling
  * Bagging - reduce possible overfitting / improve the generalization capabilities of random forests
* Randomized Node Optimization (RNO)
  * enables us to train trees on the entire training data
  * yields marginmaximization properties for the ensemble models

### 3.4 Combining Trees into a Forest Ensemble
de-correlation between the individual tree predictions --> improved generalization and robustness
When ρ = | T |, all trees are identical and as ρ decreases trees become more decorrelated.

Select more confident trees:
* simple averaging operation - reducing the effect of possibly noisy tree contributions
* multiply the tree outputs - sharper distributions / less robust to noise



### Summary

* the maximum allowed tree depth D;
* the amount of randomness (controlled by ρ) and its type;
* the forest size T ;
* the choice of weak learner model;
* the training objective function;
* the choice of features in practical applications.
