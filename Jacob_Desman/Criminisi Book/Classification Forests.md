# Classification Forests
Created: 9/7/2021

Updated: 9/7/2021

Sources:
* [Decision Forests for Computer Vision and Medical Image Analysis](https://link.springer.com/book/10.1007/978-1-4471-4929-3), Chapter 4

**Related**: [[Abstract Forest Model]]

**Tags**: #ml #ndd #trees #forest

## 4.2 Specializing the Decision Forest Model for Classification
Goals:
1. Given $v$, infer $c \in C$
2. Find some mapping for a set of training data and labels which functions similarly for some unseen test data. 

Optimize parameters of weak learner at node $j$ and use discrete information gain as objective function (see [[Abstract Forest Model#Energy Models|abstract version]]):
$$\theta_j = \underset{\theta \in T_{j}}{\mathrm{argmin}} I(S_j, \theta)$$

$$I(S_k, \theta) = H(S_j) - \sum_{i\in \{L,R\}} \frac{S^i_j}{S_j}H(S^i_j)$$

$$H(S) = - \sum_{c \in C} p(c)\log(p(c))$$

Note that class rebalancing via resampling is helpful during training.

Randomness is injected by *randomized node optimization* with $\rho = |\mathcal{T}_j|$ --> sample some number of **features** before training that the $j$th node.

Get probabilistic output by averaging the posterior for that leaf across all trees:
$$p(c|v) = \frac{1}{T} \sum^T_{t=1} p_t(c|v)$$

## 4.3 Effect of Model Parameters
### Forest Size on Generalization
Each tree is *overconfident*, but more forests --> better generalization

### Multiple Classes and Noise
Decision trees can easily convert to handle multiclass problems. Also, noise and further distance from training distribution increase uncertainty.

### Tree Depth
Deeper trees ($\uparrow$D) tend to overfit, but too shallow trees produced low-confidence posteriors. 

D is a function of problem complexity.

### Weak Learners
Choice of weak learner matters! Think axis-aligned vs. oriented line vs. conic section.

### Randomness
Lower $\rho$ increases randomness and lowers tree correlation within forest.

## 4.4 Maximum Margin Classifications with Forests
Why cover this? People love SVMs since it draws some sort of hyperplane to enforce maximum margin between classes.

If a forest uses many params ($\mathcal{T_0}$ is large) then separating line tends to be within the gap.

### Randomness on Optimal Separation
Lower $\rho$ increases randomness and causes posteriors to be more spread out --> less well defined separating surface.

