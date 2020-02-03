import numpy as np


def zhou_treshold(sample_size: int):
    """
    Computes RHS for indicator's formula. 
    :return: formula value. 
    """        
    treshold_value = 1.96 * np.sqrt(np.log(sample_size))
    return treshold_value
