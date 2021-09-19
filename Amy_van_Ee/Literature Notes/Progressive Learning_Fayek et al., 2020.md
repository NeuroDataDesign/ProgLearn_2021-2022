# Progressive learning: A deep learning framework for continual learning 

Fayek, H. M., Cavedon, L., & Wu, H. R. (2020). Progressive learning: A deep learning framework for continual learning. Neural networks : the official journal of the International Neural Network Society, 128, 345–357. https://doi.org/10.1016/j.neunet.2020.05.011
https://pubmed.ncbi.nlm.nih.gov/32470799/

## Notes

- Continual learning - learn new tasks without losing prior knowledge 
- Progressive learning - a framework in deep learning for continual learning to take place
    - Curriculum - choose a task to learn 
    - Progression - increase the model’s capacity by adding new parameters based on previous learned parameters and avoiding catastrophic forgetting 
    - Pruning - ensure that the number of parameters does not grow too large and make sure previous parameters do not get in the way of learning new parameters (negative forward transfer)
- Training
    - A model is trained using a given dataset and tries to either minimize loss or maximize reward, and this does not rely on previous knowledge learned (unlike mammals)
        - Continual learning is important because it allows for learning that build on previous tasks and repurposes them, making it more efficient
    - Definition of continual learning: a model is trained on K tasks, using K tasks to help perform K+1th task
    - Challenges
        - Catastrophic forgetting
            - The system’s performance on the K tasks decreases when it learns how to perform the K+1 th task
        - Negative forward transfer
            - Knowledge of the K tasks interferes with ability to learn K+1 th task because they unrelated
- Proposed model requirements
    - Strategy to select next task to continue learning, increase capacity of model to accommodate new learning, maintain and use knowledge to learn future tasks without catastrophic forgetting o negative forward transfer
    - Curriculum, progression, pruning
        - In progression, add new parameters to learn new tasks and not touch old tasks to avoid catastrophic forgetting, but this can lead to many tasks so have pruning - remove newly added weights in a “greedy layer-wise manner”
            - Pruning can also help against negative forward transfer by remove parameters if not related to task
    - Curriculum 
        - Active task selection - this task is chosen relative to current knowledge so that the algorithm can naturally learn more difficult tasks
    - Progression
        - Learn new tasks, can reuse features from old tasks using concatenation, avoids catastrophic forgetting
    - Pruning
        - Greedy layer-wise - counteract growth in num of parameters, knows that features vary across the layers of the deep network
            - Not pruning entire network concurrently 
    - If tasks unrelated, remove features between progressive blocks so progressive learning becomes more independent and less chance of negative forward transfer
    - Ways to test algorithm
        - Image recognition and speech recognition tasks
    - Curriculum learning - learning tasks in a meaningful order can help learning
    - Conclusion
        - Progressive learning outperformed independent, transfer, multi-task, and continual 

