from src.coef import coef
from src.create_t_par_array import create_t_par_array
from src.create_noise import create_noise
import numpy as np


def horizontal_sample_scaled_noise(sample_size: int,
                                   t_par_count: int,
                                   mean: int,
                                   sigma: int,
                                   noise_type: str,
                                   noise=None):
    """
    Creates and returns a double array of dimensions [sample_size, t_par_count].
    Each row is a noise sample, streched by coef(t).
    So it produces the double array with proportional rows.
    """
    if noise is None:
        noise = create_noise(noise_size=sample_size + 1, mean=mean, sigma=sigma,
                             noise_type=noise_type)
    elif len(noise) != sample_size + 1:
        raise ValueError("length of noise should be sample_size + 1")

    t_par_array = create_t_par_array(t_par_count=t_par_count)
    horizontal_sample_tvma1 = np.full(shape=(t_par_count, sample_size),
                                      fill_value=np.nan)

    for i in range(t_par_count):
        for j in range(sample_size):
            horizontal_sample_tvma1[i, j] = coef(t_par=t_par_array[i]) * \
                                            noise[j]
    return horizontal_sample_tvma1
