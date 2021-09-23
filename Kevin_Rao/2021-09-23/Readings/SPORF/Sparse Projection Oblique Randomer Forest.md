# Sparse Projection Oblique Randomer Forest
## Metadata
- Date Created: [[2021-09-22]]
- Status: #status/in_progress
- Note Type: #note/permenant_note
- Topic: [[Machine Learning]]
- Tags: 
---

Random forests have a strength and limitation in how they split data, which is along lines parallel to the axis of the coordinate system. Oblique random forests on the other hand use oblique decision boundaries. However, when compounded with sparse projection which determines splits over training data with random projection. In doing so, it keeps high accuracy and improves efficiency of matrix multiplication.

This introduces a new hyperparameter $\lambda \in (0, 1]$ which is the density of the random projection matrix $\mathbf{A}$, providing not only another means of tuning the forest’s growth, but addresses a number of desired features of an improved random forest algorithm.

## Training and Hyperparameter Tuning
The objective function for each split node in the random forest minimizes the Gini impurity. Trees are fully grown unpruned (nodes split until fully pure).

The first parameter tuned in SPORF is $d$, the number of columns in random projection matrix $\mathbf{A}$ and $d \ll \min(p, n)$ where $p$ is the number of columns in the data matrix $X$ and $n$ is the number of rows.

---
## Related