# Omnidirectional Transfer for Quasilinear Lifelong Learning

Dante Basile

## Transfer learning
* Catastrophic learning: performance on prior tasks degrades when learning tasks sequentially
* Lifelong learning: maintain performance on prior tasks while learning
    * Paper seeks to allow learning new tasks to improve performance on prior tasks
    * Omnidirectional transfer learning algorithms
    * Omni-voter layer: ensemble representations from all tasks to jointly predict current data

## Omnidirectional learning: allow learning to improve performance on tasks in the past or future
* Progressive Neural Networks (ProgNN): Transfer forwards but not backwards
* Omnidirectional Forests (ODIF)
    * Representer: Decision Forest where there are $B$ trees, each with $L_b$ leaves
        * Inputs: Trained on bagged data for task $t$. Predict OOB data.
        * Outputs: $B$ sparse vector of length $\sum_{b=1}^{B} {L_b}$
    * Voter: Perform argmax on average of the posterior leafs from each representer
        * Inputs: Posteriors of each representer forest
        * Outputs: Class label aggregate posterior estimates
    * Decider: averages posteriors and takes argmax to make prediction
* Omnidirectional Networks (ODIN)
    * Representer: All network layers except final layer
        * Inputs: Data for task $t$
        * Outputs: $\mathbb{R}^d$ vector to final network layer, where there are $d$ classes
    * Voter: KNN on the $\mathbb{R}^d$ points
        * Inputs: $\mathbb{R}^d$ vector from each representer taken as a point for KNN
        * Outputs: Class label aggregate posterior estimates
    * Decider: averages posteriors and takes argmax to make prediction
* Act on arbitrary number of tasks
* Evaluate with transfer efficiency ${TE}_n^t(f) := \mathbb{E}[R^t (f(\textbf{S}_n^t))] / \mathbb{E}[R^t(f(\textbf{S}_n))]$
    * Transfer learning took place iff $TE_n^t(f) > 1$
* Omnidirectional Structure
    * Representers: New added for each task. Trained on respective task.
    * Voters: New added for each task. Ensemble all representers.
    * Decider: Ensemble all voters for final prediction.
