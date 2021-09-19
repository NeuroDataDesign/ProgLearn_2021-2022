# Omnidirectional Transfer for Quasilinear Lifelong Learning

[![Paper](https://img.shields.io/badge/Paper-arXiv-green)](https://arxiv.org/pdf/2004.12908.pdf)

## Introduction

* In biological learning, the learning is lifelong, with agents conitnually building on past knowledge and experiences, improving on many tasks given data associated with any task. (e.g. learning a second language improves the individual's performance in his native language)
* Even though classical ML can simultaneously optimize for multiple tasks, if is difficult to sequentially optimize for multiple tasks.
* Catastrophic forgetting: performance on the prior tasks drop precipitously upon training on new tasks.
* Biological learning doesn't suffer from catastrophic forgetting
* Two camps of overcoming catastrophic forgetting:
    * Fixed resources, and therefore, reallocate resources (compressing representations) to incorporate new knowledge (**biologically, this is adulthood**)
    * Adds resources to incorporate new knowledge (**biologically, this is (juvenile) development**)
* The inability to omnidirectionally transfer is one of the key liming factors of AI.
* In ProgNN, new tasks yield additional representational capacity. ProgNN can transfer forward, but they cannot transfer backward.

## Main Contributions

* Representational ensembling that enables omnidirectional transfer via an "Omni-voter" layer
* Computational time reduced from quadratic to quasilinear
* Two types of omnidirectional learning algorithms: 
    * Omnidirectional Forests (ODIF)
    * Omnidirectional Networks (ODIN)
* ODIN and ODIF are resource building (juvenile) but since they can leverage prior representations, they can convert in to an resouce recruiting (adult) state too. 

## Background

===============================

* The concept of omnidirectional transfer of knowledge is proposed to overcome the issue of catastrophic forgetting. 

* Through omnidirectional transfer, it is possible to realize the goal of lifelong learning, which is to improve the performance on a new task using knowledge about existing tasks and their data, while improving the performance on the previous tasks using the knowledge about new tasks and their data. 

* Introducing the concept of representational ensembling (through the Omni-voter) to accomplish the omnidirectional transfer is quite intuitive and its success is backed by experimental evidence mentioned in the manuscript.

* This work further uses progressive learning concepts to incorporate resource building and resource recruitment into the proposed algorithms. 

# Potential Future directions? 

* How can we expand the proposed learning framework into task-agnostic situations? 
* How can we integrate tasks from different domains? (for instance, training an algorithm to learn two distinctive computer vision tasks. e.g. task 1: object recognition and task 2: semantic segmentation) 
* Would there be an upper bound / practical limitation for increasing representational capacity as the number of tasks fed into the network increases?
* How can we extend the concept of omnidirectional transfer to learning algorithms other than PLNs and PLFs? (and for the situations where the hypotheses that cannot be readily decomposed into discernible transformers, voters, and deciders)

