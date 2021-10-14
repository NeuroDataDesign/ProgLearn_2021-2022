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

# Chapter 4
## 4.1
* support vector machines (SVM)
  * one of the most widely used classification algorithms
  * in binary classification problems, it guarantees maximum margin separation
  * good generalization w/ relatively little training data
* boosting
  * builds strong classifiers as linear combos of weak classifiers
* SVM and boosting don't do well in multiple class problems
## 4.2
* each training point is (v, c)
  * v is input test data
  * c is class label
### 4.2.1
* training classification tree by maximizing info gain produces trees where entropy of class distributions associated w/ nodes decreases when going from root to leaves
* yields increasing certainty of prediction
### 4.2.2
* one class may overpower other classes
* can be mitigated by resampling data to have uniform distribution
* or use known prior class distribution to weigh contribution of each class by its inverse frequency
### 4.2.3
* randomness injected by randomized node optimization
### 4.2.4
* classification forests produce probabilistic outputs
* entire class distribution
## 4.3
* forest size, depth, randomness, and weak learner type affect performance
### 4.3.1
* increasing forest size leads to smoother posteriors
* few trees means each tree is overconfident
### 4.3.2
* picking an appropriate learner type helps the fit
* e.g conic for a spiral
### 4.3.3
* D should be chosesn carefully
* shallow D can be inaccurate
* too deep leads to overfitting
### 4.3.4
* decision forests are flexible enough to produce different confidence behaviors and show how to control them
* axis aligned may be more efficient but less accurate
### 4.3.5
* which weak learner to choose depends on efficiency as well as accuracy
## 4.4
* each tree is not guaranteed to produce maximum margin separation
  * the combo of multiple trees at the limit T -> infinity produces max-margin behavior
  * in practice T + P must be large enough
### 4.4.2
* linear weak learners still produce globally non-linear classification
### 4.4.3
* conic learners uncertainty region evolves in a curved fashion away from training data
### 4.4.4
* bagging and random node optimization together produce a greater result
* training set randomization leads to smoother posteriors whose optimal boundary doesn't coincide with max margin
* bagging advantage is increased training speed 

# Chapter 5
* Regression forests are used for the non-linear regression of dependent variables given independent input
* less popular than classification forests
* need continuous labels
## 5.1
* linear regression is sensitive to input noise
* There are a few different approaches that increase the robustness of linear regression
## 5.2
* regression task is
  * given a labeled set of training data, learn a general mapping which associates previously unseen, independent test data points with their dependent,continuous output prediction
* regression task is inductive like classification, but continuous
* training points are a pair (x,y)
* regression forests are collections of regression trees
### 5.2.1
* form of the prediction at leaves is dictated by prediciton model
* regression forests can have various prediction models, for example
  * polynomial function
  * probability density function
### 5.2.2
* forest output is the average of the tree outputs
### 5.2.3
* randomized node optimization model is used
* controlled by p = |Tj|
### 5.2.4
* forest training is achieved by optimizing an energy function defined over a training set S0 of data and associated continuous labels
* continuous formulation of information gain
* functional form of the differential entropy of a Gaussian density
* produces a point estimate of y rather than a fully probabilistic output
* using an information theoretic formulation allows us to view classification and regression forests as instances of the same, abstract forest model
### 5.2.5
* 3 types of weak learners
  * axis-aligned hyperplanes
  * oriented hyperplanes
  * conic sections
## 5.3.1
* smoothness of the interpolating curve is controlled here by the forest size T
## 5.3.2
* a depth of 1 is linear regression
* too deep a depth leads to overfitting
## 5.3.3
* smooth interpolating behavior of the mean prediction in contrast to the more jagged nature of the mode
* uncertainty increases away from training data
## 5.4
* this chapter specialized the abstract forest for regression

# 6
* given unlabeled data, estimate unobserved generative model
## 6.1
* Gaussian mixture model
  * complex distributions can be approximated via a collection of simple gaussian components
  * parameters are estimated via the Expectation Maximization algorithm
* non-parametric density estimation techniques are kernel-based algorithms
  * Parzen - Rosenblatt windows estimator
## 6.2
* each input data point is a multi-dimensional feature response vector
* desired output is entire probability density function
* density forest is a collection of randomly trained clustering trees
* leaves contain simple prediction models like Gaussians
### 6.2.1
* train each individual tree in the forest independently
* For a set of data points in feature space, the determinant of the covariance matrix is a function of the volume of the ellipsoid corresponding to that cluster
* original dataset splits into compact clusters
* centers of clusters tends to be placed in areas of high density
### 6.2.2
* In the case of axis-aligned weak learners it is possible to compute the partition
function via the cumulative multivariate normal distribution function
* the cumulative multivariate normal does not have a closed form solution
### 6.2.3
* forest density is given by the average of all tree densities
### 6.2.4
* input point v belongs deterministically to only one of its leaves
* in a forest with T trees a point v belongs to T components
* ensemble model induces a uniform mixing across different trees
## 6.3
### 6.3.1
* deeper trees create further splits and smaller gaussians, overfitting 
* deeper trees tend to fit the noise of the training data, rather than the underlying nature
### 6.3.2
* even if individual trees overfit, the addition of further trees tends to produce smoother densities
### 6.3.3
* parameter D can be used to compromise between the ouput smoothness and the ability to capture structural details
## 6.4
### 6.4.1
* multiple trees increases smoothness
### 6.4.2
* use of randomness improves results
* possible issues with EM getting stuck in local minima is not present in forest model
### 6.4.3
* GMM model has cost TxKxG, where T is number of random restarts, K is number of Gaussian components, and G is cost of evaluating v under each Gaussian
* estimating p(v) under density forest w/ T trees of max depth D has cost
  * T x (D x B + G)
## 6.5
* efficient sampling of random data under the learned model
* drawing one random sample involves generating at most D random numbers from uniform distributions plus sampling a d- dimensional vector
* slightly faster version is obtained by compounding all the probabilties associated with individual edges at different levels together
### 6.5.1
* cost of randomly drawing N smaples under forest model is N x (2J + K)
* cost of drawing N smaples under random-restart GMM is identical
* despite added richness, sampling complexity of a density forest is comparable to that of a GMM
## 6.6 
* reconstruction error decreases with the forest size
* overall error starts increasing again after an optimal value of D
## 6.7
* forests can be used for density estimation
