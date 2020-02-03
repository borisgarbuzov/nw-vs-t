from src.diagonal_sample_tvma1 import diagonal_sample_tvma1
from src.horizontal_sample_tvma1 import horizontal_sample_tvma1
from src.diagonal_sample_scaled_noise import diagonal_sample_scaled_noise
from src.horizontal_sample_scaled_noise import horizontal_sample_scaled_noise
from src.diagonal_sample_tvma3 import diagonal_sample_tvma3
from src.horizontal_sample_tvma3 import horizontal_sample_tvma3
from src.create_t_par_array import create_t_par_array
from src.true_cov_of_t import true_cov_ma1_of_t, true_cov_ma3_of_t
from src.cov_hat_of_t import cov_hat_of_t
from src.cov_hat_t_free import cov_hat_t_free
from src.plot_double_array import plot_double_array
import numpy as np


def compute_and_save_cov_and_cov_hats(sample_size,
                                      t_par_count,
                                      gamma_count,
                                      mean,
                                      sigma,
                                      lag,
                                      noise_type,
                                      diag_or_horiz,
                                      sample_type: str = "ma1"):
    """
    For all values of t, this function computes the true covariance and its estimates
    using K(t).
    Saves image image file. No CSV.
    If diag_or_horiz is horiz, we generate the 2d horizontal sample,
    and for each line we compute cov hats using the non-kernel formula.
    """
    par_list = {"sample_size": sample_size,
                "t_par_count": t_par_count,
                "gamma_count": gamma_count,
                "mean": mean,
                "sigma": sigma,
                "lag": lag,
                "sample_type": sample_type,
                "noise_type": noise_type,
                "diag_or_horiz": diag_or_horiz}

    t_par_array = create_t_par_array(t_par_count=t_par_count)

    true_gamma_array = np.full(shape=t_par_count, fill_value=np.nan)

    gamma_hat_double_array = np.full(shape=(t_par_count, gamma_count),
                                     fill_value=np.nan)

    if sample_type == "ma1":
        for t_index in range(t_par_count):
            true_gamma_array[t_index] = true_cov_ma1_of_t(t_par=t_par_array[t_index],
                                                          sigma=sigma,
                                                          lag=lag)
    elif sample_type == "ma3":
        for t_index in range(t_par_count):
            true_gamma_array[t_index] = true_cov_ma3_of_t(t_par=t_par_array[t_index],
                                                          sigma=sigma,
                                                          lag=lag)
    """
    For each index, generate a sample (later called replication)
    and compute gamma.
    """
    for index in range(gamma_count):
        if sample_type == "scaled_noise":
            if diag_or_horiz == "diag":
                sample = diagonal_sample_scaled_noise(
                    sample_size=sample_size,
                    mean=mean,
                    sigma=sigma,
                    noise_type=noise_type)
            elif diag_or_horiz == "horiz":
                horizontal = horizontal_sample_scaled_noise(
                    sample_size=sample_size,
                    t_par_count=t_par_count,
                    mean=mean,
                    sigma=sigma,
                    noise_type=noise_type)
        elif sample_type == "ma1":
            if diag_or_horiz == "diag":
                sample = diagonal_sample_tvma1(
                    sample_size=sample_size,
                    mean=mean,
                    sigma=sigma,
                    noise_type=noise_type)
            elif diag_or_horiz == "horiz":
                horizontal = horizontal_sample_tvma1(
                    sample_size=sample_size,
                    t_par_count=t_par_count,
                    mean=mean,
                    sigma=sigma,
                    noise_type=noise_type)
        elif sample_type == "ma3":
            if diag_or_horiz == "diag":
                sample = diagonal_sample_tvma3(
                    sample_size=sample_size,
                    mean=mean,
                    sigma=sigma,
                    noise_type=noise_type)
            elif diag_or_horiz == "horiz":
                horizontal = horizontal_sample_tvma3(
                    sample_size=sample_size,
                    t_par_count=t_par_count,
                    mean=mean,
                    sigma=sigma,
                    noise_type=noise_type)
        for t_index in range(t_par_count):
            if diag_or_horiz == "horiz":
                sample = horizontal[t_index]
                gamma_hat_double_array[t_index, index] = cov_hat_t_free(
                    sample=sample,
                    lag=lag)
            elif diag_or_horiz == "diag":
                gamma_hat_double_array[t_index, index] = cov_hat_of_t(
                    sample=sample,
                    t_par=t_par_array[t_index],
                    lag=lag)

        print("There are", gamma_count - (index + 1), "replications left")

    plot_double_array(x_array=t_par_array,
                      hat_double_array=gamma_hat_double_array,
                      true_array=true_gamma_array,
                      title='Autocovariance',
                      axis='column',
                      x_label='t par',
                      par_list=par_list)


if __name__ == '__main__':
    compute_and_save_cov_and_cov_hats(sample_size=10000,
                                      t_par_count=11,
                                      gamma_count=5,
                                      mean=0,
                                      sigma=2,
                                      lag=4,
                                      sample_type='ma3',
                                      noise_type='gaussian',
                                      diag_or_horiz='horiz')
