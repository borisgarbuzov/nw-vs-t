from src.diagonal_sample_tvma1 import diagonal_sample_tvma1
from src.cov_column_t_free import cov_column_t_free
from src.threshold_max_lag import threshold_max_lag
from src.lrv_hat_threshold_t_free import lrv_hat_threshold_t_free
from timeit import default_timer as timer
import numpy as np
import unittest


class Test_lrv_hat_threshold_t_free(unittest.TestCase):
    def test_lrv_hat_threshold_t_free(self,
                                      noise_type="gaussian",
                                      sd_type="block_est"):
        print('\n\n===============================================================================')
        print('RUN testing "lrv_hat_threshold_t_free"')

        start_time = timer()
        small = 0.1
        big = 1000
        sample_size = 10
        cov_hat_column = np.array([small, big])
        returned = lrv_hat_threshold_t_free(cov_hat_column=cov_hat_column,
                                            sample_size=sample_size,
                                            noise_type=noise_type,
                                            sd_type=sd_type)
        duration = timer() - start_time
        expected = 2*big
        print('Test parameters:')
        print('cov_hat_column =', cov_hat_column)
        print('sample_size =', sample_size)
        print('noise_type =', noise_type)
        print('sd_type =', sd_type)
        print('expected =', expected)
        print('returned =', returned)
        print("\nDuration: {:g} secs".format(duration))
        print('End of RUN test {}'.format('lrv_hat_threshold_t_free'))
        print('===============================================================================\n')


class Test_lrv_hat_threshold_real_t_free(unittest.TestCase):
    def test_lrv_hat_threshold_real_t_free(self,
                                           sample_size=100,
                                           noise_type="gaussian",
                                           sd_type="block_est"):
        print('\n\n===============================================================================')
        print('testing "lrv_hat_threshold_real_t_free"')

        start_time = timer()
        sample = diagonal_sample_tvma1(sample_size=sample_size,
                                       mean=0,
                                       sigma=2,
                                       noise_type="gaussian")
        max_lag = threshold_max_lag(sample_size=sample_size)
        cov_hat_column = cov_column_t_free(sample=sample, max_lag=max_lag)

        returned = lrv_hat_threshold_t_free(cov_hat_column=cov_hat_column,
                                            sample_size=sample_size,
                                            noise_type=noise_type,
                                            sd_type=sd_type)
        duration = timer() - start_time
        print('Test parameters:')
        print('sample_size =', sample_size)
        print('noise_type =', noise_type)
        print('sd_type =', sd_type)
        print('returned =', returned)
        print("\nDuration: {:g} secs".format(duration))
        print('End of test {}'.format('lrv_hat_threshold_real_t_free'))
        print('===============================================================================\n')


if __name__ == '__main__':
    unittest.main()
