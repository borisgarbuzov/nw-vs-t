from src.cov_double_array_of_t import cov_double_array_of_t
from src.diagonal_sample_tvma1 import diagonal_sample_tvma1
from src.support_bound import support_bound
from timeit import default_timer as timer
import numpy as np
import unittest


class Test_cov_double_array_of_t(unittest.TestCase):
    def test_cov_double_array_of_t(self, t_par_count=11,
                                   sample_size=20,
                                   mean=0,
                                   sigma=2,
                                   noise_type='bernoulli'):

        print('\n\n===============================================================================')
        print('Testing "cov_double_array_of_t"')
        start_time = timer()
        diagonal_sample = diagonal_sample_tvma1(sample_size=sample_size,
                                                mean=mean,
                                                sigma=sigma,
                                                noise_type=noise_type)
        max_lag = int(support_bound(sample_size=sample_size)) + 1
        returned = cov_double_array_of_t(sample=diagonal_sample,
                                         t_par_count=t_par_count,
                                         max_lag=max_lag)
        duration = timer() - start_time
        print('Test parameters:')
        print('sample_size = ', diagonal_sample.shape)
        print('t_par_count = ', t_par_count)

        print('\nreturned = ', type(returned))
        if isinstance(returned, list):
            print('returned shape = ', len(returned))
        elif isinstance(returned, np.ndarray):
            print('returned shape = ', returned.shape)
        print('returned = ', returned)

        print("\nDuration: {:g} secs".format(duration))
        print('End of test {}'.format('cov_double_array_of_t'))
        print('===============================================================================\n')


if __name__ == '__main__':
    unittest.main()
