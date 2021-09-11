# Omnidirectional Transfer for Quasilinear Lifelong Learning

Vogelstein, J., et al. Omnidirectional Transfer for Quasilinear Lifelong Learning. 

https://arxiv.org/abs/2004.12908

## Notes

**Abstract**
- Classical machine learning starts from a bank slate and learns using data intended for just one task at a time
- Catastrophic forgetting - performance decreases on previous tasks as learn new task
    - Continual/lifelong learning aims to maintain performance on previoust tasks and counteract this
    - However: goal should be to improve learning on all tasks, not just "maintain" learning
- Algorithm of omnidirectional transfer, where have an omni-voter layer which combines representations of already learned tasks to together help decide how to approach a new task - this improves performance on both new and old tasks 

**Introduction**
- Biological learning results in increased performance of previous tasks as new tasks are learned - an example is that learning a new language improves an individual's performance using their native tongue
- Simultaneous optimization for tasks is possible (multi-task learning) but sequential optimization is more difficult due to catastrophic forgetting
- Two main approaches - (1) fixed resources to incorporate knowledge, or (2) ability to add new resources with new data
    - Are able to show some continual learning, but cannot trasnfer knowledge forward and backward - omnidirectional transfer
    - Progresive Neural Networks able to transfer forward but not backwards
    - Proposal - omnidirectional transfer based on (1) decision forests and (2) deep networks

**Background**
- Classical machine learning - goal is to minimize expected loss (risk)
- Lifelong learning - not just one task but many, data comes in sequentially not in a batch, there are computational constraints on how complex the learning algorithm and hypotheses can be (we cannot just store all data)
    - Use existing data to get low generalization error on new task but also to use new data to lower generalization error on old tasks
- Two models: update a model with fixed paramters with new tasks, or add resources with new tasks
- Transfer efficiency - ratio of generalization error of algorithm that has learned using only dataset from designated task, to generalization error of same algorithm that has access to more data
- Forward transfer efficiency - ratio of risk of algorithm when only has access to data for intended task, to risk of algorithm when has access to data up to and including for intended task
    - measures the effect of previous data unrelated to the task, on performance of this task (negative forward transfer)
- Backward transfer efficiency - ratio of risk of learned hypothesis with data up to and including data for new task, to when have all data accessible
- Omnidirectional algorithms - three parts
    - representer takes in input and maps to internal representation space, voter maps this transformed data into a posterior distribution (score) in response space, and then a decider takes this in to output prediction
        - if decider operates with many voters, then is an ensemble of voters
        - each voter can also ensemble the representers, and this leads to an ``omni-voter'' layer, and so all existing representations ensembled regardless of order learned
    - Omnidirectional forest (ODIF) - transformer/representor is a decision forest, representation of input from each tree concatenates into a vector, then the posteriors are learned by taking class votes, and then the average normalized class vote across all tree collections (adjusted for sample bias) is output (honest trees), the decider then averages the honest tree decisions (posterior estimates) to output one prediction
        - decision forests all converge to minimum risk (under correct conditions) 
    - Omnidrectional network (ODIN) - deep network, each representer maps input to neurons in layers of the network, omni-voters are then learned
    - Paper algorithms build new independent represnter for each new data, then create a voter that takes in information from all parameters already in existence (allows for forward transfer of old to new learning) and voters from old tasks can be updated if new data comes from an old task (allow backward transfer)
        - new data passes through all representers and voters, leading to a prediction
    - ODIN different from ProgNN since not create lateral connections between new columns (so save parameter space and time), uses all tasks (not exclude future tasks like ProgNN) so can have backward transfer, and ODIF uses random forest representers

**Results and Discussion**
- ODIF able to have positive forward and backward transfer, whereas RF unable to do either and catastrophically forgets
- Both ODIF and ODIN show can achieve both forward and backward transfer
- Structure of having representations and not learners can be applied to other models as well 
- Ensembling is similar to how the brain develops
