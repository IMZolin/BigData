import numpy as np
from scipy import stats as stats

def generate_data():
    array = stats.norm.rvs(size=195)
    outlyings = np.array([5, -4, 3.3, 2.99, -3])
    array = np.append(array, outlyings)
    return array