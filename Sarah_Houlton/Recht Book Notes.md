[Recht Book Notes](https://mlstory.org/rl.html)

# Reinforcement learning problems
* a strategy is to estimate a predictive model for the dynamical system and then use the model as if it were the true model in the optimal control problem
# Certainty equivalence
* we have an optimization problem w/ unknown value
* we can estimate value
* use a point estimate as the true value
# Exploration-exploitation tradeoffs
* Pac-error
  * useful when we spend all of our time learning about a system
  * want to know how suboptimal our soln will be when built from what we've got so far
* regret
  * online execution
  * we evaluate reward accrued at all time steps, even if we are spending that time probing the system to learn about its dynamics
* one major way regret differs from PAC
  * policy can change w/ each time steep
* these metrics don't promise a good model
# multi-armed bandits
* we assume no state
  * k total actions
  * reward is a random fn of which action you choose
* inspired by gambling on slot machines
* k slot machines
  * each slot machine has some probability of paying when you play it
  * want to find the machine with the best chance of paying out, then only play that one
* we want to find the action corresponding to the largest mean
  * try each action N/K times and compute the empirical return
* explore-then-commit
  * given time horizon T
  * we spend the first m time steps searching for the best return
  * we choose this action for the remaining T-m time steps
  * at round t, we aplpy action k, the expected gap btwn our policy and the optimal policy is gradK
# Interleaving exploration and exploitation
* for a variety of practical concerns, it would be preferable to interleave exploration with exploitation
* succesive elimination
  * try all actions m times
  * drop actions that are performing poorly
  * try remaining actions 4m times, drop poorly performing actions, repeat
* optimism in the face of uncertainty
  * bet on the best
  * at iteration t, take all of the observations so far and form a set of upper confidence bounds
  * we maintain a set where we have confidence our true model lies
  * either we get the right model in which case we get a large reward, or
  * we learn quickly that we have a suboptimal model and we remove it from our set S
# Contextual bandits
* transition - from mult-armed bandits to reinforcement learning
* convenient way to abstractly model engagement problems on the internet
* whatever the reward is, the goal is to maximize the totla reward over time
* greedy algorithm avoids initial random exploration and instead picks whatever is optimal for the data so far
# Approximate dynamic programming
## Certainty equivalence
* estimate dynamics from some data and then use this estimated model as if it were true
## Q-learning
* attempts to solve value iteration using stochastic approximation
* Q = (1-n)Qold + n(R + YmaxQold)
* only needs data generated by Qold
* doesn't need to know the reward fn
* often called model-free
* makes an inefficient use of samples
