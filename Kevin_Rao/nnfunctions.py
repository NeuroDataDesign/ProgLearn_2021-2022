"""
Neural network functions for scene segmentation. Based off of 

"""
from keras import layers
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from keras.callbacks import EarlyStopping
from keras.optimizers import Adam
from keras.layers import Conv2D, Conv2DTranspose, MaxPool2D, concatenate
from proglearn.deciders import SimpleArgmaxAverage
from proglearn.progressive_learner import ProgressiveLearner
from proglearn.transformers import (
    NeuralClassificationTransformer,
)
from keras import Model
from proglearn.voters import KNNClassificationVoter

from proglearn.network import LifelongClassificationNetwork

from tensorflow.keras.backend import clear_session

def run_fte_bte_exp(data_x, data_y, which_task, num_tasks, network, shift=0):

    df_total = []

    for slot in range(
        1
    ):  # Rotates the batch of training samples that are used from each class in each task
        train_x, train_y, test_x, test_y = cross_val_data(data_x, data_y, shift, slot)

        clear_session()  # clear GPU memory before each run, to avoid OOM error

        default_transformer_class = NeuralClassificationTransformer

        default_transformer_kwargs = {
            "network": network,
            "euclidean_layer_idx": -2,
            "loss": "categorical_crossentropy",
            "optimizer": Adam(3e-4),
            "fit_kwargs": {
                "epochs": 100,
                "callbacks": [EarlyStopping(patience=5, monitor="val_loss")],
                "verbose": False,
                "validation_split": 0.33,
                "batch_size": 32,
            },
        }
        default_voter_class = KNNClassificationVoter
        default_voter_kwargs = {"k": int(np.log2(360))}
        default_decider_class = SimpleArgmaxAverage

        p_learner = ProgressiveLearner(
            default_transformer_class=default_transformer_class,
            default_transformer_kwargs=default_transformer_kwargs,
            default_voter_class=default_voter_class,
            default_voter_kwargs=default_voter_kwargs,
            default_decider_class=default_decider_class,
        )

        df = fte_bte_experiment(
            train_x,
            train_y,
            test_x,
            test_y,
            shift,
            slot,
            num_tasks,
            p_learner,
            which_task,
            acorn=12345,
        )

        df_total.append(df)

    return df_total

def fte_bte_experiment(
    train_x,
    train_y,
    test_x,
    test_y,
    shift,
    slot,
    num_tasks,
    p_learner,
    which_task,
    acorn=None,
):

    # We initialize lists to store the results
    df = pd.DataFrame()
    accuracies_across_tasks = []

    # Declare the progressive learner model (Odif or Odin)
    learner = p_learner

    for task_num in range((which_task - 1), num_tasks):
        # print("Starting Task {} For Shift {} For Slot {}".format(task_num, shift, slot))
        if acorn is not None:
            np.random.seed(acorn)

        # If first task, add task.
        if task_num == (which_task - 1):
            learner.add_task(
                X=train_x[(task_num * 360) : ((task_num + 1) * 360)],
                y=train_y[(task_num * 360) : ((task_num + 1) * 360)],
                task_id=task_num,
                num_transformers=1,
                transformer_voter_decider_split=[0.67, 0.33, 0],
                decider_kwargs={
                    "classes": np.unique(
                        train_y[(task_num * 360) : ((task_num + 1) * 360)]
                    )
                },
            )
            t_num = 0
            # Add tasks for all tasks up to current task (task t)
            while t_num < task_num:
                # Make a prediction on task t using the trained learner on test data
                llf_task = learner.predict(
                    test_x[((which_task - 1) * 120) : (which_task * 120), :],
                    task_id=task_num,
                )
                acc = np.mean(
                    llf_task == test_y[((which_task - 1) * 120) : (which_task * 120)]
                )
                accuracies_across_tasks.append(acc)

                learner.add_task(
                    X=train_x[(task_num * 360) : ((task_num + 1) * 360)],
                    y=train_y[(task_num * 360) : ((task_num + 1) * 360)],
                    task_id=t_num,
                    num_transformers=1,
                    transformer_voter_decider_split=[0.67, 0.33, 0],
                    decider_kwargs={
                        "classes": np.unique(
                            train_y[(task_num * 360) : ((task_num + 1) * 360)]
                        )
                    },
                )
    
                # Add task for next task
                t_num = t_num + 1

        else:
            learner.add_task(
                X=train_x[(task_num * 360) : ((task_num + 1) * 360)],
                y=train_y[(task_num * 360) : ((task_num + 1) * 360)],
                task_id=task_num,
                num_transformers=1,
                transformer_voter_decider_split=[0.67, 0.33, 0],
                decider_kwargs={
                    "classes": np.unique(
                        train_y[(task_num * 360) : ((task_num + 1) * 360)]
                    )
                },
            )

        # Make a prediction on task t using the trained learner on test data
        predictions = learner.predict(
            test_x[((which_task - 1) * 120) : (which_task * 120), :],
            task_id=(which_task - 1),
        )
        acc = np.mean(
            predictions == test_y[((which_task - 1) * 120) : (which_task * 120)]
        )
        accuracies_across_tasks.append(acc)
        # print("Accuracy Across Tasks: {}".format(accuracies_across_tasks))

    df["task"] = range(1, num_tasks + 1)
    df["task_accuracy"] = accuracies_across_tasks

    return df

