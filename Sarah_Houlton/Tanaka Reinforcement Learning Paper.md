[Lifelong Reinforcement Learning Paper](http://www.isi.imi.i.u-tokyo.ac.jp/~f-tanaka/paper/Tanaka_EWLR-97.pdf)

# Setup
* n different environments are n tasks
* They use stochastic gradient descent
  * We would replace with q-learning
  * The reinforcement part is the same
  * The reward is different
# Process
* Select an action
* calculate eligibility
* calculate history (eligibility trace)
* if reward, update weights according to history
  * This update would differ in our q-learning
# Bias
* average weight -> initial bias
* dispersion of weights -> learning bias
* initial bias is used as initial value for neural network of the nth task
* bias is oriented to reduce costs
* learning bias is used in stochastic algorithm as tuning parameter for learning rate (a) of each weight
* W = W + aB[i,j](1 - Y)gradW(t)
* Experiment 1 - both biases is best result
* Not using initial bias largely increases startup costs
