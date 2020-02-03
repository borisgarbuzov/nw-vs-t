from src.compute_and_save_cov_and_cov_hats import compute_and_save_cov_and_cov_hats
from src.compute_and_save_nw_single_n import compute_and_save_nw_single_n
from src.compute_and_save_thresholds_single_n import compute_and_save_threshold_single_n
from src.compute_and_save_nw_threshold_single_t import compute_and_save_nw_threshold_single_t
from src.compute_and_save_nw_vs_threshold import compute_and_save_nw_vs_threshold
from src.compute_and_save_multi_precision_of_t import compute_and_save_multi_precision_of_t
from src.compute_and_save_threshold_nw_t_free import compute_and_save_threshold_nw_t_free
from src.compute_and_save_v_vs_nw import compute_and_save_v_vs_nw
from src.compute_and_save_var_cov_hat_native_matrix import compute_and_save_var_cov_hat_native_matrix
from src.compute_and_save_var_cov_hat_semi_bootstrap import compute_and_save_var_cov_hat_semi_bootstrap
from src.compute_and_save_var_cov_hat_theoretical_matrix import compute_and_save_var_cov_hat_theoretical_matrix
from src.compute_and_save_var_cov_hat_native_matrix_means import compute_and_save_var_cov_hat_native_matrix_means
from timeit import default_timer as timer
import unittest
import numpy as np