def unet(input_layer, num_classes, num_input_neurons=64):
    conv1 = Conv2D(num_input_neurons, (3,3), activation='relu', padding='same')(input_layer)
    conv1 = Conv2D(num_input_neurons, (3,3), activation='relu', padding='same')(conv1)
    max_pool1 = MaxPool2D((2,2))(conv1)

    conv2 = Conv2D(num_input_neurons * 2, (3,3), activation='relu', padding='same')(max_pool1)
    conv2 = Conv2D(num_input_neurons * 2, (3,3), activation = 'relu', padding='same')(conv2)
    max_pool2 = MaxPool2D((2,2))(conv2)

    conv3 = Conv2D(num_input_neurons * 4, (3,3), activation='relu', padding='same')(max_pool2)
    conv3 = Conv2D(num_input_neurons * 4, (3,3), activation='relu', padding='same')(conv3)
    max_pool3 = MaxPool2D((2,2))(conv3)


    conv4 = Conv2D(num_input_neurons * 8, (3,3), activation='relu', padding='same')(max_pool3)
    conv4 = Conv2D(num_input_neurons * 8, (3,3), activation='relu', padding='same')(conv4)
    max_pool4 = MaxPool2D((2,2))(conv4)


    conv5 = Conv2D(num_input_neurons * 16, (3,3), activation='relu', padding='same')(max_pool4)
    conv5 = Conv2D(num_input_neurons * 16, (3,3), activation='relu', padding='same')(conv5)
    up_conv1 = Conv2DTranspose(num_input_neurons * 8, (3,3),strides=(2,2), activation='relu', padding='same')(conv5)
    up_conv1 = concatenate([up_conv1, conv4])
    up_conv1 = Conv2D(num_input_neurons * 8, (3,3), activation='relu', padding='same')(up_conv1)
    up_conv1 = Conv2D(num_input_neurons * 8, (3,3), activation='relu', padding='same')(up_conv1)

    up_conv2 = Conv2DTranspose(num_input_neurons * 4, (3,3),strides=(2,2), activation='relu', padding='same')(up_conv1)
    up_conv2 = concatenate([up_conv2, conv3])
    up_conv2 = Conv2D(num_input_neurons * 4, (3,3), activation='relu', padding='same')(up_conv2)
    up_conv2 = Conv2D(num_input_neurons * 4, (3,3), activation='relu', padding='same')(up_conv2)

    up_conv3 = Conv2DTranspose(num_input_neurons * 2, (3,3),strides=(2,2), activation='relu', padding='same')(up_conv2)
    up_conv3 = concatenate([up_conv3, conv2])
    up_conv3 = Conv2D(num_input_neurons * 2, (3,3), activation='relu', padding='same')(up_conv3)
    up_conv3 = Conv2D(num_input_neurons * 2, (3,3), activation='relu', padding='same')(up_conv3)

    up_conv4 = Conv2DTranspose(num_input_neurons, (3,3),strides=(2,2), activation='relu', padding='same')(up_conv3)
    up_conv4 = concatenate([up_conv4, conv1])
    up_conv4 = Conv2D(num_input_neurons, (3,3), activation='relu', padding='same')(up_conv4)
    up_conv4 = Conv2D(num_input_neurons, (3,3), activation='relu', padding='same')(up_conv4)

    return Model(inputs = input_layer, outputs = Conv2D(num_classes, (1,1), padding='same', activation='softmax')(up_conv4))

