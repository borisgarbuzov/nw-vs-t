def true_lrv_ma1_t_free(sigma: float):
    """
    True global LRV for given parameters. 
    Result of integration from 0 to 1 of the t-dependent LRV
    :param sigma: standard deviation of noise used to simulate the MA1 sample. 
    :return: true LRV value. 
    """    
    return (19 / 3) * (sigma ** 2)


def true_lrv_ma3_t_free(sigma: float):
    """
    True global LRV for given parameters. 
    Result of integration from 0 to 1 of the t-dependent LRV
    :param sigma: standard deviation of noise used to simulate the MA3 sample. 
    :return: true LRV value. 
    """        
    return (sigma ** 2) * (148 / 3)
