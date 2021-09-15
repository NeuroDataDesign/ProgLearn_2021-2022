# Chapter 5: Regression Forests

Source: [Decision Forests for Computer Vision and Medical Image Analysis](https://link.springer.com/book/10.1007/978-1-4471-4929-3) Chapter 5

Goal: Associate continuous output label with a continuous input value

Note: Linear Regression is simple but very sensitive to input noise and not good for non-linear systems. 

## **Specializing the Decision Forest Model for Regression**

<br>

> Regression Task: <br> Given a labeled set of training data, learn a general mapping which associates previously unseen, independent test data points with their dependent, continuous output prediction 

<br>

* It is inductive
* Training point: (**v**, **y**)
* Given a multivariate input **v**, we wish to associate a continuous multivariate label **y** &epsilon; ℝ
* AIM: Estimate a probability density function _p_(**y**|**v**)
* Regression Forest: Collection of randomly trained regression trees


<br>

* Prediction Model
    * Tasks of decision tree: Decide which branch to send data to. At leaf, make a prediction
    * Form of prediction depends on the leaf prediction model 
    * E.g. generic polynomial, line, constant
    * Because we want to know confidence of prediction, we use a probability density function
    * Therefore, we use a probability density function over the continuous variable **y**
    * Given the t<sup>th</sup> tree and an input point **v**, the associated leaf output has the form p<sub>t</sub>(**y**|**v**)

* Ensemble Model
    * Forest output = average of all tree outputs 
<br>

<img src="https://latex.codecogs.com/svg.image?p(\textbf{y}|\mathbf{v})=&space;\frac{1}{T}\sum_{t}^{T}p_{t}(\textbf{y}|\mathbf{v})" title="p(\textbf{y}|\mathbf{v})= \frac{1}{T}\sum_{t}^{T}p_{t}(\textbf{y}|\mathbf{v})" />

<br>

* Randomness Model
    * Randomized node optimization
    * Amount of randomness controlled in training by &rho; = |&Tau;<sub>j</sub>|
    * Random subsets of split parameters &Tau;<sub>j</sub> can be generated while training the j<sup>th</sup> code

* Training Objective Function
    * Train parameters of the weak learner via: 
    
    <br>

    <img src="https://latex.codecogs.com/svg.image?\textbf{}\Theta&space;_{j}&space;=&space;{\tfrac{argmax}{\Theta&space;\epsilon&space;\tau&space;_{j}}}{\textit{I}(S_{j},\theta&space;)}" title="\textbf{}\Theta _{j} = {\tfrac{argmax}{\Theta \epsilon \tau _{j}}}{\textit{I}(S_{j},\theta )}" />

    <br>

    * Objective Function _I_ takes the form of information gain, and uses the functional form of the differential entropy of a Gaussian density: 

    <br>

    <img src="https://latex.codecogs.com/svg.image?{\textit{I}(S_{j},\theta&space;)}&space;=&space;\mathbf{{H(S{j})}&space;-&space;\sum_{i&space;&space;\epsilon&space;{L,&space;R}}^{}\frac{\left|&space;{S_{i}^{j}}\right|}{\left|&space;S_{j}&space;\right|}&space;\mathbf{{H(S_{j}^{i})" title="{\textit{I}(S_{j},\theta )} = \mathbf{{H(S{j})} - \sum_{i \epsilon {L, R}}^{}\frac{\left| {S_{i}^{j}}\right|}{\left| S_{j} \right|} \mathbf{{H(S_{j}^{i})" />

    <br> 

    * Entropy for a generic set S of training points: 

    <br>

    <img src="https://latex.codecogs.com/svg.image?\mathbf{H}(S)&space;=&space;-\frac{1}{\left|&space;S&space;\right|}\sum_{x&space;\epsilon&space;S}^{}\int_{y}^{}p(y|x)log(p(y|x))dy" title="\mathbf{H}(S) = -\frac{1}{\left| S \right|}\sum_{x \epsilon S}^{}\int_{y}^{}p(y|x)log(p(y|x))dy" />

    <br>

    * Conditional Probability: Given as a Gaussian distribution:

    <br>

    <img src="https://latex.codecogs.com/svg.image?p(y|x)&space;=&space;N(y;&space;\bar{y}(x),&space;\sigma&space;_{y}^{2}x)" title="p(y|x) = N(y; \bar{y}(x), \sigma _{y}^{2}x)" />

    <br>

    * Substitution Gaussian distribution in entropy to get information gain: 

    <br>

    <img src="https://latex.codecogs.com/svg.image?I(S_{j}^{},&space;\theta)&space;=&space;\sum_{v&space;\epsilon&space;S_{j}^{}&space;}log(|\Lambda&space;_{y}(v)|)&space;-&space;\sum_{i&space;\epsilon&space;{L,&space;R}}^{}(\sum_{v&space;\epsilon&space;S_{j}^{i}&space;}log(|\Lambda&space;_{y}(v)|))" title="I(S_{j}^{}, \theta) = \sum_{v \epsilon S_{j}^{} }log(|\Lambda _{y}(v)|) - \sum_{i \epsilon {L, R}}^{}(\sum_{v \epsilon S_{j}^{i} }log(|\Lambda _{y}(v)|))" />

    <br>

    Where, &Lambda;<sub>y</sub> is the conditional covariance matrix computed from probabilistic linear fitting

    * Error / Fit Energy Function for Single Variate Output y is: 

    <br>

     <img src="https://latex.codecogs.com/svg.image?\sum_{v&space;\epsilon&space;S_{j}}^{}(y-\bar{y})^{2}&space;-&space;\sum_{i\epsilon&space;{L,R}&space;}^{}(\sum_{v&space;\epsilon&space;S_{i}^{j}}^{}(y&space;-&space;\bar{y_{j}^{i}})^{2})" title="\sum_{v \epsilon S_{j}}^{}(y-\bar{y})^{2} - \sum_{i\epsilon {L,R} }^{}(\sum_{v \epsilon S_{i}^{j}}^{}(y - \bar{y_{j}^{i}})^{2})" />

     <br>

* Weak Learner Model: 
    * Data arriving at split node _j_ is separated into its left & right children 
    * A binary weak learner is used
    * _h_(**v**,**&theta;**<sub>j</sub> &epsilon; {0, 1})
    * 0: FALSE, Go Left; 1: TRUE, Go Right
    * Types of weak learners: 
        * Axis aligned hyperplanes
        * Oriented hyperplanes
        * Conic sections

<br>

## **Effect of Model Parameters**
<br>

* Effect of Forest Size: 
    * Each leaf model produces smaller uncertainty near the training points and larger uncertainty away from them
    * Actual split in diff places within the gap (because of randomness)
    * Increase in number of trees increases prediction mean curve
    * Smoothness of interpolating mean curve increases 
* Effect of Tree Depth: 
    * Low depth - underfits 
    * High depth - overgits 
* Spatial Smoothness & Testing Uncertainty 
    * Mean & mode plotted
    * Mean is smoother & interpolating, Mode is jagged
    * Gaps in the regression forest can correctly capture multi-modal posteriors

    


