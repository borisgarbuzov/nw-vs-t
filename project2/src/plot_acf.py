from src.plot_preparations import plot_preparations
import matplotlib.pyplot as plt
import numpy as np


def plot_acf(cov_hat,
             cloud,
             max_lag_array="auto",
             par_list="",
             title="ACF"):
    """
    Plots autocovariance function given in the array. Also shows cloud and labels axes. 
    :param cov_hat: main values of ACF to be plotted. 
    :param cloud: an array of values to be used for cloud depiction. 
    :param max_lag_array: lags to be depicted. 
    :param par_list: a dictionary of name-value pairs to be shown in caption and in file name. 
    :param title: a title to be shown on the plot. 
    """
    if max_lag_array == "auto":
        max_lag_array = [lag for lag in range(len(cov_hat))]

    file_name, caption = plot_preparations(title=title, par_list=par_list)

    plt.style.use('seaborn')

    plt.stem(max_lag_array, cov_hat, use_line_collection=True)

    plt.fill_between(x=max_lag_array, y1=cloud, y2=np.negative(cloud),
                     alpha=0.4)

    plt.xlabel("lags" + '\n' + caption)
    plt.ylabel("covariance")
    plt.title(title)

    plt.tight_layout()

    plt.savefig(file_name, dpi=300, bbox_inches='tight')

    plt.close()
