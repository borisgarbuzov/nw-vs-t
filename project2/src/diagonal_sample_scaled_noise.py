from src.create_noise import create_noise
from src.coef import coef
import numpy as np


def diagonal_sample_scaled_noise(sample_size: int,
                                 mean: int,
                                 sigma: int,
                                 noise_type: str,
                                 noise=None):
    """
    Currently unused.
    Copied from the first project with translation from R to Python.
    Forms a diagonal sample of noise, stretched by coef(t) values
    at each index point.
    :sample_size: size of a sample to be generated.
    :mean: mean of a notise to be genrated.
    :noise_type: "gaussian" or "bernoulli".
    :return: one-dimensional array of noise values.
    """
    if noise is None:
        noise = create_noise(noise_size=sample_size + 1, mean=mean, sigma=sigma,
                             noise_type=noise_type)
    elif len(noise) != sample_size + 1:
        raise ValueError("length of noise should be sample_size + 1")

    diagonal_sample_scaled_noise = np.full(shape=sample_size, fill_value=np.nan)

    for i in range(1, sample_size + 1):
        diagonal_sample_scaled_noise[i - 1] = coef(t_par=i / sample_size) * \
                                              noise[i - 1]
    return diagonal_sample_scaled_noise
