# Decision Forests for Computer Vision and Medical Image Analysis
Criminisi and Shotton, 2013.

## Notes

**Chapter 1**
- Part I - general forest model <- will want to focus on this to learn more about theory behind this model

**Chapter 2 - Notation and Terminology**
- Reference this chapter for table of notation, will be very useful when reading papers in the future (pages 3,4)
- Again, reference this chapter for commonly used terms

**Chapter 3 - Introduction: The Abstract Forest Model**
- Common learning tasks - classification, regression, density estimation, manifold learning, semi-supervised learning, active learning
- Decision trees have become more popular due to their ability for generalization - greater accuracy on new data by using an ensemble of slightly different trees
    - nodes are either internal (split) or terminal (leaf), often circles or squares, respectively
    - the more questions asked, higher confidence in response - each internal node has a question
    - general layout: root node takes in input, based on reslt of first test, the data goes down to left or right child where new test and so on until hits a leaf node where most probable answer based on previous answers
- Data point and features
    - data point is a vector, where number of components refers to values of each feature
    - often do not need to have all features, and can just have a subset of interest
- Test functions = split fnction = weak learner
    - each node has test function, output is binary (1 or 0)
- Training point and training set
    - training point - data point with known attributes
    - training set is set of datapoints
    - we can consider subsets of training points that reach different nodes, so S_1 is the subset of the training points that reach node 1 for exammple
- Randomly Trained Decision Trees
    - off-line phase is training, on-line phase is testing
    - off-line training, the test function type and parameters for each split node are optimized based on an objective function defined using the training set
        - this optimization occurs in a "greedy manner"
        - at each node, we learn the function that best splits the training subsets, usually as a search over discrete number of samples to see what parameters optimize 
        - for a binary classification, the best function splits the training subset at the parent node such that the child nodes largely contain training points of just one class (like correct splititng of the data according to the label we know they have during training) 
    - Tree structure must also be determined, such as number of levels
        - generalization is better when trees are not fully grown
        - it is also possible to prune afterwards, but this textbook avoids this to keep the proess simpler
    - At end of training: (greedily) optimum split functions at each node, learned tree structure, different sets of training points at each terminal node (leaf)
- Weak learner models
    - general idea: filter (selector) function selects features from the input vector, data is separated using geometric primitive, then thresholds applied in binary test
    - Linear data separation - for example, just a line or circle to separate datapoints
    - Non-linear data separation - more complex, can use conic section as an example
- Energy Models: Entropy and Information Gain
    - information gain at a split node is a reduced uncertainty by splitting the training data into child subsets
    - entropy is measure of uncertaitny that is connected to random variable we are trying to predict, we can weight the entropy by cardinality of child sets
    - examples using classification and clustering
- Leaf prediction models
    - can use label statistics at a leaf/terminal node to predict the label that an input test point will procure
- Randomness model
    -  randomness can be inserted during the training phase - random trainng set sampling (such as in bagging) or randomized optimization of nodes
    -  Bagging - reduce overfitting by training each individual tree of the forest on a different randomly chosen subset of the training data
        -  improves generalization since not train all trees on one subset
        -  also faster training 
        -  however, would not use all of the training data to train each tree, which is wasteful of information
    -  Ranndomized node optimization (RNO) - optimize at each node using entire feature space, but this is not efficient if very large, so instead only allow access to subset of parameters
    -  note that bagging and randomized node optimization can be used together
    -  This book will focus just on RNO, since this allows use of entire training dataset and allows ensemble models to have margin-maximization properties
-  Combining trees into forest ensemble
    -   randomly trained decision trees together form a random forest - important that the trees are randomly different so de-correlation of tree predictions and therefore better generalization
-   Key parameters of the model - tree depth, randomness and type, size of forest, weak learner model type, training objective function, features chosen

**Chapter 4: Classification Forests**
- Classification: take in a data point and associate it with a discrete class
- Classification algorithms
    - Support Vector Machine (SVM): supervised machine learning, linear model for classification (and regression)
    - Boosting: many iterations, in each "boost" to focus on training examples that not work as well on
    - Advantageous to combine many simple learners
