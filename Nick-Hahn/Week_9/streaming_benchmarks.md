
# Issues with Hoeffding Tree Performance

## Default Hoeffding Tree  
![40mc](https://user-images.githubusercontent.com/85964755/140371926-42a17b16-2c69-4c5d-986c-7befaf3cf5a6.png)

### Increased Sample Size: 2500 XOR -> 2500 R-XOR -> 2500 XOR
![15rep_default_river_ht](https://user-images.githubusercontent.com/85964755/140371399-607d445d-4afc-47c0-9017-113e03e5c4e4.png)

## HT Performance with adjusted parameters 
### parameters: 
  - `grace_period: 2`  
  - `split_confidence: 1e-1`
![forcedsplitting10rep](https://user-images.githubusercontent.com/85964755/140373529-e1785951-05f3-4eea-84ba-8822a852fde8.png)

### Increased Sample Size: 2500 XOR -> 2500 R-XOR -> 2500 XOR
### parameters: 
 - `grace_period: 2`  
 - `split_confidence: 1e-5`
![20mc_gp=2](https://user-images.githubusercontent.com/85964755/140372956-30a2cec5-e1bc-461e-bb92-1277005d62c8.png)

# Issues with Scikit-Garden (MondrianForestClassifier) 
  - Error ![Screen Shot 2021-11-04 at 11 02 47 AM](https://user-images.githubusercontent.com/85964755/140375173-1d63beec-b5cd-4b65-bf28-42961fc47d37.png)

  - Potential Solution: manually change `sklearn.ensemble.forest` to `sklearn.ensemble._forest`
