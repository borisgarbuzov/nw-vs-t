from src.read_matrix import read_matrix
import numpy as np


def sd_cov_hat(sample_size: int,
               lag: int,
               noise_type: str,
               sd_type: str,
               sample_type: str = "ma1") -> float:
    """
    Computes an estimate of standard deviation for sample autocovariance,
    for a given lag, sample size and sd type.
    Upgrade considerations are described in
    LRV3a / computing 2 / project 2 / Threshold / sd_cov_hat(n, k, nType, estType)

    :param sample_size: Sample size for the sample autocovariance, whose variance we need.
    :param lag: Lag for the sample autocovariance, whose variance we need.
    :param noise_type: Noise type for the sample autocovariance, whose variance we need.
    :param sd_type: block_est or native. Depends, which threshold - estimated or exact we want to use.
    :return: A scalar value of estimated standard deviation.
    """

    if sd_type == 'block_est':
        if sample_type == "ma1":
            matrix_means_array = read_matrix(
                name="var_cov_hat_bootstrap_matrix_means_ma1.csv",
                index_col="lag")
            if lag < 2:
                value = matrix_means_array[noise_type][lag]
            elif lag > matrix_means_array.shape[0] - 1:
                value = matrix_means_array["average"][-1]
            else:
                value = matrix_means_array["average"][lag]
        elif sample_type == "ma3":
            matrix_means_array = read_matrix(
                name="var_cov_hat_bootstrap_matrix_means_ma3_non_deg.csv",
                index_col="lag")
            if lag < 4:
                value = matrix_means_array[noise_type][lag]
            elif lag > matrix_means_array.shape[0] - 1:
                value = matrix_means_array["average"][-1]
            else:
                value = matrix_means_array["average"][lag]
        else:
            raise ValueError("'sample_type' should be equal 'ma1' or 'ma3'")

    # Temporarily read the same file in lieu of native
    elif sd_type == 'native_sim':
        if sample_type == "ma1":
            matrix_means_array = read_matrix(
                name="var_cov_hat_native_matrix_means_ma1.csv", index_col="lag")
            if lag < 2:
                value = matrix_means_array[noise_type][lag]
            elif lag > matrix_means_array.shape[0] - 1:
                value = matrix_means_array["average"][-1]
                # For large lags, take the last known value
            else:
                value = matrix_means_array["average"][lag]
        elif sample_type == "ma3":
            matrix_means_array = read_matrix(
                name="var_cov_hat_native_matrix_means_ma3_non_deg.csv",
                index_col="lag")
            if lag < 4:
                value = matrix_means_array[noise_type][lag]
            elif lag > matrix_means_array.shape[0] - 1:
                value = matrix_means_array["average"][-1]
            else:
                value = matrix_means_array["average"][lag]
        else:
            raise ValueError("'sample_type' should be equal 'ma1' or 'ma3'")

    else:
        raise ValueError("'sd_type' should be equal 'block_est' or "
                         "'native_sim'")

    sd = np.sqrt(value / sample_size)

    return sd
