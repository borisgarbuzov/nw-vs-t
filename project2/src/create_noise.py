import numpy as np


def create_noise(noise_size: int, mean: float, sigma: float,
                 noise_type: str) -> float:
    """
    Create "gaussian" or "bernoulli" noise.
    Here, bernoulli means +- sigma. 
    :param noise_size: size of noise
    :param mean: mean
    :param sigma: sigma
    :param noise_type: type, equal either "gaussian" or "bernoulli". 
    :return: float noise
    """
    if noise_type == "gaussian":
        return np.random.normal(mean, sigma, noise_size)
    elif noise_type == "bernoulli":
        classic_bernoulli = np.random.binomial(1, 1 / 2, noise_size)
        return sigma * ((2 * classic_bernoulli) - 1)
    else:
        raise ValueError("noise_type should be 'gaussian' or 'bernoulli'.")


if __name__ == '__main__':
    bernoulli_noise = create_noise(noise_size = 1000, 
    mean = 0, 
    sigma = 2,
    noise_type = "bernoulli")
    bernoulli_var = np.var(bernoulli_noise)
    print("bernoulli_var = ", bernoulli_var)

    gaussian_noise = create_noise(noise_size = 1000, 
    mean = 0, 
    sigma = 2,
    noise_type = "gaussian")
    gaussian_var = np.var(gaussian_noise)
    print("gaussian_var = ", gaussian_var)
    
    

