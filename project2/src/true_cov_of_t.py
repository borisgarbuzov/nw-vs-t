from src.coef import coef, coef_2, coef_3


def true_cov_ma1_of_t(t_par, sigma, lag):
    """
    True autocovariance for given parameters. 
    :param t_par: t parameter of a scaled time. 
    :param sigma: standard deviation of noise used to simulate the MA1 sample. 
    :param lag: lag of autocovariance to be computed. 
    :return: true autocovariance value. 
    """
    if lag == 0:
        return (sigma ** 2) * (1 + (coef(t_par=t_par) ** 2))
    elif lag == 1:
        return coef(t_par=t_par) * (sigma ** 2)
    else:
        return 0


def true_cov_scaled_noise_of_t(t_par, sigma, lag):
    """
    True autocovariance for given parameters. 
    :param t_par: t parameter of a scaled time. 
    :param sigma: standard deviation of noise used to simulate the scaled noise sample. 
    :param lag: lag of autocovariance to be computed. 
    :return: true autocovariance value. 
    """
    if lag == 0:
        return coef(t_par=t_par) ** 2 * sigma ** 2
    elif lag != 0:
        return 0


def true_cov_ma3_of_t(t_par, lag, sigma):
    """
    True autocovariance for given parameters. 
    :param t_par: t parameter of a scaled time. 
    :param sigma: standard deviation of noise used to simulate the MA3 sample. 
    :param lag: lag of autocovariance to be computed. 
    :return: true autocovariance value. 
    """    
    if lag == 0:
        return ((1 ** 2) + (coef(t_par=t_par) ** 2) + (coef_2(t_par=t_par) ** 2)
               + (coef_3(t_par=t_par) ** 2)) * (sigma ** 2)
    elif lag == 1:
        return (1 * coef(t_par=t_par) + coef(t_par=t_par) *
               coef_2(t_par=t_par) + coef_2(t_par=t_par) * coef_3(t_par=t_par))\
               * (sigma ** 2)
    elif lag == 2:
        return (1 * coef_2(t_par=t_par) + coef(t_par=t_par) *
                coef_3(t_par=t_par)) * (sigma ** 2)
    elif lag == 3:
        return (1 * coef_3(t_par=t_par)) * (sigma ** 2)
    else:
        return 0
