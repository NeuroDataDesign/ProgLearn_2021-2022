# Omnidirectional Transfer for Quasilinear Lifelong Learning
Created: 9/2/2021

Updated: 9/7/2021

**Related**: [[Abstract Forest Model]]

## Introduction
Traditional machine learning is optimized for a single task or multiple tasks simulatneously. It is more difficult to **sequentially** optimize for multiple tasks. **"Catastrophic forgetting"** is a typical issue is performance drops when trained on new tasks. 

Past methods either reallocate resources to add new knowledge or build new resources as new data arrives.

The goal: few algorithms transfer knowledge forward and none transfer backward. The intention is to introduce omnidirectional transfer via an **omni-voter layer** to avoid the quadratic space and time complexity in sample size of Progressive Neural Networks (ProgNN), and become **quasilinear** (linear up to polylog terms)

## Background
### Classical Machine Learning
The goal is to find a hypothesis (or predictor/decision rule) $h : \chi \rightarrow \gamma$ that minimizes the expected loss, or *risk*:
$$R(h) = \mathbb{E}_{X,Y}[l(h(X), Y)]$$
A learning algorithm is a function $f$ that maps data sets to a hypothesis, where a data set $\mathbf{S}_n = {X_i, Y_i}^n_{i=1}$  is a set of $n$ input/response pairs $(X,Y)$. Assume the samples are iid from some true but unkown $P_{X,Y}$. 

Learning algorithms are evaluated on generalization error (or expected risk)
$$\mathbb{E}[R(f(\mathbf{S}_n))]$$
This expectation is taken w.r.t the true but unkown distribution governing the data $P_{X,Y}$. 

**The goal:** choose a learner $f$ that learns a hypothesis $h$ that has a small generalization error for the given task. 

### Lifelong Learning
This task generalizes machine learning in a few ways:
1. There are $T$ many tasks rather than only one
2. Data arrives in sequences vs. batches
3. We care about computational complexity

**Goal:** use existing data to achieve lower generalization error on new task (forward), but also use new data to obtain lower generalization on previous tasks (backward)

## Evaluation
* $R^t$ is the risk associated with task $t$
* $S^t_n$ is data from $S_n$ associated with task $t$
* $R^t(f(S^t_n))$ is the risk on task $t$ on the hypothesis learned by $f$ only for that **specific task**
* $R^t(f(S_n))$ is the risk on task $t$ of the hypothesis learned for **all** data

#### Transfer Efficiency
$$TE^t_n(f) := \frac{\mathbb{E}[R^t(f(S^t_n))]}{\mathbb{E}[R^t(f(S_n))]}$$
Algorithm $f$ has transfer learned for task $t$ iff $TE^t_n(f) > 1$

#### Forward Transfer Efficiency
**Summary**: We want to know the relative effect of previous out-of-task data on the performance on task $t$.

**Definition**: Let $N^t$ be the index most recent task $t$, and $S^{<t}_n = {(X_1, Y_1, T_1), ..., (X_{N^t}, Y_{N^t}, T_{N^t})}$ be all data up to and including that data point.
$$FTE^t_n(f) = \frac{\mathbb{E}[R^t(f(S^t_n))]}{\mathbb{E}[R^t(f(S_n^{<t}))]}$$

**Algorithm has (positive) forward transfered for task $t$ if $FTE^t_n > 1$, meaning it has used data from past tasks to improve on task $t$.**

#### Backward Transfer Efficiency
**Summary**: We want to know if the algorithm has improved on previous tasks based on the future task data

**Definition**
$$BTE^t_n(f) = \frac{\mathbb{E}[R^t(f(S_n^{<t}))]}{\mathbb{E}[R^t(f(S_n))]}$$

**Algorithm has (positive) backward transfered for task $t$ if $BTE^t_n > 1$, meaning it has used data from past tasks to improve on task $t$.**

## Omnidirectional Algorithms
Consider $h(\cdot) = w \circ v \circ u(\cdot)$:
1. Representer $u : \chi \rightarrow \tilde{\chi}$ maps $\chi$-valued input into **representation space**
2. Voter $v : \tilde{\chi} \rightarrow \Delta y$ maps representation space data into posterior distribution
3. Decider $w : \Delta y \rightarrow \gamma$ to produce label.

Note that there can be $B$ representers for $B$ voters. Instead of a typical ensemble of voters, the representers are also ensembled for each voter both forward and backward.

## Results
Shows omnidirectional learning is successful in various scenarios.

## Discussion
This paper shows the possibility of achieving forward and backward transfer with little computational cost. Essentially, this is done via ensembling **representations** rather than **learners**.

#ml #ndd
