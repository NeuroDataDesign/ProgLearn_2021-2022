import numpy as np
from sklearn.datasets import make_blobs
import numpy as np
from skmultiflow.trees import HoeffdingTreeClassifier

# from skgarden import MondrianForestClassifier
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
from sdtf import StreamDecisionForest
from sklearn.tree import DecisionTreeClassifier
from river import tree


def run(mc_rep, n_test):
    n_xor = 2500
    n_rxor = 2500
    mean_error = np.zeros((8, 75))
    for i in range(mc_rep):
        errors = experiment(n_xor, n_rxor, n_test)
        mean_error += errors
        print(mean_error.shape)
    return mean_error / mc_rep


def experiment(n_xor, n_rxor, n_test):
    X_xor, y_xor = generate_gaussian_parity(n_xor)
    X_rxor, y_rxor = generate_gaussian_parity(
        n_rxor, angle_params=np.pi / 4
    )  # 45 degree
    X_xor_2, y_xor_2 = generate_gaussian_parity(n_xor)
    test_x_xor, test_y_xor = generate_gaussian_parity(n_test)
    test_x_rxor, test_y_rxor = generate_gaussian_parity(n_test, angle_params=np.pi / 4)
    # concatenate into stream
    X_stream = np.concatenate((X_xor, X_rxor, X_xor_2), axis=0)
    y_stream = np.concatenate((y_xor, y_rxor, y_xor_2), axis=0)
    ht = tree.HoeffdingTreeClassifier(grace_period=2, split_confidence=1e-05)
    # mf = MondrianForestClassifier(n_estimators=10)
    sdt = DecisionTreeClassifier()
    sdf = StreamDecisionForest()
    errors = np.zeros((8, int(X_stream.shape[0] / 100)))
    # print(errors)
    for i in range(int(X_stream.shape[0] / 100)):
        # print(i)
        X = X_stream[i * 100 : (i + 1) * 100]
        y = y_stream[i * 100 : (i + 1) * 100]
        for j in range(X.shape[0]):
            X_t = X[j]
            y_t = y[j]
            idx = range(1024)
            X_t = dict(zip(idx, X_t))
            # print("{}{}".format(X_t,y_t))
            ht.learn_one(X_t, y_t)
        xor_y_hat = np.zeros(test_x_xor.shape[0])
        for j in range(test_x_xor.shape[0]):
            xor_y_hat[j] = ht.predict_one(test_x_xor[j])
        rxor_y_hat = np.zeros(test_x_rxor.shape[0])
        for j in range(test_x_rxor.shape[0]):
            rxor_y_hat[j] = ht.predict_one(test_x_rxor[j])

        # ht.partial_fit(X,y,classes=[0,1])
        sdt.partial_fit(X, y, classes=[0, 1])
        sdf.partial_fit(X, y, classes=[0, 1])
        # mf.fit(X,y)
        # predict xor
        # xor_y_hat = ht.predict(test_x_xor)
        # xor_y_hat_mf = mf.predict(test_x_xor)
        sdt_xor_y_hat = sdt.predict(test_x_xor)
        sdf_xor_y_hat = sdf.predict(test_x_xor)
        # predict rxor
        # rxor_y_hat = ht.predict(test_x_rxor)
        # rxor_y_hat_mf = mf.predict(test_x_rxor)
        sdt_rxor_y_hat = sdt.predict(test_x_rxor)
        sdf_rxor_y_hat = sdf.predict(test_x_rxor)
        # return errors
        errors[0, i] = 1 - np.mean(xor_y_hat == test_y_xor)  # HT xor  error
        errors[1, i] = 1 - np.mean(rxor_y_hat == test_y_rxor)  # HT rxor error
        # errors[2,i]=1-np.mean(xor_y_hat_mf == test_y_xor) # MF xor error
        # errors[3,i]=1-np.mean(rxor_y_hat_mf == test_y_rxor) # MF rxor error
        errors[4, i] = 1 - np.mean(sdt_xor_y_hat == test_y_xor)  # SDT xor error
        errors[5, i] = 1 - np.mean(sdt_rxor_y_hat == test_y_rxor)  # SDT rxor error
        errors[6, i] = 1 - np.mean(sdf_xor_y_hat == test_y_xor)  # SDF xor error
        errors[7, i] = 1 - np.mean(sdf_rxor_y_hat == test_y_rxor)  # SDF rxor error
    return errors