def unet1D(input_layer, num_classes, num_input_neurons=64):
    conv1 = Conv1D(num_input_neurons, 3, activation='relu', padding='same')(input_layer)
    conv1 = Conv1D(num_input_neurons, 3, activation='relu', padding='same')(conv1)
    max_pool1 = MaxPool1D(2)(conv1)

    conv2 = Conv1D(num_input_neurons * 2, 3, activation='relu', padding='same')(max_pool1)
    conv2 = Conv1D(num_input_neurons * 2, 3, activation = 'relu', padding='same')(conv2)
    max_pool2 = MaxPool1D(2)(conv2)

    conv3 = Conv1D(num_input_neurons * 4, 3, activation='relu', padding='same')(max_pool2)
    conv3 = Conv1D(num_input_neurons * 4, 3, activation='relu', padding='same')(conv3)
    max_pool3 = MaxPool1D(2)(conv3)


    conv4 = Conv1D(num_input_neurons * 8, 3, activation='relu', padding='same')(max_pool3)
    conv4 = Conv1D(num_input_neurons * 8, 3, activation='relu', padding='same')(conv4)
    max_pool4 = MaxPool1D(2)(conv4)


    conv5 = Conv1D(num_input_neurons * 16, 3, activation='relu', padding='same')(max_pool4)
    conv5 = Conv1D(num_input_neurons * 16, 3, activation='relu', padding='same')(conv5)
    up_conv1 = Conv1DTranspose(num_input_neurons * 8, 3,strides=2, activation='relu', padding='same')(conv5)
    up_conv1 = concatenate([up_conv1, conv4])
    up_conv1 = Conv1D(num_input_neurons * 8, 3, activation='relu', padding='same')(up_conv1)
    up_conv1 = Conv1D(num_input_neurons * 8, 3, activation='relu', padding='same')(up_conv1)

    up_conv2 = Conv1DTranspose(num_input_neurons * 4, 3,strides=2, activation='relu', padding='same')(up_conv1)
    up_conv2 = concatenate([up_conv2, conv3])
    up_conv2 = Conv1D(num_input_neurons * 4, 3, activation='relu', padding='same')(up_conv2)
    up_conv2 = Conv1D(num_input_neurons * 4, 3, activation='relu', padding='same')(up_conv2)

    up_conv3 = Conv1DTranspose(num_input_neurons * 2, 3,strides=2, activation='relu', padding='same')(up_conv2)
    up_conv3 = concatenate([up_conv3, conv2])
    up_conv3 = Conv1D(num_input_neurons * 2, 3, activation='relu', padding='same')(up_conv3)
    up_conv3 = Conv1D(num_input_neurons * 2, 3, activation='relu', padding='same')(up_conv3)

    up_conv4 = Conv1DTranspose(num_input_neurons, 3,strides=2, activation='relu', padding='same')(up_conv3)
    up_conv4 = concatenate([up_conv4, conv1])
    up_conv4 = Conv1D(num_input_neurons, 3, activation='relu', padding='same')(up_conv4)
    up_conv4 = Conv1D(num_input_neurons, 3, activation='relu', padding='same')(up_conv4)

    return Model(inputs = input_layer, outputs = Conv1D(num_classes, 1, padding='same', activation='sigmoid')(up_conv4))

