# Breiman 2001 paper notes
- **bagging:** where to grow each tree, a random selection w/o replacement is made from the examples in the training set
- **random split decision:** at eaceh node the split is selected at random from among the K best splits
- another approach select training set from a random set of weights on the examples in the training set
- common element in all is that for kth tree, a random vector, \theta_k is generated, independent of the past random vectors \theta_1....\theta_k-1 but tiwht the same distribution
- tree is grown using training set and \theta_k, resulting in a classifier h(x, \theta_k), where x is an input vector
- after large number of trees is a generated, they vote for the most popular class, we call these procedure **random forests**
- Theorem 1.2 explains why random forests do not overfit as more trees are added, but produce a limiting value and generalization error: 

![image](https://user-images.githubusercontent.com/89429238/134429948-020cb3c5-a056-44f9-8d21-c3e35acf9e44.png)

- c/s2 ratio is the correlation divided by the square of the strength, the small it is the better, useful for understand the function of random forests

- ch.2: lots of formulas and proofs that we were told not to focus too hard on

## Ch.3 Using random features
- to imporve accuracy the randomness injected has to minimize the correlation \rho bar while maintaing strength
- two reasons to use bagging
1. use of bagging seems in enhance accuracy when random features are used
2. bagging be used to give ongoing estimates of the generalization error (PE*) of the combined ensemble of trees as well as estimates for the strength and correlation
- given training set T, form boostrap training sets T_k, contruct classifiers h(x,T_k) and let these vote to form the bagged predictor, for each y,x in the training set, aggregate the votes only over those classifiers for which T_k does not contain y,x = out of bad classifier
- out of bag estimate for the generalization error is the error rate of the out of bag classifier on the training set 
- using out of bag error estimate removes the need for a set aside test set
- in each bootstrap training set, about 1/3 of the instances are left out 
- out of bad estimates are unbiased unlike cross-validation

## Ch.4 Random forests using random input selection
- growing 100 trees in random forests was was faster than 50 for Adaboost
- error rate using random input selection compare favorably with Adaboost, comp might be more favorable if the search is over more values of F instead of preset 2

## Random forests using linear combinations of inputs
- if only few inputs, M, taking F an appreciable fraction of M might lead to an increase in strength but higher correlation
- another approach: define more features by taking random linear combinations of a number of input variables = feature generated by specifying L, the number of variables to be combined
- at give node, L vars are radnomly selected and added togetehr with coeff's that are uniform random #'s [-1,1] 
- search is made over these for best split, procedure is called **Forest-RC**
- Forest-RC compares more favorably to Adaboost than Forest-RI

### Categorical variables
- each time a categorical var is selected to split on at a node, select a random subset of the categories of the variable and define a substitute var that is one when the categorical value of the var in the subset and zero outside
- many cat vars, low F results in low corr but also low strength, F must be increased about 2-3 times int(log_2(M+1)) to get enough strength to provide good test set acc

## Ch.6 empirical results on strength and correlation
- better (lower generalization error) random forests have lower correlation between classifiers and higher strength
- randomness used in tree contruction has to ain for low correlation \rho bar while maintaining reasonable strength

## Ch.8 The effects of output noise
- bagging and random split selection are more immune to noise than Adaboost
- from experiments Adaboost deteriotes markedly with 5% noise while random forests show small changes
- Randome forest procedures do not concentrate weight on any subset of the instances and the noise effect is smaller 

## Ch.9 Data with many weak inputs
- Forest-RI produced error rates not far above the Bayes error rate
- forests seem to ahve the ability to work with very weak classifiers as long as their correlation is low
- couldnt run with Adaboost on this data because the base classifiers are too weak

## Ch10 random forest mechanism
- some variables are more important than other and it is important to understand which those are and why they are more important, although it may be difficult to do so

## Ch11 random forests for regression
- formed by growing trees depending on a random vector \theta such that the tree predictor h(x,\theta) takes on numberical values as opposed to class labels
- many formulas/theorems are provided in this chapter
- theorem 11.2 pinpoints the req;s for accurate regression forests: low correlation between residules and low error trees

![image](https://user-images.githubusercontent.com/89429238/134440802-fb9cf1bb-73c6-44db-86e4-42c47f9bb83f.png)

- random forest decreases avg error of trees emplyed by the factor \rho bar
- randomization employed needs to aim at low correlation

## Ch12 empirical results in regression 
- in regression forests, use random feature selection on top of bagging
- relatively large number of features are req'd to reduce (generalization error) PE*(tree) and get near optimal test set error, but if number is too large correlation goes up and error increases again, but there is range where as # of features increases, corr increases, but PE*(tree) compensates by decreasing
- here random-forest-random features is always better than bagging
- overall, adding output noise work with random feature selection better than bagging

## Ch13 remarks and conclusions
- beacuse of law of large numbers, random forests do not overfit
- right kinda of randomness makes them accurate classifiers and regressors 
- accuracy of forests indicate that they act to reduce bias