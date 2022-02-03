# [Task-Free Continual Learning](https://openaccess.thecvf.com/content_CVPR_2019/papers/Aljundi_Task-Free_Continual_Learning_CVPR_2019_paper.pdf)

Aljundi etal.

- current methods for preserving knowledge from previous tasks is too heavily based on knowing task boundaries
- in online setting, data needs to be processed in a streaming fashion and data distributions might shift gradually
- this work aims at overcoming req of hard task boundary

## Methods
Identified **Memory Aware Synapses** (MAS) as most promising method for the following reasons: 
1. *static storage requirment* only stores an importance weight for each parameter in the network avoiding an increase of memory consumption over time 
2. *task agnostic* can be applied to any task and not limited to classification
3. *fast* only needs one backward pass to update the importance weights
4. *top performance* superior to other importance weight regularizers

### SETUP:
- assume infinite stream of data a supervisory/self-supervisory signal that is generated based on few consecutive samples
- each time step *s*, system recieves few consec samples along with their generated labels drawn non i.i.d from a current distribution D_t
- D_t could experience sudden of gradual changes from D_t to D_t+1 at any moment
- goal to update function that minimizes prediciton error on previous and future samples
- ![image](https://user-images.githubusercontent.com/89429238/151905209-7797407c-82ea-46ac-997d-61f5eb68c609.png)

- due to strong non-iid conditions and very low number of samples used for the gradient step, system is vulnerable to catastrophic interference between recent samples and prev samples and face difficutly in accumulating the knowledge over time 

### MAS
- after each traing phase/task, method estimates importance of parameter to the prev learned task, doe sthis by computing sensitivity of learned function to parameter changes
- when learning new task, changes to important params are penalized 


When to update importance weights
- in task aware setting, importance weights are updated after each task, when learning has converged
- in online/streaming setting, we look at the surface of the loss function
- plateaus in loss function indicate stable learning regimes, when model is such a stable area, it's a good time to consolidate the knowledge by updating the importance weights
- this allows us to ID params that are important for the currently acquired knowledge

Detecting plateaus in the loss surface:
- use sliding window over consecutive losses during training 
- trigger importance weight update when mean and variance of losses in the window are lower than a given threshold
- dont keep re-estimating importance weights; only re-check for plateaus in loss surface after observing a peak
- peak when window loss mean becomes high than 85% of a normal distribution estimated on the loss window of the previous plateau

Small buffer with hard samples:
- use a small buffer of hard samples thats updated at each learning step by keeping the samples with highest loss among the new samples and the current buffer = stabilizes online learning
- important since previous samples cant be revisted hence gives the system the advantage to re-process those hard samples and adjust its params towards better predictions in addtion to getting a better estimate of the gradient step by avg'ing over recent and hard samples
- hard buffer better est of acquired knowledge than a few recent samples, hence allows for a better ID of importance weights

Accumulating importance weights:
- maintain a cumulative moving avg of the estimated importance weights
- could use a decaying factor that allows replacing old knowledge in long term but authors found that cumulative working avg showed more stable results

<img width="663" alt="Screen Shot 2022-02-01 at 5 54 28 PM" src="https://user-images.githubusercontent.com/89429238/152065133-d1a9995b-0e72-44bd-a4e1-b46fe9e1e054.png">

### Experiments
1. learn actor identites from watching soap series
2. robot navigation

Soap series 
- weak supervision case, assume there is an annotator telling the agen whether two consecutive tracks are of the same identity or not
- self supervised case, use fact that if two faces are detected in the same image then their tracks must belong to two different actors

**SETUP:** start from AlexNet architecture with convolutional layers pre-trained on ImageNet nad fully connected layer inited randomly
- use triple margin loss which has been shown to work well in face recog apps

Dataset: ep's from big bang theory, breaking bad, and mad men

Hard buffer size of 100 tripletes and fixed loss window of 5

**BASELINES:**
1. *Initial*: the pretrained model, before training on any ep's
2. *Ounline Baseline*: model trained in the explained online setting but without the MAS importance weight regularizer
3. *Online Joint Training*: model trained online, without MAS regularization, but with shuffled tracks across ep's to obtain i.i.d drawn data
4. *Offline Joint Training*: model that differs from online joint training by going multiple epochs over the whole data. upper bound

### Weak supervision results
![image](https://user-images.githubusercontent.com/89429238/152277173-2519a9c5-8301-422a-b77f-e51cd928ffe2.png)

### Self-supervised results
![image](https://user-images.githubusercontent.com/89429238/152278399-29dbf6d5-f841-4155-884d-b3b3ed13f237.png)

