---
alias: "Random input selection can improve random forest better than Adaboost or bagging."
---
# Random input selection can improve random forest better than Adaboost or bagging.
## Metadata
- ID: 202109152034
- Date Created: [[2021-09-15]]
- Status: #status/in_progress
- Note Type: #note/permenant_note
- Topic: [[Random Forest]]
- Tags: 
---

[[Leo Breiman]] conducted an experiment generating forests based on several data sets comparing random input selection, Adaboost, and bagging. The ratio of computing time of random input to of unpruned tree construction using all variables was $\frac{F \log_2 N}{M}$ where $F$ is the number of variables used in random input selection, $N$ is the number of instances, and $M$ is the number of input variables. Data sets with many more variables may produce increasingly significant differences in compute time.

---
## Source
[[Breiman - Random Forest|Random Forest]]