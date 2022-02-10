Our goal is to calculate factors A and B to adjust polytopes from KDN1 to fit the dataset X2, y2. We do this with MLE.

Briefly,

    Given a set of data X, with labels 0, 1,....n and a previous polytope p
    p_hat = A * p + B where A, B are scalars
    We want to maximize the likelihood that p_hat only contains points from 1 label k, and that the points are as close to the mean as possible?
    Recount polytope samples to determine which data points are "in" this polytope by... checking which mean it's closest to within +/- stdev (sqrt(variance))? np.argmax([1/distance. if distance > sdev, distance == 0], axis = labels)
    rescale covariances by new_size/old_size (so use k-Nearest-Neighbors?)

Finally, when calculating likelihood for each label in the test set, use new size (with X2 training datapoints) and multiply by confidence (% of X2 points in polytope with the matching label)

We want to calculate and save the following outputs

    A: Double, multiplier [1 x n_polytopes]
    B: Double, additive [1 x n_polytopes]
    Size: Integer, [n_labels x n_polytopes]

Confidence is calculated as size[label, polytope]/np.sum(size[:, polytope]) and does not need to be saved independently after calculations are finished.

Size doesn't matter - we want the highest MAX likelihood, not the highest MEAN likehihood - it's fine if the polytope is small as long as it is exclusive.
