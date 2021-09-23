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
     *  if FTE > 1, the algorithm forward transfers
   * backward transfer efficiency
     * ratio of the risk of the learned hypothesis with access to the data up to and including the last observation to access to the entire dataset
     * BTE > 1 -> algorithm backward transfers
     * algorithm uses data associated with future tasks to improve performance on future tasks
# Omnidirectional algorithms
   * representer maps value into internal space
   * voter maps data into a score on reponse space Y
   * decider produces predicted label
   * decision forest learns B decision trees, 
     * with each having a tree structure corresponding to a representer 
     * decider outputs most likely class averaged over trees
  * omni-voter
     * ensembles all existing representations, regardless of order
     * ensemble of voters leads into single decider
  * omnidirectional forest
     * decision forest-based instance of ensembling representations
     * leaf nodes of each decision tree partition space
     * posteriors output average normalized class votes across trees
     * decider averages estimates and outputs argmax to give a single prediction
     * single task version simplifies to Uncertainty Forests
  * omnidirectional network
     * deep network based ensembling of representations
     * representer is the backbone of an odin, including all but final layer
     * "“5 convolutional layers followed by 2 fully-connected layers each containing 2,000 nodes with ReLU non-linearities and a softmax output layer"  
     * cross-entropy loss and adam optimizer to learn transformer
     * k-nearest neighbor to learn omni-voters
       * k = 16 log2 n
  * algorithm approach
     * new data from new task arrives
     * build a new independent representer
     * builds voter for new task -> integrates info from all existing representers (forward transfer)
     * if new data from old task, leverage new representers to update data (backward transfer)
  * odin and progNN
     * odin has no lateral connections, less time consuming
     * odin has backward transfer, progNN does not
# Results
## Computational taxonomy
  * fixed resource lifelong learning methods are parametic
  * eventually all parametric methods will have catastrophic forgetting
  * semi-parametric -> representational capacity grows slower than sample size
  * progNN is semi-parametric w/ space complexity )(n^2) + quadratic time complexity
  * Total replay is better than progNN, but neither are good
  * odin reduces space complexity to O(N), linear time complexity
  *  odif is the only non-parametric lifelong learning algorithm
     * capacity, space, and time complexity all O(N)
## Illustrating omnidirectional learning
### Simple environment
  * odif and rf perform well on XOR data, odif continues improving with XNOR data while rf takes a minute
### Adversarial
  * when XOR is rotated, odif fails gracefully, not catastrophically
  * amount of transfer is dependent on
    * difficulty of learning good representations
    * relationship btwn two tasks
    * sample size of each
## Real data experiments
  * CIFAR 100 challenge
    * 50,000 training
    * 10,000 testing
    * each a 32x32 RGB image of an object
    * 100 possible classes
  * CIFAR 10x10 
    * divides into 10 tasks, 10 classes each
  * below experiments use 500 training samples
### Resource constrained
  * odif w/ 20 trees, 10 trained on task 1, 10 trained on task 2
  * rf with 20 trees trained on task 2
  * fte and bte for odif remain positive, meaning it is transferring knowledge between tasks succesfully
  * with 5,000 samples per task, replay methods demonstrate both forward and backward transfer
  * single task learners like rf required way more resources, 550 trees vs 100 trees
### Resource recruiting
  * systems develop from building to recruiting resources
  * first 9 CIFAR tasks w/ 50 trees per task, 500 samples per task
  * 10th task
    * select 50 trees that perform best on task 10
    * train 50 new trees
    * build 25 trees and recruit 25 trees
    * or ignore all previous trees
  * odif outperforms reference algorithms, except when 5,000 samples is available
# Discussion
  * odif and odin demonstrate possibility of both forward and backward transfer due to representers w/o undue burdens
  * if we store all the data and train models w/ increasing capacity we could maintain performance, but it would quickly become quadratic
     * possible extension is store all data using generative model
     * ensembling representations rather than learners could be applied to many more problems
  * representation ensembling approach closely mirrors brain learning, but needs the pruning brains do to be computationally perfect
     * future work -> pruning adverarial representers to enhance transferability among tasks    
 
        
