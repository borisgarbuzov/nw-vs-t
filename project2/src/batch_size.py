def batch_size(sample_size: int) -> int:
    """
    Used in bootstrap.
    Zhou will suggest the optimal degree.
    May be chosen in some data driven methods?

    :param sample_size: size of sample
    :return: integer
    Zhou said to read his JASA paper to understand how to get the best batch size. 
    """
    batch_size_value = 1 * sample_size ** (1 / 3)
    return int(round(batch_size_value))
