### General Plan
Do experiment similar to Gaussian XOR/XNOR as in the tutorials. After adding the XNOR data, we will add additional XOR data to the first class 
in order to see if it performs better.

### Step 1
First, we do this with the existing function (fn.run(), as used in the experiment). We will add another clump of Gaussian distributed data after running 
the experiment, and see how it effects the generalization of each group. In theory, we don't expect much to change, because the run function should just be 
making a new tree for any new data. 

### Step 2
Once we test with the existing function, we will use the new update_task() function. In theory, it should add to the existing tree, which should improve
generalization with the added data
