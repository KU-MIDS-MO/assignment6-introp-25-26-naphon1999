import numpy as np

def get_random_subset_of_naturals_up_to_20():
    subset = []
    random = np.random.randint(0, 2**20)

    for i in range(1, 21):
        if random & (1 << (i - 1)):
            subset.append(i)

    return np.array(subset, dtype=int)


