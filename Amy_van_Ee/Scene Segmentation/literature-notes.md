The papers below were recommended by Jovo to get background on Scene Segmentation.

# A stochastic grammar of images
**Song-Chun Zhu, David Mumford**

http://www.stat.ucla.edu/~sczhu/papers/Reprint_Grammar.pdf

**Abstract**
- Grammar of images includes four objectives
  -  the grammar represents hierarchy of decomposition (objects, pixels) of images as nodes and spaital relations as horizontal connections between nodes
  -  And-Or graph representation, where Or-nodes refer to sub-configurations and And-nodes to components
  -  This representation is used to define a probabilistic model
  -  Visual dictionaries to help connect symbols and raw signals

**Introduction**
- The Hibernation and Resurgence of Image Grammars
  - Image parsing is analogous to understanding language, as we decompose an image into parts, objects and see the functional and spatial relations between nodes 
  - There are many challenges in this field
    - very much visual knowledge necessary, such as being aware of so many differnet types of objects
    - big obstacle is the waekness in top-down inference
    - there is very large computational complexity involved, as one image can contain many objects
      - human processes of edge detection and scene classification are very fast, unlike current pattern recognition and learning algorithms
    - to make this scalable, the algorithm must bebased on simple proecdures
    - there is a semantic gap between what the raw pixels are and what objects they represent symbolically - it is difficult to reliably get the representation of an object from just the pixels
    - with grammar, we can have a more consistent mathematical framework, better apperance models to connect symbols to pixels, more powerful algorithms, and many realistic training and testing datasets

- ... (will add on)


# Deep learning in radiology: now the real learning begins
**Carolina Lugo-Fagundo, Bert Vogelstein, et al.**

https://www.jacr.org/article/S1546-1440(17)30969-9/fulltext

- Felix project - apply deep learning to analyzing MRI and CT scans, specifically for pancreatic cancers
- Focus on finding standardizes methods of segmentation of the pancreas
