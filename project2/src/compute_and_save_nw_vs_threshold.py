from src.create_t_par_array import create_t_par_array
from src.cov_double_array_of_t import cov_double_array_of_t
from src.diagonal_sample_tvma1 import diagonal_sample_tvma1
from src.diagonal_sample_tvma3 import diagonal_sample_tvma3
from src.true_lrv_of_t import true_lrv_ma1_of_t, true_lrv_ma3_of_t
from src.lrv_hat_nw_of_t import lrv_hat_nw_of_t
from src.lrv_hat_threshold_of_t import lrv_hat_threshold_of_t
from src.support_bound import support_bound
from src.plot_arrays import plot_arrays
from src.threshold_max_lag import threshold_max_lag


def compute_and_save_nw_vs_threshold(sample_size: int,
                                     t_par_count: int,
                                     mean: int,
                                     sigma: int,
                                     noise_type: str,
                                     sd_type: str,
                                     sample_type: str = "ma1"):
    """
    Illustrated in
    394 LRV 3a / computing 2 / project 2 / Threshold / N: compute_and_save_nw_vs_threshold
    It saves one image file of 2 t-dependent plots. For two estimates.
    No precision is computed here so far.
    """
    par_list = {"sample_size": sample_size,
                "t_par_count": t_par_count,
                "mean": mean,
                "sigma": sigma,
                "noise_type": noise_type,
                "sd_type": sd_type,
                "sample_type": sample_type}

    t_par_array = create_t_par_array(t_par_count=t_par_count)

    if sample_type == "ma1":
        true_lrv_array = true_lrv_ma1_of_t(sigma=sigma, t_par_array=t_par_array)
        sample = diagonal_sample_tvma1(sample_size=sample_size, mean=mean,
                                       sigma=sigma, noise_type=noise_type)
    elif sample_type == "ma3":
        true_lrv_array = true_lrv_ma3_of_t(sigma=sigma, t_par_array=t_par_array)
        sample = diagonal_sample_tvma3(sample_size=sample_size, mean=mean,
                                       sigma=sigma, noise_type=noise_type)

    support_bound_value = int(support_bound(sample_size=sample_size)) + 1
    threshold_max_lag_value = threshold_max_lag(sample_size=sample_size)

    max_lag = max(support_bound_value, threshold_max_lag_value)

    cov_double_array = cov_double_array_of_t(sample=sample,
                                             t_par_count=t_par_count,
                                             max_lag=max_lag)

    nw_lrv_array = lrv_hat_nw_of_t(
        cov_double_array=cov_double_array[:support_bound_value, :],
        sample_size=sample_size)
    threshold_lrv_array = lrv_hat_threshold_of_t(
        cov_double_array=cov_double_array[:threshold_max_lag_value, :],
        sample_size=sample_size,
        noise_type=noise_type,
        sd_type=sd_type,
        sample_type=sample_type)

    arrays_dict = {"Newey-West LRV": nw_lrv_array,
                   "Threshold LRV": threshold_lrv_array}

    plot_arrays(x_array=t_par_array,
                arrays_dict=arrays_dict,
                title="Threshold vs Newey-West",
                x_label="t par",
                par_list=par_list,
                true_array=true_lrv_array,
                y_label="LRV")


if __name__ == '__main__':
    compute_and_save_nw_vs_threshold(sample_size=10000,
                                     t_par_count=11,
                                     mean=0,
                                     sigma=2,
                                     noise_type="gaussian",
                                     sd_type="block_est",
                                     sample_type="ma3")
