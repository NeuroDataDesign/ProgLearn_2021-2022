## Ch 3 Intro: The Abstract Forest Model

### Categories of ML algorithms:
- **Classification task**
  - Input: image/data
  - Output: a discrete categorical label
- **Regression problem** 
  - Input: usually continuous data
  - Output: a *continuous variable*
- **Density function** 
  - Input: (Example) medical scan image
  - Output: evaluation under probability density function made by healthy scans
- **Manifold learning**
  - Input: data that is believed to lie on low dimension manifold in higher dimensional space
  - Ouput: estimate of higher dimensional space
- **Semi-supervised** 
  - Input: unlabeled and labeled pixels
  - Output: labeled pixels
- **Active learning problem** 
  - Input: very few manual annotations
  - Output: algorithm makes categories based on differences

- Benefits of decision forests
  - High accuracy on previously unseen data (generalization)
    - This is achieved by ensembles of trees

### General Tree Structure
- Regular decision tree - one node is associated with one "question"
  - can be yes/no or threshold question
  - binary or more options

- A good functioning decision tree has:
  - Tests with each internal node
  - Decision making predictors with each leaf

### Training points and sets
- **Training Point**
  - data point with known (or partially known) attributes
    - used to obtain tree parameters
- **Training Set**
  - Splits of training data based on (often) final categories/labels

### Randomly trained decision trees: Tree Testing (On-line)
- start with previously unseen data point, decision tree hierarchially applies tests (branching data down the tree)
  - each split node applies associated test function to data point and sends it left or right in binary tree
- **leaf nodes** 
  - contain predictor/estimator
    - associates an output with input

### Randomly trained decision trees: Tree Training (Off-line)
- each internal node needs to learn test function automatically from labelled training data
  - training selects parameters of test function of each node (indexed by j) by optimizing an objective function
    - maximize objective function I at the jth split node 
    - performed as simple search over possible parameter settings theta
- our task is to choose tree structure (size and shape)
- at end of training we have
  - greedily optimum weak learners (test functions) associated with each node
  - learned tree structure
  - different set of training points at each leaf

### Weak learner models
**Parameters of weak learner model**
- **Filter (selector) function** 
  - selects a few features from all possible ones*
- **\psi** 
  - defines geometric shape used to separate the data 
- **\tau** 
  - captures thresholds for inequalities used in binary test

### Non-linear Data Separation
- we can get more complex weak leaners by replacing hyperplanes with higher DoF surfaces
- DoF of weak learner influences forest generalization properties

### Energy model
- influences the choice of weak learners
  - energy model determines prediction and estimation behavior of decision tree
- **Information Gain **
  - reduction in uncertainty achieved by splitting training data arriving at nodes into multiple child subsets
    - weighting entropy by cardinality of child sets avoids splitting off children containg very few points
    - splitting training data into purer nodes increases information on the data set and reduces the uncertainty of prediction 

### Randomness Model
- there exist two popular ways to inject randomess into trees during training
  - random training set sampling
    - train each tree on different subsets (randomly subsampled)
    - avoids specializing parameters to a single training set
  - randomized node optimization (RNO)

### Combining Trees into a Forest Ensemble 
- **Random decision forest** 
  - ensemble of randomly trained decision trees
    - all trees trained independently (possibly in parallel)
    - during testing each test point is simultaneously pushed through all trees to reach corresponding leaves
  - combine all tree predictions into one by averaging
    - combined distributions are influences more by confident trees
    - reduces effect of noisy tree contributions

### Key Model Parameters 
- maximum allowed tree depth
- amount of randomness and its type
- forest size
- choice of a weak learner model
- training objective function
- choice of features in practical applications

## Chapter 4: Classification Forests
### Specializing the Decision Forest Model for Classification 
- **Class Re-balancing** 
  - some applications have unbalanced distribution of classes in the training set 
    - resample training data to have a roughly uniform train distribution 
    - use the known prior class distribution to weigh the contribution of each class by its inverse frequency
  - larger forests --> more confidence and less uncertainty

- trees are better than SVM and boosting 
  - same classification model can handle binary and multi-class problems
- large tree depth can overfit and shallow tree depths have low-confidence posteriors
  - we control these values
- multiple trees help reduce overfitting --> does eliminate it so be careful when choosing depth

### The effect of randomness (*p*, \rho)
- lowering *p*  
  - fewer separating geometric separation available to each node during training
  - Benefits
    - increases the randmoness of each tree 
    - reduces their correlation
  - Drawbacks
    - lower overall confidence
    - complex weak learners are sampled from larger parameter spaces --> finding discriminative sets of parameter values is time consuming

### Maximum Margin Classification with Forests
- **Maximum margin solution**
  - line placed directly in the gap that seperates two classes 

### Effect of randomness on optimal seperation
- if we have sloppy or inaccurate training data we
  - increase randomness to obtain smoother and more spread-out posteriors
    - this way effect of individual training points is weaker

### Influence of the Weak Learner Model
- more complex weak learners affect 
  - shape and orientation of
    - hard classification surface 
    - uncertain region

