A polytope is any n-dimensional geometrical object with flat sides.

Each node of random forest division can be seen as splitting the data along some n-dimensional polytope where N is the number of features in the dataset, or the subset we are examining at this node. Items within the polytope go down branch A, while items outside it go down branch B.

KDG represents polytopes as a set of means and covariates.

Note: Go through the math to understand how these polytopes are used.

Note: kdf relies on sklearn.covariance.LedoitWolf to compute the covariant model, see:

“A Well-Conditioned Estimator for Large-Dimensional Covariance Matrices”, Ledoit and Wolf, Journal of Multivariate Analysis, Volume 88, Issue 2, February 2004, pages 365-411.
