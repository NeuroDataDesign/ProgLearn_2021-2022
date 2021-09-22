### Chapter 5 : Regression Forests

### Introduction

Goal: the probabilistic estimation of continuous variables
less popular than classification forests

Properties:
* output label is continuous
* training labels also continuous


### 5.1 Non-linear Regression in the Literature

linear regression
* not appropriate when trying to model most natural phenomena which are often non-linear
* sensitivity to input noise

RANSAC
* estimation of multiview epipolar geometry and image registration transformations
* disadvantage: out-put is nonprobabilistic

support vector regression
* ensembles of relevance vector machines (RVMs)
* boosted ridge regression
* Gaussian processes


### 5.2 Specializing the Decision Forest Model for Regression
Classification: Given a labeled set of training data, learn a general mapping which associates previously unseen, independent test data points with their dependent, continuous output prediction.

Training point: (v, y)

probability density function p(y|v)

Imput: v = (x1, . . . , xd ) ∈ Rd


#### The Prediction Model
output confidence as well as its actual value
![alt_text](https://github.com/NeuroDataDesign/ProgLearn_2021-2022/blob/main/Mordred_Yuan/Week%202/Screen%20Shot%202021-09-16%20at%2011.37.27%20AM.png)

leaf probability pt (y|v) can be
multi-modal

#### The Ensemble Model
the forest output is the average of all tree outputs

#### Randomness Model
randomized node optimization model
parameter ρ = |Tj |

#### The Training Objective Function
The main difference between classification and regression forests is in the form of
the objective function I.

regression information gain formula: (valid only for the case of a probabilistic linear prediction model)
![alt_text](https://github.com/NeuroDataDesign/ProgLearn_2021-2022/blob/main/Mordred_Yuan/Week%202/Screen%20Shot%202021-09-16%20at%2011.37.27%20AM.png)

#### The Weak Learner Model
1. axis-aligned hyperplanes,
2. oriented hyperplanes, 
3. conic sections
![alt_text](https://github.com/NeuroDataDesign/ProgLearn_2021-2022/blob/main/Mordred_Yuan/Week%202/Screen%20Shot%202021-09-16%20at%2011.47.39%20AM.png)


### 4.3 Effect of Model Parameters
#### The Effect of the Forest Size
![alt_text](https://github.com/NeuroDataDesign/ProgLearn_2021-2022/blob/main/Mordred_Yuan/Week%202/Screen%20Shot%202021-09-16%20at%2011.47.39%20AM.png)


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

