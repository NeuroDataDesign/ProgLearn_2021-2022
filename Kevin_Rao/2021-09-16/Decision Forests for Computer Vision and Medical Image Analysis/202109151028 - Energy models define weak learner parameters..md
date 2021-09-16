---
alias: "Energy models define weak learner parameters."
---
# Energy models define weak learner parameters.
## Metadata
- ID: 202109151028
- Date Created: [[2021-09-15]]
- Status: #status/in_progress
- Note Type: #note/permenant_note
- Topic: [[Machine Learning]], [[Decision Tree]]
- Tags: 
---

Energy models are functions that measure the energy or information gain when data is separated into different sets. When using this as an objective function for optimization, they influence the decision’s trees predictions.
![[9781447149293 Decision Forests for Computer Vision and Medical Image Analysis#^190e36]]

Using the principles of entropy and information gain, one can measure the amount of uncertainty reduced by splitting the data sample $\mathcal{S}$ into different subsets  $\mathcal{S}^L$ and $\mathcal{S}^R$:
$$
I = H(\mathcal{S}) - \sum_{I \in \{L, R\}} \frac{|\mathcal{S}^i|}{\mathcal{S}}H(\mathcal{S}^i)
$$
where $H$ is the [[Entropy|entropy]] function, a measure for the uncertainty.

---
## Related