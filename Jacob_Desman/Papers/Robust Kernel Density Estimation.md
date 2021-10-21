# Robust Kernel Density Estimation
Created: 2021-10-09, 23:43

Edited: 

**Tags**: 

**References:** [Scott, C.D., Kim, J.](https://www.jmlr.org/papers/volume13/kim12b/kim12b.pdf)

- This is intended as more of a stub that I will continue parsing as I need more from this paper. 

## Notes
- Code can be found here: https://web.eecs.umich.edu/~cscott/pubs.html --> https://web.eecs.umich.edu/~cscott/code/rkde_code.zip
- Running code:
	- Running demo.m immediately gives error in psi.m, since there is existing psi script in Matlab. Change psi --> PSI.m, change robkde psi.m references to PSI, change IF.m psi references to --> PSI.m

## Introduction
- Kernel density estimator (KDE)
- Understand situations where training sample is contaminated
- Consider training data following contamination model

$$X_1, ..., X_n ~ (1-p)f_0 + p f_1$$

Where $f_0$ is the density to be estimated, $f_1$ is the density of the contaminationg distribution, and $p < \frac{1}{2}$ is the proportion of contamination. 

Labels are unavailable --> unsupervised.

- Some assumptions need to be made in order to recover $f_0$
	- **Outlying**: f0 and f1 have relatively little overlap
	- **Diffuse**: f1 is not too spatially concentrated relative to f0
	- **Not abundant**: minority of data come from f1
- Methods
	- Positive semi-definite (PSD) kernel - sample mean in reproducing kernel Hilbert space (RKHS)
	- Robust kernel density estimator (RKDE) - use M-estation for robust estimation
	- Kernelized iteratively re-weighted least squares (KIRWLS) to compute the RKDE
- Motivation
	- Claim: traditional kernel density estimator is sensitive to outliers. KDE tends to overestimate density in regions where true density is low


