from src.plot_preparations import plot_preparations
import matplotlib.pyplot as plt
import numpy as np


def plot_histograms(arrays_dict: dict,
                    true_value: float,
                    title: str,
                    par_list: dict,
                    true_label="True value",
                    density=True):
    """
    Plots histograms of the arrays in a dictionary. 
    :param true_value: a special point on the x axis to be designated with a black vertical stick. 
    :param title: a title of a plot to be saved. 
    :param par_list: a list of parameters to be listed in caption and used for file name composition.  
    :param true_label: a label of true array, to be used in legend. Not used if true array is empty. 
    """                        
                        
    file_name, caption = plot_preparations(title=title, par_list=par_list)

    plt.style.use('seaborn')

    for label, array in arrays_dict.items():
        if not np.isnan(array).any():
            plt.hist(array, alpha=0.65, density=density, label=label)

    plt.axvline(true_value, color='black', label=true_label, linewidth=3)

    plt.xlabel("values" + '\n' + caption)
    plt.title(title.capitalize())

    # legend automatically choose best place
    plt.legend(framealpha=1, frameon=False)

    plt.tight_layout()

    plt.savefig(file_name, dpi=300, bbox_inches='tight')

    plt.close()