class Test_compute_and_save_all(unittest.TestCase):
    def test_compute_and_save_cov_and_cov_hats(self,
                                              sample_size=5,
                                              t_par_count=3,
                                              gamma_count=2,
                                              mean=0,
                                              sigma=2,
                                              lag=2,
                                              type_process='MA1',
                                              noise_type='bernoulli',
                                              diag_or_horiz='diag'):
        print('\n\n===============================================================================')
        print('Testing "compute_and_save_cov_and_cov_hats"')

        start_time = timer()
        compute_and_save_cov_and_cov_hats(sample_size, t_par_count, gamma_count, mean, sigma, lag, type_process, noise_type, diag_or_horiz)
        end_time = timer() - start_time

        print('Test parameters:')
        print('sample_size =', sample_size)
        print('t_par_count =', t_par_count)
        print('gamma_count =', gamma_count)
        print('mean =', mean)
        print('sigma =', sigma)
        print('lag =', lag)
        print('type_process =', type_process)
        print('noise_type =', noise_type)
        print('diag_or_horiz =', diag_or_horiz)

        print("\nDuration: {:g} secs".format(end_time))
        print('End of test {}'.format('compute_and_save_cov_and_cov_hats'))
        print('===============================================================================\n')

    def test_compute_and_save_nw_single_n(self,
                                        sample_size=5,
                                        t_par_count=3,
                                        mean=0,
                                        sigma=2,
                                        noise_type="gaussian",
                                        replication_count=2):
        print('\n\n===============================================================================')
        print('Testing "compute_and_save_nw_single_n"')

        start_time = timer()
        compute_and_save_nw_single_n(sample_size, t_par_count, mean, sigma, noise_type, replication_count)
        end_time = timer() - start_time

        print('Test parameters:')
        print('sample_size =', sample_size)
        print('t_par_count =', t_par_count)
        print('mean =', mean)
        print('sigma =', sigma)
        print('noise_type =', noise_type)
        print('replication_count =', replication_count)

        print("\nDuration: {:g} secs".format(end_time))
        print('End of test {}'.format('compute_and_save_nw_single_n'))
        print('===============================================================================\n')

    def test_compute_and_save_nw_threshold_single_t(self,
                                        sample_size_from=5,
                                        sample_size_to=10,
                                        sample_size_by=5,
                                        replication_count=2,
                                        mean=0,
                                        sigma=2,
                                        noise_type="gaussian",
                                        sd_type="block_est",
                                        t_par="free"):
        print('\n\n===============================================================================')
        print('Testing "compute_and_save_nw_threshold_single_t"')

        start_time = timer()
        compute_and_save_nw_threshold_single_t(sample_size_from=sample_size_from,
                                               sample_size_to=sample_size_to,
                                               sample_size_by=sample_size_by,
                                               replication_count=replication_count,
                                               mean=mean,
                                               sigma=sigma,
                                               noise_type=noise_type,
                                               sd_type=sd_type,
                                               t_par=t_par)
        end_time = timer() - start_time

        print('Test parameters:')
        print('sample_size_from =', sample_size_from)
        print('sample_size_to =', sample_size_to)
        print('sample_size_by =', sample_size_by)
        print('replication_count =', replication_count)
        print('mean =', mean)
        print('sigma =', sigma)
        print('noise_type =', noise_type)
        print('sd_type =', sd_type)
        print('t_par =', t_par)

        print("\nDuration: {:g} secs".format(end_time))
        print('End of test {}'.format('compute_and_save_nw_threshold_single_t'))
        print('===============================================================================\n')

    def test_compute_and_save_nw_vs_threshold(self,
                                            sample_size=5,
                                            t_par_count=3,
                                            mean=0,
                                            sigma=2,
                                            noise_type="gaussian",
                                            sd_type="block_est"):
        print('\n\n===============================================================================')
        print('Testing "compute_and_save_nw_vs_threshold"')

        start_time = timer()
        compute_and_save_nw_vs_threshold(sample_size=sample_size,
                                         t_par_count=t_par_count,
                                         mean=mean,
                                         sigma=sigma,
                                         noise_type=noise_type,
                                         sd_type=sd_type)
        end_time = timer() - start_time

        print('Test parameters:')
        print('sample_size =', sample_size)
        print('t_par_count =', t_par_count)
        print('mean =', mean)
        print('sigma =', sigma)
        print('noise_type =', noise_type)
        print('sd_type =', sd_type)

        print("\nDuration: {:g} secs".format(end_time))
        print('End of test {}'.format('compute_and_save_nw_vs_threshold'))
        print('===============================================================================\n')

    def test_compute_and_save_threshold_nw_t_free(self,
                                                sample_size=5,
                                                replication_count=2,
                                                mean=0,
                                                sigma=2,
                                                noise_type="gaussian",
                                                sd_type="block_est",
                                                lrv_est="both"):
        print('\n\n===============================================================================')
        print('Testing "compute_and_save_threshold_nw_t_free"')

        start_time = timer()
        compute_and_save_threshold_nw_t_free(sample_size=sample_size,
                                             replication_count=replication_count,
                                             mean=mean,
                                             sigma=sigma,
                                             noise_type=noise_type,
                                             sd_type=sd_type,
                                             lrv_est=lrv_est)
        end_time = timer() - start_time

        print('Test parameters:')
        print('sample_size =', sample_size)
        print('replication_count =', replication_count)
        print('mean =', mean)
        print('sigma =', sigma)
        print('noise_type =', noise_type)
        print('sd_type =', sd_type)
        print('lrv_est =', lrv_est)

        print("\nDuration: {:g} secs".format(end_time))
        print('End of test {}'.format('compute_and_save_threshold_nw_t_free'))
        print('===============================================================================\n')

    def test_compute_and_save_threshold_single_n(self,
                                                sample_size=5,
                                                t_par_count=3,
                                                mean=0,
                                                sigma=2,
                                                noise_type="gaussian",
                                                sd_type="block_est",
                                                replication_count=1):
        print('\n\n===============================================================================')
        print('Testing "compute_and_save_threshold_single_n"')

        start_time = timer()
        compute_and_save_threshold_single_n(sample_size=sample_size,
                                            t_par_count=t_par_count,
                                            mean=mean,
                                            sigma=sigma,
                                            noise_type=noise_type,
                                            sd_type=sd_type,
                                            replication_count=replication_count)
        end_time = timer() - start_time

        print('Test parameters:')
        print('sample_size =', sample_size)
        print('t_par_count =', t_par_count)
        print('mean =', mean)
        print('sigma =', sigma)
        print('noise_type =', noise_type)
        print('sd_type =', sd_type)
        print('replication_count =', replication_count)

        print("\nDuration: {:g} secs".format(end_time))
        print('End of test {}'.format('compute_and_save_threshold_single_n'))
        print('===============================================================================\n')

    def test_compute_and_save_v_vs_nw(self,
                                      sample_size=5,
                                      t_par_count=3,
                                      mean=0,
                                      sigma=2,
                                      noise_type='gaussian'):
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

    def test_compute_and_save_var_cov_hat_native_matrix(self,
                                                        replication_count=2,
                                                        sample_size_array=np.arange(10, 21, 10),
                                                        mean=0,
                                                        sigma=2,
                                                        noise_type='gaussian',
                                                        is_data=False):
        print('\n\n===============================================================================')
        print('Testing "compute_and_save_var_cov_hat_native_matrix"')

        start_time = timer()
        compute_and_save_var_cov_hat_native_matrix(replication_count, sample_size_array, mean, sigma, noise_type, is_data)
        end_time = timer() - start_time

        print('Test parameters:')
        print('replication_count =', replication_count)
        print('sample_size_array =', sample_size_array)
        print('mean =', mean)
        print('sigma =', sigma)
        print('noise_type =', noise_type)
        print('is_data =', is_data)

        print("\nDuration: {:g} secs".format(end_time))
        print('End of test {}'.format('compute_and_save_var_cov_hat_native_matrix'))
        print('===============================================================================\n')

    def test_compute_and_save_var_cov_hat_native_matrix_means(self):
        print('\n\n===============================================================================')
        print('Testing "compute_and_save_var_cov_hat_native_matrix_means"')

        start_time = timer()
        compute_and_save_var_cov_hat_native_matrix_means()
        end_time = timer() - start_time

        print("\nDuration: {:g} secs".format(end_time))
        print('End of test {}'.format('compute_and_save_var_cov_hat_native_matrix_means'))
        print('===============================================================================\n')

    def test_compute_and_save_var_cov_hat_semi_bootstrap(self,
                                                        sample_size_from=5,
                                                        sample_size_to=11,
                                                        sample_size_by=5,
                                                        mean=0,
                                                        sigma=2,
                                                        noise_type="gaussian",
                                                        is_data=False):
        print('\n\n===============================================================================')
        print('Testing "compute_and_save_var_cov_hat_semi_bootstrap"')

        start_time = timer()
        compute_and_save_var_cov_hat_semi_bootstrap(sample_size_from, sample_size_to, sample_size_by, mean, sigma, noise_type, is_data)
        end_time = timer() - start_time

        print('Test parameters:')
        print('sample_size_from =', sample_size_from)
        print('sample_size_to =', sample_size_to)
        print('sample_size_by =', sample_size_by)
        print('mean =', mean)
        print('sigma =', sigma)
        print('noise_type =', noise_type)
        print('is_data =', is_data)

        print("\nDuration: {:g} secs".format(end_time))
        print('End of test {}'.format('compute_and_save_var_cov_hat_semi_bootstrap'))
        print('===============================================================================\n')

    def test_compute_and_save_var_cov_hat_theoretical_matrix(self,
                                                            sample_size_array=np.arange(10, 21, 10),
                                                            lags_array=np.arange(0, 3),
                                                            noise_type='gaussian',
                                                            is_data=False):
        print('\n\n===============================================================================')
        print('Testing "compute_and_save_var_cov_hat_theoretical_matrix"')

        start_time = timer()
        compute_and_save_var_cov_hat_theoretical_matrix(sample_size_array, lags_array, noise_type, is_data)
        end_time = timer() - start_time

        print('Test parameters:')
        print('sample_size_array =', sample_size_array)
        print('lags_array =', lags_array)
        print('noise_type =', noise_type)
        print('is_data =', is_data)

        print("\nDuration: {:g} secs".format(end_time))
        print('End of test {}'.format('compute_and_save_var_cov_hat_theoretical_matrix'))
        print('===============================================================================\n')

    def test_compute_and_save_multi_precision_of_t(self,
                                                   true_array=[1,2,3],
                                                   est_dict={'est_double_array_1': [[1,2,3], [4,5,6], [7,8,9]]},
                                                   x_label="t_par",
                                                   x_array=[100,200,300]):
        print('\n\n===============================================================================')
        print('Testing "compute_and_save_multi_precision_of_t"')

        start_time = timer()
        compute_and_save_multi_precision_of_t(true_array=true_array,
                                              est_dict=est_dict,
                                              x_array=x_array)
        end_time = timer() - start_time

        print('Test parameters:')
        print('true_array =', true_array)
        print('est_dict =', est_dict)
        print('x_label =', x_label)
        print('x_array =', x_array)

        print("\nDuration: {:g} secs".format(end_time))
        print('End of test {}'.format('compute_and_save_multi_precision_of_t'))
        print('===============================================================================\n')


if __name__ == '__main__':
    unittest.main()
