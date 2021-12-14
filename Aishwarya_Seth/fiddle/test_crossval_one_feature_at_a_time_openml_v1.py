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
# %%
def get_stratified_samples(y, samples_to_take):
    labels = np.unique(y)
    sample_per_class = int(np.floor(samples_to_take/len(labels)))

    if sample_per_class < len(np.where(y==labels[0])[0]):
        stratified_indices = np.random.choice(
            (
            np.where(y==labels[0])[0]
            ), 
            sample_per_class,
            replace = False
        )
    else:
        stratified_indices = np.random.choice(
            (
            np.where(y==labels[0])[0]
            ), 
            sample_per_class,
            replace = True
        )

    for lbl in labels[1:]:
        if sample_per_class < len(np.where(y==lbl)[0]):
            _stratified_indices = np.random.choice(
                (
                np.where(y==lbl)[0]
                ), 
                sample_per_class,
                replace = False
            )
        else:
            _stratified_indices = np.random.choice(
                (
                np.where(y==lbl)[0]
                ), 
                sample_per_class,
                replace = True
            )

        stratified_indices = np.concatenate(
            (stratified_indices, _stratified_indices),
            axis=0
        )
    return stratified_indices
#%%
def experiment(task_id, folder, n_estimators=500, cv=5, reps=10):
    df = pd.DataFrame() 
    task = openml.tasks.get_task(task_id)
    X, y = task.get_X_and_y()
    print("Number of Features: ", X.shape[1]+1)

    folds = []
    samples = []
    dims = []
    features = []
    err_rf = []
    err_kdf = []

    for i in range(X.shape[1]):
        X_cur = X[:, i]
        
        dim = 1 #X.shape[1]
        max_class = len(np.unique(y))
        max_sample = min(np.floor(len(y)*(cv-1.1)/cv),10000)
        global sample_size
        sample_size = max_sample
        len_sample_size = 1 #len(sample_size)
        mean_rf = np.zeros((len_sample_size,cv), dtype=float)
        mean_kdf = np.zeros((len_sample_size,cv), dtype=float)
        mean_ece_rf = np.zeros((len_sample_size,cv), dtype=float)
        mean_ece_kdf = np.zeros((len_sample_size,cv), dtype=float)
        mean_kappa_rf = np.zeros((len_sample_size,cv), dtype=float)
        mean_kappa_kdf = np.zeros((len_sample_size,cv), dtype=float)


        error_rf = np.zeros((len_sample_size,reps), dtype=float)
        error_kdf = np.zeros((len_sample_size,reps), dtype=float)
        ece_rf = np.zeros((len_sample_size,reps), dtype=float)
        ece_kdf = np.zeros((len_sample_size,reps), dtype=float)
        kappa_rf = np.zeros((len_sample_size,reps), dtype=float)
        kappa_kdf = np.zeros((len_sample_size,reps), dtype=float)

        skf = StratifiedKFold(n_splits=cv)

        fold = 0
        for train_index, test_index in skf.split(X_cur, y):
            X_train, X_test = X_cur[train_index], X_cur[test_index]
            y_train, y_test = y[train_index], y[test_index]
            total_sample = X_train.shape[0]
            X_train = X_train.reshape(-1, 1) #scikit correction when only 1 feature is being considered 
            X_test = X_test.reshape(-1, 1)

            jj = 0 
            sample = sample_size

            #for jj,sample in enumerate(sample_size):
                #print('sample numer'+str(sample))

            if total_sample<sample:
                continue

            for ii in range(reps):
                train_idx =  get_stratified_samples(y_train, sample)
                        
                model_rf = rf(n_estimators=n_estimators).fit(X_train[train_idx], y_train[train_idx])
                proba_rf = model_rf.predict_proba(X_test)
                predicted_label = np.argmax(proba_rf, axis = 1)
                ece_rf[jj][ii] = get_ece(proba_rf, predicted_label, y_test)
                error_rf[jj][ii] = 1 - np.mean(y_test==predicted_label)
                kappa_rf[jj][ii] = cohen_kappa_score(predicted_label, y_test)

                model_kdf = kdf(kwargs={'n_estimators':n_estimators})
                model_kdf.fit(X_train[train_idx], y_train[train_idx])
                proba_kdf = model_kdf.predict_proba(X_test)
                predicted_label = np.argmax(proba_kdf, axis = 1)
                ece_kdf[jj][ii] = get_ece(proba_kdf, predicted_label, y_test)
                error_kdf[jj][ii] = 1 - np.mean(y_test==predicted_label)    
                kappa_kdf[jj][ii] = cohen_kappa_score(predicted_label, y_test)

            mean_rf[jj][fold] = np.mean(error_rf[jj])   
            #var_rf[jj] = np.var(error_rf[jj], ddof=1)
            mean_kdf[jj][fold] = np.mean(error_kdf[jj])   
            #var_kdf[jj] = np.var(error_kdf[jj], ddof=1)
            mean_kappa_rf[jj][fold] = np.mean(kappa_rf[jj])
            mean_kappa_kdf[jj][fold] = np.mean(kappa_kdf[jj])

            mean_ece_rf[jj][fold] = np.mean(ece_rf[jj])   
            #var_ece_rf[jj] = np.var(ece_rf[jj], ddof=1)
            mean_ece_kdf[jj][fold] = np.mean(ece_kdf[jj])   
            #var_ece_kdf[jj] = np.var(ece_kdf[jj], ddof=1)
            folds.append(fold)
            samples.append(sample)
            dims.append(dim)
            features.append(i+1)
            err_rf.append(np.ravel(mean_rf))
            err_kdf.append(np.ravel(mean_kdf))
            fold += 1
        
        print("Accuracy for feature {} is: {} with RF".format(i+1, 1-np.ravel(mean_rf)))
        print("Accuracy for feature {} is: {} with KDF".format(i+1, 1-np.ravel(mean_kdf)))

    df['error_rf'] = err_rf
    df['error_kdf'] = err_kdf
    df['fold'] = folds
    df['sample'] = samples
    df['feature'] = features


    df.to_csv(folder+'/'+'openML_cc18_one_feature_at_a_time'+str(task_id)+'.csv')
        
    #%%

folder = 'testing_openml'#'result_robust_cov'
#os.mkdir(folder)
cv = 5
reps = 10
n_estimators = 500
task_id = 3918
df = pd.DataFrame() 
#%%
experiment(task_id, folder)
