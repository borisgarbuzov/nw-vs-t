from src.sd_cov_hat import sd_cov_hat
from src.zhou_treshold import zhou_treshold
from src.cov_column_t_free import cov_column_t_free
from src.threshold_max_lag import threshold_max_lag
from src.diagonal_sample_tvma1 import diagonal_sample_tvma1
from src.diagonal_sample_tvma3 import diagonal_sample_tvma3
from src.plot_acf import plot_acf
import numpy as np


def compute_and_save_acf(sample_size: int,
                         mean: int,
                         sigma: int,
                         noise_type: str,
                         sd_type: str,
                         sample_type: str="ma1"):
    """
    It saves to output directory, the sample autocovariance function for several lags
    We generate the sample, given the default process, currently TVMA(1).
    If later we change the default process, we would need to change the call
    diagonal_sample_tvma1 to something else.
    Currently, max lag is the one for threshold.
    Later, if need arises, we may introduce the max_lag argument.
    """
    par_list = {"sample_size": sample_size,
                "mean": mean,
                "sigma": sigma,
                "noise_type": noise_type,
                "sd_type": sd_type,
                "sample_type": sample_type}

    if sample_type == "ma1":
        sample = diagonal_sample_tvma1(sample_size=sample_size,
                                       mean=mean,
                                       sigma=sigma,
                                       noise_type=noise_type)
    elif sample_type == "ma3":
        sample = diagonal_sample_tvma3(sample_size=sample_size,
                                       mean=mean,
                                       sigma=sigma,
                                       noise_type=noise_type)
    max_lag = threshold_max_lag(sample_size=sample_size)
    cov_hat = cov_column_t_free(sample=sample,
                                max_lag=max_lag)
    sd_cov_hat_array = np.full(shape=max_lag, fill_value=np.nan)
    for lag in range(max_lag):
        sd_cov_hat_array[lag] = sd_cov_hat(sample_size=sample_size,
                                           lag=lag,
                                           noise_type=noise_type,
                                           sd_type=sd_type,
                                           sample_type=sample_type)
    cloud = sd_cov_hat_array * zhou_treshold(sample_size=sample_size)

    plot_acf(cov_hat=cov_hat,
             cloud=cloud,
             par_list=par_list)


if __name__ == '__main__':
    compute_and_save_acf(sample_size=1000,
                         mean=0,
                         sigma=2,
                         noise_type="gaussian",
                         sample_type="ma3",
                         sd_type="block_est")
