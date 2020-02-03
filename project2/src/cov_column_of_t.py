from src.cov_hat_of_t import cov_hat_of_t
import numpy as np


def cov_column_of_t(sample: np.array, t_par: float, max_lag: int):
    """
    Computes covariance values from lags in {0, max_lag},
    corresponding to a given t_par. 
    Since for different t_pars, we call these values a matrix, 
    in that context, our function produces a column of that matrix. 
    So it returns a vector, interpreted as a column of cov matrix or double array. 
    """
    cov_column = np.full(shape=max_lag, fill_value=np.nan)
    for lag in range(max_lag):
        cov_column[lag] = cov_hat_of_t(sample=sample, t_par=t_par, lag=lag)

    return cov_column
