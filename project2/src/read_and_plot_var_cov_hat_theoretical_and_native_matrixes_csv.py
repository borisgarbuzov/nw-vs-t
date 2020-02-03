import numpy as np
import re
from src.plot_arrays import plot_arrays
from src.read_matrix import read_matrix


def read_and_plot_var_cov_hat_theoretical_and_native_matrixes_csv(noise_type: str, what_lag: int, fix_number_of_lags=None) -> None:
    """
    Read from csv and plot two var cov hat matrixes:
    The first is theoretical
    the second if native
    the third is native  means
    plot 3 lines.  The first is theoretical var cov hat,
                        the second is native var cov hat
                        the third is native var cov hat means

    :param noise_type: type of noise 'gaussian' or 'bernoulli'
    :param what_lag: for example, 0,1,2
    """
    theoretical = read_matrix(name='var_cov_hat_theoretical_matrix_{}.csv'.format(noise_type), index_col='lag')
    native_matrix = read_matrix(name='var_cov_hat_native_matrix_{}.csv'.format(noise_type), index_col='lag')

    sample_size_array = [int(re.sub("[^0-9]", "", sample_size)) for
                         sample_size in theoretical.columns]

    theoretical_lag = np.array(theoretical.loc['lag {}'.format(what_lag)])

    native_matrix_lag = np.array(native_matrix.loc['lag {}'.format(what_lag)])

    for index, sample_size in enumerate(sample_size_array):
        theoretical_lag[index] *= sample_size
        native_matrix_lag[index] *= sample_size

    native_matrix_lag_mean = np.full(shape=native_matrix_lag.shape, fill_value=float(np.mean(native_matrix_lag)))

    arrays_dict = {
        'theoretical with lag {}'.format(what_lag): theoretical_lag,
        'native matrix with lag {}'.format(what_lag): native_matrix_lag,
        'native matrix mean with lag {}'.format(what_lag): native_matrix_lag_mean
    }

    plot_arrays(x_array=sample_size_array,
                arrays_dict=arrays_dict,
                title="theoretical vs native matrixes with lag={} and {} noise".format(what_lag, noise_type),
                x_label="sample size")

    print('Made picture "theoretical vs native matrixes with lag={} and {} noise"'.format(what_lag, noise_type))


if __name__ == '__main__':
    read_and_plot_var_cov_hat_theoretical_and_native_matrixes_csv(noise_type='gaussian', what_lag=0)
    read_and_plot_var_cov_hat_theoretical_and_native_matrixes_csv(noise_type='gaussian', what_lag=1)
    read_and_plot_var_cov_hat_theoretical_and_native_matrixes_csv(noise_type='gaussian', what_lag=2)
    read_and_plot_var_cov_hat_theoretical_and_native_matrixes_csv(noise_type='bernoulli', what_lag=0)
    read_and_plot_var_cov_hat_theoretical_and_native_matrixes_csv(noise_type='bernoulli', what_lag=1)
    read_and_plot_var_cov_hat_theoretical_and_native_matrixes_csv(noise_type='bernoulli', what_lag=2)