- Specializing the decision forest model for classification
    - Optimize the parameters of the weak learner at each split node
    - Unbalanced data where the class labels are not even distributed in the training set can negatively impact forest training
        - In image segmentation, for example, we can have more background than object pixels
        -  Methods: resample the training data to create more uniform distributions or weight the contribution of each class accordingly 
    - Randomness can be added by implementing randomized node optimization
    - Probabilistic output is also provided, since the class prediction and the class distribution can be returned after implementing a random forest model and using it on data
- Effect of model parameters
    - Accuracy and generalization depend on the forest depth, size, type of weak learner, and amount of randomness injected
    - Don't want overconfident predictions - having a larger forest size of different trees can reslt in a smoother posterior and allow for more generalization 
    - With an increase in tree depth, there is an increase in overall confidence in prediction
- Maximum margin classification
    - Bagging allows for the injection of randomness by getting random subsets of the training data, as well as reduced training times due to increased speed with smaller training sets

**Chapter 5: Regression Forests**
- Random forests can also be used to estimate continuous variables, and in particular regression forests use non-linear regression to do so
- Non-linear regression in literature
    - Least squares techniques minimize error over training points
    - Random sample consensus (RANSAC) estimates a model's parameters by randomly sampling data
- Specializing the decision forest model
    - The main difference with the random forest classifier is jutst that the output is continuous
    - This consists of independently trained regression trees, just like with the classification forest - and we can see that a forest performs better than one fully developed tree
    - A non-linear regression problem is split into smaller problems that more simple models can handle
    - Prediction model
        - A probability density function over a continuous variable can be used to make decisions at nodes
    - Ensemble model
        - The output is an average of all outputs from each tree
    - Randomness model
        - A randomized node optimization can be used here just as it was for the classifier
    - Training objective function
        - The main difference between the classifier and regressor here is the objective functio, which we aim to optimize
    - Weak learner
        - Just as with the classifier, three models are considered: axis-aligned hyperplanes, oriented hyperplanes, conic sections
- Effect of model parameters
    - Forest size
        - A larger forest results in smoother uncertainty and prediction mean curve
    - Tree depth
        - A regression forest with too few levels may under-fit, whereas one with too many can over-fit
    - Spatial smoothness and testing uncertainty
        - Authors performed experiments to see that uncertainty increased moving away from training data

**Chapter 6: Density Forests**
- Density estimation in the literature
    - Here we focus on using forests in situations where the scenarios are unlabeled 
    - Given a set of observations that are unlabeled, we want to estimate the probability density function (pdf) from which the data has been made
    - Density forests are collections of randomly trained clustering trees
    - This is a generalization of the Gaussian mixture model (GMM)
        - each tree has multiple hard clustered data partitions
        - the forest posterior is a combination of tree posteriors
    - The original dataset is split into compact clusters such that the centers are in areas with high density
- Specializing the forest model for density estimation
    - Differences between the probability density model and a conventional Gaussian mixture model include that the ensemble involves mixing that is uniform across the trees, and this has its benefits
- Effect of model parameters
    - Deeper trees result in more splits and smaller Gaussians and ultimately overfitting
    - A larger forest helps accommodate for if individual trees over-fit more, which is in part due to the randomness of tree density estimation
- Comparison with alternative algorithms
    - Compared to the method of k-nearest neighbor density estimation, the random forest produces a smoother outcome
    - Randomness results in better results, whether it be randomness from the forst model or Gaussian mixture

**Chapter 7: Manifold Forests**
- Manifold learning and dimensionality reduction in the literature
    -    Manifold learning involves dimensional reduction and embedding
    -    Manifold forests include
        -    computational efficiency, discriminative features are automatically selected via optimization based on information, and benefits from being a general forest model
- Specializing the forest model for manifold learning
    - The task of manifold forests is to perform a smooth mapping that saves the observations' relative geodesic distsances given a set of unlabeled observations
    - Like density forests, manifold forests are groups of clustering trees - but these require additional components, like affinity between data points, that density forests do not 
    - A manifold forest determines the affinity between pairs of input unlabeled data points, and then given this, dimensionality reduction is performed
    - THe model tries to preserve the inter-point distances after mapping
        - mahalanobis, gaussian, and binary affinity are different methods for this
    - The pairwise affinities of the tree structure itself can be used when dealing with complex data for which pairwise distances are difficult to find
    - The slowest part of this model is solving the eigen-system, but only a few eigenvectors are necessary, and coupled with a sparse matrix in calculations, this makes for a very computationally efficient model
