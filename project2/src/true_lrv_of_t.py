from src.true_lrv_of_single_t import true_lrv_ma1_of_single_t, \
    true_lrv_scaled_noise_of_single_t, true_lrv_ma3_of_single_t
import numpy as np


def true_lrv_scaled_noise_of_t(sigma: int, t_par_array: np.array) -> np.array:
    true_lrv_scaled_noise_array = np.full(shape=len(t_par_array),
                                          fill_value=np.nan)
    for t_index, t_par in enumerate(t_par_array):
        true_lrv_scaled_noise_array[t_index] = true_lrv_scaled_noise_of_single_t(
            sigma=sigma, t_par=t_par)
        print("true_lrv_scaled_noise_of_t t_par left",
              len(t_par_array) - (t_index + 1))

    return true_lrv_scaled_noise_array


def true_lrv_ma1_of_t(sigma: int, t_par_array: np.array) -> np.array:
    true_lrv_ma1_array = np.full(shape=len(t_par_array), fill_value=np.nan)
    for t_index, t_par in enumerate(t_par_array):
        true_lrv_ma1_array[t_index] = true_lrv_ma1_of_single_t(sigma=sigma,
                                                               t_par=t_par)
        print("true_lrv_ma1_of_t t_par left", len(t_par_array) - (t_index + 1))

    return true_lrv_ma1_array


def true_lrv_ma3_of_t(t_par_array: np.array, sigma: float) -> np.array:
    """
    True local LRV for given parameters. 
    :param sigma: standard deviation of noise used to simulate the MA3 sample. 
    :param t_par: t parameter or scaled time. 
    :return: true LRV value. 
    """    
    true_lrv_ma3_array = np.full(shape=len(t_par_array),
                                 fill_value=np.nan)
    for t_index, t_par in enumerate(t_par_array):
        true_lrv_ma3_array[t_index] = true_lrv_ma3_of_single_t(t_par=t_par,
                                                               sigma=sigma)
        print("true_lrv_ma3_of_t t_par left", len(t_par_array) - (t_index + 1))

    return true_lrv_ma3_array
