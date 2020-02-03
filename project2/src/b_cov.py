def b_cov(sample_size):
    """
    We need it for kernel, so only for t-dependent values.
    If we do cov_hat_t_free, it does not use any bandwidth.
    So far we took the formula from project 1.

    :param sample_size: size of sample
    :return: float number
    """
    b_cov = 1 * sample_size ** (-1 / 4)
    return b_cov
