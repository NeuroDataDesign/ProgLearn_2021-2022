# Mining High-Speed Data Streams
https://dl.acm.org/doi/pdf/10.1145/347090.347107

# Introduction

- Knowledge discovery systems are constrained by 
	- Time
	- Memory
		- Present day applications has this as the bottleneck
	- Sample size
		- Traditional applications of machine learning has this as limitation bc massive search leads to overfitting or "data dredging"
- Most efficient algorithms concentrate on making it possible to mine databases too big for memory by requiring sequential scans of the disk
- We want to have KDD systems that operate continuously and indefinitely
- **Proposal**: Hoeffding trees
	- Can be learned in constant time but are nearly identical to trees produced by conventional batch learner
	- VFDT: decision tree learning system based on Hoeffding trees
		- Only requires space proportional to size of the tree

# Hoeffding Trees

- Goal is to design learner for extremely large datasets
	- Should require each example to be read at most once 
	- Constant time to process

- Given stream of examples, first ones will be used to choose root test
	- Once root attribute is chosen, succeeding examples passed to corresponding leaves
	- Continue recursively

- Choosing number of examples
	- Hoeffding bound
		- Benefit: independent of probability distribution generating observations

# VFDT System

- "Very Fast Decision Tree Learner"
	- Allows use of either info gain or the Gini index as the attribute evaluation measure

## Ties

- When 2 or more attributes have similar G's, potentially many examples are required to decide between them with high confidence
	- Presumably wasteful
		- Makes little difference which attribute is chosen
	- VFDT optionally decides that there is a tie and splits on current best attribute

## G computation

- Computing G: Most significant part of time cost
	- VFDT fixes but allowing user to specify min number of new examples before G is recomputed

## Memory

- Sole obstacle is finite RAM available
	- If max memory is reached, VFDT deactivates least promising leaves 
	- A leaf can be reactivated if it becomes more promising

## Poor attributes
- Memory usage is minimized by dropping early on attributes that don't look promising

## Initialization
- VFDT can be initialized with the tree produced by conventional RAM-based learner on small subset of data
	- Can either be as is, or over-pruned
		- Can give VFDT a head start

## Rescans
- VFDT can rescan previously seen examples
- Can be activated if 
	- Data arrives slowly so there is time for it
	- Dataset is small enough to make rescans feasible


# Conclusion

- Hoeffding trees
	- Small constant time per example
	- Strong guarantees of asymptotic similarity to corresponding batch trees
- VFDT
	- Effective in taking advantage of massive numbers of examples
