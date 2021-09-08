# Lifelong Learning

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
* Omnidirectional Networks (ODIN)
* Act on arbitrary number of tasks
* Evaluate with transfer efficiency ${TE}_n^t(f) := \mathbb{E}[R^t (f(\textbf{S}_n^t))] / \mathbb{E}[R^t(f(\textbf{S}_n))]$
    * Transfer learning took place iff $TE_n^t(f) > 1$
* Omnidirectional Structure
    * Representers: New added for each task. Trained on respective task.
    * Voters: New added for each task. Ensemble all representers.
    * Decider: Ensemble all voters for final prediction.
