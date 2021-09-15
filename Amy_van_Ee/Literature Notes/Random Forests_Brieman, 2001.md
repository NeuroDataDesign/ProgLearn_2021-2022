# Random Forests

Brieman, 2001.
https://link.springer.com/article/10.1023/A:1010933404324

## Notes

**Introduction**
- A random forest classifier is defined to consist of classifiers that are independently identically distributed (iid) random vectors, and given some input, each tree casts a vote

**Characterizing accuracy of random forests**
- The margin can be defined by an equation that describes how much the average number of votes for the correct class will surpass the number of votes for other (incorrect) classes
    - A larger margin means that the predicted classification is more confident
- For a large forest and as the number of trees increase, the generalization error converges -- random forests cannot actually be overfit
    - Generalation error depends on two factors
      - strength of each individual classifier/tree
      - dependence of each tree on eachother (correlation between them based on the margin function)
    - Accuracy can be improved by minimizing correlation but maximizing/maintaining strength

** Using random features**
- "Adaboost" random forest performs very well <- investigate this model more
- Bagging - fit many models on different subsets of a training dataset, then combining predictions from all of these models
    - Random forest adds on by randomly selecting different subsets of features in data samples
    - Bagging increases accuracy and can give estimates on generalization error in an ongoing manner 

**Random forests using random input selection**
- Random input selection can be a very important method when the datasets have many variables, as this method is much faster than Bagging or Adaboost

**Random forests using linear combinations of inputs**
- More features can be defined by using randomly generated linear combinations of input variables 
- Categorical variables can be converted to binary dummy variables (1 and 0) to convert them to be numerical and used in this analysis and experimentation
- The number of linear combinations (F as defined in the paper) must be sufficiently large to get the desired accuracy

**Empirical results on strength and correlation**
- As datasets become larger and more complicated, the strength increases until it plateaus 
    - Random forests that have lower generalization error have higher strength and lower correlation between classifiers 
    - Thus, the procedures to randomly make the trees should take this into account

**Conjecture: Adaboost is a random forest**
- Adaboost used weights on training set input to the next classification based on misclassifications of previous classifiers
    - The distribution of weights depends on this training set, but for a normal random forest, the distribution of random vectors has no dependence on the training set

**The effects of output noise**
- If the training set classification labels are randomly changed (noise), Adaboost accuracy decreases, but bagging and random split are less susceptible to this noise

**Data with many weak inputs**
- Much of medical data has weak inputs, and this makes it hard for trees and neural nets to perform classifications
- Found that forests can still hand this weak data, but only if the correlation between individual trees is low

**Exploring the random forest mechanism**
- Dependent variables can affect prediction error - in the paper example, one of the variables carries some of the same information as the second, and so using the second does not give more predictive accuracy and there is no decrease in error rate

**Random forests for regression**
- Regression involves numerical values instead of class labels

**Empirical results in regression**
- Random features from random forest is always better than bagging
- Different methods of randomness can be combined to create the most optimal forest

**Remarks and conclusions**
- Random forests are not effective in prediction, but can make for accurate classifiers and regressors 
    - Adaptive bagging algorithm can reduce bias, but changes the training set like arcing
    - Forests - can give accurate results without needing to change the training set 
