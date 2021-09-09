Liu Y., Wang Y., Zhang J. (2012) New Machine Learning Algorithm: Random Forest. In: Liu B., Ma M., Chang J. (eds) Information Computing and Applications. ICICA 2012. Lecture Notes in Computer Science, vol 7473. Springer, Berlin, Heidelberg. https://doi.org/10.1007/978-3-642-34062-8_32
https://link.springer.com/chapter/10.1007/978-3-642-34062-8_32#citeas

## Section  2.1: Principle of Operation
Random Forest generates trees from “identically distributed random vectors” and polls them to get final majority label for the input object {x}
  
## Section 2.2 Random Forest Characteristics 
The margin function defines the accuracy of a Random Forest classifier. Margin can be defined as follows:
  
` margin = margin(X, Y) = avg(as.binary(h<sub>k</sub>(X)==Y)) - max([avg(bin(h<sub>k</sub>(X) == j)) for j != y])`

where h<sub>k</sub>(*X*) is a tree classifier 

## Section 3: The Methods of Random Forest Construction
Article lists 2 methods of generating random vectors:
- Forest-RI, random subset of training data
- Forest-RC, linear combinations of training data (if training set is small)
Also suggests tree may be modified at output (but this just introduces noise?)

## Section 4: Random Forests for Regression
Regression modeling estimates the relationship between 1+ independent variables and a dependent variable

Data entries can be used as input into the tree predictor h(*X*, Θ) to get a numerical result for how the independent variables affect the dependent variable (regressing to the line of dependent variable defined by training data.



