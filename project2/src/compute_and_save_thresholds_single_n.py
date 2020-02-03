from src.lrv_hat_threshold_of_t import lrv_hat_threshold_of_t
from src.create_t_par_array import create_t_par_array
from src.true_lrv_of_t import true_lrv_ma1_of_t, true_lrv_ma3_of_t
from src.diagonal_sample_tvma1 import diagonal_sample_tvma1
from src.diagonal_sample_tvma3 import diagonal_sample_tvma3
from src.cov_double_array_of_t import cov_double_array_of_t
from src.plot_double_array import plot_double_array
from src.threshold_max_lag import threshold_max_lag
import numpy as np


def compute_and_save_threshold_single_n(sample_size: int,
                                        t_par_count: int,
                                        mean: int,
                                        sigma: int,
                                        noise_type: str,
                                        sd_type: str,
                                        replication_count: int,
                                        sample_type: str = "ma1"):
    """
    Saves a straw plot of several replicates of t-dependent threshold estimates
    for the given sample_size.
    Illustrated in
    385 LRV3a / computing 2 / project 2 / tests / ME: Test the function
    """
    par_list = {"sample_size": sample_size,
                "t_par_count": t_par_count,
                "mean": mean,
                "sigma": sigma,
                "noise_type": noise_type,
                "sd_type": sd_type,
                "replication_count": replication_count,
                "sample_type": sample_type}

    threshold_hat_double_array = np.full(shape=(t_par_count, replication_count),
                                         fill_value=np.nan)

    t_par_array = create_t_par_array(t_par_count=t_par_count)
    if sample_type == "ma1":
        true_lrv_ma1_array = true_lrv_ma1_of_t(sigma=sigma,
                                               t_par_array=t_par_array)
    elif sample_type == "ma3":
        true_lrv_ma1_array = true_lrv_ma3_of_t(sigma=sigma,
                                               t_par_array=t_par_array)

    max_lag = threshold_max_lag(sample_size=sample_size)

    for replication in range(replication_count):
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
        cov_double_array = cov_double_array_of_t(sample=sample,
                                                 t_par_count=t_par_count,
                                                 max_lag=max_lag)
        threshold_hat_double_array[:, replication] = lrv_hat_threshold_of_t(
            cov_double_array=cov_double_array,
            sample_size=sample_size,
            noise_type=noise_type,
            sd_type=sd_type,
            sample_type=sample_type)

    plot_double_array(x_array=t_par_array,
                      hat_double_array=threshold_hat_double_array,
                      true_array=true_lrv_ma1_array,
                      title="Thresholds vs true lrv",
                      x_label="t par",
                      par_list=par_list)


if __name__ == '__main__':
    compute_and_save_threshold_single_n(sample_size=10000,
                                        t_par_count=11,
                                        mean=0,
                                        sigma=2,
                                        noise_type="gaussian",
                                        sd_type="block_est",
                                        replication_count=5,
                                        sample_type="ma3")
