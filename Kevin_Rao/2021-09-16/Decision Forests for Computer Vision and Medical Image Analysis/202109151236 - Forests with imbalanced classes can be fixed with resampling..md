---
alias: "Forests with imbalanced classes can be fixed with resampling."
---
# Forests with imbalanced classes can be fixed with resampling.
## Metadata
- ID: 202109151236
- Date Created: [[2021-09-15]]
- Status: #status/in_progress
- Note Type: #note/permenant_note
- Topic: 
- Tags: 
---

If the training set has an unbalanced number of label classes, it can create bias in the classifier due to the higher frequency of one label class over the other, negatively affecting the training of the forest. Resampling the training data so that the distribution of classes is uniform can mitigate this problem. Alternatively, one could weigh more common classes less when computing the information gain of a split node.
![[9781447149293 Decision Forests for Computer Vision and Medical Image Analysis#^18ac99|Decision Forests for Computer Vision and Medical Image Analysis]]

---
## Related