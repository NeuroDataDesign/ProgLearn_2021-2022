[Lifelong Learning Notes](https://arxiv.org/pdf/2004.12908.pdf)

# Abstract
  * Terms
    * tabula rasa - blank slate
    * omnidirectional transfer learning algorithms 
      * decision forests
      * deep networks
    * omni-voter layer
    
# Introduction
  * Easy to simultaneously learn, hard to sequentially learn
  * Catastrophic forgetting
    * performance on prior tasks drops after training on new tasks
  * Two approaches to lifelong learning
    * fixed resources, reallocate space as new things are learned, compress
    * add resources as new data arrives
    * both can only really transfer data forward
  * Omnidirectional learning
    * Builds on progressive neural networks
      * new tasks give additional representative capacity
      * [Progressive Neural Networks paper](https://arxiv.org/pdf/1606.04671.pdf)
      * Quadratic space and time complexity
    * "introduction of representation ensembling"
      * enables omnidirectional transfer via 'omni-voter' layer
    * quasi-linear
    * two complimentary omnidirectional learning algorithms
      * based on decision forests
      * based on deep networks  
# Background
## Classical Machine Learning
  * Random variables (x,y)
  * Given a loss fn (l), we try to find a hypothesis (h) that minimizes the loss function
  * Learning algorithm (f) maps data sets to a hypothesis
  * Trying to find a learning algorithm that learns a hypothesis with the least amount of error
## Lifelong Learning
  * Generalizes classical machine learning
    * environment of possibly infinitely many tasks
    * data arrives sequentially
    * computational complexity constraints on l and h
      * this is mostly implicit
      * to constrain what is classified as lifelong learning
  * given new data and new task -> use existing data for lower error on new task -> use new data for lower error on original tasks
  * previous tasks can reoccur, so we wanna be ready
  * previous work
    * continually updating fixed parametric model
    * adding resources as new tasks come
    * some approaches store or replay tasks to reduce forgetting
  * task-aware
    * learner is aware of all task details for all tasks
  * task-unaware
    * learner may not know the task is changed
## Reference Algorithms
  * existing algorithms
    * learn new tasks by building new resources
      * progressive neural networks
        * each task introduces a new column of network
        * lateral connections from all previous columns are added
        * lateral connections are costly
      * deconvolution-factorized CNNs
        * knowledge base w/ lateral connections to each new column
        * avoids pairwise connections
        * less expensive
    * fixed capacity resources
      * elastic weight consolidation
      * online ewc
      * synaptic intelligence
      * learning without forgetting
      * 'None'
        * baseline
        * network was incrementally trained on all tasks in the standard way
        * aways using only the data from current task
      * total replay
        * replay all data from all tasks when a new task is introduced
        * "offline training"
      * partial replay
        * amount of replay is fixed to number of samples in new task
        * samples to be replayed are randomly chosen from previous tasks
 # Evaluation Criteria
   * other definitions compare the difference btwn learning w/ and w/o transfer, not the ratio
   * Pearl built his from statistics - transfer benefit ratio
   * "transfer efficiency"
     * ratio of the generalization error of an algorithm trained with only the current task data vs an algorithm trained on other data as well
     * R^t is risk associated with task t
     * R^t(f(Sn)) -> risk on task t of hypothesis on all data
   * forward transfer efficiency
     * expected ratio of the risk with
       * access to only task t data
       * access to data up to and including t
     *  relative effect of previously seen out-of-task data on the performance on task 
        