#####PLOTTING


def plot_error(mean_error):
    algorithms = [
        "Hoeffding Tree ",
        "Mondrian Forest",
        "Stream Decision Tree",
        "Stream Decision Forest",
    ]
    fontsize = 30
    labelsize = 28
    ls = ["-", "--"]
    colors = sns.color_palette("Set1", n_colors=2)
    fig = plt.figure(figsize=(21, 14))
    gs = fig.add_gridspec(14, 21)
    ax1 = fig.add_subplot(gs[7:, :6])
    # Hoeffding Tree XOR
    ax1.plot(
        (100 * np.arange(1, 76, step=1)).astype(int),
        mean_error[0],
        label=algorithms[0],
        c="m",
        ls=ls[np.sum(1 > 1).astype(int)],
        lw=3,
    )
    # Mondrian Forest XOR
    ax1.plot(
        (100 * np.arange(1, 76, step=1)).astype(int),
        mean_error[2],
        label=algorithms[1],
        c="c",
        ls=ls[np.sum(1 > 1).astype(int)],
        lw=3,
    )
    # Stream Decision Tree XOR
    ax1.plot(
        (100 * np.arange(1, 76, step=1)).astype(int),
        mean_error[4],
        label=algorithms[2],
        c="g",
        ls=ls[np.sum(1 > 1).astype(int)],
        lw=3,
    )
    # Stream Decision Forest XOR
    ax1.plot(
        (100 * np.arange(1, 76, step=1)).astype(int),
        mean_error[6],
        label=algorithms[3],
        c="r",
        ls=ls[np.sum(1 > 1).astype(int)],
        lw=3,
    )
    ax1.set_ylabel("Generalization Error (XOR)", fontsize=fontsize)
    # ax1.legend(loc="upper left", fontsize=20, frameon=False)
    ax1.set_xlabel("Total Sample Size", fontsize=fontsize)
    ax1.tick_params(labelsize=labelsize)
    ax1.set_yscale("log")
    ax1.yaxis.set_major_formatter(ScalarFormatter())
    ax1.set_yticks([0.1, 0.3, 0.5, 0.9])
    ax1.set_xticks([2500, 5000, 7500])
    ax1.axvline(x=2500, c="gray", linewidth=1.5, linestyle="dashed")
    ax1.axvline(x=5000, c="gray", linewidth=1.5, linestyle="dashed")
    ax1.set_title("XOR", fontsize=30)

    right_side = ax1.spines["right"]
    right_side.set_visible(False)
    top_side = ax1.spines["top"]
    top_side.set_visible(False)

    ax1.text(750, np.mean(ax1.get_ylim()) + 0.1, "%s" % "XOR", fontsize=26)
    ax1.text(2700, np.mean(ax1.get_ylim()) + 0.1, "%s" % "RXOR", fontsize=26)
    ax1.text(5100, np.mean(ax1.get_ylim()) + 0.1, "%s" % "XOR", fontsize=26)

    ######## RXOR
    ax1 = fig.add_subplot(gs[7:, 8:14])
    # Hoeffding Tree XOR
    ax1.plot(
        (100 * np.arange(1, 76, step=1)).astype(int),
        mean_error[1],
        label=algorithms[0],
        c="m",
        ls=ls[np.sum(1 > 1).astype(int)],
        lw=3,
    )
    # Mondrian Forest XOR
    ax1.plot(
        (100 * np.arange(1, 76, step=1)).astype(int),
        mean_error[3],
        label=algorithms[1],
        c="c",
        ls=ls[np.sum(1 > 1).astype(int)],
        lw=3,
    )
    # Stream Decision Tree XOR
    ax1.plot(
        (100 * np.arange(1, 76, step=1)).astype(int),
        mean_error[5],
        label=algorithms[2],
        c="g",
        ls=ls[np.sum(1 > 1).astype(int)],
        lw=3,
    )
    # Stream Decision Forest XOR
    ax1.plot(
        (100 * np.arange(1, 76, step=1)).astype(int),
        mean_error[7],
        label=algorithms[3],
        c="r",
        ls=ls[np.sum(1 > 1).astype(int)],
        lw=3,
    )

    ax1.set_ylabel("Generalization Error (%s)" % "RXOR", fontsize=fontsize)
    ax1.legend(bbox_to_anchor=(1.05, 1.0), loc="upper left", fontsize=20, frameon=False)
    ax1.set_xlabel("Total Sample Size", fontsize=fontsize)
    ax1.tick_params(labelsize=labelsize)
    ax1.set_yscale("log")
    ax1.yaxis.set_major_formatter(ScalarFormatter())
    ax1.set_yticks([0.1, 0.3, 0.5, 0.9])
    ax1.set_xticks([2500, 5000, 7500])
    ax1.axvline(x=2500, c="gray", linewidth=1.5, linestyle="dashed")
    ax1.axvline(x=5000, c="gray", linewidth=1.5, linestyle="dashed")
    right_side = ax1.spines["right"]
    right_side.set_visible(False)
    top_side = ax1.spines["top"]
    top_side.set_visible(False)

    ax1.text(750, np.mean(ax1.get_ylim()) + 0.1, "%s" % "XOR", fontsize=26)
    ax1.text(2700, np.mean(ax1.get_ylim()) + 0.1, "%s" % "RXOR", fontsize=26)
    ax1.text(5100, np.mean(ax1.get_ylim()) + 0.1, "%s" % "XOR", fontsize=26)

    ax1.set_title("RXOR", fontsize=30)


