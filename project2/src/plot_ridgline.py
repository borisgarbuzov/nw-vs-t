from src.plot_preparations import plot_preparations
import matplotlib.pyplot as plt
import joypy


def plot_ridgline(hat_double_array,
                  title,
                  x_label,
                  par_list,
                  bins=10):
    """
    Plots several histograms in progression one under another, agreed by hirizontal axis. 
    Is based on joypy library. 
    :param hat_double_array: a double array, containg the plotted values. Columns correspond to histograms. 
    :param title: a title for the image to be saved. 
    :param x_label: a label for the common x axis. 
    :param par_list: a dictionary of parameteres and their values that go to the caption. 
    :param bins: a number of bins to be used for histograms. 
    """
    file_name, caption = plot_preparations(title=title, par_list=par_list)

    plt.style.use('seaborn')

    joypy.joyplot(hat_double_array, hist=True, bins=bins, overlap=0, grid=True,
                  legend=False)

    plt.xlabel(x_label + '\n' + caption)
    plt.title(title)

    plt.tight_layout()

    plt.savefig(file_name, dpi=300, bbox_inches='tight')

    plt.close()
