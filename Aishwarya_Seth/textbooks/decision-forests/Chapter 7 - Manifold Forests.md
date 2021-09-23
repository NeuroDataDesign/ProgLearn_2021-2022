# Chapter 7: Manifold Forests

Source: [Decision Forests for Computer Vision and Medical Image Analysis](https://link.springer.com/book/10.1007/978-1-4471-4929-3) Chapter 7

Goal: Learn the structure of high dimensional data and map it onto a lower dimensional space, preserving spatial relationships between data points 

## Advantages of using Forests for Manifold Learning 
* Computational efficiency 
* Discriminative features automatically selected on the basis of information gain 
* Code Reusability


## **Specializing the Decision Forest Model for Density Estimation**

<br>

> Manifold Learning Task: <br> Given a set of k unlabelled observations, we wish to find a smooth mapping to a lower dimension such that it approximately preserves the relative geodesic distance between observations

<br> 

* High Level Structure of the Forest-Based Embedding Algorithm 
    * Infer k x k affinity matrix W between all pairs of input unlabeled data points 
    * Given W, perform dimensionality reduction 
    * Here, as example, Laplacian eigenmaps are used 
* Training Objective Function: 
    * Randomized node optimization used 
        <br>

    <img src="https://latex.codecogs.com/svg.image?\textbf{}\Theta&space;_{j}&space;=&space;{\tfrac{argmax}{\Theta&space;\epsilon&space;\tau&space;_{j}}}{\textit{I}(S_{j},\theta&space;)}" title="\textbf{}\Theta _{j} = {\tfrac{argmax}{\Theta \epsilon \tau _{j}}}{\textit{I}(S_{j},\theta )}" />

    <br>

    * Objective Function _I_ takes the form of generic information gain

    <br>

    <img src="https://latex.codecogs.com/svg.image?{\textit{I}(S_{j},\theta&space;)}&space;=&space;\mathbf{{H(S{j})}&space;-&space;\sum_{i&space;&space;\epsilon&space;{L,&space;R}}^{}\frac{\left|&space;{S_{i}^{j}}\right|}{\left|&space;S_{j}&space;\right|}&space;\mathbf{{H(S_{j}^{i})" title="{\textit{I}(S_{j},\theta )} = \mathbf{{H(S{j})} - \sum_{i \epsilon {L, R}}^{}\frac{\left| {S_{i}^{j}}\right|}{\left| S_{j} \right|} \mathbf{{H(S_{j}^{i})" />
* Predictor Model: 
    * Statistics of all training points at each lead are summarized as a single multivariate Gaussian 
    <br>
    <img src="https://latex.codecogs.com/svg.image?p_{t}(v)=\frac{\pi&space;_{l(v)}}{Z_{t}}\textit{N}(\textbf{v};&space;\mu&space;_{l},&space;\Lambda&space;_{l(v)})" title="p_{t}(v)=\frac{\pi _{l(v)}}{Z_{t}}\textit{N}(\textbf{v}; \mu _{l}, \Lambda _{l(v)})" />

    <br>

* Affinity Model 
    * Need a measure of similarity 
    * Unique to manifold learning 
    * Image shows possible equations 
    * Most common & efficient model: Binary 
    * Binary Model is 0 if both points are in the same leaf, infinity otherwise 
    * Given a tree _t_ and two point **v**<sub>i</sub> and **v**<sub>j</sub> we assign perfect affinity (affinity = 1 & distance = 0) to the pair if they end up in the same cluster/leaf and null affinity and infinite distance otherwise 
    * Definition of Data Neighbourhoods: Occurs trough the maximization of an unsupervised information-theoretical objective function 
    * Forest leaves automatically define pairwise relationships between data points 
    * This makes scalable (esp. in data intensive applications where it is not tractable to do this by hand)

* Ensemble Model 
    * Collection of trees averaged to get a smoother affinity matrix 
    <br>

    <img src="https://latex.codecogs.com/svg.image?\texttt{W}&space;=&space;\frac{1}{T}\sum_{t&space;=&space;1}^{T}\texttt{W}^{t}" title="\texttt{W} = \frac{1}{T}\sum_{t = 1}^{T}\texttt{W}^{t}" />

    <br>
    * Adds robustness
    * In some trees the data points may be in the same partition, in others they may not be 


* Estimating Embedding Function 
    * **Equations not written here as they are exemplar**
    * Construct k x k normalized graph-Laplacian matrix 
    * Find the mapping function via eigen decomposition 
    * Discard the first eigenvector and arrange the rest column wise in decreasing order 
    * Mapping of **v**<sub>i</sub> to **v'** is done by reading the i<sup>th</sup> row of the eigenvector matrix 
    * Do not need to finetune any parameter or neighbourhood size 


* Previously Unseen Points 
    * Done by interpolation 
    * Uses the existing embedding 
    <br>
    <img src="https://latex.codecogs.com/svg.image?\textbf{v}'&space;=&space;\frac{1}{T}\sum&space;_{t}\frac{1}{\eta&space;^{t}}\sum_{i}^{}(e^{-Q^{t}(v,&space;v_{}^{i})}\mathbf{f(v_{i})})" title="\textbf{v}' = \frac{1}{T}\sum _{t}\frac{1}{\eta ^{t}}\sum_{i}^{}(e^{-Q^{t}(v, v_{}^{i})}\mathbf{f(v_{i})})" />
    <br>
    where,
    &eta;<sup>t</sup> = &Sigma;<sub>i</sub>e<sup>-Q<sup>t</sup>(v,v<sub>i</sub>)</sup>**f**(**v**<sub>i</sub>) is the normalizing constant and distance Q<sup>t</sup> is estimated by testing the existing tree on **v**
    * Works well for points not too far from the original training set 

 * Properties and Advantages of Manifold Forests 
    * Problem of defining pairwise distances is mitigated by using the predicted pairwise affinities 
        * Can implicitly define affinities W 
        * Higher affinity = Less distance 
    * Choosing feature space 
        * Do not have to specify features 
        * Do not have to consider representation 
        * Can select a "family" of features 
        * Discriminative / specific features automatically selected 
        * Parameters calculated to greedily to optimize information gain 
        * Position & size of partition decided by the algorithm during training 
    * Computational efficiency 
        * Bottleneck: Eigen system for large number of points 
        * Matrix formed is usually sparse 
        * Only one eigensystem formed 
        * May be computed in parallel 
        * Only d' vectors needed out of all 'k' 
    * Estimate Target Intrinsic Dimensionality 
        * Can estimate d' (if unknown) by seeing: 
            * Profile of ordered eigenvalues
            * Selecting minimum number of eigenvalues for a sharp elbow 

* Effect of Model Parameters: 
    * Forest size: Increasing forest size improves smoothness and adds robustness to noise. Averaging means that the output affinity is not binary 
    * Number of trees: A small number of trees produces inaccurate mappings, but as T increases the output manifold becomes more rectangular (In 2D)
    * Manifold Intrinsic Dimensionality: Plotting eigenvalues helps determine how many dimensions are to be included. We identify a sharp elbow in the eigenvector space in order to achieve this. Higher T means a sharper elbow. 

