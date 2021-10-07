# Real Data Empirical Performance
- SPORF performs better than RF, XGBoost, RR-RF, and CCF on benchmarks from UCI machine learning repository
- Default $\lambda$ and $d$ default values good for use out of the box, especially those not familiar with details of algorithm.
- SPORF performs best when faced with high-dimensional noise. CCF performs close when there is no noise but degrades when noise added.
# Computational Efficiency and Scalability
- Time complexity for constructing random forest where $T$ is number of trees, $n$ is number of training data, and $d$ is number of features: $\mathcal{O}(Tdn\log^2 n)$
- SPORF time complexity: $\mathcal{O}(Tdn\log^2 n + Tdnp\lambda$
- Single tree space complexity: $\mathcal{O}(np)$
- SPORF space complexity: $\mathcal{O}(T(np + c))$
- Storage complexity of SPORF: $\mathcal{O}(Tnz)$.
