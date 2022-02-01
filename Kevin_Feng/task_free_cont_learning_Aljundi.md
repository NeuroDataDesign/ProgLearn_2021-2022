# [Task-Continual Learning](https://openaccess.thecvf.com/content_CVPR_2019/papers/Aljundi_Task-Free_Continual_Learning_CVPR_2019_paper.pdf)

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
