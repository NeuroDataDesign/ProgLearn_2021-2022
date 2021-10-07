# Chapter 1: Overview and Scope

This book provides a model of decision forests, unifying many different learning tasks including regression, classification, density estimation, and learning under a single decision-forest based framework with only minimal adaptations to each use-case.

The original learning method involved simple D-ary (frequently binary) decision trees, which were useful but struggled with high-dimensional data.
The development of ensembling (ex: boost) allowed algorithms to process high-dimensional data using many weak learners.
Ensembling decision trees gives rise to decision forests.
Randomization (in the form of randomized feature partitioning, bagging, and noise injection) turns decision forests into random forests, which are widely used in tasks such as image analysis - including the Kinect!

# Chapter 2: Notation and Terminology

This chapter provides a list of notation used in the book as well as synonymous terms.

# Chapter 3: Introduction: The Abstract Forest Model 

Types of task, by output:
- Classification: assign discrete categorical label based on input
- Regression: take input and calculate continuous output as a function of said input
- Density estimation: take input and run through probability density function to detect unusual areas
- Manifold learning: correlate multiple variables
- Image segmentation: with supervision, user's brush strokes define labeled area/polytope, and everything else is unlabeled
- Active learning: acquire expect annotation/labeling with minimal manual input

Decision forests are best at classification, but Criminisi and Shotton argue they can be applied to all of these tasks.

For the purposes of this book, focus only on binary decision trees: directed graph where each node has 1 input and max 2 outputs.

### Decision Trees

At each branch, implement the following:

*h*(**v**, **&theta;**<sub>j</sub>): *R*<sup>d</sup> × *T* → {0, 1} = where:
- *R*<sup>d</sup> is a d-length vector of real numbers
- *T* is the subspace of all possible split options (all possible combinations of features we can split on)
- **&theta;**<sub>j</sub> ∈ *T* are the split parameters associated with node j
- **v** is our input vector of size *R*<sup>d</sup>, containing d features

At any point, we'll extract a subset of features **φ(v)**, since **v** may be of prohibitive size.

We will train our decision trees on a set of datapoints (**v, y**) where y is the known "true" label for point v. The tree will optimize to correctly sort these points. At each branch, the tree will send a disjoint subset down each of its two children.

It's good to stop early - at a set depth, when the number of points in a branch falls below a certain threshold, etc.

The simplest way to divide data is across a **φ**-dimensional line. Even with very high-dimensional data, **φ** = 2  may suffice. This line may be linear or curved.

After each split, we gain some information about our dataset as denoted by a loss in entropy/uncertainty.

Each leaf node can be considered to represent a posterior probability p(**y|v**) - what is the probability our datapoint is in **y**, given **v**?

We would also like to inject randomness: either with bagging (randomly subsetting our data, with replacement), randomization of our split (optimize over subset *T*<sub>j</sub> ∈ *T*), or altering the nature of our dividing line.

### Random Forests

A random forest is an ensemble of randomly trained decision trees. These trees will perform better than any individual tree. Ideally trees should be correlated as little as possible.

Trees can be ensembled by summation or multiplication of the posteriors. Larger forests result in more accurate tests. Very unbalanced trees should be avoided.
