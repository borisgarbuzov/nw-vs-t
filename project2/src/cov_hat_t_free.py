import numpy as np


def cov_hat_t_free(sample: np.array, lag: int) -> float:
    """
    Computes autocovariance estimate, based lag,
    by a classic formula, not using kernel. 
    :param sample: diagonal or horizontal sample.
    :param lag: a value of lag between 0 and sample size, for which we need a covariance.
    :return: a scalar number, a result of autocovariance estimate. 
    """    
    sample_size = len(sample)

    if lag < 0:
        raise ValueError("lag should be equal or more than 0")
    elif lag > sample_size - 1:
        raise ValueError("lag should be less than sample size - 1")

    partial_sum = 0

    for index in range(sample_size - lag):
        partial_sum += sample[index] * sample[index + lag]

    return partial_sum / sample_size
