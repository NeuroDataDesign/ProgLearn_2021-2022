# Notes on Proglearn tutorials code
**Start date:** 10/9/21

## Spiral_exp
### Hyperparams
- mc_rep: number of reps to run omnidirectional learning algo
- n_test: number of data points in test set 
- n_trees: number of trees
- n_spiral3: array containing number of 3 spiral data points fed to learner
- n_spiral5: ^ but 5 spiral data

To run experiment, use *run* function!
- outputs: mean_error, std_error, mean_te, std_te (te = transfer efficiency)

*plot_results* function to plot results from above

![image](https://user-images.githubusercontent.com/89429238/136673174-658b291b-8eaf-4fb3-86ec-fe65b7d3188d.png)

## fte_bte_flowers
import data, process using algos from LLF tidy images, sort

use first 100 of 102 texture classes

init each x data array with some images and then concatenating to geth next 40 images, repeat 100 times, get 100 np arrays that are conat'd to get all 4000 images across 100 classes
