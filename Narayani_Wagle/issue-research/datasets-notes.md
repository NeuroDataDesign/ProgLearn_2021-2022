# Scene Segmentation Dataset Options
## ImageNet
- https://image-net.org/challenges/LSVRC/2016/ 
- each image labelled with presence or absence of 1000 object categories
- 200 categories which are labelled with bounding boxes in the image
- ADE20K dataset - 20K training images of scenes with annotations of multiple objects and object parts, 2K validation images
- http://sceneparsing.csail.mit.edu/ 
- dataset access: http://groups.csail.mit.edu/vision/datasets/ADE20K/ 
- github with info: https://github.com/CSAILVision/ADE20K
- ADE20K
  - 27,574 images, 365 diff scenes, 706,868 unqiue objects from 3,688 categories 
  - includes WordNet defn and hierarchy
  - 193K+ annotated object parts and parts of parts
  - polygon annotations
## CLEVR
- https://cs.stanford.edu/people/jcjohns/clevr/
- 70K images training + 15K val + 15K test
- annotations for locations, attributes, and relationships of objects
- images contain 3D shapes
- labelled with questions and answers
  - attribute identification
  - counting
  - comparison
  - spatial relationships
  - logical operations
  - e.g. are there an equal number of large things and metal spheres?
  - e.g. what size is the cylinder that is left of the brown metal thing that is left of the big sphere?
- questions are represented as natural language and functional program
