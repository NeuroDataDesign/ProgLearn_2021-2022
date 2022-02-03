# Proglearn notes
<table><tr><td valign="top" width="49%"> 

## **base.py** 
**BaseTransformer**: A base class for a transformer, derived from scikit-learn's BaseEstimator
class and TransformerMixin mixin.
- methods: `fit` (the transformer), `transform` ($X \to \tilde{X}$ tree (return the index of the leaf that each sample is predicted as.)) 

**BaseVoter**: A base class for a voter, derived from scikit-learn's BaseEstimator class.
- methods: `fit` (the transformed input data $\tilde{X}$),`predict`(class labels for transformed input data)
- **BaseClassificationVoter** BaseVoter + `predict_proba` (posterior probabilities of each class)

**BaseDecider**: A base class for a decider, derived from scikit-learn's BaseEstimator class.
- methods: `fit`, `predict`

- **BaseClassificationDecider** BaseDecider+`predict_proba`

**BaseProgressiveLearner**: base class for a progressive learner
- `add_task` - add new unseen task to progressive learner 
- `add_transformer` - add a new transformer (but no voters or transformers corresponding to the task from which the transformer data was collected)
- `predict` - perform inference corresponding to the input task_id on input data X using the progressive learner 

- **BaseClassificationProgressiveLearner**: A class for a progressive learner which inherits from the base progressive learner but adds the functionality of estimating posteriors for a given task_id.
    - `predict_proba` estimate posteriors under a given task_id using the decider

## **forest.py**
**LifeLongClassificationForest(ClassificationProgressiveLearner)**
- `default_transformer_class` = TreeClassificationTransformer
- `default_voter_class` = TreeClassificationVoter
- `default_decider_class` =SimpleArgmaxAverage

<!-- Column 2                               -->
</td><td valign="top" width="50%">

## **progressive_learner.py**
An internal class for progressive learner (either network of forest)

**attributes** (all of type dict ):
- `task_id_to_X` : 
	- key: task id for task where posteriors are to be estimated
	- value: input data matrix $X$ 
- `task_id_to_y`:
	- key: task id for task where posteriors are to be estimated 
	- value: output data matrix $y$ (class labels)
- `transformer_id_to_X` 
	- key: `transformer_id`
	- value: input data matrix $X$
- `transformer_id_to_y`
	- key: `transformer_id`
	- value: output data matrix $y$
- `transformer_id_to_transformers` 
	- key: `transformer_id`
	- value: transformer object

Voter related attributes
- `task_id_to_transformer_id_to_voters` 
	- outer key: `task_id`
	- inner key: `transformer_id`
	- value: voter object
- `task_id_to_bag_id_to_voter_data_idx`
	- outer key: `task_id`
    - inner key: `bag_id`
	- value: voter data indices 
- `task_id_to_voter_class`
	- key: `task_id`
	- value: voter class
- `task_id_to_voter_kwargs`
	- key: `task_id`
	- value: decider kwargs

Decider related attributes
- `task_id_to_decider`
	- key: `task_id`
	- value decider
	- maps deciders to a particular task
- `task_id_to_decider_class`
	- key: `task_id`
	- value: decider class
					
</td></tr></table>	

# Synergistic LL
**Channels ensemble representations from encoders which feed to decider**
- For each task the transformer/encoder $u_t$ is the representation learned by a  decision forest
- The leaf nodes of each tree partition the input space $\mathcal{X}$
- The representation of $x\in \mathcal{X}$ corresponding to a single tree can be a one-hot encoded $L_b$-dimensional vector with a 1 in the location corresponding to the leaf $x$ falls into of tree $b$. Concatenating the $B$ one-hot vectors, $u_t$ is a mapping from $\mathcal{X}$ to a $B$-sparse vector of length $\sum_{b=1}^BL_b$. 
- The voter/channel then learns posteriors by populating the cells of the partitions and taking class votes with **OOB samples**
- decider/decoder $w_t$ averages the posterior estimates and outputs argmax to produce a single prediction

-------
# 2 task example: 
### first hypothesis (u->v->w) already learned 
- new data from new task:
    1. push task 2 data through the existing encoder ($u_1$)
    2. build and train new encoder($u_2$) on new data to map each data point to a sparse vector encoding which polytope it is in 
    3. build and train channel ($v_2$) for new task on the outputs from both encoders ($u_1,u_2$)(this is what enables forward transfer)
    4. push task 1 data through new encoder ($u_2$) to get a second representation of the first task's data and train the original voter/channel ($v_1$) on both representations of the first task's data (this is what enables backward transfer)

    
-------------------------------------------------
## whats happening currently with update task
<table><tr><td valign="top" width="49%"> 

BEFORE Task Update 

