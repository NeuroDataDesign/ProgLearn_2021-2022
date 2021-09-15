# Chapter 3: The Abstract Forest Model

Source: [Decision Forests for Computer Vision and Medical Image Analysis](https://link.springer.com/book/10.1007/978-1-4471-4929-3) Chapter 3

Problems related to automatic/semi-automatic analysis of data can be thought of as a limited **set of prototypical machine learning tasks**

Types of Machine Learning Tasks: 
* Classification : Recognizing a discrete category
* Regression : Predicting a continuous value
* Density function : Detecting outliers by creating a distribution for the rest 
* Manifold learning : Establishing correlations between parameters 
* Semi-supervised : Combining influences of labelled data and already available unlabelled data 
* Active Learning : Learning a general rule with minimum annotations (because expert annotations are expensive) 


**_A unified model of decision forests is proposed which can be used to tackle all the common machine learning tasks mentioned above_**

Steps: 
1. Model definitions & components 
2. Basic principles of decision trees
3. General mathematical notations 
4. Tree -> Decision Forest

<br>
<br>


## **Decision Tree Basics**

<br>

* Generalize well 
* Achieved by ensembling

<br>

### **What is a tree?**
* Graph 
* Data structure
* Cannot have a loop 
> What is a tree? <br>
> It is a collection of nodes and edges organized in a hierarchial fashion. 

Nodes are of two types: 
1. Internal / Split : Denoted by circles
2. Terminal / Leaf : Denoted by squares

>This book only deals with binary trees i.e. each internal node has exactly two outgoing edges

<br>


### **What is a decision tree?**

A decision tree is a series of questions. The answers to these questions determine the terminal node reached by the input. This movement from input to output node is graphically represented by the path taken from root to leaf node. 

It is a hierarchial piece-wise model. It breaks a complex problem into a series of simpler ones. 

> What does a decision tree do? 
> <br> For a given input object, a decision tree estimates an unknown property of the object by asking successive questions about its known properties

The aim of these questions is to move to the right **decision space**

**Key to a good decision tree** is to establish: 
1. Tests associated with each internal node
2. Decision making predictors associated with each leaf 

<br>

### **Mathematical Notations**
<br>

#### Data points: 
* Object = Data point = Vector 
* **v** = (x<sub>1</sub>, x<sub>2</sub>, x<sub>3</sub>... x<sub>d</sub>)
* ℝ: Set of Real No. then, v ∈ ℝ<sup>d</sup>
* Each x<sub>i</sub> represents some attribute of this data point called <code> feature </code>
* Number of & specific features depend on the application 
* Dimensionality d can be vey large, we only extract a small portion on an as-needed basis
* Features of interest: Subset of all features, dimensionality d' 
* d' << d

<br>

#### Split Functions: 
* Split function = Test function = Weak learner
* Test function at node j with binary outputs (0 = false, 1 = true):
<br> h(**v**, **_θ_**<sub>j</sub>): ℝ<sup>d</sup> x &Tau; -> {0, 1}
* &theta;<sub>j</sub> ∈ &Tau; denotes split parameters of the j<sup>th</sup>node
* &Tau;: Space of all split parameters
 >Role of a split function: <br> The data point **v** arriving at the split node is sent to the left or right child node according to the results of the test/split function

<br>

 #### Training Point
 > What is a training point? <br>It is a data point for which the attributes were are seeking may be known and used to calculate tree parameters
* Defined by: 
    1. **v**: Feature vector (i.e. input)
    2. **y**: Known label (in supervised learning) (i.e. output)
* S<sub>n</sub>: Subset of training points reaching node 'n'
    * The split function divides S<sub>n</sub> into two smaller sets
    * S<sub>n</sub><sup>L</sup> : subset of training points going to the left child 
    * S<sub>n</sub><sup>R</sup>: subset of training points going to the right child 

<br>

#### Data points: 
* Object = Data point = Vector 
* **v** = (x<sub>1</sub>, x<sub>2</sub>, x<sub>3</sub>... x<sub>d</sub>)
* ℝ: Set of Real No. then, v ∈ ℝ<sup>d</sup>
* Each x<sub>i</sub> represents some attribute of this data point called <code> feature </code>
* Number of & specific features depend on the application 
* Dimensionality d can be vey large, we only extract a small portion on an as-needed basis
* Features of interest: Subset of all features, dimensionality d' 
* d' << d

<br>

#### Split Functions: 
* Split function = Test function = Weak learner
* Test function at node j with binary outputs (0 = false, 1 = true):
<br> h(**v**, **_θ_**<sub>j</sub>): ℝ<sup>d</sup> x &Tau; -> {0, 1}
* &theta;<sub>j</sub> ∈ &Tau; denotes split parameters of the j<sup>th</sup>node
* &Tau;: Space of all split parameters
 >Role of a split function: <br> The data point **v** arriving at the split node is sent to the left or right child node according to the results of the test/split function

<br>

 #### Training Point
 > What is a training point? <br>It is a data point for which the attributes were are seeking may be known and used to calculate tree parameters
* Defined by: 
    1. **v**: Feature vector (i.e. input)
    2. **y**: Known label (in supervised learning) (i.e. output)
* S<sub>n</sub>: Subset of training points reaching node 'n'
    * The split function divides S<sub>n</sub> into two smaller sets
    * S<sub>n</sub><sup>L</sup> : subset of training points going to the left child 
    * S<sub>n</sub><sup>R</sup>: subset of training points going to the right child 

<br>

### **Training Phases**
<br>

#### Phase 1: Tree Testing
* New data point
* Moves through the tree till it gets an output label 

#### Phase 2: Tree Training
* Selects **type & parameters of the test function at each internal node**
* Greedy approach, i.e. chooses the best split 
* Maximization problem 
* Left child holds output 0, Right child holds output 1
* Definition of best depends on definition of the problem 
* Also **decides tree structure**
* Stopping criteria 

<br>

**Outcome of the Training Phase**
1. Learnt the split functions for each internal node 
2. Learnt the tree structure
3. Have a different set of training points at each leaf 

<br>


> Parameters of the Split Function  &theta; = ( &phi;, &psi;, &tau;)<br>
> &phi; : Filter/Selector Function<br>
&nbsp; &nbsp; &nbsp; Selects some features (may be different for each node)  <br>
> &psi; : Defines what geometric object will be used for separation <br>
> &tau; : Captures thresholds of all inequalities in the binary tests

<br>

### **Energy Models**

They determine the prediction and estimation by a tree because their optimization is the main criteria for selecting the parameters of the weak learners

<br> 

#### **Entropy and Information Gain**
<img src="https://latex.codecogs.com/svg.image?I&space;=&space;H(S)&space;-&space;\sum_{i\epsilon&space;\left\{L,R&space;\right\}}\frac{\left|S^{i}&space;\right|}{\left|&space;S&space;\right|}H(S^{i})" title="I = H(S) - \sum_{i\epsilon \left\{L,R \right\}}\frac{\left|S^{i} \right|}{\left| S \right|}H(S^{i})" />

<br>

where, 
* I : Information gain 
* H : Entropy
* S : Dataset which gets split into S<sup>L</sup> and S<sup>R</sup> (Only two because it's a binary tree)

> Weighting the entropy by the cardinality of the child sets
avoids splitting off children containing very few points

<br>

<code> Information Gain </code> : It is the reduction in uncertainty achieved by splitting the training data into child subsets. We maximize it to select the split parameters that will generate the highest confidence (lowest uncertainty) in the final distributions

<br>

For discrete probability distributions, the entropy is defined as: 
<br>

<img src="https://latex.codecogs.com/svg.image?H(S)&space;=&space;-\sum_{c\epsilon&space;C}^{}p(c)log(p(c))" title="H(S) = -\sum_{c\epsilon C}^{}p(c)log(p(c))" />

<br> 

where, 
* c : Class label
* C : Set of all classes
* p(c) : Empirical distribution from the training points within set S

For continuous probability distributions, the entropy is defined as: 

<br>

<img src="https://latex.codecogs.com/svg.image?H(S)&space;=&space;-\int_{y\epsilon&space;Y}^{}p(y)log(p(y))dy" title="H(S) = -\int_{y\epsilon Y}^{}p(y)log(p(y))dy" />


<br>
<br> 

### **Leaf Prediction Models**
<br>

A new unseen point traverses the tree until it reaches a leaf node. Since the split nodes act on features, the input test point is likely to end up with training points similar to itself. 

Leaf Statistics are therefore conditional distributions: 
* p(c | **v**) : where c is a categorical label 
* p(**y** | **v**) : where y is a continuous llabel 

> It is advisable to keep the entire distribution until the moment when a decision MUST be taken to reduce prediction uncertainty


### **Randomness Model**
<br>

#### **Ways of Injecting Randomness**: 
* Bagging : Sample training set randomly
* Random Node Optimization : Only maximize some j parameters, picked randomly 

    * Allows us to still use the entire training data 
    * Yields margin-maximization properties 
    * Lower training efficiency

<br> 

## **The Forest Ensemble**

> **Random Decision Forest: Ensemble of randomly trained decision trees**

* All trees are different from one another 
* Improves generalization
* Makes the system more robust
* Could just take the average of all trees 
* Can move data through all trees in parallel 
* These operations choose the **most confident trees in the forst**
* Also **eliminates noisy contributions**

<br>

## **Key Model Parameters**

<br> 

1. D: Maximum allowed tree depth
2. &rho; : Amount of randomness (&type)
3. _T_ : Forest size
4. Choice of weak learner
5. Training objective function 
6. Choices of features

<br>

> The choices impact accuracy, quality, confidence, generalization and efficiency. 

<br>

Some relations: 
* Testing accuracy &prop; _T_
* Depth of trees &prop; Overfitting

<br> 

> Visualization of forests helps ensure that they are behaving as they should

