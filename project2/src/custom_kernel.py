import numpy as np


def triangular_kernel(v) -> float:
    """
    A triangle with vertexes at (0, 1), (-1, 0), (1, 0). 
    Used in Newey-West. 
    :param v: a kernel argument, usually formed as (i/n - t)/b, or lag/support_bound. 
    :return : a scalar value of a kernel at the point of v. 
    """
    if abs(v) <= 1:
        kernel = 1 - abs(v)
    else:
        kernel = 0
    return kernel 


def boxcar_kernel(v):
    """
    A rectangle with vertexes at (-1, 0), (-1, 1/2), (1, 0), (1, 1/2).
    Currenly unused. 
    :param v: a kernel argument, usually formed as (i/n - t)/b, or lag/support_bound. 
    :return : a scalar value of a kernel at the point of v. 
    """
    if abs(v) <= 1:
        kernel = 1 / 2
    else:
        kernel = 0            
    return kernel 


def gaussian_kernel(v):
    """
    Gaussian density with parameters (0,1).
    Currenly used in t-dependent computations for diagonal samples. 
    :param v: a kernel argument, usually formed as (i/n - t)/b, or lag/support_bound. 
    :return : a scalar value of a kernel at the point of v. 
    """
    kernel = np.exp(-v**2/2)/np.sqrt(2*np.pi)
    return kernel
