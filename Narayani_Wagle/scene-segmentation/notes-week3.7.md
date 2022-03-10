## Pseudocode for Potential Scene Segmentation Experiment
1) Load data and labels
2) Split data into batches
3) Run training of batches of data in parallel for each task and save accuracy
4) Average forward transfer accuracies across tasks
5) Average backward transfer accuracies across tasks
6) Plot results

# Step 3 - Running training of batches of data
1) Cross val data split
2) Create NeuralClassificationTransformer
3) create network
4) define parameters for transformer
5) create voter class
6) create progressive learner
7) run experiment 
8) output results

# Step 7 - Running experiment
1) Initialize results dataframe
2) Loop through tasks
3) For first task, add task
4) For each task, make prediction on current task using the trained learner
5) Make prediction on current task with trained learner on test data
6) Calculate accuracies across task and save
