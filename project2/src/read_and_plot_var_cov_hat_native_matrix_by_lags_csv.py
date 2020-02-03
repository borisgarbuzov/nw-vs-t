import numpy as np
import re
from src.plot_arrays import plot_arrays
from src.read_matrix import read_matrix


def read_and_plot_var_cov_hat_native_matrix_by_lags_csv(noise_type: str,
                                                        fix_number_of_lags=None,
                                                        sample_type: str = "ma1",
                                                        is_deg: bool = False,
                                                        mult_on_sample_size: bool = False) -> None:
    """
    N: Plot var cov hat vs lags
    Read from csv and plot len(sample_size_array) var cov hat lines:
    :param noise_type: type of noise 'gaussian' or 'bernoulli'
    :param fix_number_of_lags: for take cur csv
    :param sample_type: 'ma1' or 'ma3'
    :param is_deg: if True -'degenerate', if False - 'non degenerate' process
    :param mult_on_sample_size: if True - mult each cell on current sample size, if False - doesn't mult
    :return: plot len(sample_size_array) lines
    """
    # read csv
    deg = 'deg' if is_deg else 'non_deg'
    name = ''
    if fix_number_of_lags:
        name = '_{}_lags'.format(fix_number_of_lags)

    native_matrix = read_matrix(name='var_cov_hat_native_matrix_{}{}_{}_{}.csv'.format(noise_type, name, sample_type, deg),
                                index_col='lag')

    lags_array = [int(re.sub("[^0-9]", "", lag)) for
                         lag in native_matrix.index]

    sample_size_array = [int(re.sub("[^0-9]", "", sample_size)) for
                         sample_size in native_matrix.columns]

    arrays_dict = dict()
    for sample_size in sample_size_array:

        # get column
        array_for_plot = native_matrix['sample size {}'.format(sample_size)]

        if mult_on_sample_size:
            array_for_plot_mult_on_sample_size = [x * sample_size for x in array_for_plot]

            # create dict for plotting
            arrays_dict['sample size {}'.format(sample_size)] = array_for_plot_mult_on_sample_size
        else:
            arrays_dict['sample size {}'.format(sample_size)] = array_for_plot

    # create title
    sample_title = 'MA(1)' if sample_type == 'ma1' else 'MA(3)' if sample_type == 'ma3' else sample_type
    deg_title = 'degenerate' if is_deg else 'nondegenerate'
    title = 'Var(CovHat) with {} noise and {} {} sample vs lags'.format(noise_type, deg_title, sample_title)

    if mult_on_sample_size:
        title = 'sample_size*' + title

    plot_arrays(x_array=lags_array,
                arrays_dict=arrays_dict,
                title=title,
                x_label="lags",
                y_label="var(covHat)")

    print('Made picture "{}"'.format(title))


if __name__ == '__main__':
    read_and_plot_var_cov_hat_native_matrix_by_lags_csv(noise_type='gaussian', # bernoulli
                                                        fix_number_of_lags=300,
                                                        sample_type='ma3',
                                                        is_deg=False,
                                                        mult_on_sample_size=True)
