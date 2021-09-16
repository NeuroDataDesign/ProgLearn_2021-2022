---
aliases: ["Random Forest"]
---
# Random Forests
## Metadata
- Author: [[Leo Breiman]]
- Date Created: [[2021-09-13]]
- Date Published:
- Status: #status/in_progress
- Source: https://doi.org/10.1023/A:1010933404324
- Source Type: #source/article 
- Note Type: #note/highlights 
- Topic: [[Random Forest]], 
- Tags: 
---
## Summary
## Highlights
- Significant improvements in classification accuracy have resulted from growing an ensemble of trees and letting them vote for the most popular class. In order to grow these ensembles, often random vectors are generated that govern the growth of each tree in the ensemble. An early example is bagging (Breiman, 1996), where to grow each tree a random selection (without replacement) is made from the examples in the training set.
- Definition 1.1 A random forest is a classifier consisting of a collection of tree-structured classifiers $\{h(\mathbf{x}, \Theta_k), k=1,\ldots\}$ where the $\{\Theta_k\}$ are independent identically distributed random vectors and each tree casts a unit vote for the most popular class at input $\mathbf{x}$. ^f70b39
- The margin measures the extent to which average number of votes at $\mathbf{X}$, $Y$ for the right class exceeds the average vote for any other class. The larger the margin, the more confidence in the classification.
- There are two reasons for using bagging. The first is that the use of bagging seems to enhance accuracy when random features are used. The second is that bagging can be used to give ongoing estimates of the generalization error (PE∗) of the combined ensemble of trees, as well as estimates for the strength and correlation. These estimates are done out-of-bag, which is explained as follows. ^5b08ae
- One advantage of this approach is that it gets around the difficulty of what to do with categoricals that have many values. In the two-class problem, this can be avoided by using the device proposed in Breiman et al. (1985) which reduces the search for the best categorical split to an O(I ) computation. For more classes, the search for the best categorical split is an O(2I−1) computation. In the random forest implementation, the computation for any categorical variable involves only the selection of a random subset of the categories
- The Adaboost algorithm iteratively increases the weights on the instances most recently misclassified. Instances having incorrect class labels will persist in being misclassified. Then, Adaboost will concentrate increasing weight on these noisy instances and become warped. The random forest procedures do not concentrate weight on any subset of the instances and the noise effect is smaller. ^3067b5
## Further References
---
## Related