# Week 1 Notes - 9/6
## Figure Checklist
- main point should stand out
- remove unnecessary markings
- consistent color
- title has context
- legible text
- caption should be a sentence, defines acronyms, points out interesting part of figure
- consistent lines/markers
- aesthetics
- remove redundancies 
- check if table can be a figure

## How to Choose a Project
- Feasibility
  - Does one have the necessary background?
  - Does one have the time/resources?
- Significance
  - How many people were impacted?
  - How much was each person impacted?
- Motivation
  - What kinds of things does one do in one's free time?

## Omnidirectional Transfer for Quasilinear Lifelong Learning
- classical ML - starts from tabula rasa
- continual learning - improve/maintain performance on all tasks
- Intro
  - catastrophic forgetting - sequential training causes forgetting learning of prior tasks
  - past approaches to catastrophic forgetting: reallocate resources to learn new knowledge (akin to human adulthood), add new data as it comes in (akin to development in humans)
  - proposed approach: omnidirectional learning
  - ProgNN - transfer only forwards, not backwards
  - 2 algorithms: a) decision forests, b) deep networks
- Classical ML
  - minimized expected loss
  - learning algorithm = f that maps dataset to hypothesis 
  - evaluated based on generalization error
- lifelong learning
  - environment of many tasks
  - sequential, not batch mode, for data arrival
  - computational complexity constraints
  - uses existing data to get lower generalization error on new tasks and using new data to get lower generalization error on prior tasks
  - prior work: 1) updated fixed parametric model as new tasks come in 2) add resources as new tasks come in 
- omnidirectional algorithms
  - representer - maps input into internal representation space
  - voter - maps transformed data into posterior distribution on response space
  - decider - gets predicted label, ensembled voters
  - decision forest learns decision trees, each tree structure corresponds to representer and each tree is assigned to a voter, voter outputs tree's guessed probability that observation is in any class
  - decider outputs likely class averaged over trees
  - each voter ensembles representers
  - ODIN - ensemble representations

## Progressive Learning: A deep learning framework for continual learning
- Intro
  - classical ML - learn from blank slate
  - continual learning - uses knowledge from prior task to help with current task
  - catastrophic forgetting - prior task performance gets worse with learning of current tasks
  - negative forward transfer - prior tasks negatively affect current task performance
  - continual learning needs strategy to select next task to learn, mechanism to grow capacity of model to learn new tasks, method to maintain knowledge
- Progressive Learning
- Curriculum
- Progression
- Pruning
- Evaluation
- Architectures
- Conclusion
