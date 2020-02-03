from src.create_noise import create_noise
from src.coef import coef, coef_2, coef_3
import numpy as np


def diagonal_sample_tvma3(sample_size: int,
                          mean: int,
                          sigma: int,
                          noise_type: str,
                          noise=None):
    """
    Creates the diagonal time-varying MA3 sample, given
    sample size, mean, sigma and noise type.
    :param sample_size: size of a sample to be generated.
    :param mean: mean of the noise to generate, if not given.
    :param sigma: sigma of the noise to generate, if not given.
    :param noise_type: type of the noise to generate, if not given.
    :param noise: an array of the size sample_size+3. If it is given (not None), then sample size agreement is checked, and other arguments ignored.
    The cycle starts from 1, not from 0, because
    we pass i+1 to theta.
    Basically, indexation in Python is x(0), ...x(n-1),
    while in formulas, it is for the case x(1), ...x(n).
    """
    if noise is None:
        noise = create_noise(noise_size=sample_size + 3, mean=mean, sigma=sigma,
                             noise_type=noise_type)
    elif len(noise) != sample_size + 3:
        raise ValueError("length of noise should be sample_size + 3")

    diagonal_sample_tvma3 = np.full(shape=sample_size, fill_value=np.nan)

    for i in range(1, sample_size + 1):
        diagonal_sample_tvma3[i - 1] = noise[i + 2] + \
        coef(t_par=i / sample_size) * noise[i + 1] + \
        coef_2(t_par=i / sample_size) * noise[i] + \
        coef_3(t_par=i / sample_size) * noise[i - 1]
    return diagonal_sample_tvma3
