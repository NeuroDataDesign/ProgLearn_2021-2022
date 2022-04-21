import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import seaborn as sns
import numpy as np
import ast
import numpy as np
import random
from math import log2, ceil
from proglearn.forest import LifelongClassificationForest, UncertaintyForest
from proglearn.sims import *
from proglearn.progressive_learner import ProgressiveLearner
from proglearn.deciders import SimpleArgmaxAverage
from proglearn.transformers import (
    TreeClassificationTransformer,
    NeuralClassificationTransformer,
)
from proglearn.voters import TreeClassificationVoter, KNNClassificationVoter

from sdtf import StreamDecisionForest

from joblib import Parallel, delayed
import re

## Generating Batch Results


def experiment_batch(
    n_task1,
    n_task2,
    n_test=1000,
    task1_angle=0,
    task2_angle=np.pi / 2,
    n_trees=10,
    max_depth=None,
    random_state=None,
):

    """
    A function to do SynF experiment between two tasks
    where the task data is generated using Gaussian parity.
    Parameters
    ----------
    n_task1 : int
        Total number of train sample for task 1.
    n_task2 : int
        Total number of train dsample for task 2
    n_test : int, optional (default=1000)
        Number of test sample for each task.
    task1_angle : float, optional (default=0)
        Angle in radian for task 1.
    task2_angle : float, optional (default=numpy.pi/2)
        Angle in radian for task 2.
    n_trees : int, optional (default=10)
        Number of total trees to train for each task.
    max_depth : int, optional (default=None)
        Maximum allowable depth for each tree.
    random_state : int, RandomState instance, default=None
        Determines random number generation for dataset creation. Pass an int
        for reproducible output across multiple function calls.
    Returns
    -------
    errors : array of shape [6]
        Elements of the array is organized as single task error task1,
        multitask error task1, single task error task2,
        multitask error task2, naive UF error task1,
        naive UF task2.
    """

    if n_task1 == 0 and n_task2 == 0:
        raise ValueError("Wake up and provide samples to train!!!")

    if random_state != None:
        np.random.seed(random_state)

    errors = np.zeros(6, dtype=float)

    progressive_learner = LifelongClassificationForest(default_n_estimators=n_trees)
    uf1 = LifelongClassificationForest(default_n_estimators=n_trees)
    naive_uf = LifelongClassificationForest(default_n_estimators=n_trees)
    uf2 = LifelongClassificationForest(default_n_estimators=n_trees)

    # source data
    X_task1, y_task1 = generate_gaussian_parity(n_task1, angle_params=task1_angle)
    test_task1, test_label_task1 = generate_gaussian_parity(
        n_test, angle_params=task1_angle
    )

    # target data
    X_task2, y_task2 = generate_gaussian_parity(n_task2, angle_params=task2_angle)
    test_task2, test_label_task2 = generate_gaussian_parity(
        n_test, angle_params=task2_angle
    )

    if n_task1 == 0:
        progressive_learner.add_task(X_task2, y_task2, n_estimators=n_trees)
        uf2.add_task(X_task2, y_task2, n_estimators=n_trees)

        errors[0] = 0.5
        errors[1] = 0.5

        uf_task2 = uf2.predict(test_task2, task_id=0)
        l2f_task2 = progressive_learner.predict(test_task2, task_id=0)

        errors[2] = 1 - np.mean(uf_task2 == test_label_task2)
        errors[3] = 1 - np.mean(l2f_task2 == test_label_task2)

        errors[4] = 0.5
        errors[5] = 1 - np.mean(uf_task2 == test_label_task2)
    elif n_task2 == 0:
        progressive_learner.add_task(X_task1, y_task1, n_estimators=n_trees)
        uf1.add_task(X_task1, y_task1, n_estimators=n_trees)

        uf_task1 = uf1.predict(test_task1, task_id=0)
        l2f_task1 = progressive_learner.predict(test_task1, task_id=0)

        errors[0] = 1 - np.mean(uf_task1 == test_label_task1)
        errors[1] = 1 - np.mean(l2f_task1 == test_label_task1)

        errors[2] = 0.5
        errors[3] = 0.5

        errors[4] = 1 - np.mean(uf_task1 == test_label_task1)
        errors[5] = 0.5
    else:
        progressive_learner.add_task(X_task1, y_task1, n_estimators=n_trees)
        progressive_learner.add_task(X_task2, y_task2, n_estimators=n_trees)

        uf1.add_task(X_task1, y_task1, n_estimators=2 * n_trees)
        uf2.add_task(X_task2, y_task2, n_estimators=2 * n_trees)

        naive_uf_train_x = np.concatenate((X_task1, X_task2), axis=0)
        naive_uf_train_y = np.concatenate((y_task1, y_task2), axis=0)
        naive_uf.add_task(naive_uf_train_x, naive_uf_train_y, n_estimators=n_trees)

        uf_task1 = uf1.predict(test_task1, task_id=0)
        l2f_task1 = progressive_learner.predict(test_task1, task_id=0)
        uf_task2 = uf2.predict(test_task2, task_id=0)
        l2f_task2 = progressive_learner.predict(test_task2, task_id=1)
        naive_uf_task1 = naive_uf.predict(test_task1, task_id=0)
        naive_uf_task2 = naive_uf.predict(test_task2, task_id=0)

        errors[0] = 1 - np.mean(uf_task1 == test_label_task1)
        errors[1] = 1 - np.mean(l2f_task1 == test_label_task1)
        errors[2] = 1 - np.mean(uf_task2 == test_label_task2)
        errors[3] = 1 - np.mean(l2f_task2 == test_label_task2)
        errors[4] = 1 - np.mean(naive_uf_task1 == test_label_task1)
        errors[5] = 1 - np.mean(naive_uf_task2 == test_label_task2)

    return errors


