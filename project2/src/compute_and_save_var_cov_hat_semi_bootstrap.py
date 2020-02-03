from src.semi_bootstrap import semi_bootstrap
from src.support_bound import support_bound
from os.path import dirname
import numpy as np
import pandas as pd
import os
import datetime


def compute_and_save_var_cov_hat_semi_bootstrap(sample_size_from: int,
                                                sample_size_to: int,
                                                sample_size_by: int,
                                                mean: int,
                                                sigma: int,
                                                noise_type: str,
                                                is_data: bool,
                                                sample_type: str = "ma1"):
    """
    This function computes semi-bootstrapped values (or block estimate)
    of var(covHat) for different lags and sample sizes.
    The block size choice is currently in question.
    Also, we need to revisit the problem of maximal lag choice.
    Experimentally, we found out that for some choices of block size,
    Our estimations match well the native simulations.
    After we automate reading the constants off native simulations,
    we can do something similar to semi-bootstrap.
    So we eventually need to save the constants, results of averaging
    over different sample sizes.
    """
    sample_size_array = np.arange(start=sample_size_from, stop=sample_size_to,
                                  step=sample_size_by)

    max_lag = int(support_bound(sample_size=sample_size_array[-1])) + 1

    semi_bootstrap_array = np.full(shape=(max_lag, len(sample_size_array)),
                                   fill_value=np.nan)

    for col_index, sample_size in enumerate(sample_size_array):
        max_lag_by_sample_size = int(support_bound(sample_size=sample_size)) + 1
        for lag in range(max_lag_by_sample_size):
            semi_bootstrap_array[lag, col_index] = semi_bootstrap(
                sample_size=sample_size,
                lag=lag,
                mean=mean,
                sigma=sigma,
                noise_type=noise_type,
                sample_type=sample_type)
            print("lags left:", max_lag_by_sample_size - (lag + 1))
        print("sample sizes left:", len(sample_size_array) - (col_index + 1))

    column_names = ["sample size " + str(sample_size) for sample_size in
                    sample_size_array]

    index_names = ["lag " + str(lag) for lag in range(max_lag)]

    df_variance_matrix = pd.DataFrame(semi_bootstrap_array,
                                      index=index_names,
                                      columns=column_names)

    df_variance_matrix.index.name = 'lag'

    now = datetime.datetime.now()
    parent_dir = dirname(dirname(__file__))
    if is_data:
        data_folder = os.path.join(parent_dir, "data")
        date = ''
    if not is_data:
        data_folder = os.path.join(parent_dir, "output")
        date = '_{}'.format(now.strftime("%H;%M;%S;%f"))
    if not os.path.exists(data_folder):
        os.mkdir(data_folder)
    df_variance_matrix.to_csv(os.path.join(data_folder,
                                           "var_cov_hat_bootstrap_matrix{0}_{1}"
                                           ".csv".format(date, sample_type)))


if __name__ == '__main__':
    compute_and_save_var_cov_hat_semi_bootstrap(sample_size_from=1000,
                                                sample_size_to=20001,
                                                sample_size_by=1000,
                                                mean=0,
                                                sigma=2,
                                                noise_type="gaussian",
                                                is_data=True,
                                                sample_type="ma1")
