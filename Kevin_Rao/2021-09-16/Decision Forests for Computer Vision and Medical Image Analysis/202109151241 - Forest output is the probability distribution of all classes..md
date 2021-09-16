---
alias: "Forest output is the probability distribution of all classes."
---
# Forest output is the probability distribution of all classes.
## Metadata
- ID: 202109151241
- Date Created: [[2021-09-15]]
- Status: #status/in_progress
- Note Type: #note/permenant_note
- Topic: [[Random Forest]], [[Machine Learning]]
- Tags: 
---

Each tree leaf $t4$ of a random forest returns the posterior probability of input $\mathbf{v}$ being labeled class $c$ as $p_t(c|\mathbf{v})$. For a forest with $T$ leaves, the posterior probability of the tree labeling an input $\mathbf{v}$ class $c$ is equal to
$$
p(c| \mathbf{v}) = \frac{1}{T} \sum_{t=1}^T p_t(c|\mathbf{v})
$$

---
## Source
[[9781447149293 Decision Forests for Computer Vision and Medical Image Analysis]]