# Batch XNOR
def run_batch_xnor(
    mc_rep, n_test, n_trees, n_xor, n_xnor, mean_error, std_error, mean_te, std_te
):
    for i, n1 in enumerate(n_xor):
        # print('starting to compute %s xor\n'%n1)
        # run experiment in parallel
        error = np.array(
            Parallel(n_jobs=-1, verbose=0)(
                delayed(experiment_batch)(n1, 0, max_depth=ceil(log2(n1)))
                for _ in range(mc_rep)
            )
        )
        # extract relevant data and store in arrays
        mean_error[:, i] = np.mean(error, axis=0)
        std_error[:, i] = np.std(error, ddof=1, axis=0)
        mean_te[0, i] = np.mean(error[:, 0]) / np.mean(error[:, 1])
        mean_te[1, i] = np.mean(error[:, 2]) / np.mean(error[:, 3])
        mean_te[2, i] = np.mean(error[:, 0]) / np.mean(error[:, 4])
        mean_te[3, i] = np.mean(error[:, 2]) / np.mean(error[:, 5])

        # initialize learning on n-xor data
        if n1 == n_xor[-1]:
            for j, n2 in enumerate(n_xnor):
                # print('starting to compute %s nxor\n'%n2)
                # run experiment in parallel
                error = np.array(
                    Parallel(n_jobs=-1, verbose=0)(
                        delayed(experiment_batch)(n1, n2, max_depth=ceil(log2(750)))
                        for _ in range(mc_rep)
                    )
                )
                # extract relevant data and store in arrays
                mean_error[:, i + j + 1] = np.mean(error, axis=0)
                std_error[:, i + j + 1] = np.std(error, ddof=1, axis=0)
                mean_te[0, i + j + 1] = np.mean(error[:, 0]) / np.mean(error[:, 1])
                mean_te[1, i + j + 1] = np.mean(error[:, 2]) / np.mean(error[:, 3])
                mean_te[2, i + j + 1] = np.mean(error[:, 0]) / np.mean(error[:, 4])
                mean_te[3, i + j + 1] = np.mean(error[:, 2]) / np.mean(error[:, 5])

    return mean_error, std_error, mean_te, std_te


## Batch R-XOR
def run_batch_rxor(
    mc_rep, n_test, n_trees, n_xor, n_rxor, mean_error, std_error, mean_te, std_te
):
    for i, n1 in enumerate(n_xor):
        # print('starting to compute %s xor\n'%n1)
        error = np.array(
            Parallel(n_jobs=-1, verbose=0)(
                delayed(experiment_batch)(
                    n1, 0, task2_angle=np.pi / 4, max_depth=ceil(log2(n1))
                )
                for _ in range(mc_rep)
            )
        )
        mean_error[:, i] = np.mean(error, axis=0)
        std_error[:, i] = np.std(error, ddof=1, axis=0)
        mean_te[0, i] = np.mean(error[:, 0]) / np.mean(error[:, 1])
        mean_te[1, i] = np.mean(error[:, 2]) / np.mean(error[:, 3])
        mean_te[2, i] = np.mean(error[:, 0]) / np.mean(error[:, 4])
        mean_te[3, i] = np.mean(error[:, 2]) / np.mean(error[:, 5])

        if n1 == n_xor[-1]:
            for j, n2 in enumerate(n_rxor):
                # print('starting to compute %s rxor\n'%n2)

                error = np.array(
                    Parallel(n_jobs=-1, verbose=0)(
                        delayed(experiment_batch)(
                            n1, n2, task2_angle=np.pi / 4, max_depth=ceil(log2(750))
                        )
                        for _ in range(mc_rep)
                    )
                )
                mean_error[:, i + j + 1] = np.mean(error, axis=0)
                std_error[:, i + j + 1] = np.std(error, ddof=1, axis=0)
                mean_te[0, i + j + 1] = np.mean(error[:, 0]) / np.mean(error[:, 1])
                mean_te[1, i + j + 1] = np.mean(error[:, 2]) / np.mean(error[:, 3])
                mean_te[2, i + j + 1] = np.mean(error[:, 0]) / np.mean(error[:, 4])
                mean_te[3, i + j + 1] = np.mean(error[:, 2]) / np.mean(error[:, 5])

    return mean_error, std_error, mean_te, std_te


## Generating Streaming Results


## get single task errors for learning efficiency plots


def run_stream_single_task(mc_rep):
    """runs single task error experiments for mc_reps"""
    ste = np.zeros((4, 59))
    for i in range(mc_rep):
        errors = exp_stream_single_task()
        ste += errors
    return ste / mc_rep


