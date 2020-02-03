def coef(t_par):
    """
    Can be changed to any function,
    but then we need to change the true values of covariance and LRV.
    :param t_par: a value of t parameter (scaled time) at which we need a coefficient in TVMA process. 
    :return: a value of a coefficient 1 in TVMA at the point of a given t_par. 
    """
    return 2 - t_par


def coef_2(t_par):
    """
    Can be changed to any function,
    but then we need to change the true values of covariance and LRV.
    :param t_par: a value of t parameter (scaled time) at which we need a second coefficient in TVMA process. 
    :return: a value of a coefficient 2 in TVMA at the point of a given t_par. 
    """
    return 0


def coef_3(t_par):
    """
    Can be changed to any function,
    but then we need to change the true values of covariance and LRV.
    :param t_par: a value of t parameter (scaled time) at which we need a third coefficient in TVMA process. 
    :return: a value of a coefficient 3 in TVMA at the point of a given t_par. 
    """
    return -3 + t_par
