from src.plot_preparations import plot_preparations
import matplotlib.pyplot as plt
import numpy as np


def plot_arrays(x_array,
                arrays_dict,
                title,
                x_label,
                par_list="",
                true_array=np.array([]),
                true_label="True value",
                y_label='value',
                color_array=np.array([])):
    """
    Plots one-dimensional arrays in the same axes and save image in the standard place. 
    :param x_array: values for x axis.
    :param arrays_dict: a dictionary of arrays to be plotted. Arrays should be of the same length. 
    :param title: a title of a plot to be saved. 
    :param x_label: label of x axis. 
    :param par_list: a list of parameters to be listed in caption and used for file name composition.  
    :param true_array: one more array to be plotted, with a special status. Not plotted if empty. 
    :param true_label: a label of true array, to be used in legend. Not used if true array is empty. 
    :param y_label: a label for y axis.
    :param color_array: unique color for each line
    """
    file_name, caption = plot_preparations(title=title, par_list=par_list)

    if len(color_array):
        if len(color_array) != len(arrays_dict):
            raise ValueError('Length of color_array should be same with length of arrays_dict!')

    plt.style.use('seaborn')

    if not len(color_array):
        for label, array in arrays_dict.items():
            plt.plot(x_array, array, label=label)
    else:
        i = 0
        for label, array in arrays_dict.items():
            plt.plot(x_array, array, label=label, color=color_array[i])
            i += 1

    if len(true_array) > 0:
        plt.plot(x_array, true_array, color="black", linewidth=2,
                 label=true_label)

    plt.xlabel(x_label + '\n' + caption)
    plt.ylabel(y_label)
    plt.title(title)

    # legend automatically choose best place
    plt.legend(framealpha=1, frameon=False)

    plt.tight_layout()

    plt.savefig(file_name, dpi=300, bbox_inches='tight')

    plt.close()


if __name__ == '__main__':
    d = {
        'first': np.random.normal(size=5),
        'second': np.random.normal(size=5)
    }

    plot_arrays(x_array=np.arange(5),
                arrays_dict=d,
                title='somebody once told me',
                x_label="xs",
                y_label="ys",
                color_array=['red', 'blue', 'white'])