def exp_stream_single_task():
    """generates single task errors for learning efficieny plots"""
    # 0 single task xor (rxor experiment)
    # 1 single task xor (xnor experiment)
    # 2 single task rxor
    # 3 single task xnor

    test_x_xor, test_y_xor = generate_gaussian_parity(1000)
    test_x_rxor, test_y_rxor = generate_gaussian_parity(1000, angle_params=np.pi / 4)
    test_x_xnor, test_y_xnor = generate_gaussian_parity(1000, angle_params=np.pi / 2)
    X_xor, y_xor = generate_gaussian_parity(25)
    X_rxor, y_rxor = generate_gaussian_parity(25, angle_params=np.pi / 4)
    X_xnor, y_xnor = generate_gaussian_parity(25, angle_params=np.pi / 4)

    xor_forest = LifelongClassificationForest(default_n_estimators=10)
    rxor_forest = LifelongClassificationForest(default_n_estimators=10)
    xnor_forest = LifelongClassificationForest(default_n_estimators=10)
    single_task_errors = np.zeros((4, 59))
    for i in range(29):
        x, y = generate_gaussian_parity(25)
        if i == 0:
            xor_forest.add_task(X_xor, y_xor, n_estimators=10, task_id=0)
        else:
            xor_forest.update_task(x, y, task_id=0)
        xor_y_hat = xor_forest.predict(test_x_xor, task_id=0)
        single_task_errors[0, i] = 1 - np.mean(xor_y_hat == test_y_xor)
        single_task_errors[1, i] = 1 - np.mean(xor_y_hat == test_y_xor)
        single_task_errors[2, i] = 0.5
        single_task_errors[3, i] = 0.5

    for i in range(30):
        x_rxor_, y_rxor_ = generate_gaussian_parity(25, angle_params=np.pi / 4)
        x_xnor_, y_xnor_ = generate_gaussian_parity(25, angle_params=np.pi / 2)
        if i == 0:
            rxor_forest.add_task(X_rxor, y_rxor, n_estimators=10, task_id=0)
            xnor_forest.add_task(X_xnor, y_xnor, n_estimators=10, task_id=0)
        else:
            rxor_forest.update_task(x_rxor_, y_rxor_, task_id=0)
            xnor_forest.update_task(x_xnor_, y_xnor_, task_id=0)
        xor_y_hat = xor_forest.predict(test_x_xor, task_id=0)
        rxor_y_hat = rxor_forest.predict(test_x_rxor, task_id=0)
        xnor_y_hat = xnor_forest.predict(test_x_xnor, task_id=0)

        single_task_errors[0, i + 29] = 1 - np.mean(xor_y_hat == test_y_xor)
        single_task_errors[1, i + 29] = 1 - np.mean(xor_y_hat == test_y_xor)
        single_task_errors[2, i + 29] = 1 - np.mean(rxor_y_hat == test_y_rxor)
        single_task_errors[3, i + 29] = 1 - np.mean(xnor_y_hat == test_y_xnor)

    return single_task_errors


def run_stream(exp_type, mc_rep):
    # 0 sdf xor error
    # 1 sdf rxor error
    # 2 synf xor error
    # 3 synf rxor error
    n_test = 1000
    n_xor = 750
    n_rxor = 750
    if exp_type == "XNOR":
        angle = np.pi / 2
    else:  # Rxor
        angle = np.pi / 4
    mean_error = np.zeros((4, 59))
    for i in range(mc_rep):
        errors = experiment_stream(angle, n_xor, n_rxor, n_test)
        mean_error += errors
    return mean_error / mc_rep


def experiment_stream(angle, n_xor, n_rxor, n_test):
    X_xor, y_xor = generate_gaussian_parity(n_xor)
    X_rxor, y_rxor = generate_gaussian_parity(n_rxor, angle_params=angle)
    test_x_xor, test_y_xor = generate_gaussian_parity(n_test)
    test_x_rxor, test_y_rxor = generate_gaussian_parity(n_test, angle_params=angle)
    X_stream = np.concatenate((X_xor, X_rxor), axis=0)
    y_stream = np.concatenate((y_xor, y_rxor), axis=0)

    sdf = StreamDecisionForest(n_estimators=10)
    synf = LifelongClassificationForest(default_n_estimators=10)

    errors = np.zeros((4, 59))

    for i in range(59):
        X = X_stream[i * 25 : (i + 1) * 25]
        y = y_stream[i * 25 : (i + 1) * 25]
        sdf.partial_fit(X, y, classes=[0, 1])
        # SDF
        sdf_xor_y_hat = sdf.predict(test_x_xor)
        sdf_rxor_y_hat = sdf.predict(test_x_rxor)
        errors[0, i] = 1 - np.mean(sdf_xor_y_hat == test_y_xor)
        errors[1, i] = 1 - np.mean(sdf_rxor_y_hat == test_y_rxor)  # synF
        if i == 0:
            synf.add_task(X, y, n_estimators=10, task_id=0)
            synf_xor_y_hat = synf.predict(test_x_xor, task_id=0)
        elif i < (n_xor / 25):
            synf.update_task(X, y, task_id=0)
            synf_xor_y_hat = synf.predict(test_x_xor, task_id=0)
        elif i == (n_xor / 25):
            synf.add_task(X, y, n_estimators=10, task_id=1)
            synf_xor_y_hat = synf.predict(test_x_xor, task_id=0)
            synf_rxor_y_hat = synf.predict(test_x_rxor, task_id=1)
        elif i < (n_xor + n_rxor) / 25:
            synf.update_task(X, y, task_id=1)
            synf_xor_y_hat = synf.predict(test_x_xor, task_id=0)
            synf_rxor_y_hat = synf.predict(test_x_rxor, task_id=1)

        if i < (n_xor / 25):
            errors[2, i] = 1 - np.mean(synf_xor_y_hat == test_y_xor)
        if i >= (n_xor / 25):
            errors[2, i] = 1 - np.mean(synf_xor_y_hat == test_y_xor)
            errors[3, i] = 1 - np.mean(synf_rxor_y_hat == test_y_rxor)
    return errors


