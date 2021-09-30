---
aliases: ["Decision Forests for Computer Vision and Medical Image Analysis"]
---
# Decision Forests for Computer Vision and Medical Image Analysis
## Metadata
- Author: [[Antonio Criminisi]], [[Jamie Shotton]]
- Date Created: [[2021-09-13]]
- Date Published:
- Status: #status/in_progress
- Source: 9781447149293
- Source Type: #source/book 
- Note Type: #note/highlights 
- Topic: 
- Tags: 
---
## The Decision Forest Model
- In a decision tree this set of diagnostic tests is organized hierarchically in a tree structure. For a given input object, a decision tree estimates an unknown property of the object by asking successive questions about its known properties. Which question to ask next depends on the answer of the previous question and this relationship is represented graphically as a path through the tree which the object follows. The decision is then made based on the terminal node reached by the input object. ^f13ac6
- ![[Pasted image 20210913134532.png]]
-    Also, the more questions asked, the higher the confidence we should expect in the response. The tests can be represented hierarchically via a decision tree structure. In a decision tree, each internal node is associated with one such question.
- A decision tree can also be thought of as a technique for splitting complex problems into a set of simpler ones. It is a hierarchical piece-wise model. Its parameters (the node tests, the leaves predictors, etc.) could be selected by hand for simple problems. In more complex problems (such as vision related ones) the tree parameters and structure should be learned automatically from available training data. ^d4a223
-  In fact, the result of the optimization problem in (3.3) determines the parameters of the weak learners, which, in turn, determine the path followed by a data point and thus its associated prediction.
-  In fact, the result of the optimization problem in (3.3) determines the parameters of the weak learners, which, in turn, determine the path followed by a data point and thus its associated prediction. In summary, through its influence on the choice of weak learners, the energy model determines the prediction and estimation behavior of a decision tree. ^190e36
- Since the split nodes act on features, the input test point is likely to end up in a leaf associated with training points which are all similar to itself. Thus, it is reasonable to assume that the associated label must also be similar to that of the training points in that leaf. ^d173e4
- The key aspect of the forest model is the fact that its component trees are all randomly different from one another. This leads to de-correlation between the individual tree predictions and, in turn, results in improved generalization and robustness.

## Classification Forests
-  More formally, during testing we are given an input test data v and we wish to infer a class label c such that $c \in \mathcal{C}$, with $\mathcal{C} = \{c_k\}_{k=1}^{|\mathcal{C}|}$. More generally we wish to compute the whole distribution $p(c|\mathbf{v})$. ^9224b6
-  Note that in some applications one has an unbalanced distribution of classes in the training set S0. For instance, when performing semantic image segmentation the number of “background” pixels may dominate other “object” pixels. This may have a detrimental effect on forest training. This problem may be mitigated by resampling the training data so as to have roughly uniform training distributions. An alternative is to use the known prior class distribution to weight the contribution of each class by its inverse frequency when computing the information gain at each split node. ^18ac99
- Now we observe higher confidence near the training points and lower confidence away from training regions of space; a more intuitive generalization behavior. ^bbe66d
- If the noise in the position of training points increases (cf. Fig. 4.4b and Fig. 4.4c) then training points for different classes are more intermingled with one another. As expected, this increase in training noise yields a larger overall uncertainty in the testing posterior (represented by less saturated colors in Fig. 4.4c).  ^b49c01
- Thus, while using multiple trees alleviates the overfitting problem of individual trees, it does not cure it completely. In practice one has to be very careful to select the most appropriate value of D as its optimal value is a function of the problem complexity ^f91ff1
- Larger randomness reduces the blocky artifacts of the axis-aligned weak learner and produces more rounded decision boundaries (first column in Fig. 4.8). Furthermore, larger randomness yields a much lower overall confidence.
## Regression Forests
- Given a labeled set of training data, learn a general mapping which associates previously unseen, independent test data points with their dependent, continuous output prediction. ^b70f9d
- Like classification, the regression task is inductive, with the main difference being the continuous nature of the output
- A regression forest is a collection of randomly trained regression trees (Fig. 5.2). As with classification, it can be shown that in general a random regression forest generalizes better than a single fully optimized regression tree.
- However, as the number of trees increases both the prediction mean curve and its uncertainty become smoother. Thus smoothness of the interpolating curve is controlled here by the forest size T . We can also observe how the uncertainty increases as we move away from the training data (both in the interpolated gap and in the extrapolated regions). ^9f30c1
## Density Forests
- The density estimation task can be summarized as follows: Given a set of unlabeled observations we wish to estimate the probability density function from which such data have been generated. ^509b9a
- For a set of data points in feature space, the determinant of the covariance matrix is a function of the volume of the ellipsoid corresponding to that cluster. Therefore, by maximizing (6.4) the tree training procedure tends to split the original dataset S0 into a number of compact clusters (see Fig. 6.1a). The centers of those clusters tends to be placed in areas of high data density, while the separating surfaces are placed along regions of low density. ^b9feeb
## Manifold Forests
-    1. A decision forest is used to infer efficiently the k × k affinity matrix W between   all pairs of input unlabeled data points;   2In practical applications the original space is usually of much higher dimensionality than 2D.  2. Given W, dimensionality reduction is performed by applying any known technique. As an example, here we employ Laplacian eigenmaps. ^91eb9a
## Semi-supervised Classification Forests


---
## Related