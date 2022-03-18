# [Adaptive random forests for evolving data stream classification](https://link.springer.com/content/pdf/10.1007/s10994-017-5642-8.pdf)
Gomes 2017 etal.

## Abstract
- Rf most used ML algo in non-streaming (batch) setting
- Present adaptive random forest (ARF) for classification of evolving data streams
- ARF includes effective resampling method and adaptive operators that can dope with different types of concept drifts without complex optimizations for different datasets


## Intro
- Infeasible to store data prior to learning
- learning algo should process instances at least as fast as new ones are made avail
- Bagging boosting and RD are classic ensemble methods that achieve superior learning perf by agging mult weak learners
- Bagging uses sampling with reposition (i.e. resampling) to train classifiers on different subsets of instances, which effectively increases the variance
of each classifier without increasing the overall bias. 
- Boosting iteratively trains classifiers by increasing the weight of instances that were previously misclassified. 
- Random forests grow decision trees by training them on resampled versions of the original data (similarly to bagging) and by randomly selecting a small number of features that can be inspected at each node for split.
- ARF combines batch aglo traits with dynamic update methods to deal with evolving data streams
- ARF uses a theoretically sound resampling method based on online baggin and an updated adaptive strat to cope with evolving data streams
- based on using a drift monitor per tree to track warnings and drifts, and to train new trees in the background when a warning is detected and before replacing then when a drift is detected

![image](https://user-images.githubusercontent.com/89429238/158668791-b89d79da-dc4b-4b65-92cc-09a7c4d9e561.png)

## Problem statement 
- thie paper foxuses on both immediate and delayed settings 
![image](https://user-images.githubusercontent.com/89429238/158669975-deb913fb-de0d-4cab-a2d6-043e4ced5d4e.png)


## ARF
- use poisson \lambda = 6 as in leveraging bagging, instead of possion \lambda = 1, leverages resampling and has pratical effect of increasing hte prob of assigning higher weights to instances while training base model
- Function for inducing each base tree: 

![image](https://user-images.githubusercontent.com/89429238/158677466-27f01cc2-381a-4f2a-9670-3e405278b0b2.png)

- RFTreeTrain based on Hoeffding tree algo (very fast decision tree), but doesnt include any early tree pruning
- wehenever new node created (line 9) a random subset of features with size m is selcted and split attempts (line 7) are limited to these features for a given node
- small vaues of GP(line 6) causes recalcs of split heauristic more freq and tends to yield deeper trees

ARF pseudocode:
![image](https://user-images.githubusercontent.com/89429238/158677850-24f456e6-b218-49fb-976c-b43207b6abf8.png)

- to cope with evolving data streams, drift detection algo is usually coupled with ensemble algo
- ARF is not bounded to a specific detector
- to show diff detection methods would perform in implementation, present exp's with ADWIN and PAGE Hinkly Test (PHT) 

## Datasets used for experiments 
![image](https://user-images.githubusercontent.com/89429238/158679576-25eeb26d-80c2-4d0a-b87d-3c0ddf124797.png)


## Accuracy in the immediate setting 
![image](https://user-images.githubusercontent.com/89429238/158679784-e79249fa-6d21-4950-8e4d-fbfd99e8a50e.png)

Next few pages go over different forms of ARF, how they are more/less efficient than other ensemble methods.

![image](https://user-images.githubusercontent.com/89429238/158731813-58641bdb-e44a-4c43-b038-a9d9b48e5a7c.png)

## Conclusion
- ARF enables random forests algo for evolving data stream learning
- provide a serial and a parallel implementation (ARF[S], ARF[M])
- show that the parallel version can process the same amount of instances in reasonable time without any decrease in the classification performance
- can implement warning detection and background trees in other ensemble methods
- ARF obtains good results in terms of classification performance (accuracy, kappa m, and kappa temporal), reasonable performance resources usage
- ARF good classification perf on both delayed and immediate settings, esp on real word data sets
- ARF can be used to process data streams w/ a large number of features, using rel small number of tress (100)
- can train its base trees in parallel without affecting its classification perf
- might not be able to imporove on data sets where all features are necessary to build a reasonable model
