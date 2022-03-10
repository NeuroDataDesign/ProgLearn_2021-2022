#%%
import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd
import numpy as np
import openml
from scipy.interpolate import interp1d
from os import listdir, getcwd 
import glob as glob

#%%
files = glob.glob('./openml_res/*.csv')
for file in files: 
    df = pd.read_csv(file)
    file_name = file.split("_")[-1][:-4]
    print(file_name)
    #print(df.head())
    #df_bic = pd.read_csv('simulation_res_BIC.csv')
    # max_sample = int(np.max(df['samples']))
    # #print("Max Samples: ", max_sample)
    # sample_size = np.logspace(
    #         np.log10(2),
    #         np.log10(max_sample),
    #         num=10,
    #         endpoint=True,
    #         dtype=int
    #         )
    sample_size = np.unique(df['samples'])
    #print(sample_size)
    dist_kdf_med = []
    dist_kdf_25_quantile = []
    dist_kdf_75_quantile = []

    dist_kdf_bic_med = []
    dist_kdf_bic_25_quantile = []
    dist_kdf_bic_75_quantile = []

    dist_rf_med = []
    dist_rf_25_quantile = []
    dist_rf_75_quantile = []

    err_kdf_med = []
    err_kdf_25_quantile = []
    err_kdf_75_quantile = []

    err_kdf_bic_med = []
    err_kdf_bic_25_quantile = []
    err_kdf_bic_75_quantile = []

    err_rf_med = []
    err_rf_25_quantile = []
    err_rf_75_quantile = []

    #%%
    for sample in sample_size:
        # print("Current Sample: ", sample)
        # print(df['samples']==sample)
        # print(df['ece_kdf'][df['samples']==sample])
        res_kdf = df['ece_kdf'][df['samples']==sample]
        res_rf = df['ece_rf'][df['samples']==sample]
        #res_kdf_bic = df_bic['hellinger dist kdf'][df_bic['sample']==sample]

        #print(res_kdf)
        dist_kdf_med.append(np.median(res_kdf))
        dist_rf_med.append(np.median(res_rf))
        dist_kdf_25_quantile.append(
            np.quantile(res_kdf,[.25])[0]
        )
        dist_kdf_75_quantile.append(
            np.quantile(res_kdf,[.75])[0]
        )
        dist_rf_25_quantile.append(
            np.quantile(res_rf,[.25])[0]
        )
        dist_rf_75_quantile.append(
            np.quantile(res_rf,[.75])[0]
        )
        '''dist_kdf_bic_med.append(np.median(res_kdf_bic))
        dist_kdf_bic_25_quantile.append(
            np.quantile(res_kdf_bic,[.25])[0]
        )
        dist_kdf_bic_75_quantile.append(
            np.quantile(res_kdf_bic,[.75])[0]
        )'''

        err_rf = df['err_rf'][df['samples']==sample]
        
        err_rf_med.append(np.median(err_rf))
        err_rf_25_quantile.append(
                np.quantile(err_rf,[.25])[0]
            )
        err_rf_75_quantile.append(
            np.quantile(err_rf,[.75])[0]
        )

        err_kdf = df['err_kdf'][df['samples']==sample]

        err_kdf_med.append(np.median(err_kdf))
        err_kdf_25_quantile.append(
                np.quantile(err_kdf,[.25])[0]
            )
        err_kdf_75_quantile.append(
                np.quantile(err_kdf,[.75])[0]
            )

        #err_kdf_bic = df_bic['error kdf'][df_bic['sample']==sample]

        '''err_kdf_bic_med.append(np.median(err_kdf_bic))
        err_kdf_bic_25_quantile.append(
                np.quantile(err_kdf_bic,[.25])[0]
            )
        err_kdf_bic_75_quantile.append(
                np.quantile(err_kdf_bic,[.75])[0]
            )'''
    #%%
    sns.set_context('talk')
    fig, ax = plt.subplots(1,2, figsize=(16,8))

    ax[0].plot(sample_size, dist_kdf_med, c="r", label='KDF')
    #ax[0].plot(sample_size, dist_kdf_bic_med, c="b", label='KDF (bic)')
    ax[0].plot(sample_size, dist_rf_med, c="k", label='RF')

    ax[0].fill_between(sample_size, dist_kdf_25_quantile, dist_kdf_75_quantile, facecolor='r', alpha=.3)
    ax[0].fill_between(sample_size, dist_rf_25_quantile, dist_rf_75_quantile, facecolor='k', alpha=.3)
    #ax[0].fill_between(sample_size, dist_kdf_bic_25_quantile, dist_kdf_bic_75_quantile, facecolor='b', alpha=.3)

    ax[0].set_xscale('log')
    ax[0].set_xlabel('Sample size')
    ax[0].set_ylabel('Expected Calibration Error')

    right_side = ax[0].spines["right"]
    right_side.set_visible(False)
    top_side = ax[0].spines["top"]
    top_side.set_visible(False)

    ax[1].plot(sample_size, err_kdf_med, c="r", label='KDF')
    #ax[1].plot(sample_size, err_kdf_bic_med, c="b", label='KDF (bic)')
    ax[1].plot(sample_size, err_rf_med, c="k", label='RF')

    ax[1].fill_between(sample_size, err_kdf_25_quantile, err_kdf_75_quantile, facecolor='r', alpha=.3)
    ax[1].fill_between(sample_size, err_rf_25_quantile, err_rf_75_quantile, facecolor='k', alpha=.3)
    #ax[1].fill_between(sample_size, err_kdf_bic_25_quantile, err_kdf_bic_75_quantile, facecolor='b', alpha=.3)

    ax[1].set_xscale('log')
    ax[1].set_xlabel('Sample size')
    ax[1].set_ylabel('Generalization error')
    ax[1].legend()

    right_side = ax[1].spines["right"]
    right_side.set_visible(False)
    top_side = ax[1].spines["top"]
    top_side.set_visible(False)
    plt.savefig('./pca_plots/{}.pdf'.format(file_name))