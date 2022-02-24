![Screen Shot 2022-02-24 at 12 05 37 PM](https://user-images.githubusercontent.com/85964755/155581810-c040b8cd-e68d-44f9-aeb6-667eb0417ec6.png)

`update_task` pseudocode
```
1 forest.update_task:
2	progressive_learner.update_task:
3		verify task_id exists
4		create empty dictionary for voters for task_id
5		concatenate new X and y data to data for task_id
6		split data in two indices for transformer/voter and decider data with _bifurcate_decider_idxs according to transformer_voter_decider_split
7		_append_decider_idx(task_id, decider_idx) to set task_id_to_decider_idx[task_id]=decider_idx
8		call progressive_learner._update_transformer:
9			get backwards task ids
10			for all transformers for task:
11				partial fit with bootstrapped data
12				update voter data index (OOB data)
13			for all backwards task ids:
14				progressive_learner.set_voter:
15					for each transformer
16						progressive_learner._append_voter:
17							appends voter fit with transformed X data (voter_data_idx) and class labels
18				progressive_learner.set_decider: 
19					decider.fit
20						updates transformers and voters
```
