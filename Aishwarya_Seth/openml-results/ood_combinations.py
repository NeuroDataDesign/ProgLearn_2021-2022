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
import seaborn as sns

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
relevant_tasks = relevant_tasks.sort_values(by="task_id")

# Since KDF Wins in only 11 tasks, just creating an OOD distribution study table from these
# Just use all 11 tasks
# print(len(relevant_tasks))

num_features_required = int(np.min(relevant_tasks["num_input_features"]))
# print(relevant_tasks[["task_id", "dataset_name"]])

#%%

task_ids = (relevant_tasks["task_id"]).to_numpy(dtype="int32")
print(task_ids)
# ood_combinations = np.array(np.meshgrid(task_ids, task_ids)).T.reshape([-1, 2])
# print(ood_combinations.shape)

kdf_results = np.empty((11, 0), float)
rf_results = np.empty((11, 0), float)

for i in task_ids:
    training_task_id = i
    kdf_combination_result = []
    rf_combination_result = []
    training_task = pd.read_csv("./TopFeatures/{}.csv".format(training_task_id))

    X_train = training_task.iloc[:, 0:num_features_required]
    y_train = training_task.iloc[:, -1]

    model_kdf = kdf(kwargs={"n_estimators": n_estimators})
    model_kdf.fit(
        X_train.values, y_train.values
    )  # Add .values to suppress an sklearn warning about fitting the classifier without feature names

    print(i)
    for j in task_ids:
        testing_task_id = j
        testing_task = pd.read_csv("./TopFeatures/{}.csv".format(testing_task_id))

        X_test = testing_task.iloc[:, 0:num_features_required]
        y_test = testing_task.iloc[:, -1]

        kdf_combination_result.append(
            np.mean(model_kdf.predict(X_test.values) == y_test.values)
        )
        rf_combination_result.append(
            np.mean(model_kdf.rf_model.predict(X_test.values) == y_test.values)
        )

        print(j)

    kdf_results = np.append(
        kdf_results, np.array([kdf_combination_result]).transpose(), axis=1
    )
    rf_results = np.append(
        rf_results, np.array([rf_combination_result]).transpose(), axis=1
    )

    print(kdf_results)
    print(rf_results)

    # break

sns.heatmap(kdf_results, cmap="Reds")
plt.title("KDF Results on OOD Data")
plt.xlabel("Trained On")
plt.ylabel("Tested On")
plt.show()

sns.heatmap(rf_results, cmap="Reds")
plt.title("RF Results on OOD Data")
plt.xlabel("Trained On")
plt.ylabel("Tested On")
plt.show()
