# Outline for Testing Functions for partial_fit function

## Expected format of inputs
The function header for the function that Kevin is writing is:
partial_fit(X, y, task_id, classes)

## Test 1: test_predict_without_fit
This test should check that the function throws the correct exception to input where the y array is not given, and no task 
is created/added to. 
### Pseudocode:
```
  test_predict_without_fit(self):
    X = np.random.normal(0, 1, size = (100, 3))
    
    with pytest.raises(NotFittedError):
      # Create instance of a forest
      # forest.predict(X, task_id = 0)
```
      
## Test 2: Basic prediction test
This test will ensure that if no task has been added, partial_fit will correctly create a new task
### Pseudocode:
```
  test_predict_notask_exists(self):
  
    # Create instance of forest
    
    X = np.concatenate((np.zeros(100), np.ones(100))).reshape(-1, 1)
    y = np.concatenate((np.zeros(100), np.ones(100)))
    
    # Instantiate task_id and classes   
    
    forest.partial_fit(X, y, task_id, classes)
    
    u1 = forest.predict(np.array([0]).reshape(1, -1), task_id=0)
    u2 = forest.predict(np.array([1]).reshape(1, -1), task_id=0)
    assert(u1 != u2)
    
    u1 = forest.predict(np.array([0]).reshape(1, -1), task_id=0)
    u2 = forest.predict(np.array([0]).reshape(1, -1), task_id=0)
    assert(u1 == u2)
```    

## Test 3: Basic prediction probability test
This test will ensure that if no task has been added, partial_fit will correctly calculate probability
### Pseudocode:
```
  test_predict_proba_notask_exists(self):
  
    # Create instance of forest
    
    X = np.concatenate((np.zeros(100), np.ones(100))).reshape(-1, 1)
    y = np.concatenate((np.zeros(100), np.ones(100)))
    
    # Instantiate task_id and classes    
    
    forest.partial_fit(X, y, task_id, classes)
    
    u1 = forest.predict_proba(np.array([0]).reshape(1, -1), task_id=our_task_id)
    u2 = forest.predict_proba(np.array([1]).reshape(1, -1), task_id=our_task_id)
    assert not np.array_equiv(u1, u2)
    
    u1 = forest.predict_proba(np.array([0]).reshape(1, -1), task_id=our_task_id)
    u2 = forest.predict_proba(np.array([0]).reshape(1, -1), task_id=our_task_id)
    assert np.array_equiv(u1, u2)
```

Additional ideas for tests:
 - If we have created a task with task_id = 0, ensure that calling partial fit on new task_id=1 does not change it
 - Ensure that forest is being updated (see questions) if partial fit is called with same task_id

### Questions:
 - What are some tests that can detect whether an existing task was updated instead of replaced
  - If we update task with the same task_id, but different input data, is it sufficient to look for difference in output?
  - This isn't very rigorous, what are more better testing strategies?
 - Bit of confusion on what the input "classes" affects in this function - is it necessary?
  
