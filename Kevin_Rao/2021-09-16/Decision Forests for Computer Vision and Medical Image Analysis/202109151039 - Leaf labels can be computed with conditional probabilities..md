---
alias: "Leaf labels can be computed with conditional probabilities."
---
# Leaf labels can be computed with conditional probabilities.
## Metadata
- ID: 202109151039
- Date Created: [[2021-09-15]]
- Status: #status/in_progress
- Note Type: #note/permenant_note
- Topic: [[Decision Tree]] , [[Machine Learning]]
- Tags: 
---

In a decision tree, the decisions of each node with respect to an input travels until it reaches a leaf. From the root of a tree, there is only one path that reaches a leaf. Therefore, if an input reaches a leaf, then it shares characteristics with other inputs that reach the same leaf. Therefore, the label associated with the leaf must be common to the labels of the data points that reach the leaf.

![[9781447149293 Decision Forests for Computer Vision and Medical Image Analysis#^d173e4]]

So, when a leaf is given a particular data point, it has an associated probability of classifying it under a certain class; or in other words, a conditional probability $p(c|\mathbf{v})$.

Different leaf classifiers could be used, but the most common version is the Maximum A-Posteriori estimate:
$$
c^* = \arg\max_c p(c|\mathbf{v})
$$

---
## Related