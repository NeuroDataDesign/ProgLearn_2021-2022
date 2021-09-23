[Random Forest Book Notes](https://link.springer.com/book/10.1007/978-1-4471-4929-3)

# Chapter 1
* “Classification and Regression Trees (CART)" by Brieman et al is among the first works on decision trees
* Quinlan's "C4.5" is one of the most popular algorithms
* the 1990s introduced groups of learners
* Amit and Geman introduced the first combo of decision trees and ensemble methods, leading to decision forests
* Brieman introduced random forests
* Decision Forests gave rise to the Kinect

# Chapter 2
* Notation (images from decision forest book, screenshotted for ease and because these notes aren't going to be published)
* ![First part of notation table](https://github.com/NeuroDataDesign/ProgLearn_2021-2022/blob/main/Sarah_Houlton/Images/Screenshot%20(81).png)
* ![Second part of notation table](https://github.com/NeuroDataDesign/ProgLearn_2021-2022/blob/main/Sarah_Houlton/Images/Screenshot%20(82).png)

* vectors -> boldface lowercase
* matrices -> teletype uppercase
* sets -> calligraphic
## Common terms
* decision forest
  * randomized forest
  * random forest
  * randomized decision forest
* decision tree
  * randomized tree
  * randomized decision tree
* split node
  * internal node
  * decision node
  * branch node
* leaf node
  * terminal node
* weak learner
  * split function
  * test function
  * feature
* selector function
  * filter function

# Chapter 3
* Forests can be applied to 
  * classification
  * regression
  * density estimation
  * manifold learning
  * semi-supervised learning
  * active learning
## 3.1.1
* A collection of nodes and edges organized in hierarchical fashion
* internal nodes -> split -> represented by circles
* terminal nodes -> leaf -> represented by squares
## 3.1.2
* Decision trees
* binary tree
* Each node is a question, the answer is an edge
  * by following edges, we can come to a conclusion
  * more questions (more edges) = higher confidence
* Good decision tree establishes
  * tests associated w/ each internal node
  * decision-making predictors associated w/ each leaf
* Split complex problems into small ones to solve
## 3.2.1
* A data point is a vector v=(x1, x2, x3, ...) where x1, x2, etc are features
* features vary btwn applications
* number of features depends on type of data point
  *   could theoretically be very large
  *   we focus on a subset of the features d
## 3.2.2
* split function, test function, weak learner are all the same thing
  * fn that answers a node's question
  * data point goes into a function, answer comes out
  * sorts into l and r branches
## 3.2.3
* data point for which attributes are known that are used to set tree parameters
* training set is a collection of training points
## 3.3.1
* previously unseen data point, tree applies a number of tests, depending on results goes r or l, continues down to leaf
* leaf node contains predictor/estimator that associates output w/ input v
## 3.3.2
* a training phase selects type/parameters of each test fn associated w/ each split node by optimizing chosen objective fn
* optimization is greedy
  * at each node, we learn the fn that best splits the set into L and R
  * typically, this is a search over a discrete set of samples of possible parameter settings
* objective fn is computed using Sl, Sr, and splitting parameters
* structure depends on when we stop the tree
  * max levels D
  * min value of info gain at each node
  * node contains too few training points
* growing trees too much is overfitting
## 3.3.3
* axis aligned weak learner are called decision stumps
  * used in boosting
## 3.3.4
* energy model influences weak learners, therefore the prediciton and estimation behavior of the tree
* maximizing info gain helps select split parameters which produce highest confidence + lowest unncertainty
* information gain measure is flexible, can be used for different representations
## 3.3.6
* Bagging
  * train each tree in a forest on a different training subset, sampled at random from same labeled database
  * helps avoid specializing parameters to a single training set
  * training is faster w/ subsets
* Randomized Node Optimization
  * When training a node, we only make a small random subset of parameters available
  * could be all parameters or only some depending on needs
  * enables us to train on entire training data
  * yields margin-maximization properties for ensemble models
  * bagging has greater training efficiency
## 3.3.7
* A random decision forest is an ensemble of randomly trained decision trees
* randomness parameter p controls randomness w/in trees and also correlation btwn trees
* combining all tree predictioons into a single forest prediction can be as easy as averaging
  * we could also multiply outputs
#  3.4.1
* Parameters that most affect behavior
  * max tree depth
  * amount of randomness
  * forest size
  * choice of weak learner model
  * training objective fn
  * choice of features in practical applications 
