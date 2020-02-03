from timeit import default_timer as timer
from src.threshold_indicator import threshold_indicator
import unittest

class Test_threshold_indicator(unittest.TestCase):
    def test_threshold_indicator(self,
                                 sample_size=10,
                                 cov_hat=0,
                                 lag=0,
                                 noise_type="gaussian",
                                 sd_type="block_est"):
        print('\n\n===============================================================================')
        print('Testing "threshold_indicator"')

        start_time = timer()
        returned = threshold_indicator(sample_size=sample_size,
                                       cov_hat=cov_hat,
                                       lag=lag,
                                       noise_type=noise_type,
                                       sd_type=sd_type)
        duration = timer() - start_time
        expected = 0
        self.assertEqual(returned, expected)

        print('Test parameters:')
        print('sample_size =', sample_size)
        print('cov_hat =', cov_hat)
        print('lag =', lag)
        print('noise_type =', noise_type)
        print('sd_type =', sd_type)
        print('expected =', expected)
        print('returned =', returned)
        print("\nDuration: {:g} secs".format(duration))
        print('End of test {}'.format('threshold_indicator'))
        print('===============================================================================\n')

if __name__ == '__main__':
    unittest.main()
