
# XOR R-XOR Experiment 

## Data generation 
- `generate_gaussian_parity(n_samples, angle_params)`: generates n_samples points divided among four clusters with equal probability. 
Distribution is rotated by angle_params radians if provided 
- returns array of generated samples X [n_samples, 2] as well as array of integer labels of cluster membership size Y [n_samples]
- generate_gaussian_parity is called in experiment function

## Running the Experiment 
hyperparameters:
- `mc_rep`: number of repetitions to run the omnidirectional learning algorithm for
- `n_test`: number of xor/rxor data points in the test set
- `n_trees`: number of trees
- `n_xor`: array containing number of xor data points fed to learner, ranges from 50 to 725 in increments of 25 (50,75,100,125,...725)
- `n_rxor`: array containing number of rxor data points fed to learner, ranges from 25 to 750 in increments of 25 (25,50,75,1)

arrays for plotting: 
- `mean_error` 6 x len(xor)+len(rxor)
    - `mean_error[1]`: ODIF XOR GE
    - `mean_error[3]`: ODIF RXOR GE
    - `mean_error[4]`: RF XOR GE
    - `mean_error[5]`: RF RXOR GE
- `mean_te`: 
    - `mean_te[0]`: ODIF BTE 
    - `mean_te[1]`: ODIF FTE 
    - `mean_te[2]`: RF BTE 
    - `mean_te[3]`: RF FTE 
   


Run function (streaming "hack")
- `fn.run(mc_rep, n_test, n_trees,n_xor,n_rxor, mean_error, std_error, mean_te, std_te)`: 
- iterate through n_xor (ie 50,75,100...) calling experiment function for each n1 in n_xor
- once n1 has reached 725 we call experiment and pass in n1=725, and n2=25,50,75,etc

`add_task (X, y, n_estimators=n_trees)`: 
 - called in experiment function 
 - returns pl_.add_task (progressive_learner.py)-> adds task to progressive learner, since num_transformers (n_trees) > 0 adds n_trees transformers and trains voters and deciders from new transformer(s) to previous tasks


Experiment function
- `experiment(
    n_task1,
    n_task2,
    n_test=1000,
    task1_angle=0,
    task2_angle=np.pi / 2,
    n_trees=10,
    max_depth=None,
    random_state=None,
):`
- instantiates the lifelong classification forest with n_trees =10 
- *Question*: Why ` uf = LifelongClassificationForest(default_n_estimators=n_trees)`? instead of `uf=UncertaintyForest(n_estimators=n_trees)`
- generate data X,Y for task1 (XOR) and task 2 (rotated)
- if `n_task2==0` (ie. n1 still < 725/only xor data)
    - add task 1 data to lifelong classification forest. this calls add_transformer  and trains voters and deciders from new transformer to the specified backward task ids
- else
    - add task 1, add task 2 
    - predict


- Returns `errors`:
    - `errors[0]`: UF task 1 error 
    - `errors[1]`: LF task 1 error 
    - `errors[2]`: UF task 2 error 
    - `errors[3]`: LF task 2 error 
    - `errors[4]`: naive UF task 1 error 
    - `errors[5]`: naive UF task 2 error 
