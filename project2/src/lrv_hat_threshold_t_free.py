from src.threshold_indicator import threshold_indicator
import numpy as np


def lrv_hat_threshold_t_free(cov_hat_column: np.array,
                             sample_size: int,
                             noise_type: str,
                             sd_type: str,
                             sample_type: str = "ma1") -> float:
    """
    Computes a t-free threshold estimate of LRV, given the covariances and other parameters. 
    :param cov_hat_column: A vertical vector of covariances for lags from 0 to length of cov_hat_column. 
    :param sample_size: a size of a sample that was used to compute cov_hat_column. 
    :param noise_type:  a type of a sample that was used to compute cov_hat_column. Could be 'gaussian' or 'bernoulli'. It will be used for sd computation. 
    :param sd_type: block_est or native. Depends, which threshold - estimated or exact we want to use. Is piped 2 levels down. 
    :param sample_type: 'ma1' or 'ma3'. Potentially may have more, but these two are only working now. 
    :return: LRV estimated value. 
    """
    max_lag = len(cov_hat_column)
    indicator_array = []
    print('--------------------------------------------------')
    print('cov_hat_column=', cov_hat_column)
    print('sample_size=', sample_size)
    print('max_lag=', max_lag)
    indicator_value = threshold_indicator(sample_size=sample_size,
                                          cov_hat=cov_hat_column[0],
                                          lag=0,
                                          noise_type=noise_type,
                                          sd_type=sd_type,
                                          sample_type=sample_type)
    indicator_array.append(indicator_value)
    cum_sum = cov_hat_column[0] * indicator_value
    for lag in range(1, max_lag):
        indicator_value = threshold_indicator(sample_size=sample_size,
                                              cov_hat=cov_hat_column[lag],
                                              lag=lag,
                                              noise_type=noise_type,
                                              sd_type=sd_type,
                                              sample_type=sample_type)
        term = 2 * cov_hat_column[lag] * indicator_value
        indicator_array.append(indicator_value)
        cum_sum += term
    print('indicator_array=', indicator_array)
    print('--------------------------------------------------')
    return cum_sum
