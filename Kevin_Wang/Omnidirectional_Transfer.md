# Omnidirectional Transfer for Quasilinear Lifelong Learning

> https://arxiv.org/abs/2004.12908

Inability to omnidirectionally transfer learned intelligence is one of the key obstacles limiting AI
Key Innovation: introduction of representation ensembling which enables omnidirectional transfer via an “omni-voter” layer, reducing computational time
and space from quadratic to quasilinear

- Implemented 2 omnidirectional learning algorithms: one based on decision forest and one based on deep network
- Odin vs. ProgNN
  1. Odin excludes lateral connections built by ProgNN. This reduces the number of parameters and train time. It also makes each representation independent
  2. For inference, Odin uses representations from all tasks, while ProgNN only uses some
- 
