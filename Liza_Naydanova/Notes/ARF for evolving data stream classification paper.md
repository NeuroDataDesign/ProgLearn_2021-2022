# Adaptive random forests for evolving data stream classification
https://link.springer.com/article/10.1007/s10994-017-5642-8

## Introduction
- Adaptive Random Forests (ARF) algorithm
  - A new streaming classifier for evolving data streams
  - Novelty
    - combines batch algorithm traits with dynamic update methods to deal with evolving data streams

- Main contributions
  - Adaptive random forests (ARF)
    - ARF is able to obtain high classification in data streams with different characteristics without further hyperparameter tuning
  - Drift adaptation
    - propose a drift adaptation strategy that does not simply reset base models whenever a drift is detected
    -  start training a background tree after a warning has been detected and only replace the primary model if the drift occurs
  - Parallel implementation
  - Comprehensive experimental setting
  - Open source
    - All data sets and algorithms used in this paper are going to be available as an extension to the MOA software

## Problem Statement
- A data stream learner must be prepared to process a possibly infinite amount of instances, such 
that storage for further processing is possible as long as the algorithm can keep processing instances 
at least as fast as they arrive
  - Algorithm must incorporate mechanisms to adapt its model to concept drifts, while selectively 
  maintaining previously acquired knowledge
  
  ![image](https://user-images.githubusercontent.com/55554531/136395461-68215140-a82c-4df4-9726-d799bfbf2c0a.png)

## Related Work
- (ARF) algorithm resembles dynamic streaming random forests as both use Hoeffding trees as base learners and include a drift detection operator
- Differences
  - ARF simulates sampling with reposition via online bagging instead of growing each tree sequentially
  - ARF is based on warning and drift detection scheme instead of reseting trees every new batch
  - ARF hyper-parameters are limited to subset of features, number of trees, and thresholds that control drift detection
  vs difficult hyper-parameters like the number of instances tree must be trained on or min accuracy that should be achieved

## Adaptive Random Forests
- Algorithm 1

![image](https://user-images.githubusercontent.com/55554531/136396335-0a697728-69c4-4594-b756-34d135ce6794.png)

- Algorithm 2

![image](https://user-images.githubusercontent.com/55554531/136396546-93d56446-ce4e-4764-9a46-5fe1f8d1d748.png)

### ARF variations

### Resources comparison between ARF[S] and ARF[M]

### ARF compared to other ensembles

## Conclusion