'task_id_to_X': {0: array([[ 0.53050096, -0.6554739 ],
       [-0.57503941,  0.11047619],
       [-0.60970147, -0.35920428],
       [-0.36438432, -0.64900599],
       [ 0.36997967, -0.44096243],
       [ 0.98416961,  0.451652  ],
       [ 0.6928975 , -0.46240818],
       [ 0.48044165, -0.43725596],
       [-0.4535142 , -0.55974148],
       [ 0.46090935,  0.6746796 ]])}




       
        'task_id_to_y': {0: array([0, 0, 1, 1, 0, 1, 0, 0, 1, 1])}
        
        'transformer_id_to_X': {}, 'transformer_id_to_y': {}
        
        'transformer_id_to_transformers': {0: [TreeClassificationTransformer(kwargs={'max_depth': 30}),TreeClassificationTransformer(kwargs={'max_depth': 30})]}
        
        'task_id_to_transformer_id_to_voters': {0: {0: [TreeClassificationVoter(classes=array([0, 1])), TreeClassificationVoter(classes=array([0, 1]))]}}, 
        
        'task_id_to_decider': {0: SimpleArgmaxAverage(classes=array([0, 1]))},
        
        'task_id_to_decider_class': {0: <class 'proglearn.deciders.SimpleArgmaxAverage'>},
        
        'task_id_to_decider_kwargs': {0: {'classes': array([0, 1])}}, 
         
        'task_id_to_voter_class': {0: <class 'proglearn.voters.TreeClassificationVoter'>},
         
        'task_id_to_voter_kwargs': {0: {'classes': array([0, 1]), 'kappa': inf}},
          
        'task_id_to_bag_id_to_voter_data_idx': {0: {0: array([3, 0, 2, 7]), 1: array([8, 3, 0, 7])}},
           
        'task_id_to_decider_idx': {0: array([], dtype=int32)}, 
            
        'default_transformer_class': <class 'proglearn.transformers.TreeClassificationTransformer'>,
            
        'default_transformer_kwargs': {},

        'default_voter_class': <class 'proglearn.voters.TreeClassificationVoter'>,

        'default_voter_kwargs': {'kappa': inf},

        'default_decider_class': <class 'proglearn.deciders.SimpleArgmaxAverage'>,

        'default_decider_kwargs': {},

        'default_n_estimators': 2,

        'default_tree_construction_proportion': 0.67,

        'default_kappa': inf,

        'default_max_depth': 30}







</td><td valign="top" width="50%">
AFTER task update

{'task_id_to_X': {0: array([[ 0.53050096, -0.6554739 ],
       [-0.57503941,  0.11047619],
       [-0.60970147, -0.35920428],
       [-0.36438432, -0.64900599],
       [ 0.36997967, -0.44096243],
       [ 0.98416961,  0.451652  ],
       [ 0.6928975 , -0.46240818],
       [ 0.48044165, -0.43725596],
       [-0.4535142 , -0.55974148],
       [ 0.46090935,  0.6746796 ],
       [ 0.24545313, -0.72527366],
       [-0.10413911,  0.82002139],
       [ 0.1960006 ,  0.68781848],
       [ 0.62974451, -0.72010911],
       [ 0.4065345 , -0.30632441],
       [ 0.75606139, -0.5502452 ],
       [ 0.54629393,  0.90304505],
       [ 0.28651701, -0.72556064],
       [-0.58336142, -0.54671086],
       [ 0.84976384, -0.70872052]])}
       
        'task_id_to_y': {0: array([0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0])},
        
        'transformer_id_to_X': {}, 'transformer_id_to_y': {},
          
        'transformer_id_to_transformers': {0: [TreeClassificationTransformer(kwargs={'max_depth': 30}), TreeClassificationTransformer(kwargs={'max_depth': 30})]},

        'task_id_to_transformer_id_to_voters': {0: {0: [TreeClassificationVoter(classes=array([0, 1])), TreeClassificationVoter(classes=array([0, 1])), TreeClassificationVoter(classes=array([0, 1])), TreeClassificationVoter(classes=array([0, 1]))]}},
        
        'task_id_to_decider': {0: SimpleArgmaxAverage(classes=array([0, 1]))},
        
        'task_id_to_decider_class': {0: <class 'proglearn.deciders.SimpleArgmaxAverage'>},
        
        'task_id_to_decider_kwargs': {0: {'classes': array([0, 1])}},
        
        'task_id_to_voter_class': {0: <class 'proglearn.voters.TreeClassificationVoter'>},
        
        'task_id_to_voter_kwargs': {0: {'classes': array([0, 1]), 'kappa': inf}}, 
         
        'task_id_to_bag_id_to_voter_data_idx': {0: {0: array([3, 0, 2, 7, 5, 1, 9, 2]), 1: array([8, 3, 0, 7, 3, 5, 6, 9])}}, 
         
        'task_id_to_decider_idx': {0: array([], dtype=int32)},
         
        'default_transformer_class': <class 'proglearn.transformers.TreeClassificationTransformer'>,
        
        'default_transformer_kwargs': {},
        
        'default_voter_class': <class 'proglearn.voters.TreeClassificationVoter'>,
        
        'default_voter_kwargs': {'kappa': inf},
        
        'default_decider_class': <class 'proglearn.deciders.SimpleArgmaxAverage'>, 
        
        'default_decider_kwargs': {},
        
        'default_n_estimators': 2,
        'default_tree_construction_proportion': 0.67,
        'default_kappa': inf,
        'default_max_depth': 30}



</td></tr></table>	

















##  INCOMPLETE/need to redo: updating a task pseduocode
```
`synX.update_task`:
    `progressive_learner.update_task`:
	    verify task $t$ already exists 
		update progressive learner $X$ and $y$ data for task $t$ task_id
		get indices for transformer/voter/decider splits with `progressive_learner._bifurcate_decider_idxs`
				update decider index with `progressive_learner._append_decider_idx`
				update the transformer(s) for task $t$ with a new function `progressive_learner._update_transformer`:
					for all task $t$ transformers:
						update transformer/voter index 
						update progressive learner dictionaries mapping transformer ids to $X$ and $y$ data
						partial fit transformer
						update voters fits transformed data 
						update decider
					
```

