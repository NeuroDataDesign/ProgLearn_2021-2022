# Chapter 8: Semi-Supervised Classification Forests

Source: [Decision Forests for Computer Vision and Medical Image Analysis](https://link.springer.com/book/10.1007/978-1-4471-4929-3) Chapter 8

Goal: Transfer ground truth labels to the unlabeled and already available data 
<br> 
This is an example of **transductive learning**. The other forms seen so far are **inductive**. 

<br>

## Aims of Transductive Classification 
<br> 
* Keep different known class labels in different regions 
* Ensure that classification boundaries are in areas of low density 

<br> 

Here we use decision forests to perform: 
* Transductive classification 
* Build an inductive classifier on top of a trained transductive one 

## **Specializing the Decision Forest Model for Density Estimation**

<br>

> Semi-Supervised Classification Task: Given a set of both labeled and unlabeled data points, we wish to associate a class label to all the already available unlabeled data points 

<br> 

* Unlabeled data can be used as test 
* Desired o/p is discrete, unordered, categorical 
* Given an input point **v**, we want to find a discrete class label _c_ 
* Types of inputs data: **v**<sup>l</sup> (labeled) and **v**<sup>u</sup> (unlabeled)

* Training Objective Function 
    * Optimize parameters of each internal node _j_ via: 
            <br>

    <img src="https://latex.codecogs.com/svg.image?\textbf{}\Theta&space;_{j}&space;=&space;{\tfrac{argmax}{\Theta&space;\epsilon&space;\tau&space;_{j}}}{\textit{I}(S_{j},\theta&space;)}" title="\textbf{}\Theta _{j} = {\tfrac{argmax}{\Theta \epsilon \tau _{j}}}{\textit{I}(S_{j},\theta )}" />

    <br>

* Objective Function _I_ must encourage 
    * Separation of training data 
    * Separation of different high density regions 
    * Done by maximizing the mixed information gain, given by: 

    <br> 
    <img src="https://latex.codecogs.com/svg.image?I(S_{j},&space;\theta&space;)&space;=&space;I^{\texttt{u}}(S_{j},&space;\theta&space;)&space;&plus;&space;\alpha&space;I^{\texttt{s}}(S_{j},&space;\theta&space;)" title="I(S_{j}, \theta ) = I^{\texttt{u}}(S_{j}, \theta ) + \alpha I^{\texttt{s}}(S_{j}, \theta )" />

    <br> 
    where: 
    * I<sup>s</sup> is the supervised term (depends on labeled training points only)
    * I<sup>u</sup> is the unsupervised term (depends on all data points)
    * &alpha; is a scalar, user-defined parameter that specifies the relative weight between the two terms 

    * I<sup>s</sup> is an information gain defined over discrete class distributions
    <br>
    <img src="https://latex.codecogs.com/svg.image?I^{\texttt{s}}(S_{j},&space;\theta&space;)&space;=&space;H(_{}\widetilde{S_{j}})&space;-&space;\sum_{i\epsilon&space;\left\{L,R&space;\right\}}^{}\frac{\widetilde{S_{j}^{i}}}{\widetilde{S_{j}}}H(\widetilde{S_{j}^{i}})" title="I^{\texttt{s}}(S_{j}, \theta ) = H(_{}\widetilde{S_{j}}) - \sum_{i\epsilon \left\{L,R \right\}}^{}\frac{\widetilde{S_{j}^{i}}}{\widetilde{S_{j}}}H(\widetilde{S_{j}^{i}})" />
    <br>

    * I<sup>u</sup> is the unsupervised gain term, defined as differential entropy of a multivariate Gaussian density 
    <br>
    <img src="https://latex.codecogs.com/svg.image?I^{\texttt{u}}(S_{j},&space;\theta&space;)&space;=&space;log\left|&space;\Lambda&space;(S_{j})\right|&space;-&space;\sum_{i\epsilon&space;\left\{&space;L,&space;R\right\}}^{}\frac{|S_{j}^{i}|}{|S_{j}|}log\left|&space;\Lambda&space;(S_{j}^{i})\right|" title="I^{\texttt{u}}(S_{j}, \theta ) = log\left| \Lambda (S_{j})\right| - \sum_{i\epsilon \left\{ L, R\right\}}^{}\frac{|S_{j}^{i}|}{|S_{j}|}log\left| \Lambda (S_{j}^{i})\right|" />
    <br>


## **Transduction Trees for Classifying Already Available Data**

<br>

* Label transduction from annotated data to unannotated data can be achieved directly via the following minimization: 
    <br>
    <img src="https://latex.codecogs.com/svg.image?\textit{c}(\mathbf{v}^\texttt{u})&space;\leftarrow&space;c&space;(argmin:&space;v^l&space;\epsilon&space;L)Q(\mathbf{v^\texttt{u}},&space;\mathbf{v^\texttt{l}})&space;\forall&space;\mathbf{v^\texttt{u}&space;\epsilon&space;U" title="\textit{c}(\mathbf{v}^\texttt{u}) \leftarrow c (argmin: v^l \epsilon L)Q(\mathbf{v^\texttt{u}}, \mathbf{v^\texttt{l}}) \forall \mathbf{v^\texttt{u} \epsilon U" />
    <br>
    where, c is the class index associated with a point in the set of labeled data

* Generic Geodesic distance Q: 
    <br> 
    <img src="https://latex.codecogs.com/svg.image?Q(\mathbf{v^\texttt{u}},&space;\mathbf{v^\texttt{l}})&space;=&space;(min:&space;\Gamma&space;\epsilon&space;G)\sum_{i=0}^{\left|&space;\Gamma&space;\right|&space;-&space;1}&space;d(s_{i},s_{i&plus;1})" title="Q(\mathbf{v^\texttt{u}}, \mathbf{v^\texttt{l}}) = (min: \Gamma \epsilon G)\sum_{i=0}^{\left| \Gamma \right| - 1} d(s_{i},s_{i+1})" />
    <br>

    where, 
    * &Gamma; : geodesic path
    * |&Gamma;| : path length 
    * _G_ : Set of all possible geodesic paths 
    * Initial point: **s**<sub>0</sub> = **v**<sup>u</sup>
    * End point: **s**<sub>|&Gamma;|</sub> = **v**<sup>l</sup>

* Local distance d are defined by the symmetric Mahalanobis distances 
    <br> 
    <img src="https://latex.codecogs.com/svg.image?d({s_{i},s_{j})&space;=&space;\frac{1}{2}(d_{ij}^\top&space;\Lambda&space;_{l(v_{i})}^{-1}d_{ij}&space;&plus;&space;d_{ij}^\top&space;\Lambda&space;_{l(v_{j})}^{-1}d_{ij})" title="d({s_{i},s_{j}) = \frac{1}{2}(d_{ij}^\top \Lambda _{l(v_{i})}^{-1}d_{ij} + d_{ij}^\top \Lambda _{l(v_{j})}^{-1}d_{ij})" />
    <br>
    where, 
    * d<sub>ij</sub> = s<sub>i</sub> - s<sub>j</sub>
    * &Lambda;<sub>l(v<sub>i</sub>)</sub> = covariance associated with leaf reached by point v<sub>i</sub> in the t<sup>th</sup> tree

    * Mahalanobis discourages paths from cutting across regions of low data density 
    * All points on leaf have the same Gaussian, therefore can approximate label by acting on leaf cluster instead of acting on separate points 

* Label assignment 
    * Each individual tree produces a distribution 
    * Given by p<sub>u</sub><sup>t</sup>(c|v<sup>u</sup>)
    * Defined for existing unlabeled data points in U

* Transductive Ensemble 
    * Transductive labels assigned to a point v<sup>u</sup> are (generally) different for each tree
    * More stable for points closer to the original supervised data points 
    * Average the posteriors from all trees 
* Induction after Transduction 
    * It is possible to just use the created trees 
    * Include the propagated values + original values
    * We now have a set of partitions which is effectively trained on 'all available data' 
    * Therefore can now find posteriors for the leaves
    * Averaging across trees will give probability for each leaf

    <br>


## **Examples, Comparisons & Effect of Model Parameters**

<br>

* Active Learning 
    * May annotate additional points at low confidence regions 
    * The confidence of prediction decides which additional data should be annotated
* Comparison with Transductive SVMs
    * Forests capture uncertainty 
    * SVM produces hard, binary classification
* Multiple Classes
    * Hierarchical structure
    * Handles both 2-class & multiple class problems effectively 
    * Regions of low confidence = Regions of low data density 
    * Largest amount of labeled data + Deepest trees = Best fit to annotated data
* Effect of Tree Depth 
    * More depth / More supervision = more confidence + accuracy
    * More manually annotated data at central region = Better dilineation of each individual spiral arm 
    
