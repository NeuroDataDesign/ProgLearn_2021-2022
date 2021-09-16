---
alias: "Larger forests improves generalization behavior."
---
# Larger forests improves generalization behavior.
## Metadata
- ID: 202109151250
- Date Created: [[2021-09-15]]
- Status: #status/in_progress
- Note Type: #note/literature_note
- Topic: [[Random Forest]], [[Machine Learning]]
- Tags: 
---

When the size of the forest is small, individual trees produce overconfident predictions due to a single tree making binary confident decision between two classes depending on their feature distribution. This does not represent generalizable behavior because confidence should decrease the more a given input deviates from the training data. 

To improve generalizability, the forest size should increase. When the decision boundaries and their respective confidences are overlaid, confidence is greatest closest to the training data points and less confident further away from them, producing more generalizable behavior.
![[Pasted image 20210915125157.png]]
![[9781447149293 Decision Forests for Computer Vision and Medical Image Analysis#^bbe66d]]

---
## Source
[[9781447149293 Decision Forests for Computer Vision and Medical Image Analysis|Decision Forests for Computer Vision and Medical Image Analysis]]