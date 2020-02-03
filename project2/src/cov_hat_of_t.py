from src.custom_kernel import gaussian_kernel, triangular_kernel
from src.b_cov import b_cov


def cov_hat_of_t(sample, t_par, lag):
    """
    Computes autocovariance estimate, based on t_par and lag,
    using kernel. 
    :param sample: diagonal sample.
    :param t_par: a value of t parameter, for which we need a covariance.
    :param lag: a value of lag between 0 and sample size, for which we need a covariance.
    :return: a scalar number, a result of autocovariance estimate. 
    """
    sample_size = len(sample)

    b_cov_value = b_cov(sample_size=sample_size)

    if lag < 0:
        raise ValueError("lag should be equal or more than 0")
    elif lag > sample_size - 1:
        raise ValueError("lag should be less than sample size - 1")

    partial_sum = 0
    for term_index in range(1, (sample_size - lag) + 1):
        K = gaussian_kernel((term_index / sample_size - t_par) / b_cov_value)
        term = sample[term_index - 1] * sample[(term_index - 1) + lag] * K
        partial_sum += term

    cov_hat = partial_sum / (sample_size * b_cov_value)

    return cov_hat
