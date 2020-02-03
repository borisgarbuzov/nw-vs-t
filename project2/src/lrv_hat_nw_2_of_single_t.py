from src.custom_kernel import gaussian_kernel, triangular_kernel
from src.b_cov import b_cov
from src.support_bound import support_bound
import numpy as np


def lrv_hat_nw_2_of_single_t(sample: np.array, t_par: float) -> float:
    '''
    This function should give the same result as lrv_hat_of_single_t_nw,
    though it does not so far. 
    In this connection, we need to look at lag bounds. 
    It returns the value for a single t_par. 
    Recently renamed. Was lrv_hat_of_t_nw_2.
    Note that here we do nt have the explicit notion of lag. 
    '''
    sample_size = len(sample)
    b_cov_value = b_cov(sample_size=sample_size)

    nw_hat = 0
    for i, x_i in enumerate(sample, start=1):
        for j, x_j in enumerate(sample, start=1):
            kernel_cov = gaussian_kernel(v=((np.minimum(i, j) / sample_size) -
                                            t_par) / b_cov_value) * (1 / (
                    sample_size * b_cov_value))
            lag = i-j
            kernel_nw = triangular_kernel(v=np.abs(lag) / support_bound(
                sample_size=sample_size))
            nw_hat += kernel_cov * kernel_nw * x_i * x_j
        print("lrv_hat_of_single_t_nw_2 external sum", len(sample) - i)

    return nw_hat
