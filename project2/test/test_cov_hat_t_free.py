from src.cov_hat_t_free import cov_hat_t_free
from timeit import default_timer as timer
import numpy as np
import unittest

class Test_cov_hat_t_free(unittest.TestCase):
    def test_cov_hat_t_free(self,
                            sample = np.array([1, 2, 3]), lag0 = 0, lag1 = 1):
        print('\n\n===============================================================================')
        print('Testing "cov_hat_t_free"')
        start_time = timer()
        returned_lag_0 = cov_hat_t_free(sample, lag0)
        returned_lag_1 = cov_hat_t_free(sample, lag1)
        duration = timer() - start_time
        expected_lag_0 = 4.6667
        expected_lag_1 = 2.6667
        self.assertEquals(round(returned_lag_0, 3), round(expected_lag_0, 3))
        self.assertEquals(round(returned_lag_1, 3), round(expected_lag_1, 3))
        print('Test parameters:')
        print('sample =', sample)
        print('lag0 =', lag0)
        print('lag1 =', lag1)
        print('expected_lag_0 = ', round(expected_lag_0, 3))
        print('returned_lag_0 = ', round(returned_lag_0, 3))
        print('expected_lag_1 = ', round(expected_lag_1, 3))
        print('returned_lag_1 = ', round(returned_lag_1, 3))
        print("\nDuration: {:g} secs".format(duration))
        print('End of test {}'.format('cov_hat_t_free'))
        print('===============================================================================\n')

if __name__ == '__main__':
    unittest.main()