import numpy as np
import src.custom_kernel
from src.support_bound import support_bound
    

def lrv_hat_nw_t_free(cov_column: np.array, sample_size: int) -> float:
    '''
    In place of deprecated lrv_hat_nw_of_single_t
    sample_size used to be computed as a length of cov_column
    Since now we do not have the full set of lags, we accept it as an argument. 
    :param cov_column: a column-vector of t-free covariance values for different lags. 
    :param sample_size: size of a sample that was used for computation of cov_column. Used for support_bound computation.  
    :return: out_value, an estimate of LRV by NW method. 
    '''
    out_value = 0.0
    
    for lag in range(len(cov_column)):
        if lag == 0:
            rep = 1
        else:
            rep = 2
        K = src.custom_kernel.triangular_kernel(
            v=lag / support_bound(sample_size=sample_size)) * rep
        out_value += cov_column[lag] * K
    return out_value
