from src.create_t_par_array import create_t_par_array
from timeit import default_timer as timer
import numpy as np
import unittest


class Test_create_t_par_array(unittest.TestCase):
    def test_create_noise(self, t_par_count=11):
        print('\n\n===============================================================================')
        print('Testing "create_t_par_array"')
        start_time = timer()
        
        returned = create_t_par_array(t_par_count=t_par_count)
        print('Test parameters:')
        print('t_par_count = ', t_par_count)

        
        print('\nreturned = ', type(returned))
        if isinstance(returned, list):
            print('returned shape = ', len(returned))
        elif isinstance(returned, np.ndarray):
            print('returned shape = ', returned.shape)
        print('returned = ', returned)
        
            
        print("\nDuration: {:g} secs".format(timer() - start_time))
        print('End of test {}'.format('create_t_par_array'))
        print('===============================================================================\n')


if __name__ == '__main__':
    unittest.main()
