from src.block_sums import block_sums
from timeit import default_timer as timer
import numpy as np
import unittest


class Test_block_sums(unittest.TestCase):
    def test_block_sums(self,
                        paired_product_array = np.array([1, 4, 9, 16, 25]),
                        true_array = np.array([5., 13., 25., 41.])):

        print('\n\n===============================================================================')
        print('Testing "block_sums"')

        start_time = timer()
        block_sum_array = block_sums(paired_product_array=paired_product_array)

        print('Test parameters:')
        print('paired_product_array =', paired_product_array)
        print('true_array =', true_array)

        self.assertEqual(block_sum_array.tolist(), true_array.tolist())

        print('\nreturned = ', type(block_sum_array))
        if isinstance(block_sum_array, list):
            print('returned shape = ', len(block_sum_array))
        elif isinstance(block_sum_array, np.ndarray):
            print('returned shape = ', block_sum_array.shape)
        print('block_sum_array = ', block_sum_array)

        print("\nDuration: {:g} secs".format(timer() - start_time))
        print('End of test {}'.format('block_sums'))
        print('===============================================================================\n')


if __name__ == '__main__':
    unittest.main()
