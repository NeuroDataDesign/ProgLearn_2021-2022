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

#### 
