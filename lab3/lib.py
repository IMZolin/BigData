import numpy as np
import scipy as sc
import scipy.stats as st

def generate_sample(k, h):
    return np.array([0.5 * np.sin(i * h) + np.random.normal() for i in range(k)])

def generate_model(k, h):
    return np.array([0.5 * np.sin(i * h) for i in range(k)])

def slide_exp(sample, alpha):
    res = []
    res.append(sample[0])
    for i in range(1, sample.size):
        res.append(alpha * sample[i] + (1 - alpha) * res[i - 1])
    return res

def calculate_amplitude_spectrum(sample, k):
    sample_fft = np.fft.fft(sample)
    amplitude_spectrum = 2 / k * np.abs(sample_fft[:len(sample) // 2])
    frequencies = np.linspace(0, 1 / (2.0), len(sample) // 2)
    main_frequency_index = np.argmax(amplitude_spectrum)
    main_frequency = frequencies[main_frequency_index]
    return amplitude_spectrum, main_frequency, frequencies

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
    mean = tail.mean()
    devotion = st.tstd(tail)
    normal = st.normaltest(tail)[1]
    return p_size, kendall, p_type, mean, devotion, normal

def print_task5(data_name, slide, sample, k):
    p_size, kendall, p_type, mean, devotion, normal = check_kendall(slide, sample, k)
    print(f"\nKendall {data_name}")
    print(f"Number of Turning Points: {p_size}")
    print(f"Kendall coef: {kendall}")
    print(f"Mean: {mean}")
    print(f"Standart devotion: {devotion}")
    print(f"Probability of Normal: {normal}")
    print(p_type)