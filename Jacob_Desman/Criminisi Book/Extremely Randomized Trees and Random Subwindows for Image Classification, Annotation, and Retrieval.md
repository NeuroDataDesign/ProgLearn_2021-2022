# Extremely Randomized Trees and Random Subwindows for Image Classification, Annotation, and Retrieval
Created: 9/19/2021

Updated: 9/19/2021

Sources:
* [Decision Forests for Computer Vision and Medical Image Analysis](https://link.springer.com/book/10.1007/978-1-4471-4929-3), Chapter 10

**Related**: 

**Tags**: #ml #ndd #trees #forest #textbook #application #classification #segmentation #retrieval

Essentially, a framework for extracting subwindows for solving image classification, segmentation, retrieval, and interest point problems. 

## 10.1 Introduction
Authors are motivated to create generalized frameworks that do not rely on strong handcrafted/researched assumptions about patterns or acquisition conditions.

## 10.1 Random Subwindow-Based Image Analysis
**Problem statement**: From some set of labeled images $J_i, Y_i$ with N images, co9nstruct a function $\hat{y} : \mathcal{J} \leftarrow \mathcal{Y}$ that successfully works for any new test image $J_{\mathrm{test}}$.
- This includes classifciation, regression, image annotation, or segmentation. 

Traditional supervised learning (SL) needs training sets with fixed vector sizes (many images are of different sizes), but even if you rescale, what features do you use? One could use pixels, but most methods need features that describe the relationships between them. Thus, what features do you use? Do you use domain knowledge to construct them, or make a set so large that it is likely to encompass the problem? 

The authors propose a method that extracts a large number of random subwindows --> use a fixed number of features --> compute output prediction by combining subwindow predictions

### Training Stage
- **Subwindow extraction**: $i = 1, ..., N_{sw}$. $s_i \in J$, representing possible overlapping subwindows within parent image. 
	- Higher $N_{sw}$ is often better. 
	- Can uniform sample or assert a prior (ex. to account for class imbalance)
- **Subwindow transformations**: To make model invariant to some variations, consider a new set of subwindows $\{s'_1, s'_2,..., s'_{N_{sw}}\}$ that are transformed
- **Feature extraction**: feature vector computed for each window. $v(s) = (x_1(s), ..., x_d(s)) \in \mathcal{F}$
- **Output computation**: $y_{sw}$ associated with each window. 
- **Training**: some method to acquire a prediciton model $\hat{y}_{sw}(\cdot)$

### Prediction Stage
- Extract subwindows, transform subwindows, extract feratures. Ideally, extract a maximal number of subwindows $N_{sw, \mathrm{test}}$
- **Per-subwindow output computation**: get prediction $\hat{y}_{sw}(v(s))$ for all subwindows
- **Aggregate output**:  over all subwindows, $\hat{y}_{\mathrm{aggr}}(J_{\mathrm{test}}) \in \mathcal{Y}$. Procedure is highly variable

### Subwindow Discussion
#### Extraction
- $N << N_{sw}$
- Overlap is good --> reduce variance
- Subwindow size is important hyperparameter
	- Can use cross-validation to find optimal size from training data
	- Can randomize subwindows during extraction --> rescale. Introduces scale invariance

#### Transformation
- Goal is to inject invariance into model
- Ex. scale to fixed size
- Or use transformation operator $O(s, \lambda)$ --> could be rotation, could be masking, etc. 

## 10.3 Extremely Randomized Trees
### Extremely and Totally Randomized Trees
- No subsambling is used
- Split functions are limited to axis-aligned splits (binary splits): $h(v,(i,\tau)) = [x_i < \tau]$.
	- Parameterized by attribute number $(1 \leq i \leq d)$ and discretization threshold $\tau \in \mathbb{R}$
- Split function optimization
	- Set of random candidate splits $\mathcal{T_j} = \{(i_1, \tau_1), ..., (i_\rho, \tau_\rho)\}$ at node $j$. 
	- Essentially, $\rho$ feature and discretization threshold pairs.
	- $i_l$ sampled uniformly and without replacement from $d$ features. 
	- Discretization thresholds $\tau_l$ are drwan between the min/max values of features $i_l$ in training instances that have reached the node. 
	- Can grow until constant output/feature vector or until instances that reach a node is less than a param $n_{\mathrm{min}}$
- Considerations
	- Number trees, T
	- Number of inputs randomly selected at each node $\rho$ 
	- Stoppiung criterion parameters $n_{\mathcal{min}}$

$\rho = 1$ means only one random split considered at each node --> randomization is pushed further, hence the name *totally randomized trees*. Less robust to noise, but fast to construct.

### Multiple Output Trees
Can basically associate a vector (for regression) or a multi-class output (classification) by 
1. Modifying the objective function used to evaluate splits - sum the individual objective functions for each output
2. Modify the predictions at the leaves. Either output vectors or $n$ conditional class probability distributions for the $n$ respective outputs

### Kernel View of Tree-Based Ensembles
Kernel ~ similarity metric.

$k_t(v, v') = \frac{1}{N_L}$ if v and v' reach the same leaf L in t, and 0 otherwise. 

$$k_{\mathrm{ens}} = \frac{1}{T} \sum_{t=1}^T k_t(v, v')$$

Basically, two examples are considered similar if they are considered similar by *a large portion of the trees*. This is highly infleunced by the $n_{\mathrm{min}}$ parameter, since more training examples tend to fall in a leaf --> higher similarity measure. 

Similarity from before dsecribes measure between subwindows, and derives a similarity between images $J$ and $J'$ as follows:

$$k(J, J') = \frac{1}{|\mathcal{S}(J)| |\mathcal{S}(J')|a} \sum_{s \in \mathcal{S}(J), s' \in \mathcal{S}(J')} k_{\mathrm{ens}}(v(s), v(s'))$$

- $S(J)$ and $S(J')$ are sets of transformed subwindows
- Similarity is average similarity between all pairs of subwindows describes by features

## 10.4 Applications
### Content-Based Image Retrieval
Window based similarity and indexing from subwindows to essentially query for similar images.

### Image Classification
Bag of visual words, and then SVM to classify.

### Interest Point Detection
Basically tries to determine if subwindows are actually close to the point of interest, thus allowing it to be binary classification for any subwindow. Predicted point within new image is the median point of all subwindows central pixels that are predicted to be the interest point. 

### Image Segmentation
Did pixel-wise segmentation. 
- Dense sampling of random subwindows
- Approach 1: output associated to each subwindow is class of central pixel
- Approach 2: output of subwindow consists of classes of all subwindow pixels predicted pointly by a multiple [[Extremely Randomized Trees and Random Subwindows for Image Classification, Annotation, and Retrieval#Multiple Output Trees|multiple output model]].
	- Class prediction is obtained for each image pixel by averaging predictions for all subwinodws that contain that pixel. 


## 10.5 Coinclusions and Future Works
There are many uses for trees.

