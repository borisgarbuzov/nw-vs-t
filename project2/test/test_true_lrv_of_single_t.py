from src.true_lrv_of_single_t import true_lrv_ma1_of_single_t, true_lrv_scaled_noise_of_single_t
from timeit import default_timer as timer
import unittest
import numpy as np

class Test_true_lrv_of_single_t(unittest.TestCase):
    def test_true_lrv_ma1_of_single_t(self,
                                      sigma = 1,
                                      t_par = 1):
        print('\n\n===============================================================================')
        print('Testing "true_lrv_ma1_of_single_t"')
        start_time = timer()
        returned = true_lrv_ma1_of_single_t(sigma, t_par)
        duration = timer() - start_time
        print('Test parameters:')
        print('sigma = ', sigma)
        print('t_par = ', t_par)
        print('returned = ', returned)
        print("\nDuration: {:g} secs".format(duration))
        print('End of test {}'.format('true_lrv_ma1_of_single_t'))
        print('===============================================================================\n')

    def test_true_lrv_scaled_noise_of_single_t(self,
                                               sigma = 1,
                                               t_par = 1):
        print('\n\n===============================================================================')
        print('Testing "true_lrv_scaled_noise_of_single_t"')
        start_time = timer()
        returned = true_lrv_scaled_noise_of_single_t(sigma, t_par)
        duration = timer() - start_time
        print('Test parameters:')
        print('sigma = ', sigma)
        print('t_par = ', t_par)
        print('returned = ', returned)
        print("\nDuration: {:g} secs".format(duration))
        print('End of test {}'.format('true_lrv_scaled_noise_of_single_t'))
        print('===============================================================================\n')
        
if __name__ == '__main__':
    unittest.main()
