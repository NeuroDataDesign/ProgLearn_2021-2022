## [Adaptive random forests for evolving data stream classification](https://link.springer.com/article/10.1007/s10994-017-5642-8#change-history)

### Evolving Data Stream Learning Setting 
- infeasible to store data prior to learning because it is not useful or practical (old data may not represent the current concept and data may surpass available memory) 
- it is expected that the learning algo can process instances at least as fast as new ones are made available 
- ensemble methods are preferred because they can achieve high learning performance without much optimization
    - bagging: sampling with replacement to train classifiers on different subsets of data 
    - boosting: iteratively trains classifiers by increasing the weight of instances that were previously misclassified 
    - random forests: grow decision trees by training them on resampled versions of the original data and by randomly selecting a small number of features that can be inspected at each node for split
 - no random forests algorithms considered SOTA compared to bagging/boosting based algorithms 

### Adaptive Random Forests 
- Adaptive random forests (ARF): algorithm for evolving data stream classification able to obtain high classification in data streams with different characteristics without further hyperparameter tuning. (sustainable and off the shelf learner - good for benchmarking)
- the main novelty of ARF is in how it combines the batch algorithm traits with dynamic update methods to deal with evolving data streams. 
- ARF uses a theoretically sound resampling method based on online bagging and an updated adaptive strategy based on using a drift monitor per tree to track warnings and drifts, and to train new trees in the background (when a warning is detected) before replacing them (when a drift is detected)
- drift algos used in the paper include ADWIN and Page Hinkley Test

### Problem Statement
A data stream *S* presents, every *u* time units, new unlabeled instances *x^t* to the classifier for prediction, such that *x^t* represents a vector of features made available at time *t*. In many real world problems, the class label *y^t* corresponding to *x^t* is not available before the next instance *x^t+1* is presented to the learning algorithm. Three situations arise regarding availability of labels: 
  - Immediate: labels are presented to the learner before the next instance arrives 
  - Delayed: labels arrive with delay *d* which may be fixed or vary for different instances 
  - Never: labels are never available to the learner

<img width="670" alt="Screen Shot 2021-10-13 at 2 43 10 PM" src="https://user-images.githubusercontent.com/85964755/137202131-0cd0df47-f6c7-4971-b21a-c7c40e4e096c.png">
(ARF is only evaluated in immediate and delayed setting in this paper)

### ARF Algorithm
<img width="650" alt="Screen Shot 2021-10-13 at 2 48 23 PM" src="https://user-images.githubusercontent.com/85964755/137202812-cc13494b-7e9a-42b7-ba87-9919a62f4f6b.png"><img width="650" alt="Screen Shot 2021-10-13 at 2 49 06 PM" src="https://user-images.githubusercontent.com/85964755/137202919-aa1e00fd-a218-4787-bbc9-f1ba41505f65.png">

### ARF[M] vs ARF[S]
- In ARF, training a tree with an instance includes updates to the underlying drift detector, incrementing its estimate test-then-train accuracy, and, if a warning is signalled, starting a new background tree which can all be executed independently for each tree / sepearate threads
- ARF[M] is a parallel implementation and ARF[S] is a serial implementation 
- ARF[M] is around 3times faster than ARF[S] and there is no loss in classification performance/results exactly the same

### Experiments 
- experiments evaluated in terms of memory, time and classification performance
- ARF obtains good classification performance on both delayed and immediate settings, especially on real world data sets
- ARF can be used to process data streams with a large number of features, such as SPAM data set with almost fourty thousand features, using a relatively small number of trees (in our experiments 100)
- ARF can train its base trees in parallel without affecting its classification performance. This is an implementation concern, but it is useful to investigate and make it available along with the algorithm as scalability is often a concern
- ARF might not be able to improve on data sets where all features are necessary to build a reasonable model.
