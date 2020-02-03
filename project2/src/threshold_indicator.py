from src.sd_cov_hat import sd_cov_hat
from src.zhou_treshold import zhou_treshold

def threshold_indicator(sample_size,
                        cov_hat,
                        lag,
                        noise_type,
                        sd_type,
                        sample_type="ma1"):
    """
    Indicator of the threshold estimate of LRV. 
    Is used as a coefficient to multiply the covariance(lag). 
    :param sample_size: size of a sample, for which LRVHat is computed. 
    :param cov_hat: estimate of a covariance(lag) for which the coefficient is computed. 
    :param lag: a lag, for which the coefficient is computed. 
    :param noise_type: type of a noise used for construction of current MA sample. Used for choice of cov_hat estimate from some csv. 
    :param sd_type: a string "block_est" or "native_sim" to be passed to sd_cov_hat. 
    :param sample_type: a string "ma1", "ma3" to be passed to sd_cov_hat. 
    :return: 1 if ratio is bigger, and 0 otherwise. 
    """
    ratio = abs(cov_hat) / sd_cov_hat(sample_size=sample_size,
                                      lag=lag,
                                      noise_type=noise_type,
                                      sd_type=sd_type,
                                      sample_type=sample_type)
    is_ratio_bigger = (ratio > zhou_treshold(sample_size))
    indicator_value = int(is_ratio_bigger)
    return indicator_value
