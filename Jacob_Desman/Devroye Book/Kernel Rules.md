# Kernel Rules
Created: 2022-02-02, 12:49

Edited: 

**Tags:** #book #chapter 

**References:** [[Probabilstic Theory of Pattern Recognition]]

## Kernel Classification Rule
$$g(x) = 0 if \sum_{i=1}^n I_{Y_i = 0}K(\frac{x-X_i}{h}) \geq \sum_{i=1}^n I_{Y_i = 1}K(\frac{x-X_i}{h})$$

Here, h is the **bandwidth**

## Consistency
- Kernel-based rules have strong universal consistency under general conditions on $h$ and $K$
- Let $h > 0$ be a smoothing factor dependent on $n$ and $K$ is a kernel function


### Definition
Kernel K is regular if it nonnegative, and there is a ball $S_{0, r}$ of radius $r > 0$ centered at the origin, and constant $b > 0$ such that $K(x) \geq b I_{S_{0, r}}$ and $\int sup_{y \in x + S_{0, r}} K(y)dx < \infty$

### Theorem 10.1 (Devroye and Krzyzak (1989))
Assume that $K$ is a regular kernel. If $h \rightarrow 0$ and $nh^d \rightarrow \infty$, then for any distribution of (X, Y) and for every $\epsilon > 0$ there is an integer $n_0$ s.t. for $n > n_0$ for the error probability $L_n$ of the kernel rule

$$P[L_n - L^* > \epsilon] \leq 2 e^{-n \epsilon^2 / (32 \rho^2)}$$

where $\rho$ depends on kernel K and the dimension only. Therefore kernel rule is strongly universally consistent. 

## Proof of Consistency Theorem
See book for proof