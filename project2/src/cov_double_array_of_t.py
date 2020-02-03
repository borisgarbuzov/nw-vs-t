from src.create_t_par_array import create_t_par_array
from src.cov_column_of_t import cov_column_of_t
import numpy as np


def cov_double_array_of_t(sample: np.array,
                          t_par_count: int,
                          max_lag: int) -> np.array:
    """
    Compute covariance double array.
    First, wanted to call it covariance matrix. 
    But the specific composition of it has different indexing 
    than rhe regular covariance matrix.
    Here we have rows corresponding to lags, 
    and columns, corresponding to t values. 
    :param sample: array
    :param t_par_count: count of t
    :return: double array
    """

    cov_double_array = np.full(shape=(max_lag, t_par_count),
                               fill_value=np.nan)
    t_par_array = create_t_par_array(t_par_count=t_par_count)

    for t_par_index in range(t_par_count):
        cov_double_array[:, t_par_index] = cov_column_of_t(
            sample=sample,
            t_par=t_par_array[t_par_index],
            max_lag=max_lag)
        print("cov_double_array_of_t there are",
              t_par_count - (t_par_index + 1), "lags left")

    return cov_double_array
