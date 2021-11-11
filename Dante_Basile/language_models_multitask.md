# Language Models are Unsupervised Multitask Learners

Dante Basile

## Motivation
* Multitask learning rare in NLP, but could improve generality

## Problem Space
* Language modeling framed as unsupervised distribuition from a set of examples $(x_1, x_2, ..., x_n)$ composed of variable length sequences $(s_1, s_2, ..., s_n)$. 
* Language has sequential ordering
    * Factorize joint probabilities over symbols as product of conditional probabilities
    * Transformer architecture computes these conditional probabilities.
* Learning to perform task: $p(output | input)$. 
* $P(output | input, task)$
* Supervised objective is the same as the unsupervised objective but only evaluated on a subset of the sequence
