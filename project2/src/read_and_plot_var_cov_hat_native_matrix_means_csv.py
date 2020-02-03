import numpy as np
import re
from src.plot_arrays import plot_arrays
from src.read_matrix import read_matrix


def read_and_plot_var_cov_hat_native_matrix_means_csv(lags_array: np.array = np.array([]),
                                                      sample_type: str = "ma1",
                                                      is_deg: bool = False) -> None:
    """
    Plot var cov hat means for both noise types.
    Plot two lines
    the first is gaussian
    the second is bernoulli
    plot 2 lines
    :param lags_array: array of lags, example: [0,1,2,3,4,5]
    :param sample_type: 'ma1' or 'ma3'
    :param is_deg: if True -'degenerate', if False - 'non degenerate' process
    """
    deg = 'deg' if is_deg else 'non_deg'
    native_matrix = read_matrix(name='var_cov_hat_native_matrix_means_{}_{}.csv'.format(sample_type, deg),
                                index_col='lag')

    noise_type_array = [str(noise_type) for noise_type in native_matrix.columns][:2]

    if not len(lags_array):
        lags_array = [int(re.sub("[^0-9]", "", lag)) for lag in native_matrix.index]

    par_list = {
        'sample_type': sample_type,
        'is_deg': deg
    }

    # create dict for plotting
    arrays_dict = dict()
    for type in noise_type_array:
        arrays_dict[type] = np.full(shape=len(lags_array), fill_value=np.NaN)

        for i, lag in enumerate(lags_array):
            arrays_dict[type][i] = native_matrix[type][lag]

    # create title
    sample_title = 'MA(1)' if sample_type == 'ma1' else 'MA(3)' if sample_type == 'ma3' else sample_type
    deg = 'degenerate' if is_deg else 'nondegenerate'
    title = 'sample_size*Var(CovHat) means for {} {} sample'.format(deg, sample_title)

    plot_arrays(x_array=lags_array,
                arrays_dict=arrays_dict,
                title=title,
                x_label="lags",
                y_label="var(covHat)",
                par_list=par_list,
                color_array=['red', 'blue'])
    print('Made picture "{}"'.format(title))


if __name__ == '__main__':
    lags_array = np.arange(21)
    read_and_plot_var_cov_hat_native_matrix_means_csv(lags_array=lags_array, sample_type='ma3', is_deg=False)
