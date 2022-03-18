# [GPU-based State Adaptive Random Forest for Evolving Data Streams](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9207333)
Wu etal

## Abstract
- intro rf model utilizing a both gpu and cpu called gpu-based state-adaptive random forest (GSARF)
- address pre-existing challenges of adapting rf for data streams, specifically in the area of continual learning
- reuses previously seen trees in the random forest when previous concepts reappear = retain prior knowledge and provide a more stable predictive accuracy when changes occur in the data stream

Use 3 types of trees:
1. foreground trees: trees that are currently used in prediction
2. background trees: trees that are built when we are aware of possible changes in the data streams
3. candidate: trees that had been highly used in the previous concepts, but are now discarded due to changes in data stream (stored in repo and can be accessed when needed)

Concept drift adaptation: maintain a pool of trees and use a single or ensemble of them when we detect a change in the data stream

when drift detected, compare candidates and backgrounds and pick the one that works best for the data

Forest layout on GPU:
![image](https://user-images.githubusercontent.com/89429238/158738097-efc42ad6-39e0-46d2-8344-25119fabd248.png)

## GSARF
- The main novelty of our GPU-based State Adaptive Random Forest (GSARF) is the additional **pool trees** to allow for faster updating of the random forest when concept drift occurs
- prev research randomly train new trees in background when drift waring is detected and replacing drifted trees in the foreground when a drift is detected in the forest
- GSARF has additional candidate trees to cope with evolving data streams
- candidate trees stored on cpu instead of gpu
- **State matching process:** when drift warnings are detected, algo tries to find the closest match from candidate or background trees 
- **Tree replacement process:** when actual drifts are detected, drifted trees are either replaced by their corresponding background trees, or the best candidate trees in the forest dep on acc
- above seen in fig 2
![image](https://user-images.githubusercontent.com/89429238/158739585-f6902d00-5024-4372-aaf5-649f33b30c35.png)
- maintain pool of trees built on gpu in cpu, show by cpu tree pool in fig 3
- keep state patterns in linked list called Least Recently Used (LRU) state list, also seen if fig 3

![image](https://user-images.githubusercontent.com/89429238/158739927-b784c195-6267-481b-97d2-5077f72fbce1.png)

## State matching process
