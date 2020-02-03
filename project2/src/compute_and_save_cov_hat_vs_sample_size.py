from src.cov_hat_t_free import cov_hat_t_free
from src.diagonal_sample_tvma1 import diagonal_sample_tvma1
from src.diagonal_sample_tvma3 import diagonal_sample_tvma3
from src.plot_double_array import plot_double_array
from src.true_cov_t_free import true_cov_ma1_t_free, true_cov_ma3_t_free
import numpy as np

def compute_and_save_cov_hat_vs_sample_size(sample_size_from: int,
                                            sample_size_to: int,
                                            sample_size_by: int,
                                            replication_count: int,
                                            mean: int,
                                            sigma: int,
                                            noise_type: str,
                                            lag: int,
                                            sample_type: str = "ma1"):
    par_list = {"sample_size_from": sample_size_from,
                "sample_size_to": sample_size_to,
                "sample_size_by": sample_size_by,
                "replication_count": replication_count,
                "mean": mean,
                "sigma": sigma,
                "noise_type": noise_type,
                "lag": lag,
                "sample_type": sample_type}

    sample_size_array = np.arange(start=sample_size_from, stop=sample_size_to,
                                  step=sample_size_by)
    cov_hat_t_free_array = np.full(shape=(replication_count,
                                          len(sample_size_array)),
                                   fill_value=np.nan)

    if sample_type == "ma1":
        true_cov_array = np.repeat(true_cov_ma1_t_free(lag=lag, sigma=sigma),
                                   len(sample_size_array))
    elif sample_type == "ma3":
        true_cov_array = np.repeat(true_cov_ma3_t_free(lag=lag, sigma=sigma),
                                   len(sample_size_array))

    for index_col, sample_size in enumerate(sample_size_array):
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
            cov_hat_t_free_array[replication, index_col] = cov_hat_t_free(
                sample=sample,
                lag=lag)

    plot_double_array(x_array=sample_size_array,
                      hat_double_array=cov_hat_t_free_array,
                      true_array=true_cov_array,
                      title="Cov hat t free by sample size",
                      x_label="sample size",
                      par_list=par_list,
                      axis='row',
                      true_label="true autocovariance t free",
                      y_label='autocovariance')


if __name__ == '__main__':
    compute_and_save_cov_hat_vs_sample_size(sample_size_from=1000,
                                            sample_size_to=10001,
                                            sample_size_by=1000,
                                            replication_count=5,
                                            mean=0,
                                            sigma=2,
                                            noise_type="gaussian",
                                            lag=4,
                                            sample_type="ma3")