def bte_v_angle(angle_sweep, task1_sample, task2_sample, mc_rep):
    mean_te = np.zeros(45, dtype=float)
    for ii, angle in enumerate(angle_sweep):
        error = np.array(
            Parallel(n_jobs=-1, verbose=0)(
                delayed(experiment_batch)(
                    task1_sample,
                    task2_sample,
                    task2_angle=angle * np.pi / 180,
                    max_depth=ceil(log2(task1_sample)),
                )
                for _ in range(mc_rep)
            )
        )

        mean_te[ii] = np.mean(error[:, 0]) / np.mean(error[:, 1])
    return mean_te


def plot_bte_v_angle(mean_te, mc_reps):
    angle_sweep = range(0, 90, 2)

    sns.set_context("talk")
    fig, ax = plt.subplots(1, 1, figsize=(8, 8))
    ax.plot(angle_sweep, mean_te, linewidth=3, c="r")
    ax.set_xticks([0, 45, 90])
    ax.set_title("BLE v Angle: {} MC repetitions".format(mc_reps))
    ax.set_xlabel("Angle of Rotation (Degrees)")
    ax.set_ylabel("Backward Learning Efficiency (XOR)")
    ax.hlines(1, 0, 90, colors="gray", linestyles="dashed", linewidth=1.5)

    ax.set_yticks([0.9, 1, 1.1, 1.2])
    ax.set_ylim(0.89, 1.22)
    log_lbl = np.round(np.log([0.9, 1, 1.1, 1.2]), 2)
    labels = [item.get_text() for item in ax.get_yticklabels()]

    for ii, _ in enumerate(labels):
        labels[ii] = str(log_lbl[ii])

    ax.set_yticklabels(labels)

    right_side = ax.spines["right"]
    right_side.set_visible(False)
    top_side = ax.spines["top"]
    top_side.set_visible(False)



def load_ble_v_angle(file):
    data = []
    with open(file) as f:
        lines = f.readlines()
        for line in lines:
            new_line = line.strip("[")
            new_line = new_line.replace("]",'')
            data.append(new_line.split())
    flat_data = [float(item) for sublist in data for item in sublist]
    split_data = np.zeros(45)
    mc_reps = int(len(flat_data)/45)
    for i in range(mc_reps):
        split_data+= np.array(flat_data[i * 45 : (i + 1) * 45])

    split_data = split_data/mc_reps
    return mc_reps, split_data 




def stream_ble_v_angle(angle_sweep, task1_sample, task2_sample, mc_rep): 
    for i in range(mc_rep):
        ble = np.zeros(45)
        for j, angle in enumerate(angle_sweep):
            ble[j] = stream_ble_v_angle_exp(angle * np.pi / 180, task1_sample, task2_sample)
        write_ble_v_angle("ble_v_angle/04_20_22.txt", ble)



def stream_ble_v_angle_exp(angle, task1_sample, task2_sample):
    synf_single_task = LifelongClassificationForest(default_n_estimators=20)
    synf_two_task = LifelongClassificationForest(default_n_estimators=10)
    x, y = gen_gauss_parity(25, None)
    x2, y2 = gen_gauss_parity(25,angle)
    x_test, y_test = gen_gauss_parity(1000, None)
    synf_single_task.add_task(x, y, task_id=0, classes= [0,1])
    synf_two_task.add_task(x, y, task_id=0, classes= [0,1])
    for i in range(int(task1_sample / 25) - 1):
        x, y = gen_gauss_parity(25, None)
        synf_single_task.update_task(x, y, task_id=0)
        synf_two_task.update_task(x, y, task_id=0)
    synf_two_task.add_task(x2, y2, task_id=1, classes= [0,1])
    for i in range(int(task2_sample / 25) - 1):
        x2, y2 = gen_gauss_parity(25, angle)
        synf_two_task.update_task(x2, y2, task_id=1)
    y1_hat = synf_single_task.predict(x_test, task_id=0)
    y2_hat = synf_two_task.predict(x_test, task_id=0)
    single_task_error = 1 - np.mean(y1_hat == y_test)
    two_task_error = 1 - np.mean(y2_hat == y_test)
    return single_task_error / two_task_error

