import numpy as np
import re
from src.plot_arrays import plot_arrays
from src.read_matrix import read_matrix


def read_and_plot_var_cov_hat_native_matrix_by_sample_size_csv(noise_type: str,
                                                               count_lags: np.array,
                                                               fix_number_of_lags=None,
                                                               sample_type: str = 'ma1',
                                                               is_deg: bool = False,
                                                               mult_on_sample_size: bool = False) -> None:
    """
    N: Plot var cov hat vs sample size
    Read from csv and plot len(count_lags) var cov hat lines:
    plot len(count_lags) lines
    :param noise_type: type of noise 'gaussian' or 'bernoulli'
    :param count_lags: array of lags, example: [0,1,2,3,4,5]
    :param fix_number_of_lags: for take cur csv
    :param sample_type: 'ma1' or 'ma3'
    :param is_deg: if True -'degenerate', if False - 'non degenerate' process
    :param mult_on_sample_size: if True - mult each cell on current sample size, if False - doesn't mult
    :return plot len(count_lags) lines
    """
    # read csv
    deg = 'deg' if is_deg else 'non_deg'
    name = ''
    if fix_number_of_lags:
        name = '_{}_lags'.format(fix_number_of_lags)
    native_matrix = read_matrix(
        name='var_cov_hat_native_matrix_{}{}_{}_{}.csv'.format(noise_type, name, sample_type, deg),
        index_col='lag')

    sample_size_array = [int(re.sub("[^0-9]", "", sample_size)) for
                         sample_size in native_matrix.columns]

    matrix_for_plot = np.full(shape=(len(count_lags), len(sample_size_array)), fill_value=np.NaN)

    # get 1 row from csv
    for i, lag in enumerate(count_lags):
        row = native_matrix[lag:lag+1]

        if mult_on_sample_size:
            new_row = np.full(shape=len(sample_size_array), fill_value=np.NaN)
            for j, sample_size in enumerate(sample_size_array):
                new_row[j] = row['sample size ' + str(sample_size)][0] * sample_size

            matrix_for_plot[i] = new_row
        else:
            matrix_for_plot[i] = row

    # create dict for plotting
    arrays_dict = dict()
    for i, lag in enumerate(count_lags):
        arrays_dict['lag {}'.format(lag)] = matrix_for_plot[i]

    # create title
    sample_title = 'MA(1)' if sample_type == 'ma1' else 'MA(3)' if sample_type == 'ma3' else sample_type
    deg_title = 'degenerate' if is_deg else 'nondegenerate'
    title = 'Var(CovHat) with {} noise and {} {} sample vs sample sizes'.format(noise_type, deg_title, sample_title)

    if mult_on_sample_size:
        title = 'sample_size*' + title

    plot_arrays(x_array=sample_size_array,
                arrays_dict=arrays_dict,
                title=title,
                x_label="sample size",
                y_label="var(covHat)")

    print('Made picture "{}"'.format(title))


if __name__ == '__main__':
    count_lags = np.arange(0, 5)
    read_and_plot_var_cov_hat_native_matrix_by_sample_size_csv(noise_type='gaussian',   # bernoulli
                                                               count_lags=count_lags,
                                                               fix_number_of_lags=300,
                                                               sample_type='ma3',
                                                               is_deg=False,
                                                               mult_on_sample_size=False)
