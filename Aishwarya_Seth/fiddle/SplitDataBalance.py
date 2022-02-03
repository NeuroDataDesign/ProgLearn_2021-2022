from kdg import kdf
from kdg.utils import get_ece
import openml
import multiprocessing
from joblib import Parallel, delayed
import numpy as np
import pandas as pd
from sklearn.model_selection import StratifiedKFold
from sklearn.ensemble import RandomForestClassifier as rf
from sklearn.metrics import cohen_kappa_score
import os
from sklearn.datasets import fetch_openml
import matplotlib.pyplot as plt


def split_balanced(data, target, test_size=0.2):

    classes = np.unique(target)
    # can give test_size as fraction of input data size of number of samples
    if test_size < 1:
        n_test = np.round(len(target) * test_size)
    else:
        n_test = test_size
    n_train = max(0, len(target) - n_test)
    n_train_per_class = max(1, int(np.floor(n_train / len(classes))))
    n_test_per_class = max(1, int(np.floor(n_test / len(classes))))

    ixs = []
    for cl in classes:
        if (n_train_per_class + n_test_per_class) > np.sum(target == cl):
            # if data has too few samples for this class, do upsampling
            # split the data to training and testing before sampling so data points won't be
            #  shared among training and test data
            splitix = int(
                np.ceil(
                    n_train_per_class
                    / (n_train_per_class + n_test_per_class)
                    * np.sum(target == cl)
                )
            )
            ixs.append(
                np.r_[
                    np.random.choice(
                        np.nonzero(target == cl)[0][:splitix], n_train_per_class
                    ),
                    np.random.choice(
                        np.nonzero(target == cl)[0][splitix:], n_test_per_class
                    ),
                ]
            )
        else:
            ixs.append(
                np.random.choice(
                    np.nonzero(target == cl)[0],
                    n_train_per_class + n_test_per_class,
                    replace=False,
                )
            )

    # take same num of samples from all classes
    ix_train = np.concatenate([x[:n_train_per_class] for x in ixs])
    ix_test = np.concatenate(
        [x[n_train_per_class : (n_train_per_class + n_test_per_class)] for x in ixs]
    )

    X_train = data[ix_train, :]
    X_test = data[ix_test, :]
    y_train = target[ix_train]
    y_test = target[ix_test]

    return X_train, X_test, y_train, y_test


#%%
# Considering dataset: pc1
dataset_1 = fetch_openml(name="pc1")
# print(dataset_1.feature_names)
task_id = 3918
# dataset_id = 1068
# %%
# dataset = openml.datasets.get_dataset(dataset_id)
# X, y, categorical_indicator, attribute_names = dataset.get_data(
#    dataset_format="array", target=dataset.default_target_attribute
# )
# print(categorical_indicator)

accuracy_kdf = []
accuracy_rf = []
n_estimators = 500
reps = 10
task = openml.tasks.get_task(task_id)
X, y = task.get_X_and_y()

for i in range(reps):
    X_train, X_test, y_train, y_test = split_balanced(X, y, test_size=0.2)
    train_0, train_1 = len(y_train[y_train == 0]), len(y_train[y_train == 1])
    test_0, test_1 = len(y_test[y_test == 0]), len(y_test[y_test == 1])
    print(">Train: 0=%d, 1=%d, Test: 0=%d, 1=%d" % (train_0, train_1, test_0, test_1))

    model_kdf = kdf(kwargs={"n_estimators": n_estimators})
    model_kdf.fit(X_train, y_train)
    accuracy_kdf.append(np.mean(model_kdf.predict(X_test) == y_test))
    accuracy_rf.append(np.mean(model_kdf.rf_model.predict(X_test) == y_test))
print("KDF: ", accuracy_kdf)
print("RF: ", accuracy_rf)

print("Average KDF accuracy across reps: ", np.mean(accuracy_kdf))
print("Average RF accuracy across reps: ", np.mean(accuracy_rf))
