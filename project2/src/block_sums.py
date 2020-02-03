from src.batch_size import batch_size
import numpy as np


def block_sums(paired_product_array: np.array) -> np.array:
    """
    This is Q in the bootstrap.
    It looks like stable function.
    Has deterministic test that passed successfully.

    :param paired_product_array: this is Z in bootstrap
    :return: numpy array
    """
    sample_size = len(paired_product_array)
    batch_size_value = batch_size(sample_size=sample_size)
    block_sum_array = np.full(shape=sample_size - batch_size_value + 1,
                              fill_value=np.nan)

    for index in range(sample_size - batch_size_value + 1):
        block_sum_array[index] = np.sum(paired_product_array[index:index +
                                                                   batch_size_value])

    return block_sum_array
