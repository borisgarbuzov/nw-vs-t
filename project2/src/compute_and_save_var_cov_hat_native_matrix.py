"""
compute_and_save_var_cov_hat_native_matrix(replication_count=1000,
                                                      sample_size_array=sample_size_array,
                                                      mean=0,
                                                      sigma=2,
                                                      noise_type='bernoulli',
                                                      is_data=True,
                                                      fix_number_of_lags=300)
                                                      
=========================================
Gaussian matrix duration:        12536.306257610999 secs
=========================================

=========================================
Bernoulli matrix duration:       21139.880215758 secs
=========================================
"""


from timeit import default_timer as timer
from os.path import dirname
import numpy as np
import pandas as pd
import datetime
import os
from src.support_bound import support_bound
from src.diagonal_sample_tvma1 import diagonal_sample_tvma1
from src.horizontal_sample_tvma1 import horizontal_sample_tvma1
from src.diagonal_sample_tvma3 import diagonal_sample_tvma3
from src.cov_hat_t_free import cov_hat_t_free


def compute_and_save_var_cov_hat_native_matrix(replication_count: int,
                                               sample_size_array: np.array,
                                               mean: int,
                                               sigma: int,
                                               noise_type: str,
                                               is_data: bool = False,
                                               fix_number_of_lags: int = None,
                                               sample_type: str = "ma1") -> np.array:
    """
    N: Returns and saves to CSV the matrix of variance values of covHat
    for different lags and sample sizes.
    The values currently do not match theoretical ones.
    But I think, it is in a minor way, and the values are usable.

    :param replication_count:
    :param sample_size_array:
    :param mean:
    :param sigma:
    :param noise_type: type of noise 'gaussian' or 'bernoulli'
    :param is_data: save in "data" folder or in "output" folder
    :param fix_number_of_lags: how many lags should use
    :param sample_type: 'ma1' or 'ma3'
    :return:
    """
 
    if fix_number_of_lags:
        date = '_{}_{}_lags'.format(noise_type, fix_number_of_lags)
    else:
        date = '_{}'.format(noise_type)

    # create directory for data if it doesn't exist
    now = datetime.datetime.now()
    parent_dir = dirname(dirname(__file__))
    if is_data:
        data_folder = os.path.join(parent_dir, "data")
    if not is_data:
        data_folder = os.path.join(parent_dir, "output")
        date += '_{}'.format(now.strftime("%H;%M;%S;%f"))
    if not os.path.exists(data_folder):
        os.mkdir(data_folder)

    if fix_number_of_lags:
        max_lag_array = np.arange(0, fix_number_of_lags + 1)
    else:
        max_lag_array = [int(support_bound(sample_size)) for sample_size in sample_size_array]

    # result matrix
    var_cov_hat_native_matrix = np.full(shape=(max_lag_array[-1] + 1,
                                               len(sample_size_array)),
                                        fill_value=np.nan)

    # for DataFrame
    column_names = ["sample size " + str(sample_size) for sample_size in sample_size_array]
    index_names = ["lag " + str(lag) for lag in range(max_lag_array[-1] + 1)]

    for i, sample_size in enumerate(sample_size_array):
        # max lag for current sample_size
        max_lag = max(max_lag_array)
        
        print('sample size:', sample_size)
        for lag in range(max_lag + 1):
            cov_array = np.full(shape=replication_count, fill_value=np.nan)

            for r in range(replication_count):
                # sample = horizontal_sample_tvma1(sample_size=sample_size,
                #                                  t_par_count=11,
                #                                  mean=mean,
                #                                  sigma=sigma,
                #                                  noise_type=noise_type)[5, :]
                sample = diagonal_sample_tvma3(sample_size=sample_size,
                                               mean=mean,
                                               sigma=sigma,
                                               noise_type=noise_type,
                                               noise=None)
                cov_array[r] = cov_hat_t_free(sample, lag)

            var_cov_hat_native_matrix[lag, i] = np.var(cov_array)
            print('lags left:', max_lag - lag)

            # convert to Pandas DataFrame
            df_var_cov_hat_native_matrix = pd.DataFrame(var_cov_hat_native_matrix,
                                                        index=index_names,
                                                        columns=column_names)
            df_var_cov_hat_native_matrix.index.name = 'lag'

            df_var_cov_hat_native_matrix.to_csv(os.path.join(data_folder,
                                                             "var_cov_hat_native_matrix{}_{}.csv".format(date,
                                                                                                         sample_type)))
            
    return var_cov_hat_native_matrix
    
    
if __name__ == '__main__':
    sample_size_array = np.arange(1000, 5001, 1000)

    start_time = timer()
    res = compute_and_save_var_cov_hat_native_matrix(replication_count=1000,
                                                     sample_size_array=sample_size_array,
                                                     mean=0,
                                                     sigma=2,
                                                     noise_type='gaussian',
                                                     is_data=True,
                                                     fix_number_of_lags=300,
                                                     sample_type='ma3')
    duration = timer() - start_time


    start_time = timer()
    res2 = compute_and_save_var_cov_hat_native_matrix(replication_count=1000,
                                                      sample_size_array=sample_size_array,
                                                      mean=0,
                                                      sigma=2,
                                                      noise_type='bernoulli',
                                                      is_data=True,
                                                      fix_number_of_lags=300,
                                                      sample_type='ma3')
    duration2 = timer() - start_time
    # print(np.around(res, decimals=4))

    # print(np.around(res, decimals=4))
    print('=========================================')
    print('Gaussian matrix duration:\t', duration, 'secs')
    print('=========================================\n')

    print('=========================================')
    print('Bernoulli matrix duration:\t', duration2, 'secs')
    print('=========================================\n')
