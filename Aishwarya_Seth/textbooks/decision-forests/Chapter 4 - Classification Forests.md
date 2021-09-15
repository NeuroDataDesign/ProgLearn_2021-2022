# Chapter 4: Classification Forests

Source: [Decision Forests for Computer Vision and Medical Image Analysis](https://link.springer.com/book/10.1007/978-1-4471-4929-3) Chapter 4

Goal: Associate input **v** with a discrete class _c_ &epsilon; {_c<sub>k</sub>_}

## **Properties of Classification Forests**
* Extendable to more than 2 classes 
* Provide probabilistic output
* Generalize well to previously unseen data 
* Efficient (only a small set of tasks applied to each data point)
* Can be parallelized 
* Yield good generalization, even in problems with high dimensionality 
* _Under certain conditions_ classification forests show margin maximization properties 
* _By controlling choice of specific parameters_ the quality of the posterior and the associated confidence can be controlled 

<br>

**In principle, Classification Trees can work unmodified with any number of classes** <br>
Other classification algorithms such as SVMs, boosting, etc cannot work with more than 2 classes without a forced extension  

<br>

## **Specializing the Decision Forest Model for Classification**

<br>

> Classification Task: <br> Given a labelled set of training data, learn a general mapping which associates previously unseen test data with their corresponding classes 

<br> 

> Inductive Task: <br> Typically has the need for a general rule that can be applied to "not-yet-available" test data 

<br> 

Each training point is denoted as a pair (**v**, _c_) <br>
More generally, we wish to find the whole distribution p(_c_|**v**) <br>
And input **v** is represented as multi-dimensional vector of feature responses **v** = (x<sub>1</sub>, x<sub>2</sub>, x<sub>3</sub>... x<sub>d</sub>) &epsilon; ℝ

<br>


* Training Object Function: 
    * Train parameters of the weak learner via: 
    
    <br>

    <img src="https://latex.codecogs.com/svg.image?\textbf{}\Theta&space;_{j}&space;=&space;{\tfrac{argmax}{\Theta&space;\epsilon&space;\tau&space;_{j}}}{\textit{I}(S_{j},\theta&space;)}" title="\textbf{}\Theta _{j} = {\tfrac{argmax}{\Theta \epsilon \tau _{j}}}{\textit{I}(S_{j},\theta )}" />

    <br> 

    * Objective Function _I_ takes the form of information gain: 

    <br>

    <img src="https://latex.codecogs.com/svg.image?{\textit{I}(S_{j},\theta&space;)}&space;=&space;\mathbf{{H(S{j})}&space;-&space;\sum_{i&space;&space;\epsilon&space;{L,&space;R}}^{}\frac{\left|&space;{S_{i}^{j}}\right|}{\left|&space;S_{j}&space;\right|}&space;\mathbf{{H(S_{j}^{i})" title="{\textit{I}(S_{j},\theta )} = \mathbf{{H(S{j})} - \sum_{i \epsilon {L, R}}^{}\frac{\left| {S_{i}^{j}}\right|}{\left| S_{j} \right|} \mathbf{{H(S_{j}^{i})" />

    <br> 

    * Entropy for a generic set S of training points: 

    <br>

    <img src="https://latex.codecogs.com/svg.image?\mathbf{{H(S)}&space;=&space;-\sum_{c&space;\epsilon&space;C}^{}\textit{p(c)}&space;log(\textit{p(c)})" title="\mathbf{{H(S)} = -\sum_{c \epsilon C}^{}\textit{p(c)} log(\textit{p(c)})" />

    <br> 

    * _p(c)_ is calculated as the normalized empirical histogram of labels correctly corresponding to the training points in S 

    * Maximizing information gain -> Produces trees where the entropy of the class distributions associated with the nodes decreases i.e. the prediction confidence increases when going from the root towards the leaves 

     Thus, certainty of prediction keeps increasing 

* Class Re-balancing 
    * PROBLEM: Unbalanced distribution of classes in the training set S<sub>0</sub>
    * FIX v1: Resample training data to get roughly uniform training distributions
    * FIX v2: Use the known prior class distribution : Weight contribution of each class by inverse frequency while computing info gain

* Randomness
    * Injected via randomize dnode optimization
    * &rho; = |&Tau;<sub>j</sub>| controls the amount of randomness
    * Generate each random subset &Tau;<sub>j</sub> before starting training of the corresponding node 

* Leaf & Ensemble Prediction Models 
    * Tree leaf yields the posterior _p<sub>t</sub>_(_c_|**v**)
    * Forest output is defined as: 
    <br>
    <img src="https://latex.codecogs.com/svg.image?\textit{p}&space;=&space;(\textit{c}|\textbf{v})&space;=&space;\frac{1}{T}\sum_{t&space;=&space;1}^{T}p_{t}(\textit{c}|\textbf{v})" title="\textit{p} = (\textit{c}|\textbf{v}) = \frac{1}{T}\sum_{t = 1}^{T}p_{t}(\textit{c}|\textbf{v})" />
    
<br>
        
## **Effect of Model Parameters**
<br>

* Objective function (direct relation)
* Prediction model (direct relation )
* Effect of Forest Size: 
    * Increasing forest size produces smoother posteriors
    * Higher confidence near training points and lower further away 
    * Few trees -> Rigid boundaries, imperfect generalization
* Multiple Classes & Training Noise: 
    * Training Noise: Larger overall uncertainty in the testing posterior 
* Effect of Tree Depth: 
    * Increase of tree depth increases the overall prediction confidence 
    * In large gaps, the optimal separating surface tends to be placed in the middle of the gap (yay!)
    * Large value of D (Tree Depth) causes overfitting 
    * Shallow trees produced washed-out, low-confidence posteriors
    * Multiple trees alleviates overfitting problems of individual trees, but does not eliminate it completely 
    * Important to select the most appropriate value of D 
* Effect of the Weak Learner 
    * Weak learner with best behavior depends on the application
    * AIM: To show that decision forests are flexible & can produce different confidence behaviours 
    * Choice of weak learner is based on: 
        * Accuracy
        * Efficiency
        * Specific application
* Effect of Randomness
    * Large randomness: blocky artifacts in axis-aligned weak learners, more rounded decision boundaries
    * Much lower overall confidence 
    * Complex weak learners work well for large randomness, but take time to stabilize

<br>

## **Maximum Margin Classification with Forests**
<br>

The ability to separate data belonging to different classes via a margin-maximizing surface allows good generalization even with relatively little training data. <br>

When we train the root of the first tree, if we have enough candidate features i.e. |&Tau;<sub>0</sub>| is large, the decision boundary lies in the gap. Any separating line in the gap can act as a decision boundary, and will be associated with the exact same maximum information gain. <br>

AIM: To pick the line so that the posteriors of both the adjacent classes are equal at the line i.e. pick the solution right in the middle of the gap <br> 

Consider the example of linearly separable training data: 
* Weak learners: Vertical lines only i.e. _h_(**v**, **&theta;<sub>j</sub>**) = [ &phi;(**v**) > &tau;] with &phi;(**v**) = _x<sub>1</sub>_
* Define gap &Delta; = _x"<sub>1</sub> - x'<sub>1</sub>_ (_x"<sub>1</sub>_ = 1st feature of support vectors & _x'<sub>1</sub>_ 2nd feature of support vectors)
* If we keep y-coordinate fixed, the posteriors are _p_(_c_|x<sub>1</sub>) and _p_(_c_|x<sub>2</sub>) for c<sub>1</sub> and c<sub>2</sub> respectively
* Optimal separating line is at &tau;* where:
    &tau;* = minimize by varying &tau; |p(c=c<sub>1</sub>|x<sub>1</sub> = &tau;) - p(c = c<sub>2</sub>|x<sub>1</sub> = &tau;)|
* ASSUME: When training a node, its available test parameters (here, just &tau;) are sampled from a uniform distribution 
* THEN, Forest posteriors behave linearly within the gap region and pick the centre as the decision boundary 
* This only occurs as number of trees tends to infinity 

![Maximum-Margin](MaxMargin.jpg)

<br> 

### **Effect of Randomness on Optimal Separation**

<br>

More randomness -> Fewer trees -> Individual trees may not split data perfectly -> Sub optimal information gain -> Lower confidence in posterior -> Decision boundary is not at the centre & is less sharply defined -> Effect of Mass of Training Data > Effect of Individual Points 

<br>

### **Influence of the Weak Learner Model**

<br>
Linear weak learners -> Globally non linear classification (due to hierarchy and averaging)
    