def gen_gauss_parity(n, angle):
 '''Generate gaussian parity ensuring there is atleast one sample from each class'''
 x,y = generate_gaussian_parity(n, angle_params=angle)
 if len(np.unique(y))<2:
    return gen_gauss_parity(n, angle)
 return x,y

def write_ble_v_angle(filename, acc_ls):
    output = open(filename, "a")
    output.write(str(acc_ls)+ "\n")



def stream_ble_v_nsamples(task1_samples, task2_samples, task2_angle,update_samples, mc_rep):
    for i in range(mc_rep):
        for t1_n in task1_samples:
            for u_n in update_samples:
                ble = stream_ble_v_nsamples_exp(t1_n, task2_samples, task2_angle, u_n)
                save_file = "ble_v_nsamples/t1-{}_u-{}_t2-{}_xnor.csv".format(t1_n, u_n, task2_samples)
                with open(save_file, 'a') as f:
                    np.savetxt(f, ble)

def stream_ble_v_nsamples_exp(task1_sample, task2_samples, task2_angle, update_samples):
    ble = np.zeros((1,int(task2_samples/50)),dtype=float)
    synf_single_task = LifelongClassificationForest(default_n_estimators=20)
    synf_two_task = LifelongClassificationForest(default_n_estimators=10)
    x, y = gen_gauss_parity(50, None)
    x2, y2 = gen_gauss_parity(50,angle=task2_angle)
    x_test, y_test = gen_gauss_parity(1000, None)
    synf_single_task.add_task(x, y, task_id=0)
    synf_two_task.add_task(x, y, task_id=0)
    for i in range(int((task1_sample -50)/update_samples)):
        x, y = gen_gauss_parity(update_samples, None)
        synf_single_task.update_task(x, y, task_id=0, inputclasses=[0,1])
        synf_two_task.update_task(x, y, task_id=0, inputclasses=[0,1])
    synf_two_task.add_task(x2, y2, task_id=1)
    j = 0
    for i in range(int((task2_samples-50)/update_samples)):
        x2, y2 = gen_gauss_parity(update_samples, angle=task2_angle)
        synf_two_task.update_task(x2, y2, task_id=1, inputclasses=[0,1])
        if (i*update_samples)% 50 == 0 and i>0:
            j+=1
            y1_hat = synf_single_task.predict(x_test, task_id=0)
            y2_hat = synf_two_task.predict(x_test, task_id=0)
            single_task_error = 1 - np.mean(y1_hat == y_test)
            two_task_error = 1 - np.mean(y2_hat == y_test)
            ble[0,j] = single_task_error/two_task_error
    return ble










## PLOTTING
def load_result(filename):
    """Loads results from specified file"""
    inputs = open(filename, "r")
    lines = inputs.readlines()
    ls = []
    for line in lines:
        ls.append(ast.literal_eval(line))
    return ls


def load_data():
    prefixes = ["stream_synf/", "sdf/", "batch_synf/", "df/"]
    xnor_mean_errors = []
    rxor_mean_errors = []
    rxor_single_task_errors = []
    xnor_single_task_errors = []
    for prefix in prefixes:
        xor_error = load_result(prefix + "xnor_exp_xor_error.txt")
        xnor_error = load_result(prefix + "xnor_exp_xnor_error.txt")
        xnor_mean_errors.append(xor_error)
        xnor_mean_errors.append(xnor_error)
        xor_error_rxor = load_result(prefix + "rxor_exp_xor_error.txt")
        rxor_error = load_result(prefix + "rxor_exp_rxor_error.txt")
        rxor_mean_errors.append(xor_error_rxor)
        rxor_mean_errors.append(rxor_error)
        single_task_error_rxor = load_result(prefix + "rxor_single_task_error_rxor.txt")
        single_task_error_xnor = load_result(prefix + "xnor_single_task_error_xnor.txt")
        rxor_single_task_errors.append(single_task_error_rxor)
        xnor_single_task_errors.append(single_task_error_xnor)
    for prefix in prefixes:
        single_task_error_xor = load_result(prefix + "rxor_single_task_error_xor.txt")
        single_task_error_xnor = load_result(prefix + "xnor_single_task_error_xor.txt")
        rxor_single_task_errors.append(single_task_error_xor)
        xnor_single_task_errors.append(single_task_error_xor)
    return (
        rxor_mean_errors,
        xnor_mean_errors,
        rxor_single_task_errors,
        xnor_single_task_errors,
    )


def get_mean_te(multi_task_errors, single_task_errors):
    te = np.empty((8, 59))
    #FTE
    te[0, :] = np.array(single_task_errors[0]) / np.array(multi_task_errors[1])
    # stream synf
    te[1, :] = np.array(single_task_errors[1]) / np.array(multi_task_errors[3])
    # SDF
    te[2, :] = np.array(single_task_errors[2]) / np.array(multi_task_errors[5])
    # batch synf
    te[3, :] = np.array(single_task_errors[3]) / np.array(multi_task_errors[7])
    # batch df]

    # bte

    te[4, :] = np.array(single_task_errors[4]) / np.array(multi_task_errors[0])
    # stream synf
    te[5, :] = np.array(single_task_errors[5]) / np.array(multi_task_errors[2])
    # SDF
    te[6, :] = np.array(single_task_errors[6]) / np.array(multi_task_errors[4])
    # batch synf
    te[7, :] = np.array(single_task_errors[7]) / np.array(multi_task_errors[6])
    # batch df]

    return te


