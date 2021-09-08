# Progressive learning: A deep learning framework for continual learning

>Haytham M. Fayek, Lawrence Cavedon, Hong Ren Wu,
>Progressive learning: A deep learning framework for continual learning, Neural Networks, Volume 128, 2020, Pages 345-357, ISSN 0893-6080, https://doi.org/10.1016/j.neunet.2020.05.011. (https://www.sciencedirect.com/science/article/pii/S0893608020301817)

- Tasks are learned in sequence with the ability to use prior knowledge from previously learned tasks to facilitate the learning and execution of new ones
- 3 procedures: Curriculum, Progression, Pruning

## Curriculum
- determine appropriate task to learn with respect to current knowledge
- tasks chosen based on performance
- iterative procedure, for N tasks, requires N(N+1)/2 models to be trained

## Progression
- Objectives
  1. Increase the capacity of the model by adding new parameters to accommodate learning a new task
  2. Provide a mechanism to leverage parameters learned in prior tasks while learning the new task at hand from data available for the task without being susceptible to catastrophic forgetting
- Uses a progressive block
  - Instantiates and trains a new multi-layered neural network for each new task with randomly initialized parameters
  - Catastrophic forgetting is prevented by only training the newly added parameters of progressive block, while all parameters in prior blocks remain constant
## Pruning
- Counteract the growth in the number of parameters in the model
  - Removes weights in a progressive block after each progression procedure
- Mitigates negative forward transfer
- Iterative greedy layer-wise pruning procedure proposed

## Results
- Evaluated in image and speech recognition
- Progressive learning outperforms independent learning, transfer learning, multi-task learning, and related continual learning baselines

## Limitations
- Absence of a mechanism to allow backward knowledge transfer
