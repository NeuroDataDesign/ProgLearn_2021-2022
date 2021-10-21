# Initial KDG Code Investigation
Created: 2021-09-28, 11:39

Edited: 2021-09-28

**Tags**: #ndd #kdg #ml 

**References:** 

## Installing `kdg`
- Something is very clearly incorrect with my usually venv's setup, so created a new environment kdg-env
- Gives a lot of errors when I use pip or pip3 within my virtual environment, but installed fine via `python3 setup.py install`

## Verifying Installation: Run Previous Experiment
- To verify that the installation is working, before looking through the code, try replicating `benchmarks/test_on_specific_openml.py` simply by running
- Install dependencies I don't have: openml
- Issue: cannot run because `AttributeError: module 'keras.optimizers' has no attribute 'Adam'`

## Code Notes
### kdn
- fit
	- Check X_y --> restrict 2d
	- Proper args (think cat cross entropy, epochs) --> then fit
	- feature_dims = number of cols/features
	- For each label
		- Convert to data (line 74)
		- Get polytopes
		- Get the indices where that have a polytope of the current interest
		- If there is no criterion (must be 'aic', or 'bic', what happens if not? - constraint must be set)
			- Fit a Gaussian to the data points X_[idx]
			- Generate a covariance matrix
		- Else
			- Not sure what this is doing differently. Min val is `np.inf`, and so this should be larger than the constraint unless it is also infinite
		- Then assign the means and covariance matrix
- _get_polytopes
	- last activations are all X's with the current label
	- Propagate X's through network
	- Basically, use the binary_preactivation to wipe out some of the weights
	- **Not entirely sure what `polytope_memberships` looks like**
		- Expression is relatively convoluted
- _compute_pdf
	- Given a label and polytope index, find the associated mean and covariance
	- Compute a normal distribution
	- Compute the pdf given the X data

