# Week 2 Notes - 9/13
## Textbook
- Chapter 1
  - regression, classification, semi-supervised tasks --> general decision forest model
  - optimize algorithm once --> adapt easily to applications
  - decision trees useful but limited to low dimensional data --> ensembles have better acc and generalizability including for high dimensional data --> decision forests
- Chapter 2
  - Forest notation
  - data notation
  - common terms
- Chapter 3 - Introduction: Abstract Forest Model
  - good generalization through ensembles of different trees
  - tree - type of graph made of nodes and edges
  - nodes = internal (split) nodes + terminal (leaf) nodes
  - internal nodes = circles
  - terminal nodes = square
  - devision tree - asks questions about properties of object to make decision
  - question depends on prior question response
  - leaf has most probable answer
  - key = tests with each internal node + decision making predictors at each leaf node
  - split complec problems into smaller ones
  - dimensionality of feature space can be infinite --> don't extract all d dimensions ahead of time --> extract on as-needed basis
  - split (test) functions at each node
  - function output = true or false to send to a child node
  - randomly trained decision trees - 2 phases (training or testing)
  - on-line phase (testing) - each split node applies test function to v until data point reaches leaf, leaf node has predictor that associates label with the input
  - off-line phase (training) - greedy approach to optimization, 
- Chapter 4
## Progressive Learning: A deep learning framework for continual learning
