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
from openml.tasks import TaskType

#%%
tasks = openml.tasks.list_tasks(tag="OpenML-CC18", output_format="dataframe")
n_estimators = 500
n_repeats = 1

relevant_tasks = pd.read_csv(
    "/Users/aishwaryaseth/Desktop/JHU/Spring2021/NDD/Code/Updated_kdg_OpenML/kdg/benchmarks/openml_experiments/OpenML_KDFvsRF_RAW_Results.csv"
)
# CLARIFY: Just accuracy > than the other? Or some minimum difference between them is required?
# Just use accuracy > than the other
relevant_tasks["kdf_wins"] = relevant_tasks.apply(
    lambda x: True if x["mean_accuracy_kdf"] > x["mean_accuracy_rf"] else False, axis=1
)

relevant_tasks = relevant_tasks[relevant_tasks["kdf_wins"] == True]

# CLARIFY: Sort values by the margin between KDF & RF?
# No need
relevant_tasks = relevant_tasks.sort_values(by="mean_accuracy_kdf")

# Since KDF Wins in only 11 tasks, just creating an OOD distribution study table from these
# Just use all 11 tasks
# print(len(relevant_tasks))

num_features_required = int(np.min(relevant_tasks["num_input_features"]))
# print(relevant_tasks[["task_id", "dataset_name"]])

#%%


#%%

for task_id in relevant_tasks["task_id"]:
    cur_task_id = int(task_id)
    task = openml.tasks.get_task(cur_task_id)
    # print(task)  # Verify that it is the same 11 tasks being picked up
    X, y = task.get_X_and_y()
    # print(X[:5])
    # print(y[:5])

    try:
        skf = StratifiedKFold(n_splits=10, shuffle=True)
        cur_importances = []

        for train_index, test_index in skf.split(X, y):

            for repeat_idx in range(n_repeats):
                # for fold_idx in range(n_folds):
                # for sample_idx in range(n_samples):
                X_train, X_test = X[train_index], X[test_index]
                y_train, y_test = y[train_index], y[test_index]

                # X_train, X_test, y_train, y_test = train_test_split(
                #     X, y, test_size=0.5, random_state=2, stratify=y
                # )

                train_0, train_1 = len(y_train[y_train == 0]), len(
                    y_train[y_train == 1]
                )
                test_0, test_1 = len(y_test[y_test == 0]), len(y_test[y_test == 1])
                print(
                    ">Train: 0=%d, 1=%d, Test: 0=%d, 1=%d"
                    % (train_0, train_1, test_0, test_1)
                )

                model_kdf = kdf(kwargs={"n_estimators": n_estimators})
                model_kdf.fit(X_train, y_train)

                cur_importances.append(
                    (model_kdf.rf_model.feature_importances_.tolist())
                )
        importances = np.mean(cur_importances, axis=0)
        sorted_indices = np.argsort(importances)[::-1]
        print("Sorted: ", sorted_indices[:num_features_required])
        X_new = X[:, sorted_indices[:num_features_required]]
        df = pd.DataFrame(X_new)
        df["target"] = y
        print(df.head())

        df.to_csv("./TopFeatures/{}.csv".format(cur_task_id), index=False)
    except (ValueError):
        print(ValueError)
