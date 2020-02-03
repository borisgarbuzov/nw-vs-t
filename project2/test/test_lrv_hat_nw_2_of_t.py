from src.lrv_hat_nw_2_of_t import lrv_hat_nw_2_of_t
from timeit import default_timer as timer
import unittest
import numpy as np

class Test_lrv_hat_nw_2_of_t(unittest.TestCase):
    def test_lrv_hat_nw_2_of_t(self,
                               sample = np.array([1, 2, 3]),
                               t_par_array = np.array([1, 2, 3])):
        print('\n\n===============================================================================')
        print('Testing "lrv_hat_nw_2_of_t"')
        start_time = timer()
        returned = lrv_hat_nw_2_of_t(sample, t_par_array)
        duration = timer() - start_time
        print('Test parameters:')
        print('sample = ', sample)
        print('t_par_array = ', t_par_array)
        print('returned = ', returned)
        print("\nDuration: {:g} secs".format(duration))
        print('End of test {}'.format('lrv_hat_nw_2_of_t'))
        print('===============================================================================\n')

if __name__ == '__main__':
    unittest.main()