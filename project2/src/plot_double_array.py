from src.plot_preparations import plot_preparations
import matplotlib.pyplot as plt


def plot_double_array(x_array,
                      hat_double_array,
                      true_array,
                      title,
                      x_label,
                      par_list,
                      axis='column',
                      true_label='True value',
                      y_label='value'):
    """
    Plots rows or columns of two-dimensional arrays in the same axes and saves image in the standard place. 
    :param x_array: values for x axis.
    :param hat_double_array: a double array containing the values to be plotted. 
    :param true_array: one more array to be plotted, with a special status. Not plotted if empty. 
    :param title: a title of a plot to be saved. 
    :param x_label: label of x axis. 
    :param par_list: a list of parameters to be listed in caption and used for file name composition.  
    :param true_label: a label of true array, to be used in legend. Not used if true array is empty. 
    :param y_label: a label for y axis. 
    """
                          
    file_name, caption = plot_preparations(title=title, par_list=par_list)

    if axis == 'row':
        hat_double_array = hat_double_array.T

    plt.style.use('seaborn')

    for ax_value in range(hat_double_array.shape[1]):
        plt.plot(x_array, hat_double_array[:, ax_value])

    plt.plot(x_array, true_array, color="black", linewidth=2,
             label=true_label)

    plt.xlabel(x_label + '\n' + caption)
    plt.ylabel(y_label)
    plt.title(title)

    plt.legend(framealpha=1, frameon=False)

    plt.tight_layout()

    plt.savefig(file_name, dpi=300, bbox_inches='tight')

    plt.close()
