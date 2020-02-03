import numpy as np
import re
from src.plot_arrays import plot_arrays
from src.read_matrix import read_matrix


def read_and_plot_var_cov_hat_csv(noise_type: str):
    """
    M. Reads 2 CSV's and saves one image by calling plot function. 
    CSV1 is about block estimate of var(covHat). 
    CSV2 is about natively simulated var(covHat). 
    Currently does not work because file names changed. 
    Image is 2 curves in the same axes - naitve and block estimate.  
    :param noise_type: type of noise 'gaussian' or 'bernoulli'
    """
    bootstrap = read_matrix(name="var_cov_hat_bootstrap_matrix_batch_size_formula.csv", index_col='lag')
    native_matrix = read_matrix(name='var_cov_hat_native_matrix_{}.csv'.format(noise_type), index_col='lag')

    sample_size_array = [int(re.sub("[^0-9]", "", sample_size)) for
                         sample_size in bootstrap.columns]

    bootstrap_lag_0 = np.array(bootstrap.loc['lag 0'])
    native_matrix_lag_0 = np.array(native_matrix.loc['lag 0'])

    for index, sample_size in enumerate(sample_size_array):
        native_matrix_lag_0[index] *= sample_size

    arrays_dict = {"bootstrap with lag 0": bootstrap_lag_0,
                   "native matrix with lag 0": native_matrix_lag_0}

    plot_arrays(x_array=sample_size_array,
                arrays_dict=arrays_dict,
                title="bootstrap vs native matrix with {} noise batch size by power".format(noise_type),
                x_label="sample size")

    print('Made picture "bootstrap vs native matrix with {} noise batch size by power"'.format(noise_type))


if __name__ == '__main__':
    read_and_plot_var_cov_hat_csv(noise_type='gaussian')