def write_result(filename, acc_ls):
    output = open(filename, "w")
    for acc in acc_ls:
        output.write(str(acc)+ "\n")



def run_gaussian_experiments(mc_rep):
    ##### Running The batch XNOR experiment######
    n_test = 1000
    n_trees = 10
    n_xor = (100 * np.arange(0.25, 7.50, step=0.25)).astype(int)
    n_xnor = (100 * np.arange(0.25, 7.75, step=0.25)).astype(int)
    mean_error = np.zeros((6, len(n_xor) + len(n_xnor)))
    std_error = np.zeros((6, len(n_xor) + len(n_xnor)))
    mean_te = np.zeros((4, len(n_xor) + len(n_xnor)))
    std_te = np.zeros((4, len(n_xor) + len(n_xnor)))

    # run the experiment
    mean_error, std_error, mean_te, std_te = run_batch_xnor(
        mc_rep, n_test, n_trees, n_xor, n_xnor, mean_error, std_error, mean_te, std_te
    )


    # 0 single task error task 1 (batch synf and df)
    # 1 synf xor 
    # 2 single task error task 2 
    # 3 synf rxor
    # 4 RF xor 
    # 5 RF rxor

    # write results to appropriate folders for XNOR experiment 
    write_result("batch_synf/xnor_single_task_error_xor.txt", mean_error[0])
    write_result("df/xnor_single_task_error_xor.txt", mean_error[0])
    write_result("batch_synf/xnor_exp_xor_error.txt", mean_error[1])
    write_result("batch_synf/xnor_single_task_error_xnor.txt", mean_error[2])
    write_result("df/xnor_single_task_error_xnor.txt", mean_error[2])
    write_result("batch_synf/xnor_exp_xnor_error.txt", mean_error[3])
    write_result("df/xnor_exp_xor_error.txt", mean_error[4])
    write_result("df/xnor_exp_xnor_error.txt", mean_error[5])

    ##### Running The batch RXOR experiment######

    mean_error = np.zeros((6, len(n_xor) + len(n_xnor)))
    std_error = np.zeros((6, len(n_xor) + len(n_xnor)))
    mean_te = np.zeros((4, len(n_xor) + len(n_xnor)))
    std_te = np.zeros((4, len(n_xor) + len(n_xnor)))

    mean_error, std_error, mean_te, std_te = run_batch_rxor(
        mc_rep, n_test, n_trees, n_xor, n_xnor, mean_error, std_error, mean_te, std_te
    )

    # write results to appropriate folders for RXOR experiment 
    write_result("batch_synf/rxor_single_task_error_xor.txt", mean_error[0])
    write_result("df/rxor_single_task_error_xor.txt", mean_error[0])
    write_result("batch_synf/rxor_exp_xor_error.txt", mean_error[1])
    write_result("batch_synf/rxor_single_task_error_rxor.txt", mean_error[2])
    write_result("df/rxor_single_task_error_rxor.txt", mean_error[2])
    write_result("batch_synf/rxor_exp_rxor_error.txt", mean_error[3])
    write_result("df/rxor_exp_xor_error.txt", mean_error[4])
    write_result("df/rxor_exp_rxor_error.txt", mean_error[5])

    ##### running the streaming RXOR experiment #####
    mean_error = run_stream("RXOR", mc_rep)
    single_task_mean_error = run_stream_single_task(mc_rep)

    # write results to appropriate folders for XNOR experiment 
    write_result("sdf/rxor_exp_xor_error.txt", mean_error[0]) 
    write_result("sdf/rxor_exp_rxor_error.txt", mean_error[1])
    write_result("stream_synf/rxor_exp_xor_error.txt", mean_error[2])
    write_result("stream_synf/rxor_exp_rxor_error.txt", mean_error[3])
    write_result("stream_synf/rxor_single_task_error_xor.txt", single_task_mean_error[0])
    write_result("sdf/rxor_single_task_error_xor.txt", single_task_mean_error[0])
    write_result("stream_synf/rxor_single_task_error_rxor.txt", single_task_mean_error[2])
    write_result("sdf/rxor_single_task_error_rxor.txt", single_task_mean_error[2])

    ##### running the streaming XNOR experiment #####

    mean_error = run_stream("XNOR", mc_rep)
    # write results to appropriate folders for XNOR experiment 
    write_result("sdf/xnor_exp_xor_error.txt", mean_error[0])
    write_result("sdf/xnor_exp_xnor_error.txt", mean_error[1])
    write_result("stream_synf/xnor_exp_xor_error.txt", mean_error[2])
    write_result("stream_synf/xnor_exp_xnor_error.txt", mean_error[3])
    write_result("stream_synf/xnor_single_task_error_xor.txt", single_task_mean_error[0])
    write_result("sdf/xnor_single_task_error_xor.txt", single_task_mean_error[0])
    write_result("stream_synf/xnor_single_task_error_xnor.txt", single_task_mean_error[3])
    write_result("sdf/xnor_single_task_error_xnor.txt", single_task_mean_error[3])




