import numpy as np

def estimate_pi(num_samples):
    random = np.random.rand(num_samples, 2)
    count = 0

    x = random[:, 0]
    y = random[:, 1]

    for i in range(random.shape[0]):
        if x[i]**2 + y[i]**2 <= 1:
            count += 1

    pi = count*4 / num_samples

    return pi
