from src.compute_and_save_v_vs_nw import compute_and_save_v_vs_nw
from timeit import default_timer as timer
import numpy as np
import unittest

class Test_compute_and_save_v_vs_nw(unittest.TestCase):
    def test_compute_and_save_v_vs_nw(self, sample_size = 10,
                                            t_par_count = 11,
                                            mean = 0,
                                            sigma = 2,
                                            noise_type = 'bernoulli'):
        print('\n\n===============================================================================')
        print('Testing "compute_and_save_v_vs_nw"')
        start_time = timer()
        compute_and_save_v_vs_nw(sample_size, t_par_count, mean, sigma, noise_type)
        end_time = timer() - start_time
        print('Test parameters:')
        print('sample_size =', sample_size)
        print('t_par_count =', t_par_count)
        print('mean =', mean)
        print('sigma =', sigma)
        print('noise_type =', noise_type)

        print("\nDuration: {:g} secs".format(end_time))
        print('End of test {}'.format('compute_and_save_v_vs_nw'))
        print('===============================================================================\n')


if __name__ == '__main__':
    unittest.main()

