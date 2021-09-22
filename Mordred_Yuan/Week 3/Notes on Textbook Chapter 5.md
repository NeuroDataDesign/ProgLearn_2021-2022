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

![alt_text](https://github.com/NeuroDataDesign/ProgLearn_2021-2022/blob/main/Mordred_Yuan/Week%203/Screen%20Shot%202021-09-22%20at%201.49.54%20AM.png)

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

![alt_text](https://github.com/NeuroDataDesign/ProgLearn_2021-2022/blob/main/Mordred_Yuan/Week%202/Screen%20Shot%202021-09-16%20at%2011.37.27%20AM.png)

regression information gain formula: (valid only for the case of a probabilistic linear prediction model)

![alt_text](https://github.com/NeuroDataDesign/ProgLearn_2021-2022/blob/main/Mordred_Yuan/Week%203/Screen%20Shot%202021-09-22%20at%202.01.15%20AM.png)

#### The Weak Learner Model
1. axis-aligned hyperplanes,
2. oriented hyperplanes, 
3. conic sections
![alt_text](https://github.com/NeuroDataDesign/ProgLearn_2021-2022/blob/main/Mordred_Yuan/Week%203/Screen%20Shot%202021-09-22%20at%202.15.40%20AM.png)


### 4.3 Effect of Model Parameters
#### The Effect of the Forest Size
y(x) = E[y|x] = 	integral y · p(y|x)dy
- as the number of trees increases both the prediction mean curve and its uncertainty become smoother

#### The Effect of the Tree Depth

D = 1 counld lead to underfitting
D (a large value) -> overfitting

#### Spatial Smoothness and Testing Uncertainty
The forest is capable of capturing
multi-modal behavior in the gaps

### Summary
the abstract decision forest model introduced in Chap. 3 --> regression

