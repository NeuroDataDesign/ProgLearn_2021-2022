# Supervised Contrastive Learning

Dante Basile

## Extend contrastive loss to the supervised setting
* Take label information into account
* Images with the same label are positive pairs
* Now there are many positives per anchor
* New loss function:

$$\mathcal{L}_{\textrm{out}}^{\textrm{sup}} = \sum_{i \in I} {\mathcal{L}_{\textrm{out, i}}^{\textrm{sup}}} = \sum_{i \in I} {\frac{-1} {|P(i)|} \sum_{p \in P(i)} {\log{\frac{\textrm{exp}(z_i \cdot z_p / \tau)} {\sum_{a \in A(i)} {\textrm{exp}(z_i \cdot z_a / \tau)}}}}}$$

$$\mathcal{L}_{\textrm{in}}^{\textrm{sup}} = \sum_{i \in I} {\mathcal{L}_{\textrm{in, i}}^{\textrm{sup}}} = \sum_{i \in I} {-\log{\texttt{\{} \frac{1} {|P(i)|} \sum_{p \in P(i)} { \frac{\textrm{exp}(z_i \cdot z_p / \tau)} {\sum_{a \in A(i)} {\textrm{exp}(z_i \cdot z_a / \tau)}}}} \texttt{\}} }$$

* Normalize by set of positives inside or outside of the log
* Encourages encoder to give similar representations throughout a class
* `out` upper bounds `in` and is the superior loss function
    * Multiplying by the normalizing factor inside the log is equivalent to addition and has no effect on the gradient

## Achieve best reported ImageNet accuracy for the ResNet-200 architecture

## First contrastive loss to consistently outperform cross-entropy in large-scale classification