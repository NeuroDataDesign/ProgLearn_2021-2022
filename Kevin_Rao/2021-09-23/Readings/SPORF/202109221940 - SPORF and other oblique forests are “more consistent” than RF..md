---
alias: "SPORF and other oblique forests are “more consistent” than RF."
---
# SPORF and other oblique forests are “more consistent” than RF.
## Metadata
- ID: 202109221940
- Date Created: [[2021-09-22]]
- Status: #status/in_progress
- Note Type: #note/permenant_note
- Topic: [[Random Forest]], [[Machine Learning]]
- Tags: 
---

A problem proposed by Biau et al. demonstrated that random forest is inconsistent. In this problem, a countably infinite number of splits in the data instead of a more practical finite split identified. On the other hand, SPORF and other oblique forests perform the task well due to their greedy approach of selecting splits. This makes SPORF more consistent than random forest. This finding suggests that the removal of the constraint that random forest forms decision boundaries aligned to the axis enables improved consistency for more classification problems.
![[Pasted image 20210922194534.png]]

---
## Source
[[Sparse Projection Oblique Randomer Forest]]