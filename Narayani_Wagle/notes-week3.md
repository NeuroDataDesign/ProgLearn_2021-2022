# Week 3 Notes - 9/20
## Textbook
Chapter 4: Classification Forests
- specializing decision forest model for classification
  - output - discrete, categorical, unordered
  - train objective function which is in form of classical information gain for discrete distributions
  - instantiate via information gain or entropy
  - rebalance classes if one has unbalanced distribution in training set such that the training set has a uniform distribution
  - can also use prior known class distribution 
  - randomly optimize nodes and control randomness 
  - forests give class distribution predictions
- effect of model parameters
  - forest size, depth, and amount of randomness affect performance
  - shallow trees use axis-aligned weak learners that are simple
  - stump trees only have one split node which is the root
  - individual trees have overconfident predicitons which is bad
  - increase forest size to get smoother posteriors with more uncertainty 
  - one decision forest model can do binary and multi-class classification
  - more noise in training = more uncertainty in testing posterior
  - increase tree depth to increase prediciton confidence
  - large depth values can cause overfitting
  - low depth values can cause low-confidence posteriors
  - axis-aligned weak learned causes overconfident predictions
  - more randomness causes blocky artifacts in the weak learner and more rounded decision boundaries
- maximum margin classification with forests
  - more randomness causes individual trees to not split data perfectly and causes not good information gain and lower confidence in posterior
  - weak learners affect shape and oreitnation of classification surface

Chapter 5: Regression Forests
- specializing decision forest model for regression
  - each input has a continuous multivariate label
  - goal: estimate probability density function
  - regression forests are collection of randomly trained regression trees
  - need to use something in place of the pre-stored empirical class posterior for the classification forests
  - use polynomial function 
  - output confidence and value
  - ensemble model - forest output is avg of all tree outputs
  - randomness model - randomized node optimization used, amount of randomness used is controlled by a parameter
  - training objective function - minimize least-square function
  - weak learner model - axis-aligned hyperplanes, oriented hyperplanes, conic sections
- effect of model parameters
  - more trees -> smoother prediction mean and uncertainty curves
  - low depth --> underfit
