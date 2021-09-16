---
alias: "Weak learners construct the class boundaries in decision trees."
---
# Weak learners construct the class boundaries in decision trees.
## Metadata
- ID: 202109151021
- Date Created: [[2021-09-15]]
- Status: #status/in_progress
- Note Type: #note/permenant_note
- Topic: [[Decision Tree]]
- Tags: 
---

Weak learners constitute the split functions inside of a decision tree. Represented as a split function $h(\mathbf{v}, \boldsymbol{\theta})$ where $\mathbf{v}$ is the input to the split function and $\boldsymbol{\theta} = (\boldsymbol{\phi}, \boldsymbol{\psi}, \boldsymbol{\tau})$ are the function’s parameters. These split functions when represented graphically define decision boundaries separating different classes. A decision tree has many nodes with their own weak learner models which collectively define the spaces where data points would correspond to different classes.

![[Pasted image 20210915102734.png]]

---
## Related