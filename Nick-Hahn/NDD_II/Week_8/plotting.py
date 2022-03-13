import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import seaborn as sns
import numpy as np
import ast


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
    return (
        rxor_mean_errors,
        xnor_mean_errors,
        rxor_single_task_errors,
        xnor_single_task_errors,
    )


def get_mean_te(multi_task_errors, single_task_errors):
    te = np.empty((4, 59))
    te[0, :] = np.log(
        np.array(single_task_errors[0]) / np.array(multi_task_errors[1])
    )  # stream synf
    te[1, :] = np.log(
        np.array(single_task_errors[1]) / np.array(multi_task_errors[3])
    )  # SDF
    te[2, :] = np.log(
        np.array(single_task_errors[2]) / np.array(multi_task_errors[5])
    )  # batch synf
    te[3, :] = np.log(
        np.array(single_task_errors[3]) / np.array(multi_task_errors[7])
    )  # batch df]

    return te


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
    fig = plt.figure(figsize=(21, 14))
    gs = fig.add_gridspec(14, 21)
    ax1 = fig.add_subplot(gs[7:, :6])
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
    ax1 = fig.add_subplot(gs[7:, 8:14])
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
        bbox_to_anchor=(0.5, -0.25),
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
    ax1 = fig.add_subplot(gs[7:, 16:])
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
        transfer_efficiencies[0, 30:],
        label=algorithms[0],
        c=colors[3],
        ls=ls[1],
        lw=3,
    )
    # Stream Decision Forest RXOR
    ax1.plot(
        rxor_range,
        transfer_efficiencies[1, 30:],
        label=algorithms[1],
        c=colors[2],
        ls=ls[1],
        lw=3,
    )
    # Batch Synergistic Forest RXOR
    ax1.plot(
        rxor_range,
        transfer_efficiencies[2, 30:],
        label=algorithms[2],
        c=colors[3],
        ls=ls[0],
        lw=3,
    )
    # Batch Decision Forest RXOR
    ax1.plot(
        rxor_range,
        transfer_efficiencies[3, 30:],
        label=algorithms[3],
        c=colors[2],
        ls=ls[0],
        lw=3,
    )

    ax1.set_ylabel("log Learning Efficiency", fontsize=fontsize)
    ax1.set_xlabel("Total Sample Size", fontsize=fontsize)
    ax1.tick_params(labelsize=labelsize)
    # ax1.set_yscale("log")
    ax1.yaxis.set_major_formatter(ScalarFormatter())
    ax1.set_yticks([-3, 0, 1])
    ax1.set_xlim(-1, 1)
    ax1.set_xticks([0, 750, 1500])
    ax1.axvline(x=750, c="gray", linewidth=1.5, linestyle="dashed")
    ax1.axvline(x=1500, c="gray", linewidth=1.5, linestyle="dashed")
    right_side = ax1.spines["right"]
    right_side.set_visible(False)
    top_side = ax1.spines["top"]
    top_side.set_visible(False)
    ax1.axhline(y=0, c="gray", linewidth=1.5, linestyle="dashed")
    ax1.text(200, np.mean(ax1.get_ylim()) + 2.1, "XOR", fontsize=26)
    ax1.text(850, np.mean(ax1.get_ylim()) + 2.1, experiment, fontsize=26)
