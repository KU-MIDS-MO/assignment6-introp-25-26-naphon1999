import numpy as np
from numpy.linalg import norm

def random_unit_vectors(num_vectors, dim):
    M = np.random.randn(num_vectors, dim)

    for i in range(M.shape[0]):
        row_norm = np.linalg.norm(M[i])
        M[i] = M[i] / row_norm

    return M

