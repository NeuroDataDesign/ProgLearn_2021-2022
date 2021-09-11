# Decision Forests for Computer Vision and Medical Image Analysis [Textbook](https://link.springer.com/book/10.1007/978-1-4471-4929-3) - Notes

## Ch 3 Intro: The Abstract Forest Model

### Some machine learing categories with examples:
- **Classification** task: recognizing type of a scene captured in a photo, desired output is a discrete, categorical label
- **Regression** problem: predicting price of a house as a function of its distance from a good school, output is a *continuous variable*
- **Density** function: dtecting abnormalities in a medical scan can be achieved by evaluating the image under a probability *density* function learned from scans of healthy indivs
- **Manifold learning**: correlation size + shape of some key brain structions in images with patient's age + health can be cast as this 
- **Semi-supervised** problem: interactive image segmentation, user's brush strokes define labeled data and the rest of image pixels provide *already available* unlabled data
- **Active learning** problem: learning gen rule for detecting tumors in images using min amount of manual annotations

- Decision forests popularity rise due to recent success in *classification* tasks
- Decision trees higher accuracy on prev unseen data, *generalization*, achieved by ensembles of slightly different trees

### General Tree Structure
![image](https://user-images.githubusercontent.com/89429238/132411238-6e585224-4d6c-44ce-ae24-8d75c4c52137.png)
- In a decision tree, each node is associated with one question (ie. is the top portion of the picture blue?)

### A decision tree
![image](https://user-images.githubusercontent.com/89429238/132412270-b234179c-0e9e-43d8-8504-a4abac4ef1db.png)
- The image is injected at the root node, and a test is applied to it 

### Key to good functioning of a decision tree is to establish:
1. Tests associated with each internal node
2. Decision-making predictors associated with each leaf

- Decision tree can be thought of as splitting complex problems into a set of simpler ones: **hierarchical piece-wise** model 

- **Split function, test function, weak learner** are used interchangeably in this book 

### Test function at a split node j as a function with binary output:
![image](https://user-images.githubusercontent.com/89429238/132415312-d3711a36-0146-4138-8194-fa4a4c25e601.png)

### Training points and sets
- **Training Point**: data point for which the attriibutes we are seeking for may be known and used to computer tree params
- **Training Set**: ie. set of photos associated with "indoor" or "outdoor" labels. Denoted S0, is a collection of different training data points
![image](https://user-images.githubusercontent.com/89429238/132419183-b1c0ac08-9cc4-4c79-bd2e-c5289896c109.png)

### Randomly trained decision trees: Tree Testing (On-line Phase)
- given previously unseen data point **v**, decision tree hierarchially applies a # of prev selected tests
- starting at root, each split node applies its associated test function h(.,.) to **v**
- data point **v** is sent to left or right child based on this binary test
- **leaf nodes** contain a predictor/estimator (eg. classifier or a regressor) which associates an output (eg. class label or continuous value) with input **v**

### Randomly traiend decision trees: Tree Training (Off-line Phase)
- split/test function at each internal node needs to learned automatically from example data
- training phase takes care of selecting type and params of test function h(v,theta) associated with each split node (indexed by j) by optimizing a chosen objective function defined on an avail training set
- maximize objective function I at the jth split node 
![image](https://user-images.githubusercontent.com/89429238/132419935-18cfd087-fe62-4bc3-9ca6-eaede15a6485.png)
- typically performed as simple search over discrete set of samples of possible param settings theta
![image](https://user-images.githubusercontent.com/89429238/132420024-c2c391b2-4289-4669-b575-aa1357c1a157.png)
- during training we need to choose tree structure (size and shape)
- training starts at j=0 (root node), optimum split params above, construct two child nodes (each with different disjoint subset of training set), procedure then applied recursively to all newly constructed nodes and training phase continues until stopping criterion met

#### At the end of the training phase we have:
1. greedily optimum weak learners (split functions) associated with each node
2. learned tree structure
3. different set of training points at each leaf

### Weak learner models
**Parameters of weak learner model:**
![image](https://user-images.githubusercontent.com/89429238/132929705-0b37192a-be7a-487e-8f45-62ce2001233a.png)

- **Filter (selector) function:** selecets some feautres of choice out of the entire vector **v**
- **\psi :** defines geometric primitive used to seperate the data (eg. axis-aligned hyperplane, oblique hyperplane, general surface)
- **\tau :** caputres thresholds for the inequalities used in the binary test

#### Linear Data Seperation 
Define linear model:

![image](https://user-images.githubusercontent.com/89429238/132929874-cb0277fd-dc98-41c3-b576-ed3f8acd9c99.png)
- [dot] is the indicator function

#### Non-linear Data Separation
- more complex weak leaners obtained by replacing hyperplanes with higher degree of freedom surfaces, ie in 2D we could use conic sections:
- ![image](https://user-images.githubusercontent.com/89429238/132930543-ace9b1d0-63e8-48b7-8459-e87da633d54a.png)

- low dim weak learners liek this can be used for data orig reside in very high dim space (d >> 2), selector function \phi can select diff, small set of features and they can be diff for diff nodes
- Degrees of freedom of weak learner influences heavily the forest generalization properties

#### Energy model
- through its influence on the choice of weak learners, energy model determines the prediction and estimation behavior of a decision tree
- information gain associated with tree split node is defined as reduction in uncertainty achieved by splitting training data arriving at nodes into multiple child subsets
- information gain commonly defined as follows:

![image](https://user-images.githubusercontent.com/89429238/132930877-b68bb5c8-fe9d-4205-9590-f0bab7d01590.png)
- H is the entropy: measure of unvertainty associated with random var we wish to predict
- Weighting entropy by cardinality of child sets avoids splitting off children containg very few points
- Splitting training data into purer nodes increases information on the data set and reduces the *uncertainty* of prediction 
-  For discrete probability distributions we use the **Shannon entropy**:

![image](https://user-images.githubusercontent.com/89429238/132931025-3c111782-155b-4f50-9eaf-0f886b4255d6.png)

- *S* is the set of training points, *c* indicates class label, *C* set of all classes, *p(c)* indicates empirical distribution extraced from training points within set *S*

- splitting into purer child nodes corresponds to lower child entropies and higher info gain
- Max info gain helps select split params which produce the highest *confidence (lowest uncertainty)* in final distributions, basis of decision tree training
- 
On example 2, bottom of pg 32
