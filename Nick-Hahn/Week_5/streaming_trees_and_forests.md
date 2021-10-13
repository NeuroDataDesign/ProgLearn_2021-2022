# Notes on Streaming Decision Trees & Forests 
[Machine Learning for Data Streams by Albert Bifet Chapters 2 & 6](https://direct.mit.edu/books/book/4475/Machine-Learning-for-Data-Streamswith-Practical)
## Data Streams
- Data streams are sequences of items, possibly infinite, each item having a timestamp, and so a temporal order 
- There are two main algorithmic challenges when dealing with streaming data 
    1. the stream is large and fast and we need to extract information in real time 
    2. the data may be evolving, so our models have to adapt when there are changes in the data 
- Time & Memory 
    - accuracy, time, and memory are the three main resource dimensions of the stream mining process. We are interested in methods that obtain the maximum accuraccy with minimum time and low total memory 
    - since data arrives at high speed, it cannot be buffered, so time to process one item is as relevant as the total time
- Algorithms: 
    - the main algorithms in data stream mining are classification, regression, clustering, and frequent patttern mining 
    - most significant requirements for streaming algorithm
        1. process an instance at a time, and inspect it (at most) once 
        2. use a limited amount of time to process each instance 
        3. use a limited amount of memory 
        4. be ready to give an answer (predicition) at any time 
        5. adapt to temporal changes 


## Classification
- In batch classification there is first a training phase, clearly separated in time from the prediction phase.
- In the online setting, and in particular in streaming, this separation between training, evaluating, and testing is far less clear-cut, and is interleaved. 
- In streaming, the data may be infinite, we need to use the data whose label we predict to keep training the model if possible, and we probably need to continuously evaluate the model in some wat to decide if it needs more or less aggressive retraining 
- a large part of the research in stream classification deals with a simplified cycle of training/prediction: we assume that we get the true label of every unlabeled instance, and that furthermore we get it immediately after making the prediction and before the next instance arrives
    - Get an unlabeled instance x 
    - make a prediction y^ =f(x) for x's label, where f is the current model 
    - get the true label y for x 
    use the pair (x,y) to train f, and the pair (y^,y) to update statistics about classifier performance \
    - proceed to next instance 
- this simplified model however ignores delayed/missing label feedback

### Classifier Evaluation in Data Streams 
- in traditional batch learning, evaluation is typically performed by randomly splitting the data into training and testing sets (holdout) and if data is limited cross-validation 
- in streaming, infinite data tends to make cross-validation too expensive computationally (and less necessary)
-  In a streaming environment no part of the IID assumption remains valid.
- An evaluation framework should be composed of the following parts: 
    - error estimation 
    - evaluation performance measures 
    - statistical significance validation
    - cost measure of the process 

- Error Estimation
    - holdout - measuring performance on a single holdout partition. It is most useful when the division between train and test sets has been predefined, so that results from different studies can be directly compared
    - Interleaved test-then-train or prequential - Each individual example is used to test the model before it is used for training, and from this the accuracy can be incrementally updated.  This scheme has the advantage that no holdout set is needed for testing, making maximum use of the available data. It also ensures a smooth plot of accuracy over time, as each individual example will become less and less significant to the overall average. In test-then-train evaluation, all examples seen so far are taken into account to compute accuracy, while in prequential, only those in a sliding window of the most recent ones are.
- Distributed Evaluation
    - In a distributed data stream setting, we have classifiers that can be trained at the same time.
    - k-fold distributed split-validation: when there is abundance of data and k classifiers. Each time a new instance arrives, it is decided with probability 1/k whether it will be used for testing. If it is used for testing, it is used by all the classifiers. If not, then it is used for training and assigned to only one classifier. Thus, each classifier sees different instances, and they are tested using the same data.
    - k-fold distributed cross-validation: when data is scarce and we have k classifiers. Each time a new instance arrives, it is used for testing in one classifier selected at random, and for training in the others. This evaluation is equivalent to k-fold distributed cross-validation.
- Performance Evaluation Measures 
    - Cohen's Kappa 
        - $\kappa = \frac{p_0-p_c}{1-p_c}$ where $p_0$ is the classifiers prequential accuracy, and $p_c$ is the probability that a chance classifier makes a correct prediciton 
        - if the classifier is always correct, the k=1, if the predicitions coincide with the correct ones as often as those of a chance classifier then k=0
    - Kappa temporal statisitc
        -  $\kappa_{per} = \frac{p_0-p_e'}{1-p_e'}$ where $p_e'$ is the accuracy of the No-change classifier (the classifier that echose the last label received)
        - k_per takes values 0 to 1 with 1 indicating perfectly correct and achieving the same accuracy as the no change classifier k_per =0
- Statistical Significance 
    - Hoeffding's bounds 
    - explanation: https://www.youtube.com/watch?v=iJbuyAggtao (helps to watch previous lecture first)
- Cost Measure of Process
    - estimating the combined cost of performing the learning and prediction processes in terms of time and memory.
    - RAM-hours


## Decision Trees 
### Hoeffding Trees
- In stream mining the state of the art decision tree classifier is the Hoeffding tree 
    - [Mining High-Speed Data Streams](https://dl.acm.org/doi/10.1145/347090.347107)
    - The Hoeffding tree is based on the idea that instead of looking at previous stored instances to decide what splits to do in trees, we can wait to recieve enough instances and make split decisions when they can be made confidently 
    - builds a tree that provably converges to the tree built by a batch learner with sufficiently large data 
  ![Screen Shot 2021-10-07 at 11 12 56 AM](https://user-images.githubusercontent.com/85964755/136423408-15327ff2-25e6-46e1-90b4-90c515c4f9ed.png)
### Very Fast Decision Trees 

![Screen Shot 2021-10-07 at 11 16 56 AM](https://user-images.githubusercontent.com/85964755/136423985-655e87c4-1155-46eb-8a6c-653c177173c2.png)

### Concept-adapting Very Fast Decision Trees 
- an extension of VFDT to deal with concept drift
![Screen Shot 2021-10-07 at 11 18 58 AM](https://user-images.githubusercontent.com/85964755/136424289-bca93752-594a-4fb8-ada8-9a5584944d4c.png)



### Hoeffding Adaptive Trees
 - [Adaptive hoeffding trees](https://www.cs.upc.edu/~gavalda/papers/ida2009slides.pdf)
 - an extension of the Hoeffding tree that is able to create and replace new branches when the data stream is evolving and the class label distribution or instance distribution is changing 

# Notes continued (Week 6)

[Machine Learning for Data Streams by Albert Bifet Chapter 7](https://direct.mit.edu/books/book/4475/Machine-Learning-for-Data-Streamswith-Practical)
 ## Ensembles 
 - In both batch and streaming, ensembles tend to improve prediction accuracy and are often easy to parallelize
 - In streaming, they are easy to scale and can be made to adapt to change by pruning underperforming parts of the ensemble and adding new classifiers 
 - Ensemble methods include weighting/voting existing classifiers (weighted majority and stacking), creating ensebles by transforming the input distribution before giving it to a base algorithm (bagging and boosting), and methods that use Hoeffding Trees as the base classifiers.
 
 
 
 
 ### ADWIN bagging 
 - [New ensemble methods for evolving data streams](https://researchcommons.waikato.ac.nz/handle/10289/3982)
 - an extension of bagging that is able to create and replace ne classifiers when the data stream is evolving and the class label distribution is changing 






