from src.coef import coef, coef_2, coef_3
from src.true_cov_of_t import true_cov_scaled_noise_of_t


def true_lrv_scaled_noise_of_single_t(sigma, t_par):
    """
    True local LRV for given parameters. 
    :param sigma: standard deviation of noise used to simulate the scaled noise sample. 
    :param t_par: t parameter or scaled time. 
    :return: true LRV value. 
    """    
    return true_cov_scaled_noise_of_t(t_par, sigma, lag=0)


def true_lrv_ma1_of_single_t(sigma, t_par):
    """
    True local LRV for given parameters. 
    :param sigma: standard deviation of noise used to simulate the MA1 sample. 
    :param t_par: t parameter or scaled time. 
    :return: true LRV value. 
    """    
    lrv = sigma ** 2 * (1 + coef(t_par)) ** 2
    return lrv


def true_lrv_ma3_of_single_t(sigma, t_par):
    """
    True local LRV for given parameters. 
    :param sigma: standard deviation of noise used to simulate the MA3 sample. 
    :param t_par: t parameter or scaled time. 
    :return: true LRV value. 
    """    
    lrv = (sigma ** 2 ) * (1 + coef(t_par) + coef_2(t_par) + coef_3(t_par)) ** 2
    return lrv
