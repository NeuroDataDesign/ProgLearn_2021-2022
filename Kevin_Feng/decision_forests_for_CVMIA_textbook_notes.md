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

### Linear Data Seperation 
Define linear model:

![image](https://user-images.githubusercontent.com/89429238/132929874-cb0277fd-dc98-41c3-b576-ed3f8acd9c99.png)
- [dot] is the indicator function

### Non-linear Data Separation
- more complex weak leaners obtained by replacing hyperplanes with higher degree of freedom surfaces, ie in 2D we could use conic sections:
- ![image](https://user-images.githubusercontent.com/89429238/132930543-ace9b1d0-63e8-48b7-8459-e87da633d54a.png)

- low dim weak learners liek this can be used for data orig reside in very high dim space (d >> 2), selector function \phi can select diff, small set of features and they can be diff for diff nodes
- Degrees of freedom of weak learner influences heavily the forest generalization properties

### Energy model
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

- For continuous-valued labels and continuous distributions, def of information gain remains the same, but **differential (continuous) entropy** is used in place of Shannon entropy: 

![image](https://user-images.githubusercontent.com/89429238/132931691-279d0da9-9f5b-48f6-8354-dca385530a4c.png)
 - *y* is a continuous label of interest and *p* is the probability density function estimated from the training points in set *S*
 - in discrete case *p(c)* defined as empirical distribution computed from training set, in continuous case *p(y)* defined either using parametric distributions or non-parametric methods
 - Differential entropy of *d*=variate Gaussian can be derived analytically as:

![image](https://user-images.githubusercontent.com/89429238/132931789-f86bf666-37dd-47d8-b86b-c1911576121a.png)

### Leaf prediction model
- unseen point traverses tree until it lands at a leaf, the input point is likely end up in a leaf associated with training points which are all similar to itsself because the split nodes act on features
- associated label must also be similarr to that of th training points in that leaf


### Randomness Model
- two popular ways to inject randomess into trees during training phase
1. random training set sampling (eg. bagging)
2. randomized node optimization

#### Bagging 
- in bagged training intro'd as way of reducing opssible overfitting and improving generalization capabilities of rand forests
- Train each tree in a forest on a different training subsets, sampled at random from the same labeled database
- This helps avoid specializing the selected params to single training set and has been shown to improve generalization 
- faster training than having to use entire labeled set, but not using all avail training data for all trees seems wasteful

#### Randomized Node Optimization (RNO)
- Under randomness model, training a tree is achieved by optimizing each split node *j* as:

![image](https://user-images.githubusercontent.com/89429238/132966474-5d4d8f9b-9fee-49e4-b12f-d6e92bde2688.png)

where \Tau_j is a small random subset of \Tau
- in some cased \Tau = \infinity, so we define \rho = \Tau_j 
- \rho belongs to {1,...,\Tau} controls the degree of randomness in a tree and (usually) its value is fixed for all nodes
- In practical applications one might want to randomize none, some, or all the params \phi, \psi, \tau. eg one might want to randomize the \phi selector function parameters and the \psi parameters that define the orientation of a weak learner hyperplane, but search over a predefined set of thresholds \tau

![image](https://user-images.githubusercontent.com/89429238/132966640-82b2aa8a-6c36-4d94-a1c9-9828153e307b.png)
- \rho = \Tau trees identical
- \rho decreases, trees become more decorrelated

### Combining Trees into a Forest Ensemble 
- a random decision forest is an ensemble of *randomly trained* decision trees
- in forest with T trees, use *t* belongs to {1,...,T} to index each component tree
- all trees trained independently (possibly in parallel)
- during testing, each test point **v** is simultaneously pushed through all trees until it reaches the corresponding leaves (can also be done in parallel -> high computational efficiency)
- can combine all tree predictions into one by averaging eg:

![image](https://user-images.githubusercontent.com/89429238/132969133-76c12475-a9f8-4296-8802-22d87df39d1d.png)

- Combinined distributions are more heavily influenced by most confident/informative trees
- averaging out many tree posteriors also had advantage of reducing effect of possibly noisy tree contributions
- product based ensemnble model produces sharper distributions and may be less robust to noise
![image](https://user-images.githubusercontent.com/89429238/132969180-f7e0f97a-48f6-4559-aae7-1c485d7a1700.png)

### Key Model Parameters (params that most influece behavior of a decision forest)
- the maximum allowed tree depth D
- the amount of randomness (controlled by \rho) and its type
- the forest size (T)
- the choice of a weak learner model
- the training objective function
- the choice of features in practical applications

## Chapter 4: Classification Forests
### Specializing the Decision Forest Model for Classification 
- **Classification:**  given a labeled set of training data learn a general mapping which associates previously unseen test data with their corresponding classes
- **Class Re-balancing:** some applications have an unbalanced distribution of classes in the training set S_0 (ie background pixels domiate other object pixels) which can have a detrimental effect on the training forest. Can be mitaged by resampling the training data to have a roughly uniform train distribution of can use the known prior class distribution to weight the contribution of each class by its inverse frequency when computing the info gain at each split node
- larger forests lead to more conidence and less uncertainty
- tree > SVM and boosting because same classification model can handle binary and multi-class problems
- large tree depth **D** can lead to overfitting -> changning this value is one way to control overfitting
- tree depths that are too shallow produce washed-out, low-confidence posteriors
- Using multiple trees helps alleviate overfitting but does not cure it completely, must be careful when choosing D

### The Effect of the Weak Learner model on forest behavior
![image](https://user-images.githubusercontent.com/89429238/133354696-3f334baa-8c69-4c5b-828b-a508fbcee6c4.png)

### The effect of randomness (*p*, \rho)
- lowering *p* yields much fewer separating lines/curves available to each node during training
- This increases the randmoness of each tree and reduces their correlation
- larger randomness yields a much lower overall confidence (most noticeable in shallower trees)
- more complex weak learners are sampled from larger parameter spaces so finding discriminative sets of parameter values may be time consuming

### Maximum Margin Classification with Forests
- Maximum margin solution: a line placed directly in the middle of a gap that seperates two classes 

![image](https://user-images.githubusercontent.com/89429238/133361816-268e7d36-b0fc-45f6-a99a-6e32594e01e7.png)

### Effect of randomnesse on optimal seperation
- given sloppy or inaccurate training data, we may want to increase randomness (decrease *p*) to obtain smoother and more spread-out posteriors. The effeect of individual training points is weaker compared to the entire mass of the training data

### Influence of the Weak Learner Model
- more complex weak learners affect shape and orientation of the hard classification surface as well as the uncertain region

### Maximum Margin with Multiple Classes
- works similarily to two class example
- RNO controls max - margin behavior simply by changing p 
- advantage of bagging is increased training speed due to reduced training set size

## Chapter 5: Regression Forests
- used for non-linear regression of dependent variables given independent input, where both input and output may be multi-dimensional
- output label to be associated with input data point is continuous so training labels also need to be continuous

### Specializing the Decision Forest Model for Regression
- **Problem statement:** given a labeled set of training data, learn a general mapping which associates previously unseen, independent test data opints with their dependent continuous output prediction
- A regression tree splits a complex non-linear regression problem into a set of smaller problem which can be more easily handled by simpler models (eg. linear ones)
- **Regression Forest:**

![image](https://user-images.githubusercontent.com/89429238/133526769-0025d56b-3000-469a-8fba-5b571dfda2fa.png)

### The Training Objective Function
- forest training achieved by optimizing an energy function defined over a training set *S _0* of data and associated continuous labels
- split node j optimized as: \theta_j = argmax I (S_j, \theta), \theta belongs to T_j
- Main diff between classification and regression forests is in form of objective function I
- Information gain associated with jth split node is:

![image](https://user-images.githubusercontent.com/89429238/133527365-f26822e9-e8f5-4371-8267-6849b06a2456.png)

- S_j = set of training data arriving at node j, SL_j and SR_j are left and right split sets
- Given training set S_0, avg entropy for generic trainig subset S is defined as:

![image](https://user-images.githubusercontent.com/89429238/133527484-b06b6f19-1be8-4e0f-91f7-d010eef251b9.png)

### The Effect of Forest Size, T
- more trees = smoother mean curves 

![image](https://user-images.githubusercontent.com/89429238/133531071-6b8c45c2-83cc-4f4b-8c2b-f3299d499084.png)

### The Effect of Tree Depth, D
- too shallow, underfit
- too deep, overfit

### Spatial Smoothness and Testing Uncertainty
![image](https://user-images.githubusercontent.com/89429238/133531870-c41cd559-e3c6-47ac-b317-84e756fb2a5c.png)

## Chapter 6: Density Forests
- ch 4-5 discussed use of decision forests with labeled training data (supervised), here discusses forests in unlabeled scenarios
- goal to learn PDF p(v) which generated the data, closely related to data clustering
- **Problem statement:** given a set of unlabeled obervations we wish to estimate the probability density function from which such data have been generated 
- **Density forest:** collection of randomly trained clustering trees, leaves contain simple prediction models such as Gaussians

### The Training Objective Function
- given collection of S_0 = {v} (absence of training labels)
- emply randomized node optimization, optimizing the jth split node as done before:

![image](https://user-images.githubusercontent.com/89429238/133905791-92978823-9f76-405c-be0e-2a3236e73df5.png)
- Define *unsupervised* entropy H(S) of a set points S, differential (continuous) entropy of d-dimensional Gaussian show as:

![image](https://user-images.githubusercontent.com/89429238/133905862-a8d70c93-df53-487b-a49f-99a216403c27.png)

- A tree density is a piece wise Gaussian, so output of tth tree is 

![image](https://user-images.githubusercontent.com/89429238/133906023-414564eb-c2d3-4825-aed6-6c90348fb636.png)

and partition function Z_t is

![image](https://user-images.githubusercontent.com/89429238/133906033-21f0e24d-d3bf-4303-8e75-904f8a1cb0ff.png)

### Ensemble model
- forest density is aberage of all tree densities 
![image](https://user-images.githubusercontent.com/89429238/133906099-f369ebaa-517e-44f9-a0c6-fc8080185483.png)

### Effect of tree depth D
- forests that are unnecessarily deep -> produce small, high freq artifacts from training noise
- ie 2 visual clusters but if you have depth set high, insead of 2 circles you'll have a bunch of small sub circles in each of the two main circles

### Effect of forest size T
- increasing forest size always improves smoothness of the density and the forest generalization, even for deep trees
- in practice, set T to a sufficiently large value w/o worrying too much about optimizing its value, may come at an increased computational cost

### Density forest vs non-parametric estimators (parzen, kNN)
- forest density looks the best, other two arent as smooth and produce artifacts

### vs GMM EM
- forest density produced the most visually appealing results, but adding randomness to the EM algo improves the smoothness of the output density considerably

### Efficiency 
- cost of randmoly drawing N samples under forest model:
- N X (2J+K)
- with J (almost negligible) of radnomly generating a scalar number and K the cost of drawing a d-dimensional vector from a multivariate Gaussian distribution
- Despite added richness in heirarchical struction of deisity forest, its sampling complexity is very much comparable to that of a random-restart GMM

### Results
- randmon points generated from the learned forests produce visually convincing results for simpler Gaussian mixture dists as well as more complext densities like spirals and other convolved shapes
- reconstruction error decreases with forest size
- overall error start increasing again after an optimal value D (suggests overfitting for larger tree depths)

## Chapter 7: Manifold Forests (pg. 91)
- delves further into issue of learning structure of high dim data as well as mapping it onto a lower dim space, while preserving spatial relationships between points = **manifold learning**, closely related to dimensionality reduction and embedding
- PCA is a simple and common example, based on the computation of directions of maximum data spread, is a linear model so has considerable limitations
- **Problem statement:** Given a set of k unlabeled observations {v_1, v_2,....,v_i,...v_k} with v_i belong the R^d we wish to find a smooth mapping f:R^d -> R^Dprime with f(v_i) = v_iprime that approximately preserves the obersvations' relative geodesic distances, with dprime << d.

### High level structure of the forest-based embedding algo
1. decision forest is used to infer efficiently the kxk affinity matrix w between all pairs of imput unlabeled data points
2. given w, dimensionality reduction is performed by applying any know technique (eg Lapacian eigenmaps)

### Training objective function
- also use randomized node optimization by maxing the cont info gain measure from ch6 with I defined as for density forests also from ch6

### Predictor model
For density model, stats for all training points arriving at each leaf node are summarized with a single multivariate Gaussian:

![image](https://user-images.githubusercontent.com/89429238/133912159-93a7024a-b72f-4779-84bd-6550f94a78a9.png)

### Affinity model
- unlike others, in manifold learning, need to estimate measure of similarity, affinity, or distance between data points so we can try and preserve those inter-point distances after mapping
- see pg 83 for equations and definitions 
- binary affinity model most interesting and says: give a tree t and two points v_i and v_j we assign perfect affinity (affinity = 1, distance = 0) to the pair (v_i, v_j) if those two points end up in the same cluster (leaf) and null affinity (infinite distance) otherwise

### The Ensemble Model
- in a forest of *T* trees its affinity matrix is defined as: 

![image](https://user-images.githubusercontent.com/89429238/133912262-75505ae3-74ae-4b8c-8065-5ae779108d3b.png)

- the averaging operation in above has the effect of adding robustness to the pairwise addinities across the graph of all points

### Estimating the Embedding Function
- estimating the mapping function can be done with any existing non-linear dimensionality reduction technique, use Laplacian eigenmaps here
- given W, a low dimensional embedding is found using:

![image](https://user-images.githubusercontent.com/89429238/133912336-dcd224ae-cbf9-47a1-9470-276d1cb7a4b2.png)

- \upsilon = normalizing diagonal matrix (often called a "degree" matrix), such that \upsilon_ii = sum(W_ij) 
- mapping function **f** found via eigen-decomposition of L
- **f** remains implicitly defined by its *k* corresponding point pairs through the eigenvector matrix E

![image](https://user-images.githubusercontent.com/89429238/133912373-89509780-7194-44bd-ae86-5da36a25a0af.png)

### Mapping previously unseen points 
- instead of retraining manifold, approx technique consists of interpolating the point position given the already avail embedding
- given prev unseen point **v** and an already trained manifold forest we wish to find the corresponding point **v**' in the low-dim space, point **v**' computer as follows:

![image](https://user-images.githubusercontent.com/89429238/133912414-e5f83fe9-5635-4118-abf8-7da242ff6b2d.png)

### Properties and advantages
- eg. dist between beach and forest small cuz they both have trees but dist between beach city big cuz they dont share many similarities (image example)
- do not need to manually specifiy features to use for a manifold forest, can define a generic family of features, then tree training process with auto select discriminative features and corresponding parameters for each node of the forest, so as to greedily optimize the info gain measure

### Effect of Forest Size pg101
- more trees increase asccuracy of mappings and the ordering and position of mapped points is more correctly estimated

### Manifold learning in higher dimensions
- 3D images can be converted to 2D manifolds and 2D color maps that can be used to visualize the evolution of such a surface directly in the original 3D space

### Discovering the Manifold Intrinsic Dimensionality 
- d' at the elbow should be chose because at a certain point d'+1 does not provide that much more info
- high values of T produce more prominent elbows
- Gaussian affinities produce slighly sharper elbows than binary ones

![image](https://user-images.githubusercontent.com/89429238/133947276-c985ca82-1965-4282-bec5-24d9e0c5475b.png)

### Summary
- choose forest depth D carefully, param influences number of cluster and smoothness of recovered mapping
- choose weak learner model to guide way in which diff clusters are sep'd
- increasing forest size T should always result in highers test accuracy

## Chapter 8: Semi-supervised Classification Forests
- Tries to transfer existing ground truth labels to the unlabeled and already available data
- Transductive classification task: given a set of both labeled and unlabeled data points, we wish to associate a class label to all the already available data points
- Unlike inductive classification, here all unlabeled test data are already avail during training 
- 
