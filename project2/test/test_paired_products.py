from src.paired_products import paired_products
from timeit import default_timer as timer
import numpy as np
import unittest


class Test_paired_products(unittest.TestCase):
    def test_paired_products(self,
                             sample = np.array([1, 2, 3, 4, 5]),
                             lag=0,
                             true_array = np.array([1., 4., 9., 16., 25.])):

        print('\n\n===============================================================================')
        print('Testing "paired_products"')

        start_time = timer()
        paired_product_array = paired_products(sample=sample, lag=lag)

        print('Test parameters:')
        print('sample =', sample)
        print('lag=', lag)
        print('true_array =', true_array)

        self.assertEqual(paired_product_array.tolist(), true_array.tolist())

        print('\nreturned = ', type(paired_product_array))
        if isinstance(paired_product_array, list):
            print('returned shape = ', len(paired_product_array))
        elif isinstance(paired_product_array, np.ndarray):
            print('returned shape = ', paired_product_array.shape)
        print('block_sum_array = ', paired_product_array)

        print("\nDuration: {:g} secs".format(timer() - start_time))
        print('End of test {}'.format('paired_products'))
        print('===============================================================================\n')


if __name__ == '__main__':
    unittest.main()
