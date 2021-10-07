# Streaming Random Forests
https://ieeexplore.ieee.org/document/4318108

## Introduction
### Difficulties
- Algorithms must be online and incremental, so that results can be produced at any time
- Algorithms must be fast enough to handle the rate at which new data arrives
- Algorithms should be adaptive to changes in the distribution of values in the underlying stream
- Results of stream mining must necessarily be an approximation

### Classic Classification
- Train on labelled data -> test on test data -> deploy

### Streaming
- Only 1 stream of data -> different approaches based on type of data stream

### Standard Random forest 
- multiple passes through data
  - A pass through the data is made to create the tradining data for each tree that will be built
  - For each tree, a pass is made through (some columns of the data) for each internal node of the tree, to generate the counts that are used to decide which attribute and split point to select for it

# Streaming Random Forest Algorithm
- Still builds a set of trees like random forest
- Arrival of new record
  - Routed down current tree to frontier node
  - Attribute values of the record contribute to class counts that are used to compute Gini indexes
  
## When and how to change a frontier node
  - Parameter nmin: how often to check if a frontier node should be changed
  - When a node acquires nmin labelled records
    - Gini index and the Hoeffding bound tests are applied.
    - If the Hoeffding bound test is satisfied, then the frontier node has seen enough records to determine the best attribute and split value.  
    - Gini index test is  used to select the best attribute and split point
    - Frontier node is transformed into an internal node with an inequality based on attribute and split point
    - Results in 2 new frontier nodes
  - When a node exceeds node window
  -   Algorithm checks to see if it should be converted into a leaf or internal node
- Tree construction completes when a total of tree window records used. Algorithm then builds new trees

## Pruning
  - If two sibling nodes have failed to receive enough records when the tree window is reached, the node purity is calculated for both
  - If both siblings’ node purity < 1/number of classes
    - Both nodes are pruned
    - Parent node is labelled as a leaf rather than an internal node
  - Else
    - Sibling nodes become leaf nodes labelled with the majority class among the records in their parent that would have flowed down to them
    
## Conclusion
- Streaming RF algorithm is an extension of standard RF
  - Comparable classification accuracy to standard RF despite seeing each data record once
- Stream algorithms can never see all of the data 
  - Use node windows and tree windows to decide where to construct new trees, transfer frontier nodes or carry out pruning
  - Means we require fewer labelled records for training than other stream based tree algorithms
