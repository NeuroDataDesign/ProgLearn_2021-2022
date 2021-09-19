# Semi-supervised Classification Forests
Created: 9/19/2021

Updated: 9/19/2021

Sources:
* [Decision Forests for Computer Vision and Medical Image Analysis](https://link.springer.com/book/10.1007/978-1-4471-4929-3), Chapter 9

**Related**: 

**Tags**: #ml #ndd #trees #forest #textbook #application

* Consider traditional CV point matching as a classification problem

# 9.1 Introduction
* View sets: the set of all possible appearances of each individual object keypoint
* Extract interest points --> generate synthetic data (i.e. perspective disrortion/data augmentation) --> train classifier
* Use [[Classification Forests]] since they adapt well to multi-class problems

## 9.2 Wide-Baseline Point Matching as a Classification Problem
* $\mathcal{K}$ of K keypoints from model, used to match onto target object $\mathcal{O}$. K = -1 is points that are not a keypoint.
* $v$ is an input patch centered at a keypoint from input image

## 9.3 Keypoint Recognition with Classification Forests

### Random Classification Forests
- Recall how tree leaves store posterior probabilities: $p(c|l(t,v)) = p_t(c|v)$, meaining that $c$ is a class label and $l$ is the leaf of the tree.
- Probalities are the number of patches of class $c$ in training that reach $l$ to total number of patches that reach $l$. 
- Patch $v$ classified by average of probs:
$$\tilde{Y}(v) = \underset{c}{\mathrm{argmax}}\sum_{t=1...T}p(c|l(t,v))$$

### Node Tests
-  Binary test based on pixel intensity J of patch v at pixel location p
$$h_i(v, (p^i_1, p^i_2)) = [J(v, p^i_1) \leq J(v, p^i_2)]$$
- Run a small number of tests, since 32x32 could be $2^{19}$ possible tests

### Building the Trees
- Suggests method such that instead of picking questions according to criterion, pick a random set as in *extremely randomized trees*

## 9.4 Keypoint Recognition with Random Ferns
- Suggest that randomly choosing tests derives power from the fact that combining groups of binary tests improves classification rate
	- --> group tests into flat structure **ferns**

### Random Ferns
- See book for full derivation
- $F$ represents the $f$th fern
	- Groups are of size $S = \frac{N}{F}$, where N is the number of point comparisons we are making
- $F_f = \{h_{\sigma(f,1)}, h_{\sigma(f,2)}, ..., h_{\sigma(f,S)}\}$
	- $\sigma(f, j)$ is a random permutation function with range 1, ..., N 
- Instead of using all points in the patch, becomes a tractable problem:

$$\tilde{Y}(v) = \underset{c}{\mathrm{argmax}}\prod_{f=1}^F p(F_f|c)$$

### Training the Ferns
Each fern $F_j$ has a class conbditional probability: $p_{k,c} = p(F_j = k | c)$. However, we can simplify this. Each fern can take $K=2^S$ values, and the **goal** is to estimate the $p_{k,c}, k = 1,2,...,K$ where sum over $k$ should equal 1. After some adjustments, we use:

$$p_{k,c} = \frac{N_{k,c} + N_r}{N_c + K \times N_r}$$

where $N_r$ is a regularization term. 

## 9.5 Comparing Random Forests, Random Ferns, and SIFT
### Empirical Comparisons of Trees and Ferns
Note that a fern is kind of a simplified tree. Think of it as a tree asking the same question across the hierarchy, which means that the same feature is evaluated **independent** of the path taken.

![[Pasted image 20210919181006.png|400]]

Note that increasing fern size S or tree depth by one doubles the number of parameters (and memory) storing distributions. 
- Also needs more parameters!

Adding more ferns or trees to a classifier requires a linear increase in memory and computation for training, but results in longer run times at test.

### Empirical Compartisons Between SIFT and Ferns
Hard to compare. Timing and test matters (i.e. computing SIFT might be longer, but can be done for arbitrary images, which might be useful in many use cases.)



