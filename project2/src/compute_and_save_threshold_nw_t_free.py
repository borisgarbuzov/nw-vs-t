from src.cov_column_t_free import cov_column_t_free
from src.diagonal_sample_tvma1 import diagonal_sample_tvma1
from src.diagonal_sample_tvma3 import diagonal_sample_tvma3
from src.lrv_hat_threshold_t_free import lrv_hat_threshold_t_free
from src.lrv_hat_nw_t_free import lrv_hat_nw_t_free
from src.true_lrv_t_free import true_lrv_ma1_t_free, true_lrv_ma3_t_free
from src.support_bound import support_bound
from src.threshold_max_lag import threshold_max_lag
from src.plot_histogram import plot_histograms
import numpy as np


def compute_and_save_threshold_nw_t_free(sample_size: int,
                                         replication_count: int,
                                         mean: int,
                                         sigma: int,
                                         noise_type: str,
                                         sd_type: str,
                                         lrv_est: str,
                                         sample_type: str = "ma1"):
    """
    Illustrated in
    402 LRV 3a / computing 2 / project 2 / Threshold / M: threshold t free
    Saves a single image file with
    histogram of replicated NW estimate threshold or both.
    True value is marked on all histograms.
    """
    par_list = {"sample_size": sample_size,
                "replication_count": replication_count,
                "mean": mean,
                "sigma": sigma,
                "sd_type": sd_type,
                "noise_type": noise_type,
                "sample_type": sample_type}

    threshold_t_free_array = np.full(shape=replication_count, fill_value=np.nan)
    nw_t_free_array = np.full(shape=replication_count, fill_value=np.nan)

    if sample_type == "ma1":
        true_lrv = true_lrv_ma1_t_free(sigma=sigma)
    elif sample_type == "ma3":
        true_lrv = true_lrv_ma3_t_free(sigma=sigma)

    support_bound_value = int(support_bound(sample_size=sample_size)) + 1
    threshold_max_lag_value = threshold_max_lag(sample_size=sample_size)

    max_lag = max(support_bound_value, threshold_max_lag_value)

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
        cov_column = cov_column_t_free(sample=sample,
                                       max_lag=max_lag)
        if lrv_est == "threshold" or lrv_est == "both":
            threshold_t_free_array[replication] = lrv_hat_threshold_t_free(
                cov_hat_column=cov_column[:threshold_max_lag_value],
                sample_size=sample_size,
                noise_type=noise_type,
                sd_type=sd_type,
                sample_type=sample_type)
        if lrv_est == "nw" or lrv_est == "both":
            nw_t_free_array[replication] = lrv_hat_nw_t_free(
                cov_column=cov_column[:support_bound_value],
                sample_size=sample_size)
        print("compute_and_save_threshold_nw_t_free", replication_count -
              (replication + 1), "left")

    arrays_dict = {"Newey-West": nw_t_free_array,
                   "Threshold": threshold_t_free_array}

    plot_histograms(arrays_dict=arrays_dict,
                    true_value=true_lrv,
                    title="{} t free lrv".format(lrv_est),
                    par_list=par_list)


if __name__ == '__main__':
    compute_and_save_threshold_nw_t_free(sample_size=10000,
                                         replication_count=1,
                                         mean=0,
                                         sigma=2,
                                         noise_type="gaussian",
                                         sd_type="block_est",
                                         lrv_est="threshold",
                                         sample_type="ma3")
