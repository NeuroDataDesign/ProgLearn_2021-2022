# Decision Forests for Computer Vision and Medical Image Analysis

## Notes

**Chapter 1**
- Part I - general forest model <- will want to focus on this to learn more about theory behind this model

**Chapter 2 - Notation and Terminology**
- Reference this chapter for table of notation, will be very useful when reading papers in the future (pages 3,4)
- Again, reference this chapter for commonly used terms

**Chapter 3 - Introduction: The Abstract Forest Model**
- Common learning tasks - classification, regression, density estimation, manifold learning, semi-supervised learning, active learning
- Decision trees have become more popular due to their ability for generalization - greater accuracy on new data by using an ensemble of slightly different trees
    - nodes are either internal (split) or terminal (leaf), often circles or squares, respectively
    - the more questions asked, higher confidence in response - each internal node has a question
    - general layout: root node takes in input, based on reslt of first test, the data goes down to left or right child where new test and so on until hits a leaf node where most probable answer based on previous answers
