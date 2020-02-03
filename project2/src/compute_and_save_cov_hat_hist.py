from src.cov_hat_t_free import cov_hat_t_free
from src.diagonal_sample_tvma1 import diagonal_sample_tvma1
from src.diagonal_sample_tvma3 import diagonal_sample_tvma3
from src.plot_histogram import plot_histograms
from src.true_cov_t_free import true_cov_ma3_t_free, true_cov_ma1_t_free
import numpy as np


def compute_and_save_cov_hat_hist(sample_size: int,
                                  replication_count: int,
                                  mean: int,
                                  sigma: int,
                                  noise_type: str,
                                  lag: int,
                                  sample_type: str = "ma1"):
    par_list = {"sample_size": sample_size,
                "replication_count": replication_count,
                "mean": mean,
                "sigma": sigma,
                "noise_type": noise_type,
                "lag": lag,
                "sample_type": sample_type}

    cov_hat_t_free_array = np.full(shape=replication_count, fill_value=np.nan)

    if sample_type == "ma1":
        true_cov = true_cov_ma1_t_free(lag=lag, sigma=sigma)
    elif sample_type == "ma3":
        true_cov = true_cov_ma3_t_free(lag=lag, sigma=sigma)

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
        cov_hat_t_free_array[replication] = cov_hat_t_free(sample=sample,
                                                           lag=lag)

    arrays_dict = {"Autocovariance": cov_hat_t_free_array}

    plot_histograms(arrays_dict=arrays_dict,
                    true_value=true_cov,
                    title="Autocovariance",
                    par_list=par_list,
                    true_label="true autocovariance")


if __name__ == '__main__':
    compute_and_save_cov_hat_hist(sample_size=1000,
                                  replication_count=1000,
                                  mean=0,
                                  sigma=2,
                                  noise_type="gaussian",
                                  lag=4,
                                  sample_type="ma3")
