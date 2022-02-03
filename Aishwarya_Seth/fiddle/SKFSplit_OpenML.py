#%%
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
from sklearn.model_selection import train_test_split

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

task = openml.tasks.get_task(task_id)
X, y = task.get_X_and_y()

# X, y = task.get_X_and_y(dataset_format="dataframe")
n_repeats, n_folds, n_samples = task.get_split_dimensions()

skf = StratifiedKFold(n_splits=10, shuffle=True)

for train_index, test_index in skf.split(X, y):

    for repeat_idx in range(n_repeats):
        # for fold_idx in range(n_folds):
        # for sample_idx in range(n_samples):
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]

        # X_train, X_test, y_train, y_test = train_test_split(
        #     X, y, test_size=0.5, random_state=2, stratify=y
        # )

        train_0, train_1 = len(y_train[y_train == 0]), len(y_train[y_train == 1])
        test_0, test_1 = len(y_test[y_test == 0]), len(y_test[y_test == 1])
        print(
            ">Train: 0=%d, 1=%d, Test: 0=%d, 1=%d" % (train_0, train_1, test_0, test_1)
        )

        model_kdf = kdf(kwargs={"n_estimators": n_estimators})
        model_kdf.fit(X_train, y_train)
        accuracy_kdf.append(np.mean(model_kdf.predict(X_test) == y_test))
        accuracy_rf.append(np.mean(model_kdf.rf_model.predict(X_test) == y_test))
print("KDF: ", accuracy_kdf)
print("RF: ", accuracy_rf)

print("Average KDF accuracy across reps: ", np.mean(accuracy_kdf))
print("Average RF accuracy across reps: ", np.mean(accuracy_rf))

# # %%
# reps = 10
# cv = 5
# n_estimators = 500
# len_sample_size = 1

# accuracy_kdf = []
# accuracy_rf = []
# jj = len_sample_size
# flag_rf_wins = 0
# flag_kdf_wins = 0
# #%%


# max_class = len(np.unique(y))

# skf = StratifiedKFold(n_splits=5, shuffle = True)
# num_rf_wins = 0
# num_kdf_wins = 0

# for train_index, test_index in skf.split(X, y):
#     X_train, X_test = X[train_index], X[test_index]
#     y_train, y_test = y[train_index], y[test_index]

#     train_0, train_1 = len(y_train[y_train==0]), len(y_train[y_train==1])
#     test_0, test_1 = len(y_test[y_test==0]), len(y_test[y_test==1])
#     print('>Train: 0=%d, 1=%d, Test: 0=%d, 1=%d' % (train_0, train_1, test_0, test_1))
#     total_sample = X_train.shape[0]
#     X_train = X_train.reshape(
#         -1, 1
#     )  # scikit correction when only 1 feature is being considered
#     X_test = X_test.reshape(-1, 1)

#     for ii in range(reps):
#         model_kdf = kdf(kwargs={"n_estimators": n_estimators})
#         model_kdf.fit(X_train, y_train)
#         accuracy_kdf.append(np.mean(model_kdf.predict(X_test) == y_test))
#         accuracy_rf.append(np.mean(model_kdf.rf_model.predict(X_test) == y_test))

#         if accuracy_rf > accuracy_kdf:
#             num_rf_wins = num_rf_wins + 1
#         else:
#             num_kdf_wins = num_kdf_wins + 1

# if num_rf_wins > num_kdf_wins:
#     print(dataset_1.feature_names[i] + " RF Wins")
#     if flag_rf_wins == 0:
#         #data_rf_wins = X_cur
#         flag_rf_wins = 1

# else:
#     print(dataset_1.feature_names[i] + " KDF Wins")
#     if flag_kdf_wins == 0:
#         #data_kdf_wins = X_cur
#         flag_kdf_wins = 1

# print("Number of Reps RF Wins: ", num_rf_wins)
# print("Number of Reps KDF Wins: ", num_kdf_wins)

# plt.hist(
#     [data_rf_wins, data_kdf_wins],
#     color=["g", "r"],
#     alpha=0.8,
#     label=["RF Wins", "KDF Wins"],
# )
# plt.show()
# print(accuracy_rf)
# avg_accuracy_rf = np.mean(accuracy_rf)
# print(avg_accuracy_rf)
# print(accuracy_kdf)
# avg_accuracy_kdf = np.mean(accuracy_kdf)
# print(avg_accuracy_kdf)

# if avg_accuracy_rf > avg_accuracy_kdf:
#    print(dataset_1.feature_names[i] + "RF Wins")
# else:
#    print(dataset_1.feature_names[i] + "KDF Wins")


# %%
