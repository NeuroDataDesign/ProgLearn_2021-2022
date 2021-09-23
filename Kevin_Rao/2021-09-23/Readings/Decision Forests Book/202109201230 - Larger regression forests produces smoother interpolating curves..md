---
alias: "Larger regression forests produces smoother interpolating curves."
---
# Larger regression forests produces smoother interpolating curves.
## Metadata
- ID: 202109201230
- Date Created: [[2021-09-20]]
- Status: #status/in_progress
- Note Type: #note/permenant_note
- Topic: [[Random Forest]], [[Machine Learning]]
- Tags: 
---

The mean prediction curve denotes the mean prediction $\bar{y}(x)$ of a random forest for a particular input $x$, with each possible prediction weighed by the conditional probability $p(y|x)$:
$$
\bar{y}(x) = \int yp(y|x)dy
$$

When the training data are in two separate clusters, smaller forests produced prediction mean curves with sharper turns. As the number of trees in the forest increases, the smoothness and by extension its uncertainty becomes smoother. Uncertainty also increases in gaps between training data clusters. This behavior demonstrates strong generalizability of the model.

![[Pasted image 20210920123118.png]]

> ![[9781447149293 Decision Forests for Computer Vision and Medical Image Analysis#^9f30c1]]

---
## Source
[[9781447149293 Decision Forests for Computer Vision and Medical Image Analysis|Decision Forests for Computer Vision and Medical Image Analysis]]