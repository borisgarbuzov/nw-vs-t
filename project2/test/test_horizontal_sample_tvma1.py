from src.horizontal_sample_tvma1 import horizontal_sample_tvma1
from timeit import default_timer as timer
import numpy as np
import unittest


class Test_horizontal_sample_tvma1(unittest.TestCase):
    def test_horizontal_sample_tvma1(self, sample_size=8, t_par_count=11,
                                     mean=5,
                                     sigma=0.12,
                                     noise_type= ["bernoulli","gaussian"]):

        print('\n\n===============================================================================')
        print('Testing "horizontal_sample_tvma1"')
        start_time = timer()
        
        for each in noise_type:
            
            returned = horizontal_sample_tvma1(sample_size=sample_size, t_par_count=t_par_count, mean=mean, sigma=sigma, noise_type=each)
            print('Test parameters:')
            print('sample_size = ', sample_size)
            print('t_par_count = ', t_par_count)
            print('mean = ', mean)
            print('sigma = ', sigma)
            print('noise_type = ', each)
            
            
            print('\nreturned = ', type(returned))
            if isinstance(returned, list):
                print('returned shape = ', len(returned))
            elif isinstance(returned, np.ndarray):
                print('returned shape = ', returned.shape)
            print('returned = ', returned)
            
                
            print("\nDuration: {:g} secs".format(timer() - start_time))
            print('End of test {}'.format('horizontal_sample_tvma1'))
            print('===============================================================================\n')


if __name__ == '__main__':
    unittest.main()
