from src.coef import coef, coef_2, coef_3
from src.create_noise import create_noise
from src.create_t_par_array import create_t_par_array
import numpy as np


def horizontal_sample_tvma3(sample_size: int,
                            t_par_count: int,
                            mean: int,
                            sigma: int,
                            noise_type: str,
                            noise=None):
    """
    Generates MA(3) sample for the given noise or its parameters. 
    :sample_size: number of observations or number of columns in the returned matrix.
    :t_par_count: number of t values or number of rows in the returned matrix.
    :mean: mean of the noise.
    :return: a double array t_par_count by sample_size
    of stationary MA1 samples. Each line, corresponding to tPar value.
    """
    if noise is None:
        noise = create_noise(noise_size=sample_size + 3, mean=mean, sigma=sigma,
                             noise_type=noise_type)
    elif len(noise) != sample_size + 3:
        raise ValueError("length of noise should be sample_size + 3")
    t_par_array = create_t_par_array(t_par_count=t_par_count)
    horizontal_sample_tvma3 = np.full(shape=(t_par_count, sample_size),
                                      fill_value=np.nan)
    for i in range(t_par_count):
        for j in range(sample_size):
            t_par = t_par_array[i]
            horizontal_sample_tvma3[i, j] = noise[j + 3] + coef(t_par=t_par) * \
                                            noise[j + 2] + coef_2(t_par=t_par) * \
                                            noise[j + 1] + coef_3(t_par=t_par) * \
                                            noise[j]
    return horizontal_sample_tvma3
