from src.precision_of_t import precision_of_t
from src.plot_preparations import plot_preparations
import numpy as np
from matplotlib import pyplot as plt

"""
This module contains several functions, 
connected to computation and output of precision. 
It is still under construction. 
"""

def compute_multi_precision_of_t(true_array: np.array,
                           est_dict: dict):
    precision_dict = {}
    bias_dict = {}
    mean_dict = {}
    mse_dict = {}
    variance_dict = {}

    for i in range(len(est_dict)):
        name = tuple(est_dict.items())[i][0]
        precision_dict[name] = precision_of_t(true_array, tuple(est_dict.items())[i][1], par_list="")

    for i in range(len(precision_dict)):
        name = tuple(precision_dict.items())[i][0]
        bias_dict[str(name)] = precision_dict.get(name).get('bias')

    for i in range(len(precision_dict)):
        name = tuple(precision_dict.items())[i][0]
        mean_dict[str(name)] = precision_dict.get(name).get('mean')

    for i in range(len(precision_dict)):
        name = tuple(precision_dict.items())[i][0]
        mse_dict[str(name)] = precision_dict.get(name).get('mse')

    for i in range(len(precision_dict)):
        name = tuple(precision_dict.items())[i][0]
        variance_dict[str(name)] = precision_dict.get(name).get('variance')

    return {'bias': bias_dict,
            'mean': mean_dict,
            'mse': mse_dict,
            'variance': variance_dict
    }

def plot_precision_of_t(precision_dict: dict,
                        true_array: np.array,
                        x_array: np.array,
                        x_label="t_par",
                        y_label="value",
                        par_list=""):
    plt.style.use('seaborn')
    for i in range(len(precision_dict)):
        name = tuple(precision_dict.items())[i][0]
        value = tuple(precision_dict.items())[i][1]
        plt.plot(x_array, value, marker='o', label=name)
        file_name, caption = plot_preparations(par_list=par_list, title='multi_'+y_label)

    if y_label == 'bias':
        plt.axhline(y=0, color='black', linestyle='-', linewidth=2)
    if y_label == 'mean':
        plt.plot(x_array, true_array, marker='o', label="true_array")

    plt.title(y_label)
    plt.tight_layout()
    plt.xlabel(x_label + '\n' + caption)
    plt.ylabel(y_label)
    plt.legend()
    plt.savefig(fname=file_name, dpi=300, bbox_inches='tight')
    plt.close()

def plot_multi_precision_of_t(precision_dict: dict,
                              true_array: np.array,
                              x_array: np.array,
                              x_label="t_par",
                              par_list=""):
    for i in range(len(precision_dict)):
        name = tuple(precision_dict.items())[i][0]
        plot_precision_of_t(precision_dict.get(name),
                            true_array=true_array,
                            x_label=x_label,
                            y_label=name,
                            par_list=par_list,
                            x_array=x_array)

def compute_and_save_multi_precision_of_t(true_array: np.array,
                                          est_dict: dict,
                                          x_array: np.array,
                                          par_list="",
                                          x_label="t_par"):
    precision_dict = compute_multi_precision_of_t(true_array, est_dict)
    plot_multi_precision_of_t(precision_dict=precision_dict,
                              true_array=true_array,
                              x_label=x_label,
                              par_list=par_list,
                              x_array=x_array)


if __name__ == '__main__':
    compute_and_save_multi_precision_of_t([1,2,3],
                                        {'est_double_array_1': [[1,2,3], [4,5,6], [7,8,9]],
                                         'est_double_array_2': [[4,23,5], [1,64,2], [9, 0, 1]]},
                                         x_label="t_par",
                                         x_array=[100,200,300])
