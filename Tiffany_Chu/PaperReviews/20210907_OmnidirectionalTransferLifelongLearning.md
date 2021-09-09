Vogelstein, J., et al. Omnidirectional Transfer for Quasilinear Lifelong Learning. https://arxiv.org/abs/2004.12908 

## Background: Amnesiac Computers

A major problem with normal machine learning: “catastrophic forgetting” - a machine trained on a new dataset forgets how to handle previous data/tasks

Also, machines struggle to transfer data forwards/backwards - i.e. to generalize across knowledge. This is something humans do all the time.

## Evaluation Criteria: Forwards and Backwards
Given a set of N tasks *t* and their associated training data, for a given task *t<sub>n</sub>*, 1 <= *n* <= *N*, we are interested in the following metrics:
- Forward  transfer efficiency (FTE): the difference in performance between an algorithm trained only on data for task *t<sub>n</sub>* and an algorithm trained on all data for tasks *{t<sub>1</sub>...t<sub>n</sub>}*. If FTE>1, the machine is learning from past tasks. 
- Backward transfer efficiency (BTE): the difference in performance the difference in performance between an algorithm trained on all data for tasks *{t<sub>1</sub>...t<sub>n</sub>}* and an algorithm trained on all data for tasks *{t<sub>1</sub>...t<sub>N</sub>}*, i.e. all data in the dataset. If BTE>1, the machine uses new data to improve performance on prepvious tasks. Normally, BTE << 1, hence catastrophic forgetting occurs, similar to a machine going on summer break.

## Omnidirectional Forests (ODIF)

A random forest containing *B* trees with *L* leaves can be represented as a series of *one-hot vectors* with length *L* - 1 bit will be 1 and the rest 0. 

Ex: Given a forest with *B* = 4 and *L* = 8, the output can be represented as a sparse matrix: 

- 0000 1000
- 0000 1000
- 0000 0100
- 0100 0000

And polling these four trees would suggest the answer is Leaf 4 (0000 1000)

Omnidirectional forest algorithm creates a new representer forest *u<sub>t</sub>* for each task. The omnivoters will then all poll ALL forests for the correct answer, coming up with posterior probabilities for the potential outputs *y* for input *x* given task *t*, i.e. *h(x|t)*. Decider averages these posteriors to decide on predicted label *y*.

## Omnidirectional Networks (ODIN)

Neural networks are made of layers of neurons. For each task, a subset of neurons from all layers except final are used to create the neural network representer *u<sub>t</sub>*. *u<sub>t</sub>* can be said to represent the neurons that are activated in the penultimate layer (right before decision).

The final layer is a k-Nearest-Neighbors (kNN check) - paper does not explicitly state what neighbors kNN uses as reference. Best guess: given *n* neurons in *u<sub>t</sub>*, represent training answers as *n*-dimensional space. Take Euclidian distance from new datapoint *x* to other datapoints *x*. Then given k=16*log*<sub>2</sub>*n*, poll the k nearest neighbors for final identity.

## Notes

Both ODIN and ODIF algorithms described in this paper assume preexisting knowledge of the correct task - this is different from humans, who must figure out what task to enact when faced with a problem. (ex: how do you wash a spoon? In a washing machine or a dishwasher? Hopefully you do not have to be told this.)

