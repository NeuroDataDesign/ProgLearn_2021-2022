#%%
from kdg import kdf
from kdg.utils import get_ece
import openml
from joblib import Parallel, delayed
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier as rf
from sklearn.metrics import cohen_kappa_score
from kdg.utils import get_ece
import os
from os import listdir, getcwd 
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
# %%
# %%
def experiment(dataset_id, folder, n_estimators=500, reps=30):
    if (dataset_id in executed_ids):
      print("Already executed: ", dataset_id)
      return
    else:
      print("Executing: ", dataset_id)
    dataset = openml.datasets.get_dataset(dataset_id)
    X, y, is_categorical, _ = dataset.get_data(
                dataset_format="array", target=dataset.default_target_attribute
            )


    if np.mean(is_categorical) >0:
        return

    if np.isnan(np.sum(y)):
        return

    if np.isnan(np.sum(X)):
        return

    normalized_x = StandardScaler().fit_transform(X)
    print(np.mean(normalized_x), np.std(normalized_x))

    pca_data = PCA(n_components=4)
    principalComponents = pca_data.fit_transform(normalized_x)

    X = pd.DataFrame(data = principalComponents
             , columns = ['principal component 1', 'principal component 2', 'principal component 3', 'principal component 4'])

    X = X.to_numpy() 
    
    total_sample = X.shape[0]
    unique_classes, counts = np.unique(y, return_counts=True)

    test_sample = min(counts)//3

    indx = []
    for label in unique_classes:
        indx.append(
            np.where(
                y==label
            )[0]
        )

    max_sample = min(counts) - test_sample
    train_samples = np.logspace(
        np.log10(2),
        np.log10(max_sample),
        num=10,
        endpoint=True,
        dtype=int
        )
    
    err = []
    err_rf = []
    ece = []
    ece_rf = []
    kappa = []
    kappa_rf = []
    mc_rep = []
    samples = []

    for train_sample in train_samples:
        
        for rep in range(reps):
            indx_to_take_train = []
            indx_to_take_test = []

            for ii, _ in enumerate(unique_classes):
                np.random.shuffle(indx[ii])
                indx_to_take_train.extend(
                    list(
                            indx[ii][:train_sample]
                    )
                )
                indx_to_take_test.extend(
                    list(
                            indx[ii][-test_sample:counts[ii]]
                    )
                )
            model_kdf = kdf(kwargs={'n_estimators':n_estimators})
            model_kdf.fit(X[indx_to_take_train], y[indx_to_take_train])
            proba_kdf = model_kdf.predict_proba(X[indx_to_take_test])
            proba_rf = model_kdf.rf_model.predict_proba(X[indx_to_take_test])
            predicted_label_kdf = np.argmax(proba_kdf, axis = 1)
            predicted_label_rf = np.argmax(proba_rf, axis = 1)

            err.append(
                1 - np.mean(
                        predicted_label_kdf==y[indx_to_take_test]
                    )
            )
            err_rf.append(
                1 - np.mean(
                    predicted_label_rf==y[indx_to_take_test]
                )
            )
            kappa.append(
                cohen_kappa_score(predicted_label_kdf, y[indx_to_take_test])
            )
            kappa_rf.append(
                cohen_kappa_score(predicted_label_rf, y[indx_to_take_test])
            )
            ece.append(
                get_ece(proba_kdf, predicted_label_kdf, y[indx_to_take_test])
            )
            ece_rf.append(
                get_ece(proba_rf, predicted_label_rf, y[indx_to_take_test])
            )
            samples.append(
                train_sample*len(unique_classes)
            )
            mc_rep.append(rep)

    df = pd.DataFrame() 
    df['err_kdf'] = err
    df['err_rf'] = err_rf
    df['kappa_kdf'] = kappa
    df['kappa_rf'] = kappa_rf
    df['ece_kdf'] = ece
    df['ece_rf'] = ece_rf
    df['rep'] = mc_rep
    df['samples'] = samples

    df.to_csv(folder+'/'+'openML_cc18_'+str(dataset_id)+'.csv')

#%%
folder = 'openml_res'
#os.mkdir(folder)
benchmark_suite = openml.study.get_suite('OpenML-CC18')
current_dir = getcwd()
files = listdir(current_dir+'/'+folder)
executed_ids = [1049, 1050, 11, 12, 14, 16, 18, 22, 37, 44, 458, 54]
Parallel(n_jobs=10,verbose=1)(
        delayed(experiment)(
                dataset_id,
                folder
                ) for dataset_id in openml.study.get_suite("OpenML-CC18").data
            )

'''for task_id in benchmark_suite.tasks:
    filename = 'openML_cc18_' + str(task_id) + '.csv'

    if filename not in files:
        print(filename)
        try:
            experiment(task_id,folder)
        except:
            print("couldn't run!")
        else:
            print("Ran successfully!")'''
# %%