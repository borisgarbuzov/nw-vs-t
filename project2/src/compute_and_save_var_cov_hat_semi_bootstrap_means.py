from src.semi_bootstrap import semi_bootstrap
from os.path import dirname
import numpy as np
import pandas as pd
import os
import datetime


def compute_and_save_var_cov_hat_semi_bootstrap_means(sample_size_from: int,
                                                      sample_size_to: int,
                                                      sample_size_by: int,
                                                      mean: int,
                                                      sigma: int,
                                                      max_lag: int,
                                                      is_data: bool,
                                                      sample_type: str="ma1",):
    """
    This function computes and saves to CSV file
    estimates of constants, corresponding to variance of sample covariance,
    for specified lags and noise type.
    It computes those constants on the assumption
    that variance is approximately equal to const / sample_size.
    The constant is computed by averaging of block estimate values
    over different sample sizes.
    :sample_size_from: the minimal sample size to be used,
    :sample_size_to: the maximal sample size to be used,
    :sample_size_by: the step in sample sizes to be used,
    :mean: mean of noise to be used for sample generation,
    :sigma: standard deviation of noise to be used for sample generation,
    :max_lag: maximal lag to be used for covariance, (the minimal lag being 0)
    :is_data:  if true, the CSV file is saved to data folder, and output folder otherwise.
    :return: nothing. Just saves CSV.
    """
    sample_size_array = np.arange(start=sample_size_from, stop=sample_size_to,
                                  step=sample_size_by)

    noise_types = ["gaussian", "bernoulli"]

    semi_bootstrap_array = np.full(shape=(max_lag, len(noise_types) + 1),
                                   fill_value=np.nan)

    for col_index, noise_type in enumerate(noise_types):
        print("Current noise", noise_type)
        for lag in range(max_lag):
            temp = []
            for sample_size in sample_size_array:
                temp.append(semi_bootstrap(
                    sample_size=sample_size,
                    lag=lag,
                    mean=mean,
                    sigma=sigma,
                    noise_type=noise_type,
                    sample_type=sample_type))
            semi_bootstrap_array[lag, col_index] = np.mean(temp)
            print("lags left:", max_lag - (lag + 1))

    for lag in range(2, max_lag):
        semi_bootstrap_array[lag, 2] = np.mean(semi_bootstrap_array[lag, 0:2])

    noise_types.append("average")
    index_names = ["lag " + str(lag) for lag in range(max_lag)]

    df_variance_matrix = pd.DataFrame(semi_bootstrap_array,
                                      index=index_names,
                                      columns=noise_types)

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
                                           "var_cov_hat_bootstrap_matrix_means{0}_{1}"
                                           ".csv".format(date, sample_type)))


if __name__ == '__main__':
    compute_and_save_var_cov_hat_semi_bootstrap_means(sample_size_from=1000,
                                                      sample_size_to=100001,
                                                      sample_size_by=1000,
                                                      mean=0,
                                                      sigma=2,
                                                      max_lag=301,
                                                      sample_type="ma3",
                                                      is_data=True)
