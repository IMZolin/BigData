import numpy as np
import scipy 

def prony(x: np.array, T: float):
    if len(x) % 2 == 1:
        x = x[:len(x)-1]

    p = len(x) // 2

    shift_x = [0] + list(x)
    a = scipy.linalg.solve([shift_x[p+i:i:-1] for i in range(p)], -x[p::])

    z = np.roots([*a[::-1], 1])

    h = scipy.linalg.solve([z**n for n in range(1, p + 1)], x[:p])

    f = 1 / (2 * np.pi * T) * np.arctan(np.imag(z) / np.real(z))
    alfa = 1 / T * np.log(np.abs(z))
    A = np.abs(h)
    fi = np.arctan(np.imag(h) / np.real(h))

    return f, alfa, A, fi  


def generate_sample(N, h):
    return np.array([sum([(k * np.exp(-h * i / k) * np.cos(2 * np.pi * k * h * i + np.pi / 4.)) for k in range(1, 4)]) for i in range(1, N + 1)])

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
    p_type = ""
    if p_size < p_mean + p_disp and p_size > p_mean - p_disp:
        p_type ="Randomness"
    elif p_size > p_mean + p_disp:
        p_type ="Rapidly oscillating"
    elif p_size < p_mean - p_disp:
        p_type = "Positively correlated"
    return p_size, p_type