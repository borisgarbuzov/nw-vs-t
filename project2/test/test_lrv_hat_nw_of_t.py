from src.lrv_hat_nw_of_t import lrv_hat_nw_of_t
from src.cov_double_array_of_t import cov_double_array_of_t
from src.diagonal_sample_tvma1 import diagonal_sample_tvma1
from src.support_bound import support_bound
from timeit import default_timer as timer
import numpy as np
import unittest


class Test_run_lrv_hat_nw_of_t(unittest.TestCase):
    def test_run_lrv_hat_nw_of_t(self, t_par_count=11,
                             sample_size=20,
                             mean=0,
                             sigma=2,
                             noise_type='bernoulli'):

        print('\n\n===============================================================================')
        print('RUN testing "lrv_hat_nw_of_t"')
        diagonal_sample = diagonal_sample_tvma1(sample_size=sample_size,
                                                mean=mean,
                                                sigma=sigma,
                                                noise_type=noise_type)

        max_lag = int(support_bound(sample_size=sample_size)) + 1

        cov_double_array = cov_double_array_of_t(sample=diagonal_sample,
                                                 t_par_count=t_par_count,
                                                 max_lag=max_lag)
        start_time = timer()
        returned = lrv_hat_nw_of_t(cov_double_array=cov_double_array, sample_size=sample_size)
        duration = timer() - start_time
        print('Test parameters:')
        print('t_par_count = ', t_par_count)
        print('sample_size = ', sample_size)
        print('mean = ', mean)
        print('sigma = ', sigma)
        print('noise_type = ', noise_type)
        
        print('\ncov_double_aray_size = ', cov_double_array.shape)

        print('\nreturned = ', type(returned))
        if isinstance(returned, list):
            print('returned shape = ', len(returned))
        elif isinstance(returned, np.ndarray):
            print('returned shape = ', returned.shape)
        print('returned = ', returned)

        print("\nDuration: {:g} secs".format(duration))
        print('End of RUN test {}'.format('lrv_hat_nw_of_t'))
        print('===============================================================================\n')


class Test_lrv_hat_nw_of_t(unittest.TestCase):
    def assertListAlmostEqual(self, list1, list2, places):
        self.assertEqual(len(list1), len(list2))
        for a, b in zip(list1, list2):
            self.assertAlmostEqual(a, b, places)

    def test_lrv_hat_nw_of_t(self, sample_size=2,
                             cov_double_array = [[1,2,3],[5,6,7]],
                             true_returned=[3.063, 4.4756, 5.8882]):
        print('\n\n===============================================================================')
        print('Testing "lrv_hat_nw_of_t"')
        
        start_time = timer()
        returned = lrv_hat_nw_of_t(cov_double_array=cov_double_array,
                                   sample_size=sample_size)
        duration = timer() - start_time
        
        self.assertListAlmostEqual(list(returned), list(true_returned), places=4)
        
        print('Test parameters:')
        print('sample_size = ', sample_size)
        print('cov_double_array = ', cov_double_array)
        print('true_returned = ', true_returned)
        
        print('\ncov_double_aray_size = ', np.array(cov_double_array).shape)

        print('\nreturned = ', type(returned))
        if isinstance(returned, list):
            print('returned shape = ', len(returned))
        elif isinstance(returned, np.ndarray):
            print('returned shape = ', returned.shape)
        print('returned = ', returned)

        print("\nDuration: {:g} secs".format(duration))
        print('End of test {}'.format('lrv_hat_nw_of_t'))
        print('===============================================================================\n')


if __name__ == '__main__':
    unittest.main()
