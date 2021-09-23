# Tomia 2015 - Sparse Projection Oblique Randomer Forests

## Introduction
  - Random Forests and XGBoost - popular ensembles of axis-aligned trees
    - Both require deep trees and step-like decision boundaries
      - Leads to overfitting and variance
  - Oblique splits
    - Forest-RC (described by Breiman) splits on linear combinations of coordinates instead of individual coordinates
  - Sparse Projection Oblique Randomer Forests (SPORF)
	  - At each node, SPORF searches for splits over a sample of sparse random projections instead of axis-aligned splits

## Background and related work
### Random Forests
  - Splits based on information gain
    - i.e. reduction in Gini impurity
  - **Process**
    1. We index a dimension and splitting threshold and make left and right partitions
    2. Sample a random subset of features and evaluate objective function
    3. Recursively split nodes until stopping cue
      - max depth
      - min number observations in node
      - purity

### Oblique Extensions to Random Forest
  - Relax the axial restriction of RF 
    - These are oblique to the coordinate axes
    - *Past approaches:*
      - Breiman F-RC
      - Random Rotation Random Forest 
        - We rotate data prior to creating trees
      - Canonical Correlation Forests 
        - Perform correlation analysis to correlate with class labels

### Gradient Boosted Trees
  - GBT 
    - Are learned iteratively by minimizing cost function via gradient descent
    - Accurate over a wide range of settings

## Methods
### Sparse Projection Oblique Randomer Forests
  - Search for best split in the dimensions of projected space
  - Default projection distirbution are based on:
	  - Random search for splits
	    - Can identify good splits, such as success to RF
	  - Flexibile sparsity
      - E.g. The case of highly uninformative features or a high dimensionsal space with only a few informative features
        - Appropriate amount of sparsity needed
	  - Ease of tuning 
	  - Data insight
	    - Other oblique forests don't lend themselves well to Gini importance
	  - Scalability

### Training and Hyperparameter Tuning
  - Nodes are split until they are pure 
    - We average over many uncorrelated trees to alleviate overfitting
	- Tune the number of candidate split directions at each node 
	- Tune the average sparsity of univariate projections at each split node
	- *These values are optimized in the authors' experiments over certain ranges*

## Simulated Data Emperical Performance
  - SPORF is robust to hyperparameter selection 
  - SPORF performs better than F-RC in orthant and sparse parity simulations
  - Feature importances can be computed via Gini importance 
 
## Computational Efficiency and Scalability
  - Time complexity
    - RF: $\mathcal{O}(Tdn \log^2n)$
    - SPORF: $\mathcal{O}(Tdnlog^2n + Tdnp\lambda)$
	    - $d > p$ may mean longer SPORF training times, but $d > p$ may mean improved classification performance
  - Space complexity of RF and SPORF are both $\mathcal{O}(T(np + c))$

## Conclusion
  - SPORF preserves good properties of RF while gaining performance benefits of oblique splitting 
    - Statistically robust
    - Computationally efficient
    - Scalable
    - Interpretable
