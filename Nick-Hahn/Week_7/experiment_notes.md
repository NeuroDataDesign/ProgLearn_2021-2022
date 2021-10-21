# Notes for streaming XOR,RXOR,XOR experiment

### Adversarial tasks 
- A task t is adversarial with respect to task t' if the true joint distribution of task t, without any domain adaptation, impedes performance on task t' ie. training data from task t can only add noise for task t'
- training data R-XOR (45 degrees) is an adversarial task for Gaussian XOR
- in experiment from paper sweeping across all angles 0-90, BTE peaks at 0 and 90 (>0) (same discriminate boundaries) lowest at 45 degrees (adversarial) (<0)
- XOR followed by R-XOR 
    - not backwards transfering but no catastrophic forgetting (*graceful* forgetting) (no backwards transfer=data from the current task has *not* been used to improve performance on past tasks ie data from RXOR is not imporving performance of XOR at 45 degree)
    - positive forward transfer to R-XOR (past task data,XOR, used to improve performance on current task, RXOR)

- new experiment will introduce XOR after RXOR
- want to verify streaming does not hinder performance <- most important as adding streaming capabilites should only be done if it makes proglearn more flexible 
- expect to see FT from XOR_1 to R-XOR as shown in LL paper 
- graceful, not catastrophic, forgetting from RXOR to XOR_1 
- by introducing XOR_2 we can test if there is transfer from XOR_2 to RXOR 

    ### Questions/clarifications
    - BTE is expected ratio of risk of learned hypothesis with access to data up to and including task t and access to the entire dataset 
        - in this experiment measuring BT includes data from XOR_1. will a different definition of transfer be required (only including RXOR data)? need to clarify this
        - some gaps in understanding here 


