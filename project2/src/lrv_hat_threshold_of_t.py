from src.lrv_hat_threshold_t_free import lrv_hat_threshold_t_free
import numpy as np


def lrv_hat_threshold_of_t(cov_double_array: np.array,
                           sample_size: int,
                           noise_type: str,
                           sd_type: str,
                           sample_type: str = "ma1") -> np.array:
    """
    LRV estimate by threshold method.
    The naming convention is a bit confusing. 
    Of_t means for all t here. 
    The formula does not differ in cases for a single t and t-fre, 
    so we call it t-free in both cases. 
    All info is in the cov_double_array that is submitted as an argument. 
    :cov_double_array: double array of autocovariance. Columns - tPar values, rows - lags.
    :sample_size: size of a sample that was used to compute these covariances. Used for max lag computation. 
    :return: a one-dimensional array of LRV estimates. Elements correspond to tPar values.
    """
    column_count = cov_double_array.shape[1]
    lrv_hat_threshold_array = np.full(shape=column_count, fill_value=np.nan)

    for index in range(column_count):
        lrv_hat_threshold_array[index] = lrv_hat_threshold_t_free(
            cov_hat_column=cov_double_array[:, index],
            sample_size=sample_size,
            noise_type=noise_type,
            sd_type=sd_type,
            sample_type=sample_type)
        print("lrv_hat_threshold_of_t t_par left", column_count - (index + 1))

    return lrv_hat_threshold_array
