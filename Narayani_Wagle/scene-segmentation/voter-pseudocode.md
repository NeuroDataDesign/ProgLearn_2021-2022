# Pseudocode for KNNClassificationVoter Class
Functions:
- init - initialize the voter object
- fit - fit the sklearn knn object
- predict_proba - use the sklearn knn object to predict on new data
- predict - output the class predictions on new data

KNNClassificationVoter.predict:
- Parameters 
  - X - an array of shape [n_samples, n_features] which represents the transformed input data
- Returns
  - y_hat - an ndarray of shape [n_samples] with the predicted class label per example
1) call the predict_proba function (detailed below)
2) take the max probability for each row of the output (find the class with the highest probability)
3) take the list of indices output by argmax and select the corresponding classes to output
4) return the class predictions

KNNClassificationVoter.predict_proba:
- Parameters - X - an array of shape [n_samples, n_features] which represents the transformed input data
- Returns - y_proba_hat - an ndarray of shape [n_samples, n_classes] which represent the posteriors per example
1) check if the KNNClassificationVoter is fitted first, if not, raise error
2) check if X is a non-empty 2D array
3) call the predict_prob function of the knn object on X to get the class probabilities per sample, assign output to votes_per_example
4) if there are missing labels, then assign a column of zeros in the votes_per_example which corresponds to the missing class label
5) return the votes_per_example

KNNClassificationVoter.fit:
- Parameters - X - array of shape [n_samples, n_features] which represents the transformed data that will be used for training, y - an array of shape [n_samples] which represents the label for class membership of the X data
- Returns - a KNNClassificationVoter object
1) check that the dimensions of X and y are consistent
2) if the class attribute k has already been set, then assign it to k
3) if the class attribute k has not been set, then take the log2 of the # of samples and assign it to k
4) fit the knn classifier object with X and y
5) assign the number of unique y values to num_classes
6) initialize the missing label indices list
7) if the number of classes is not 0 and the num_classes is less than the length of the class attribute classes then add the missing label indices to the missing_label_indices list
8) return the KNNClassificationVoter object

KNNClassificationVoter.__init__:
- Parameters - k - int representing the number of neighbors used for prediction by the knn object for fitting and voting, kwargs - a dictionary containing all the keyword arguments for the underlying knn object, classes - a list of all possible output label values
- Class attributes - missing_label_indices - list of label values that exist are in the classes parameter but are missing from the fit function call, knn_ - the KNeighborsClassifier classifier
1) set k input to the class attribute k
2) set the kwargs input to the class attribute kwargs
3) set the classes input to an array and assign to the the class attribute classes