#### DATA GENERATION
"""From proglearn/sims/gaussian_sim.py"""


def _generate_2d_rotation(theta=0):
    R = np.array([[np.cos(theta), np.sin(theta)], [-np.sin(theta), np.cos(theta)]])

    return R


def generate_gaussian_parity(
    n_samples,
    centers=None,
    class_label=None,
    cluster_std=0.25,
    angle_params=None,
    random_state=None,
):
    """
    Generate 2-dimensional Gaussian XOR distribution.
    (Classic XOR problem but each point is the
    center of a Gaussian blob distribution)
    Parameters
    ----------
    n_samples : int
        Total number of points divided among the four
        clusters with equal probability.
    centers : array of shape [n_centers,2], optional (default=None)
        The coordinates of the ceneter of total n_centers blobs.
    class_label : array of shape [n_centers], optional (default=None)
        class label for each blob.
    cluster_std : float, optional (default=1)
        The standard deviation of the blobs.
    angle_params: float, optional (default=None)
        Number of radians to rotate the distribution by.
    random_state : int, RandomState instance, default=None
        Determines random number generation for dataset creation. Pass an int
        for reproducible output across multiple function calls.
    Returns
    -------
    X : array of shape [n_samples, 2]
        The generated samples.
    y : array of shape [n_samples]
        The integer labels for cluster membership of each sample.
    """

    if random_state != None:
        np.random.seed(random_state)

    if centers == None:
        centers = np.array([(-0.5, 0.5), (0.5, 0.5), (-0.5, -0.5), (0.5, -0.5)])

    if class_label == None:
        class_label = [0, 1, 1, 0]

    blob_num = len(class_label)

    # get the number of samples in each blob with equal probability
    samples_per_blob = np.random.multinomial(
        n_samples, 1 / blob_num * np.ones(blob_num)
    )

    X, y = make_blobs(
        n_samples=samples_per_blob,
        n_features=2,
        centers=centers,
        cluster_std=cluster_std,
    )

    for blob in range(blob_num):
        y[np.where(y == blob)] = class_label[blob]

    if angle_params != None:
        R = _generate_2d_rotation(angle_params)
        X = X @ R

    return X, y
