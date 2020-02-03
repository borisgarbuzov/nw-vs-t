from src.cov_hat_t_free import cov_hat_t_free
import numpy as np


def cov_column_t_free(sample: np.array,
                      max_lag: int) -> np.array:
    """
    Same as cov_column_of_t, but disregarding t, 
    not using kernel. 
    :return: a vecor of covariance values for lags 0 to max_lag. 
    """
    cov_column = np.full(shape=max_lag, fill_value=np.nan)

    for lag in range(max_lag):
        cov_column[lag] = cov_hat_t_free(sample=sample,
                                         lag=lag)
        print("cov_column_t_free there are", max_lag - (lag + 1), "lags left")

    return cov_column
