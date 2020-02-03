import numpy as np


def create_t_par_array(t_par_count: int) -> np.array: 
    """
    Splits [0, 1] interval into t_par_count-1 intervals.
    :param t_par_count: a size of array to be returned
    :return : a numpy array of t_par_count values, 
    starting with 0 and ending with 1, equally spaced. 
    """
    if t_par_count <= 1:
        raise ValueError(
            "t_par_count is 1 or smaller, whereas it should be 2 or greater")
    t_par_count_inner = t_par_count - 1
    t_par_array = np.arange(0, 1, 1 / t_par_count_inner)
    return np.append(t_par_array, 1)
