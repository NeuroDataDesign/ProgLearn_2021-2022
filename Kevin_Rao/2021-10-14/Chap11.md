* Implicit shape model: set of interest point descriptors for a given class
  * Each entry assigned set of offsets with respect to centroid
  * Interest point descriptors in image matched against codebook and probabilities generated for possible positions of object and summed into Hough image.
* ISM integrate information from large number of parts nad have good generalization by combining observations from different training examples
  * Codebook-based Hough transform has significant computational price due to high space to have good discrimination and solving of large-scale clustering problems
* Hough forests
  * Set of leaf nodes in tree treateed as disciminative code book. Each node decides if a patch of image is part of an object or background and casts probabilistic vote
  * Trees optimize voting performance; leaves produce votes with small uncertainty
  * Tree based on collection of patches from training data
  * Short training time and little overfitting
  * Efficient at run time
  * Tolerates labeling noise and errors in training data.
* Generative codebooks for ISM are unsupervised but each tree in Hough forest are constructed in a supervised way, allowing for optimization of codebook entries to produce better votes in Hough space
* Hough forests involves predicing a continuous variable to identify the patch beloning to an object and a discrete variable to identify the class.
  *   Hough forests trained to the above objectives and computing $p(c|\mathbf{v})$ and $p(\mathbf{y}|c, \mathbf{v})$ where $\mathbf{v}$ is the appearance vector of a patch, $c$ si the class label of the patch, and $\mathbf{y}$ is the offset vector of the patch relative to the centroid of the object.
* Each tree based on a set of training patches sampled from collection of training images containing examples of interest in known areas.
  * Each leaf contain information of patches that reach that node, storing proportion of object patches of a particular class and the offset vectors corresponding to those patches.
* While training, non-leaf nodes assigned binary test for the appearance of the patch.
* Trees are constructed recursively from the root where a node becomes a leaf when its depth is equal to the maximum or the number of patches it holds is small.
  * Label objective optimized for using Shannon entropy
  * Displacement vector optimized using variance
* Binary test
  * : generate pool of pixel tests sampling five parameters uniformly
  * Choose random handicap value
  * Randomized decision made to split that optimizes the objective function
* Hough transform localizes bounding boxes for instance of a class
  * Given a patch centered at a position $\mathbf{p}$.
  * $E(\mathbf{q})$ is the random event corresponding to the existence of the object centered at location $\mathbf{q}$.
  * Want to compute probabilistic evidence $$p(E(\mathbf{q})|\mathbf{v}(\mathbf{p}))$$ that the appearance of the patch brings about availability of $E(\mathbf{q})$ at different positions in the image.
  * The probability of a tree is a gaussian distribution of the difference between $p$ and $q$ normalized by the number of offset vectors collected in the leaf.
  * The overall forest estimate is the average coming from the trees.
* Scale variations handled by rescaling image to different vactors and computing Hough images at each scale. They are stacked into a 3D scale frustrum, Gaussian filtered across the scale dimension, and maxima of functions localized.
* Leaves pruned with low class confidence
