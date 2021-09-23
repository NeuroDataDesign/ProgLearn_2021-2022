[Notes on the Brieman paper](http://link.springer.com/content/pdf/10.1023/A:1010933404324.pdf)

# Random Forests
## Introduction
* random split selection
  * at each node the split is selected from k best splits
* random subspace
  * random selection of a subset of features to use to grow each tree
* Amit and Geman define a large number of geometric features and search over a random selection of these for the best split at each node
* common element
  * for kth tree, a random vector is generated, independent of other random vectors, but with the same distribution
  * tree is grown using training set and random vector
  * resulting in a classifier where x is an input vector       
