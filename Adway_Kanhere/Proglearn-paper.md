# Omnidirectional Transfer for Quasilinear Lifelong Learning

Paper:

[![arXiv](https://img.shields.io/badge/arXiv-2004.12908-red.svg?style=flat)](https://arxiv.org/abs/2004.12908)

## Summary

*How can we avoid catastrophic forgetting while also improving performance on new and previous tasks*

Presents Omni-voter layer - Ensembling representations independently omnidirectionally by connecting past and future tasks

## Introduction

- Classical ML is designed to perform well on a single task with no prior knowledge.
- This theory can be extended to multi-class problems
- *This fails when we have to sequentially optimize for multiple tasks*

SOTA sequential learning algorithms are unable to transfer knowledge forward and back for small sample sizes

## Background

The goal of lifelong learning: Given new data and task at hand, get the lowest generalization error for the new task while using the new data to lower generalization error on already learned tasks.

Evaluation criteria:

Forward transfer function (**Is the model learning on new data quickly?**) - The forward transfer efficiency of $f$ for task $t$ given $n$ samples is
$$TE_n^t (f) := \\{E} [R^t (f(D_n^{t}) )] / \\{E} [R^t (f(D_n^{<t}))]$$

We say an algorithm achieves forward transfer for task $t$ if and only if $FTE_n^t(f) > 1$

Backward transfer function (**Is the model forgetting?**) - The backward transfer efficiency of $f$ for task $t$ given $n$ samples is \n
$$BTE_n^t (f) := \\{E} [R^t (f(D_n^{<t}) )] / \\{E} [R^t (f(D_n))]$$

We say an algorithm achieves backward transfer for task $t$ if and only if $BTE_n^t(f) > 1$

The transfer efficiency of $f$ for task $t$ given $n$ samples is \n

$$TE_n^t (f) := \\{E} [R^t (f(D_n^{t}) )] / \\{E} [R^t (f(D_n))]$$

We say an algorithm has transfer learned for task $t$ with data $D_n$ if and only if $TE_n^t(f) > 1$

## Results

Shows Omnidirectional learning is successful by detailing about various scenarios.

## Further discussion

1. Need to look into storing all the data using Generative modelling

2. To enhance transfer of knowledge between tasks, we need pruning of representers
