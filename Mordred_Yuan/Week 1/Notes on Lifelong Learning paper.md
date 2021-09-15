Paper: https://arxiv.org/abs/2004.12908
## Omnidirectional Transfer for Quasilinear Lifelong Learning

### Introduction 
classical machine learning - tabula rasa to be optimized for a single task

If trained:
* simultaneously - relatively easy
* sequentially - difficult (catastrophic forgetting)

Key obstables in AI - inability to omnidirectionally transfer

Omnidirectional learning algorithms h(⋅) = w ∘ v ∘ u(⋅) (The representer u / The voter v / decider w)
* Progressive Neural Networks (ProgNN) 
  * cannot transfer backwards
  * quadratic space and time complexity
* representation ensembling

In this paper:
1. Omnidirectional Forests, ODIF
2. Omnidirectional Networks, ODIN

Lifelong Learning - use the new learning to better the previous learning while learning and vice versa

### Evaluation Criteria
1. Transfer Efficiency
2. Forward Transfer Efficiency
3. Backward Transfer Efficiency

### Omnidirectional Forests, ODIF
* Based on decision forest
* Transformer ut - decision forest - mapping from X to a B sparse vector
* Decider wt - calculates the average for posterior estimates and creates a prediction

### mnidirectional Networks, ODIN
* Based on deep network
* Transformer ut - DN structure w/o final layer
* cross-entropy loss / the Adam optimizer / k-NN

### Results
* A computational taxonomy of lifelong learning
  * fixed resources and growing resources
  * ODIN and ODIF - reduced space complexity and time

* Omnidirectional Learning with ODIF
  * in a simple environment...
    * ODIF and random forest - same generalization error on XOR with XOR data
    * In comparison to RF, ODIF improves on XOR given XNOR data -- backward transfer
  * in adversarial environments...
    * adversarial - training data from task t can only add noise for task t' 
    * ODIF - positive forward transfer / RF - negative forward and backward tranfer
    * varying the rotation angle

* Real data experiments
  * ODIF and ODIN are being compared to ProgNN and DF-CNN - positive forward transfer / positive backwards transfer/ positive final transfer efficiency

