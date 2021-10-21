# Stochastic Grammar of Images: http://www.stat.ucla.edu/~sczhu/papers/Reprint_Grammar.pdf 
*This paper is somewhat long so these notes are not the entirety of the paper*
## Abstract
- stochastic + context sensitive grammar of images
- grammar - unified framework for representation, learning, recognition
- grammer is a hierarchical decomposition of scenes into objects, parts, etc
- grammar is embodied in And-Or graph representation
- given input, image parsing tasks should construct probable parse graph 
- probabilistic model defined on graph accounts for natural frequency for objects, parts, and their relations
- grammar includes many visual dictionaries and organizes them into a graph 
## Introduction
- problem 1 - too much visual knowledge in real world scenes for a computer to represent to make inferences
- problem 2 - computational complexity
- problem 3 - semantic gap btwn pixels and representation
- objective 1 - common framework for visual knowledge representation and object categorization
  - hierarchic + structural composition - grammar
  - image gramar has an And-Or graph representation
  - Or-node - points to alternative sub-configs
  - And-node - decomposed into components
  - And-Or graphc represents hierarchical decompositions from scenes and contexts for spatial relations via horizontal links --> contains all possible parse trees
  - probabilistic model for And-Or graph is learned from examples using MLE
  - object category is defined as the set of all valid configs that are produced by grammar with its probability learned to reproduce the natural freq of instances occurring in the observed ensemble
  - probability model used sparse coding (wavelet coding), stochastic context free grammars (SCFG) with descriptive models lke markov random fields and graphical models
- objective 2 - scalable and recursive top-down/bottom-up computation
  - xyz

# Deep Learning in Radiology: https://www.jacr.org/article/S1546-1440(17)30969-9/fulltext
*One of the paper's with Dr. Yuille and Jovo's dad, not sure if this was among the correct ones but it summarizes how segmentation tasks are prepared prior to model work.*
- weak supervision - bounding box instead of pixel level label, doesn't work well for deep networks
- weak supervision not great for medical applications
- goal: reduce radiologist error, diagnose changes in pancreas to signal cancer
- step 1 - annotate images 
- step 2 - train on normal CT scans to identify normal pancreas
- step 3 - train on abnormal pancreas to identify variety of abnormalities
- annotations include segmentation of pancreas, adjacent organs, and vessels
- 800 cases annotated
- velocity is software used for annotation
