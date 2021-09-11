# Decision Forests for Computer Vision and Medical Image Analysis

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
