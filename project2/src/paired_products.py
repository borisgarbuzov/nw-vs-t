import numpy as np


def paired_products(sample: np.array, lag: int) -> np.array:
    """
    Computes and returns the array of paired lagged products of a given sample. 
    Is denoted by Z in a formula. 
    :param sample: the sample to be used in lagged paired products computation. 
    :param lag: the lag to be used in lagged paired products computation. 
    :return: paired_product_array, an array of lagged products of a sample. 
    """
    sample_size = len(sample)

    if lag < 0:
        raise ValueError("lag should be equal or more than 0")
    elif lag > sample_size - 1:
        raise ValueError("lag should be less than sample size - 1")

    paired_product_array = np.full(shape=sample_size - lag, fill_value=np.nan)

    for index in range(sample_size - lag):
        paired_product_array[index] = sample[index] * sample[index + lag]

    return paired_product_array