def plot_error(mean_error, experiment, transfer_efficiencies):
    """Plot Generalization Errors for experiment type (RXOR or XNOR)"""
    algorithms = [
        "Stream Synergistic Forest",
        "Stream Decision Forest",
        "Batch Synergistic Forest",
        "Batch Decision Forest",
    ]
    fontsize = 30
    labelsize = 28
    ls = ["-", "--"]
    colors = sns.color_palette("bright")
    fig = plt.figure(figsize=(26, 14))
    gs = fig.add_gridspec(14, 26)
    ax1 = fig.add_subplot(gs[7:, :5])
    # Stream Synergistic Forest XOR
    ax1.plot(
        (100 * np.arange(0.25, 15, step=0.25)).astype(int),
        mean_error[0],
        label=algorithms[0],
        c=colors[3],
        ls=ls[1],
        lw=3,
    )
    # Stream Decision Forest XOR
    ax1.plot(
        (100 * np.arange(0.25, 15, step=0.25)).astype(int),
        mean_error[2],
        label=algorithms[1],
        c=colors[2],
        ls=ls[1],
        lw=3,
    )
    # Batch Synergistic Forest XOR
    ax1.plot(
        (100 * np.arange(0.25, 15, step=0.25)).astype(int),
        mean_error[4],
        label=algorithms[2],
        c=colors[3],
        ls=ls[0],
        lw=3,
    )
    # Batch Decision Forest XOR
    ax1.plot(
        (100 * np.arange(0.25, 15, step=0.25)).astype(int),
        mean_error[6],
        label=algorithms[3],
        c=colors[2],
        ls=ls[0],
        lw=3,
    )

    ax1.set_ylabel("Generalization Error (XOR)", fontsize=fontsize)
    ax1.set_xlabel("Total Sample Size", fontsize=fontsize)
    ax1.tick_params(labelsize=labelsize)
    ax1.set_yscale("log")
    ax1.yaxis.set_major_formatter(ScalarFormatter())
    ax1.set_yticks([0.1, 0.3, 0.5, 0.9])
    ax1.set_xticks([0, 750, 1500])
    ax1.axvline(x=750, c="gray", linewidth=1.5, linestyle="dashed")
    ax1.axvline(x=1500, c="gray", linewidth=1.5, linestyle="dashed")

    right_side = ax1.spines["right"]
    right_side.set_visible(False)
    top_side = ax1.spines["top"]
    top_side.set_visible(False)

    ax1.text(200, np.mean(ax1.get_ylim()) + 0.5, "XOR", fontsize=26)
    ax1.text(850, np.mean(ax1.get_ylim()) + 0.5, experiment, fontsize=26)

    ######## RXOR
    ax1 = fig.add_subplot(gs[7:, 7:12])
    rxor_range = (100 * np.arange(0.25, 15, step=0.25)).astype(int)[30:]
    # Stream Synergistic Forest RXOR
    ax1.plot(
        rxor_range,
        mean_error[1, 30:],
        label=algorithms[0],
        c=colors[3],
        ls=ls[1],
        lw=3,
    )
    # Stream Decision Forest RXOR
    ax1.plot(
        rxor_range,
        mean_error[3, 30:],
        label=algorithms[1],
        c=colors[2],
        ls=ls[1],
        lw=3,
    )
    # Batch Synergistic Forest RXOR
    ax1.plot(
        rxor_range,
        mean_error[5, 30:],
        label=algorithms[2],
        c=colors[3],
        ls=ls[0],
        lw=3,
    )
    # Batch Decision Forest RXOR
    ax1.plot(
        rxor_range,
        mean_error[7, 30:],
        label=algorithms[3],
        c=colors[2],
        ls=ls[0],
        lw=3,
    )
    ax1.set_ylabel("Generalization Error (%s)" % experiment, fontsize=fontsize)
    ax1.legend(
        bbox_to_anchor=(1, -0.25),
        loc="upper center",
        fontsize=20,
        ncol=4,
        frameon=False,
    )
    ax1.set_xlabel("Total Sample Size", fontsize=fontsize)
    ax1.tick_params(labelsize=labelsize)
    ax1.set_yscale("log")
    ax1.yaxis.set_major_formatter(ScalarFormatter())
    ax1.set_yticks([0.1, 0.3, 0.5, 0.9])
    ax1.set_xticks([0, 750, 1500])
    ax1.axvline(x=750, c="gray", linewidth=1.5, linestyle="dashed")
    ax1.axvline(x=1500, c="gray", linewidth=1.5, linestyle="dashed")
    right_side = ax1.spines["right"]
    right_side.set_visible(False)
    top_side = ax1.spines["top"]
    top_side.set_visible(False)

    ax1.text(200, np.mean(ax1.get_ylim()) + 0.5, "XOR", fontsize=26)
    ax1.text(850, np.mean(ax1.get_ylim()) + 0.5, experiment, fontsize=26)

    #### Transfer Efficiency
    ax1 = fig.add_subplot(gs[7:, 14:19])
    algorithms = [
        "Stream Synergistic Forest TE",
        "Stream Decision Forest TE",
        "Batch Synergistic Forest TE",
        "Batch Decision Forest TE",
    ]
    rxor_range = (100 * np.arange(0.25, 15, step=0.25)).astype(int)[30:]
    # Stream Synergistic Forest RXOR
    ax1.plot(
        rxor_range,
        transfer_efficiencies[0,30:],
        label=algorithms[0],
        c=colors[3],
        ls=ls[1],
        lw=3,
    )
    # Stream Decision Forest RXOR
    ax1.plot(
        rxor_range,
        transfer_efficiencies[1,30:],
        label=algorithms[1],
        c=colors[2],
        ls=ls[1],
        lw=3,
    )
    # Batch Synergistic Forest RXOR
    ax1.plot(
        rxor_range,
        transfer_efficiencies[2,30:],
        label=algorithms[2],
        c=colors[3],
        ls=ls[0],
        lw=3,
    )
    # Batch Decision Forest RXOR
    ax1.plot(
        rxor_range,
        transfer_efficiencies[3,30:],
        label=algorithms[3],
        c=colors[2],
        ls=ls[0],
        lw=3,
    )

    ax1.set_ylabel("Log Forward Learning Efficiency", fontsize=fontsize)
    ax1.set_xlabel("Total Sample Size", fontsize=fontsize)
    ax1.tick_params(labelsize=labelsize)
    # ax1.set_yscale("log")
    ax1.yaxis.set_major_formatter(ScalarFormatter())
    ax1.set_yticks([-1, 0, 1])
    ax1.set_xlim(-1, 1)
    ax1.set_xticks([0, 750, 1500])
    ax1.axvline(x=750, c="gray", linewidth=1.5, linestyle="dashed")
    ax1.axvline(x=1500, c="gray", linewidth=1.5, linestyle="dashed")
    right_side = ax1.spines["right"]
    right_side.set_visible(False)
    top_side = ax1.spines["top"]
    top_side.set_visible(False)
    ax1.axhline(y=0, c="gray", linewidth=1.5, linestyle="dashed")

    if experiment == "XNOR":
        ax1.text(200, np.mean(ax1.get_ylim()) + 2, "XOR", fontsize=26)
        ax1.text(850, np.mean(ax1.get_ylim()) + 2, experiment, fontsize=26)
    else:
        ax1.text(200, np.mean(ax1.get_ylim()) + 1.25, "XOR", fontsize=26)
        ax1.text(850, np.mean(ax1.get_ylim()) + 1.25, experiment, fontsize=26)

    #### BACKWARDS Transfer Efficiency
    ax1 = fig.add_subplot(gs[7:, 21:])
    algorithms = [
        "Stream Synergistic Forest TE",
        "Stream Decision Forest TE",
        "Batch Synergistic Forest TE",
        "Batch Decision Forest TE",
    ]
    rxor_range = (100 * np.arange(0.25, 15, step=0.25)).astype(int)
    # Stream Synergistic Forest RXOR
    ax1.plot(
        rxor_range,
        transfer_efficiencies[4,:],
        label=algorithms[0],
        c=colors[3],
        ls=ls[1],
        lw=3,
    )
    # Stream Decision Forest RXOR
    ax1.plot(
        rxor_range,
        transfer_efficiencies[5, :],
        label=algorithms[1],
        c=colors[2],
        ls=ls[1],
        lw=3,
    )
    # Batch Synergistic Forest RXOR
    ax1.plot(
        rxor_range,
        transfer_efficiencies[6,:],
        label=algorithms[2],
        c=colors[3],
        ls=ls[0],
        lw=3,
    )
    # Batch Decision Forest RXOR
    ax1.plot(
        rxor_range,
        transfer_efficiencies[7,:],
        label=algorithms[3],
        c=colors[2],
        ls=ls[0],
        lw=3,
    )

    ax1.set_ylabel("Log Backward Learning Efficiency", fontsize=fontsize)
    ax1.set_xlabel("Total Sample Size", fontsize=fontsize)
    ax1.tick_params(labelsize=labelsize)
    # ax1.set_yscale("log")
    ax1.yaxis.set_major_formatter(ScalarFormatter())
    ax1.set_yticks([-1, 0, 1])
    ax1.set_xlim(-1, 1)
    ax1.set_xticks([25, 750, 1500])
    ax1.axvline(x=750, c="gray", linewidth=1.5, linestyle="dashed")
    ax1.axvline(x=1500, c="gray", linewidth=1.5, linestyle="dashed")
    right_side = ax1.spines["right"]
    right_side.set_visible(False)
    top_side = ax1.spines["top"]
    top_side.set_visible(False)
    ax1.axhline(y=0, c="gray", linewidth=1.5, linestyle="dashed")

    if experiment == "XNOR":
        ax1.text(200, np.mean(ax1.get_ylim()) + 2.0, "XOR", fontsize=26)
        ax1.text(850, np.mean(ax1.get_ylim()) + 2.0, experiment, fontsize=26)
    else:
        ax1.text(200, np.mean(ax1.get_ylim()) + 1.5, "XOR", fontsize=26)
        ax1.text(850, np.mean(ax1.get_ylim()) + 1.5, experiment, fontsize=26)
