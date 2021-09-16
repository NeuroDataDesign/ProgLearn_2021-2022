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

Training point: (v, c)

Input: v = (x1, . . . , xd ) ∈ Rd

#### The Training Objective Function
optimizing the parameters of the weak learner at each split node j: θj = argmax I (Sj , θ). θ ∈ Tj

Information Gain 
  * ![alt_text](https://github.com/NeuroDataDesign/ProgLearn_2021-2022/blob/main/Mordred_Yuan/Week%201/Screen%20Shot%202021-09-09%20at%2011.40.22%20AM.png)
  * Maximizing the information gain - select the split parameters which produce the highest confidence (lowest uncertainty) in the final distributions

Entropy: H(S)=− Σ p(c) log p(c) c∈C 

(p(c): the normalized empirical histogram of labels corresponding to the training points in S)

Fig: Classification training data and tree training.
![alt_text](https://github.com/NeuroDataDesign/ProgLearn_2021-2022/blob/main/Mordred_Yuan/Week%202/Screen%20Shot%202021-09-16%20at%2011.27.23%20AM.png)

#### Class Re-balancing
unbalanced distribution of classes

Solutions:
* resampling the training data so as to have roughly uniform training distributions
* use the known prior class distribution to weight the contribution of each class by its inverse frequency when computing the information gain at each split node

#### Randomness
randomized node optimization

#### The Leaf and Ensemble Prediction Models
probabilistic output - predict an entire class distribution

![alt_text](https://github.com/NeuroDataDesign/ProgLearn_2021-2022/blob/main/Mordred_Yuan/Week%202/Screen%20Shot%202021-09-16%20at%2011.37.27%20AM.png)

### 4.3 Effect of Model Parameters
#### The Effect of the Forest Size on Generalization
![alt_text](https://github.com/NeuroDataDesign/ProgLearn_2021-2022/blob/main/Mordred_Yuan/Week%202/Screen%20Shot%202021-09-16%20at%2011.47.39%20AM.png)
b. axis-aligned weak learn

c. classification posteriors (quality of uncertainty)

#### Multiple Classes and Training Noise
conic section weak learner model - yields smoother posteriors

noise increases -> a larger overall uncertainty in the testing posterior

#### The Effect of the Tree Depth
tree depth increases -> the overall prediction confidence also increases

D (a large value) -> overfitting

#### The Effect of the Weak Learner
Choice of different weak learners:
![alt_text](https://github.com/NeuroDataDesign/ProgLearn_2021-2022/blob/main/Mordred_Yuan/Week%202/Screen%20Shot%202021-09-16%20at%2012.04.15%20PM.png)

* axis-aligned weak learner produces overconfident predictions
* conic sections yield a possibly more intuitive decrease of confidence with distance from training data

Depend on specific application

#### The Effect of Randomness
* Larger randomness reduces the blocky artifacts of the axis-aligned weak learner and produces more rounded decision boundaries
* larger randomness yields a much lower overall confidence

### 4.4 Maximum Margin Classification with Forests
SVM - margin-maximizing surface

Random Forests:
h(v, θj ) = [φ(v) > τ] with φ(v) = x1

not individual tree, instead the combination of multiple trees that at the limit T →∞ produces the desired max-margin behavior
![alt_text](https://github.com/NeuroDataDesign/ProgLearn_2021-2022/blob/main/Mordred_Yuan/Week%202/Screen%20Shot%202021-09-16%20at%2012.26.34%20PM.png)

* The Effect of Randomness on Optimal Separation
  * not guaranteed to split the data perfectly and thus they may yield a sub-optimal information gain
  * parameter ρ is very similar to that of “slack” variables in SVM
* Influence of the Weak Learner Model
* Maximum Margin with Multiple Classes
* The Effect of the Randomness Model
  * bagging and RNO
  * RNO randomness model - use all available training data and enables us to control the maximum margin behavior simply, by means of changing ρ.


### Summary
the abstract decision forest model introduced in Chap. 3 --> multi-class classification
