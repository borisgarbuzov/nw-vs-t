from src.create_noise import create_noise
from timeit import default_timer as timer
import numpy as np
import unittest


class Test_create_noise(unittest.TestCase):
    def test_create_noise(self, noise_size=8, mean=5, sigma=0.12,
                          noise_type= ["bernoulli","gaussian"]):
        print('\n\n===============================================================================')
        print('Testing "create_noise"')
        start_time = timer()
        
        for each in noise_type:
            returned = create_noise(noise_size=noise_size, mean=mean,
                                    sigma=sigma,
                                    noise_type=each)
            print('Test parameters:')
            print('noise_size = ', noise_size)
            print('mean = ', mean)
            print('sigma = ', sigma)
            print('type_of_noise = ', each)

            print('\nreturned = ', type(returned))
            if isinstance(returned, list):
                print('returned shape = ', len(returned))
            elif isinstance(returned, np.ndarray):
                print('returned shape = ', returned.shape)
            print('returned = ', returned)
                
            print("\nDuration: {:g} secs".format(timer() - start_time))
            print('End of test {}'.format('create_noise'))
            print('===============================================================================\n')


if __name__ == '__main__':
    unittest.main()
