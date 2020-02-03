from src.compute_and_save_var_cov_hat_native_matrix import compute_and_save_var_cov_hat_native_matrix
from timeit import default_timer as timer
import numpy as np
import unittest


class Test_run_compute_and_save_var_cov_hat_native_matrix(unittest.TestCase):
    def test_run_compute_and_save_var_cov_hat_native_matrix(self,
                                                            replication_count=3,
                                                            sample_size_array=[1000],
                                                            mean=0,
                                                            sigma=2,
                                                            noise_type='gaussian',
                                                            is_data=False,
                                                            fix_number_of_lags=None):

        print('\n\n===============================================================================')
        print('RUN testing "compute_and_save_var_cov_hat_native_matrix"')
        
        start_time = timer()
        returned = compute_and_save_var_cov_hat_native_matrix(replication_count=replication_count,
                                                              sample_size_array=sample_size_array,
                                                              mean=mean,
                                                              sigma=sigma,
                                                              noise_type=noise_type, 
                                                              is_data=is_data,
                                                              fix_number_of_lags=fix_number_of_lags)
        duration = timer() - start_time
        
        print('Test parameters:')
        print('replication_count = ', replication_count)
        print('sample_size_array = ', sample_size_array)
        print('mean = ', mean)
        print('sigma = ', sigma)
        print('noise_type = ', noise_type)
        print('is_data = ', is_data)
        print('fix_number_of_lags = ', fix_number_of_lags)

        print('\nreturned = ', type(returned))
        if isinstance(returned, list):
            print('returned shape = ', len(returned))
        elif isinstance(returned, np.ndarray):
            print('returned shape = ', returned.shape)
        print('returned = ', returned)

        print("\nDuration: {:g} secs".format(duration))
        print('End of RUN test {}'.format('compute_and_save_var_cov_hat_native_matrix'))
        print('===============================================================================\n')


if __name__ == '__main__':
    unittest.main()
