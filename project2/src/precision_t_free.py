import numpy as np
from sklearn.metrics import mean_squared_error

def mean_t_free(est_array: np.array):
    """
    Computes mean of an array of values
    :param est_array: array to be averaged. 
    :return: sample mean of the given array. 
    """
    return np.mean(est_array)

def bias_t_free(true_value: float, est_array: np.array):
    mean = np.mean(est_array)
    return mean - true_value

def variance_t_free(est_array: np.array):
    return np.var(est_array)
    
def mse_t_free(true_array: np.array, est_array: np.array):
    return mean_squared_error(true_array, est_array)

def precision_t_free(true_value: float, est_array: np.array):
    return_of_mean_t_free = mean_t_free(est_array)
    return_of_bias_t_free = bias_t_free(true_value, est_array)
    return_of_variance_t_free = variance_t_free(est_array)
    return_of_mse_t_free = mse_t_free(true_value, est_array)
    
    return {'mean_t_free:':return_of_mean_t_free,
            'bias_t_free:':return_of_bias_t_free,
            'variance_t_free:':return_of_variance_t_free,
            'mse_t_free:':return_of_mse_t_free
    }