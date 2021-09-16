---
alias: ["Random forests converge"]
---
# Random forests converge
## Metadata
- ID: 202109131139
- Date Created: [[2021-09-13]]
- Status: #status/in_progress
- Note Type: #note/literature_note
- Topic: [[Random Forest]]
- Tags: 
---

## Margin Function
The margin function is a measurement of confidence a classifier has in its decision. For an ensemble of classifiers $h_1(\mathbf{x}) \ldots h_K\mathbf{x})$ with a training set sampled from the distribution $(\mathbf{X}, Y)$:
$$
mg(\mathbf{X}, Y) = av_kI(h_k(\mathbf{X}) = Y) - \max_{j\neq Y}av_kI(h_k(\mathbf{X}) = j)
$$
The margin is the difference between the difference between the average vote for the most popular class and the average vote for the second most popular class.

## Generalization Error
The generalization error is the probability that the margin 

---
## Related