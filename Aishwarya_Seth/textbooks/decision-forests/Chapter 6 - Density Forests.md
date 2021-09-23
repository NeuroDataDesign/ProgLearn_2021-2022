# Chapter 6: Density Forests

Source: [Decision Forests for Computer Vision and Medical Image Analysis](https://link.springer.com/book/10.1007/978-1-4471-4929-3) Chapter 6

Goal: Use forests in unlabeled scenarios. Helps discover instrinsic nature & structure of large sets of unlabeled data 

## **Specializing the Decision Forest Model for Density Estimation**

<br>

> Density Estimation Task: <br> Given a set of unlabeled observations we wish to estimate the probability density function from which such data have been generated  

<br>

* Input data: multi-dimensional feature vector **v** = (x<sub>1</sub>, x<sub>2</sub>, ..., x<sub>d</sub>) &epsilon; ℝ<sup>d</sup>
* Desired output: p(**v**) >= 0, such that: <br>

<img src="https://latex.codecogs.com/svg.image?\int&space;p(\textbf{v})&space;d\textbf{v}&space;=&space;1&space;" title="\int p(\textbf{v}) d\textbf{v} = 1 " />

<br>

* Density forest: Collection of randomly trained density trees
* Forest posterior = Combination of tree posterior
* Multiple hard data partitions: One for each tree 


<br>

* Training Objective Function: 
    * Given a collection of points S<sub>0</sub> = {**v**} 
    * No training labels 
    * Train each individual tree independently
    * Use randomized node optimization 
    * Optimize the _j_<sup>th</sup> split noce
    
    <br>

    <img src="https://latex.codecogs.com/svg.image?\textbf{}\Theta&space;_{j}&space;=&space;{\tfrac{argmax}{\Theta&space;\epsilon&space;\tau&space;_{j}}}{\textit{I}(S_{j},\theta&space;)}" title="\textbf{}\Theta _{j} = {\tfrac{argmax}{\Theta \epsilon \tau _{j}}}{\textit{I}(S_{j},\theta )}" />

    <br>

    * Objective Function _I_ takes the form of generic information gain

    <br>

    <img src="https://latex.codecogs.com/svg.image?{\textit{I}(S_{j},\theta&space;)}&space;=&space;\mathbf{{H(S{j})}&space;-&space;\sum_{i&space;&space;\epsilon&space;{L,&space;R}}^{}\frac{\left|&space;{S_{i}^{j}}\right|}{\left|&space;S_{j}&space;\right|}&space;\mathbf{{H(S_{j}^{i})" title="{\textit{I}(S_{j},\theta )} = \mathbf{{H(S{j})} - \sum_{i \epsilon {L, R}}^{}\frac{\left| {S_{i}^{j}}\right|}{\left| S_{j} \right|} \mathbf{{H(S_{j}^{i})" />

    <br> 

    * Entropy for a generic set S of training points (Takes the form of unsupervised entropy): 

    <br> 
    <img src="https://latex.codecogs.com/svg.image?H(S)&space;=&space;\frac{1}{2}&space;log((2\pi&space;e)^d\left|&space;\Lambda&space;(S)\right|)" title="H(S) = \frac{1}{2} log((2\pi e)^d\left| \Lambda (S)\right|)" />

    <br>

    where, &Lambda; is the associated d x d covariance matrix 
    * Information Gain is simplified as: 
    <br>

    <img src="https://latex.codecogs.com/svg.image?I(S_{j},&space;\theta)&space;=&space;log(\left|&space;\Lambda&space;(S_{j})\right|)&space;-&space;\sum_{i&space;\epsilon&space;{L,&space;R}}^{}\frac{\left|&space;S_{j}^{i}\right|}{\left|&space;S_{j}\right|}log(\left|&space;\Lambda&space;(S_{j}^{i})\right|)" title="I(S_{j}, \theta) = log(\left| \Lambda (S_{j})\right|) - \sum_{i \epsilon {L, R}}^{}\frac{\left| S_{j}^{i}\right|}{\left| S_{j}\right|}log(\left| \Lambda (S_{j}^{i})\right|)" />

    <br>
    where, |.| is the determinant (if matrix) or cardinality (if set)
    * By maximizing info gain, tree training tends to split the original data into compact clusters
    * Centers of clusters are in areas of high data density, while the separating surfaces are placed along regions of low density 
    * We have assumed distribution in Gaussian - simple & effective but not representative of real data 
    * Because of hierarchy of trees, Gaussian is sufficient even for complex structures 

* Prediction model 
    * Set of leaves in each tree defines a partition of data 
    * Set of points at a leaf is taken to be a multivariate Gaussian distribution
    * Ensure probabilistic normalization via partition function 
    <br>
    <img src="https://latex.codecogs.com/svg.image?Z_{t}&space;=&space;\int_{v}^{}(\sum_{l}^{}\pi_{l}N((v;&space;\mu_{l},\Lambda&space;_{l})p(l|v))" title="Z_{t} = \int_{v}^{}(\sum_{l}^{}\pi_{l}N((v; \mu_{l},\Lambda _{l})p(l|v))" />
    <br>
    * Each data point reaches exactly one terminal node 
    * Conditional p(l|v) is a delta function and =1 in the equation 
    * Computing Z<sub>t</sub> in high dimensions may be challenging
    * Axis-aligned weak learners:
        * Can find partition function by cumulative multivariate normal distribution function 
        * Partition function Z<sub>t</sub> is the sum of all volumes subtended by each Gaussian, cropped by its associated partition cell 
        * No closed form solution, but can be approximated
    * Complex weak learners
        * Z<sub>t</sub> is easier to approximate by integration over a regular grid 
        * Consider points in a finite regular grid with uniform spacing and add them up instead of integrating 
        * Small grid cells -> More accurate approximation of partition function BUT higher computational cost 

    **Revisit this subheading** 

* Ensemble model
    * Average tree densities
    * A point belongs to T component, one per tree
    * Allows for mixing of information from across trees 
    

* Effect of Model Parameters: 
    * Tree Depth: Deep trees create further splits & smaller Gaussians, therefore overfitting (i.e. fit to the noise)
    * Forest size: Increasing forest size improves smoothness and generalization (even if individual trees overfit)