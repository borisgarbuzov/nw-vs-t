from src.true_lrv_of_t import true_lrv_ma1_of_t, true_lrv_scaled_noise_of_t
from timeit import default_timer as timer
import unittest
import numpy as np

class Test_true_lrv_of_t(unittest.TestCase):
    def test_true_lrv_ma1_of_t(self,
                                sigma = 1,
                                t_par_array = np.array([1, 2, 3])):
        print('\n\n===============================================================================')
        print('Testing "true_lrv_ma1_of_t"')
        start_time = timer()
        returned = true_lrv_ma1_of_t(sigma, t_par_array)
        duration = timer() - start_time
        print('Test parameters:')
        print('sigma = ', sigma)
        print('t_par_array = ', t_par_array)
        print('returned = ', returned)
        print("\nDuration: {:g} secs".format(duration))
        print('End of test {}'.format('true_lrv_ma1_of_t'))
        print('===============================================================================\n')

    def test_true_lrv_scaled_noise_of_t(self,
                                        sigma = 1,
                                        t_par_array = np.array([1, 2, 3])):
        print('\n\n===============================================================================')
        print('Testing "true_lrv_scaled_noise_of_t"')
        start_time = timer()
        returned = true_lrv_scaled_noise_of_t(sigma, t_par_array)
        duration = timer() - start_time
        print('Test parameters:')
        print('sigma = ', sigma)
        print('t_par_array = ', t_par_array)
        print('returned = ', returned)
        print("\nDuration: {:g} secs".format(duration))
        print('End of test {}'.format('true_lrv_scaled_noise_of_t'))
        print('===============================================================================\n')

if __name__ == '__main__':
    unittest.main()
