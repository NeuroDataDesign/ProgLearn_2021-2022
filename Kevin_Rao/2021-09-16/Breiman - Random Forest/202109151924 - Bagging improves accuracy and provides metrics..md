---
alias: "Bagging improves accuracy and provides metrics."
---
# Bagging improves accuracy and provides metrics.
## Metadata
- ID: 202109151924
- Date Created: [[2021-09-15]]
- Status: #status/in_progress
- Note Type: #note/permenant_note
- Topic: [[Random Forest]], [[Machine Learning]]
- Tags: 
---

Bagging is the process of randomly sampling from the original training set for a set of features and growing a new tree in the forest using the sampled random features. 
Bagging has two benefits: 
- It improves accuracy when random features are used.
- It can provide ongoing estimates of generalization error of the tree ensemble, strength, and correlation (done out-of-bag)
> ![[Breiman - Random Forest#^5b08ae]]

Bootstrap training sets $T_k$ are sampled from training set $T$. The bootstrapped training sets are used to train classifier $h(\mathbf{x}, T_k)$ which forms the bagged predictor. Then, for each data point, the classifiers that were not constructed using that data point performs a classification on it, producing an out-of-bag classifier that classifiers that were out of the bag of the sample being classified. The error rate of all out-of-bag classifiers result in a generalization error.
[[Leo Breiman]] (1996) demonstrated that out-of-bag estimate is as accurate as using a test set of the same size as the data set, removing the need to reserve a test set.

Unlike cross-validation, out-f-bag estimates are unbiased.

---
## Source
[[Breiman - Random Forest|Random Forest]]