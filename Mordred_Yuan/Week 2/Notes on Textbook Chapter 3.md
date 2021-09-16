### Chapter 4 Introduction: Classification Forests
Goal: automatically associate an input data point v with a discrete class c ∈ {ck}

Properties:
* Multiple classes
* Probabilistic output
* Generalize well to previously unseen data
* Efficient
* Margin-maximizing behavior under certain conditions
* The quality of the posterior and associated confidence can be controlled via the choice of the specific parameters
### 4.1 Classification Algorithms in the Literature

* Support Vector Machine(SVM)
* Boosting - linear combination of many weak classifiers

Problem: Cannot deal with multi class problems

Classification Forests: 
* yield good generalization, even in problems with high dimensionality
* practical vision and medical applications

### 4.2 Specializing the Decision Forest Model for Classification
Classification: Given a labeled set of training data learn a general mapping which associates previously unseen test data with their corresponding classes.
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

### 4.3 Effect of Model Parameters


### 4.4 Maximum Margin Classification with Forests




### Summary