- Experiments and the effect of model parameters
    - Larger forests result in models that are more robust to noise

**Chapter 8: Semi-supervised Classification Forests**
- Introduction and semi-supervised learning in literature 
    - Regression and classification use decision forests in supervised problems, density and manifold estimation use decision forests in unsupervised problems
    - Semi-supervised: only have a small set of available labeled training data points, and a large set of unlabeled
        - very applicable in medical settings where cannot diagnose all data
    - Transductive learning - use underlying data distribution, vs inductive learning where not have test data available during training
    - We need to separate different known class labels and ensure classification boundaries only go through regions of low data density
- Specializing the Decision Forest Model for semi-supervised classification
    - Problem statement: given both labeled and unlabeled data points, we want to associate the unlabeled data points that are already available with a particular class label
    - Semi-supervised forest - a transductive forest that has trees trained on partially labeled data (some labeled, some unlabeled)
- Transduction trees for classifying already available data
    - Transduction is first performed in which labels are propagated, using annotated data points to then annotate the originally un-annotated data points
- Induction from transduction
    - This method involves the development of a general probabilitistic classifcation rule
    - Should not use newly labeled data as ground truth and develop an inductive classifier from scratch
    - Two alternatives but simplest is to make an inductive posterior using feature space partitions that already exist
- Examples, Model Parameters
    - Compared to transductive SVMs, the forest captures more uncertainty, with more noise in the input translating to lower prediction confidence
    - Increasing tree depth results in more accurate and confident output

**Chapter 9: Keypoint Recognition Using Random Forests and Random Ferns**
- Introduction
    - Goal is to move much of computational burden to training phase so run-time detection fast and reliable
    - method: match interest points taken from tarining images with interest points taken from input images acquired at run-time
        - match interest points by make affine-invariant desriptors of image patches surrounding the points, compare across many images
- Wide-Baseline Point Matching as a Classification Problem
    -   Method is to match keypoints in an input image to those in a target object
- Keypoint Recognition with Classification Forests
    - Random Classification Forests
        - A negative side to using classification forests is their greedy use of memory, with memory size increasing exponentially with depth and linearly with number of trees
    - Node Tests
        - A simple binary test is performed between two pixel intensities at two points adjacent to the keypoint 
    - Building the Tree
        - Many trees are used to increase the rate of recognition
        - Instead of top-down construction of trees, they will be made by randomly picking a set, and this results in a faster and simpler method
- Keypoint Recognition with Random Ferns
    - Random Ferns
        - The approach is powerful because groups of binary tests are combined thereby improving classification rates, not based on a feature of the tree structure itself
    - Training the Ferns
        - This involves estimating the class conditional probabilities for each fern and class
- Comparing Random Forests, Random Ferns, and SIFT
    - Empirical Comparisons of Trees and Ferns
        - To convert a tree into a fern, the tree must perform the same test across a hierarchy level (so same test independent of path chosen), and the hierarchy structure is removed to just have feature values at each level 
        - Ferns are essentially simplified trees
    - Empirical Comparisons Between SIFT and Ferns
        - Ferns are much faster, but SIFT does not require training which can be advantageous
- Discussion
    - Compared to averaging probabilities like in random forests, ferns that use Naïve-Bayesian combination of classifiers perform better

**Chapter 10: Extremely Randomized Trees and Random Subwindows for Image Classification, Annotation, and Retrieval**
- Random Subwindow-Based Image Analysis
    - Training Stage
    - Prediction Stage
    - Discussion
        - Subwindows Extraction
        - Subwindows Transformation
        - Feature Extraction
- Extremely Randomized Trees
    - Extremely and Totally Randomized Trees
    - Multiple Output Trees
    - Kernel View of Tree-Based Ensembles
- Applications
    - Content-Based Image Retrieval
    - Image Classification
    - Interest Point Detection
    - Image Segmentation
