import numpy as np
from scipy.stats import kendalltau

def generate_sample(k, h):
    return np.array([np.sqrt(i * h) + np.random.normal() for i in range(k)])

def generate_model(k, h):
    return np.array([np.sqrt(i * h) for i in range(k)])

def slide_mean(sample, m):
    res = []
    for i in range(sample.size):
        if i < m:
            res.append(sum([sample[j] for j in range(0, 2 * i + 2)]) / (2.0 * i + 1))
        elif i >= sample.size - m - 1 :
            res.append(sum([sample[j] for j in range(i - (sample.size - i), sample.size)]) / len(range(i - (sample.size - i), sample.size)))
        else:
            res.append(sum(sample[j] for j in range(i - m, i + m + 1)) / (2.0 * m + 1))
    return res

def slide_median(sample, m):
    res = []
    for i in range(sample.size):
        if i < m:
            res.append(np.median(sample[0 : 2 * i + 1]))
        elif i >= sample.size - m - 1 :
            res.append(np.median(sample[i - (sample.size - i) : sample.size]))
        else:
            res.append(np.median(sample[i - m : i + m + 1]))
    return res

def calculate_turning_points(sample):
    res = []
    for i in range(1, len(sample) - 2):
        if (sample[i] > sample[i - 1] and sample[i] > sample[i + 1]) or (sample[i] < sample[i - 1] and sample[i] < sample[i + 1]):
            res.append(sample[i])
    return res

def check_kendall(sample, trend, k):
    tail = sample - trend
    turning_points = calculate_turning_points(tail)
    p_mean = (2.0 / 3.0) * (len(sample) - 2)
    p_disp = (16 * len(sample) - 29) / 90.0
    p_size = len(turning_points)
    kendall = 1 - (4 * p_size) / (k * (k - 1))
    p_type = ""
    if p_size < p_mean + p_disp and p_size > p_mean - p_disp:
        p_type ="Randomness"
    elif p_size > p_mean + p_disp:
        p_type ="Rapidly oscillating"
    elif p_size < p_mean - p_disp:
        p_type = "Positively correlated"
    return p_size, kendall, p_type

def print_task4(data_name, slide, sample, k):
    p_size, kendall, p_type = check_kendall(slide, sample, k)
    print(f"\nKendall {data_name}")
    print(f"Number of Turning Points: {p_size}")
    print(f"Kendall coef: {kendall}")
    print(p_type)