### Chapter 6: Density Forests

Goal: Given some observed unlabeled data which we
assume have been generated from an underlying probabilistic density function, we
wish to estimate the unobserved generative model itself

### 6.1 Density Estimation in the Literature

Gaussian mixture model (GMM)

### 6.2 Specializing the Decision Forest Model for Density Estimation

Density Estimation Task: Given a set of unlabeled observations and estimate the probability density function from which such data have been generated  

* Input data: multi-dimensional feature vector **v** = (x1, x2, ..., xd) &epsilon; ℝd
* Output: p(v) >= 0, such that: /int/p(v)dv = 1

Density forest: Collection of randomly trained density trees
* multiple hard
clustered data partitions are created, one for each tree. (This is in contrast to the
single soft clustering generated by the EM algorithm.)
* Forest posterior is the combination of tree posterior


#### Training Objective Function: 

* Given a collection of points S0 = {v} (No labels)
* Each individual tree was trained independently
* Randomized node optimization 
* Optimize the jth split node (eq 6.1)
    

generic information gain I (eq 6.2)

Entropy for a generic set S of training points (nsupervised entropy): (eq 6.3)

Information Gain reduces to: (eq 6.4)

* By maximizing info gain, the tree training procedure tends to split the
original dataset S0 into a number of compact clusters
* Centers of clusters are in areas of high data density, while the separating surfaces are placed along regions of low density 
* an assumption of Gaussian distribution at the nodes (not realistic but syields a simple and efficient objective function)
* Hierarchy of trees --> construct very complex distributions
by mixing the individual Gaussians base functions associated at the leaves

#### Prediction model 
* The set of leaves in the tth tree in a forest defines a partition of the data (eq 6.5)
* single multivariate Gaussian distribution N(v;μl(v), Λl(v)) estimated
here via maximum likelihood (eq 6.6)

* to ensure probabilistic normalization --> incorporate the partition function Zt (eq 6.7)

    * Each data point reaches exactly one terminal node 
    * Conditional p(l|v) is a delta function (eq 6.8)
    * Computing Zt in high dimensions may be challenging
    * Axis-aligned weak learners:
        * Can compute partition function by cumulative multivariate normal distribution function 
        * Partition function Zt is the sum of all volumes subtended by each Gaussian, cropped by its associated partition cell 
        * No closed form solution
    * Complex weak learners
        * Zt is easier to approximate by integration over a regular grid 
        * Consider points in a finite regular grid with uniform spacing --> add up 
        * General smaller grid cells -> yield more accurate approximations of the partition function at a greater computational cost

#### Ensemble model
* Average of all tree densities (eq 6.10)
* induces a uniform “mixing” across the different trees
* Expectation Maximization (EM) / greedy information gain maximization criterion

    
### 6.3 Effect of Model Parameters: 
* Tree Depth: Deeper trees create further splits and smaller Gaussians --> overfitting (noise)
* Forest size: Increasing forest size improves smoothness and generalization (even if individual trees overfit)
* A larger forest helps accommodate for if individual trees over-fit more, which is in part due to the randomness of tree density estimation


### 6.4 Comparison with alternative algorithms
* k-nearest neighbor density estimation - RF produces a smoother outcome
* efficiency - despite the added richness in the hierarchical structure of the density forest, its sampling
complexity is very much comparable to that of a random-restart GMM
* Randomness --> better results, whether it be randomness from the forst model or Gaussian mixture

