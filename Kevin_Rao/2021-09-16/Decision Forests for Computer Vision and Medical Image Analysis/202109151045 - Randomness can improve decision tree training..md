---
alias: "Randomness can improve decision tree training."
---
# Randomness can improve decision tree training.
## Metadata
- ID: 202109151045
- Date Created: [[2021-09-15]]
- Status: #status/in_progress
- Note Type: #note/permenant_note
- Topic: [[Decision Tree]], [[Random Forest]], [[Machine Learning]], 
- Tags: 
---

There are various random techniques that can be used to improve the training of a decision tree and random forest.

## Bagging
[[Bagging]] improves the generalizability and reduces overfitting in a random forest. It works by training each tree in a random forest on a different training subset which are randomly sampled from the same common database. It also avoids the specialization of parameters to a single training set to improve generalization. It is also faster than using the entire labeled set. However, this could compromise the accuracy of individual trees since they do not use the whole data set.

## Randomized Node Optimization
Under this method, optimization for each node is done with respect to the entire parameter space $\mathcal{T}$

$$\boldsymbol{\theta_j} = \arg\max_{\boldsymbol{\theta} \in \mathcal{T}_j} I(\mathcal{S_j}, \boldsymbol{\theta})$$

However, this process is not efficient searching the entire parameter space which could be infinite.
Instead, one may attempt to randomize the parameters from the parameter space

---
## Source
[[9781447149293 Decision Forests for Computer Vision and Medical Image Analysis|Decision Forests for Computer Vision and Medical Image Analysis]]