from src.lrv_hat_nw_2_of_single_t import lrv_hat_nw_2_of_single_t
from timeit import default_timer as timer
import numpy as np
import unittest


class Test_lrv_hat_nw_2_of_signle_t(unittest.TestCase):
    def test_lrv_hat_nw_2_of_single_t(self,
                                      sample=np.array([1, 2, 3, 4, 5]),
                                      t_par=0.5):

        print('\n\n===============================================================================')
        print('Testing "lrv_hat_nw_2_of_single_t"')

        start_time = timer()

        returned = lrv_hat_nw_2_of_single_t(sample=sample,
                                             t_par=t_par)
        print('Test parameters:')
        print('sample =', sample)
        print('t_par =', t_par)

        print('\nreturned = ', type(returned))
        if isinstance(returned, list):
            print('returned shape = ', len(returned))
        elif isinstance(returned, np.ndarray):
            print('returned shape = ', returned.shape)
        print('returned = ', returned)

        print("\nDuration: {:g} secs".format(timer() - start_time))
        print('End of test {}'.format('lrv_hat_nw_2_of_single_t'))
        print('===============================================================================\n')


if __name__ == '__main__':
    unittest.main()
