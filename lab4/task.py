from lib import *
import matplotlib.pyplot as plt
import pandas as pd
from dateutil import parser, rrule
from datetime import datetime, time, date
from hurst import compute_Hc, random_walk

class Task:
    def __init__(self):
        self.N = 200
        self.h = 0.02
        self.sample = None
    def task1(self):
        print("TASK 1:")
        self.sample = generate_sample(self.N, self.h)
        print("Sample:\n", self.sample)
        plt.figure()
        plt.title("Task 1")
        plt.plot(self.sample, 'o', color = 'black', label = "sample")
        plt.legend()
        
        n = 128
        # Time vector
        t = np.linspace(0, 1, n, endpoint=True)

        # Amplitudes and freqs
        f1, f2, f3 = 2, 7, 12
        A1, A2, A3 = 5, 1, 3

        # Signal
        x = A1 * np.cos(2*np.pi*f1*t) + A2 * np.cos(2*np.pi*f2*t) + A3 * np.cos(2*np.pi*f3*t)

        f, alfa, A, fi = prony(x, 0.1)
        plt.figure()
        plt.stem(2*A)
        plt.plot()
        plt.grid()

        plt.show()
    
    def task2(self):
        print("TASK 2:")
        data_raw = pd.read_csv('kemerovo.csv')
        data_raw['MeanTemp'] = data_raw['MeanTemp'].astype(float)
        data_raw['FullDate'] = pd.to_datetime(data_raw['FullDate'], format='%m/%d/%Y')
        data = data_raw[['FullDate', 'MeanTemp']]
        print(data)

        plt.title("Kemerovo (Siberia) trend")
        plt.plot(data['FullDate'], data['MeanTemp'], label='temp')
        
        trend = slide_median(data['MeanTemp'], 55)
        plt.plot(data['FullDate'], trend, label='trend')
        plt.legend()
        
        check_kendall(trend, data['MeanTemp'])
        
        H, c, data_Hc = compute_Hc(trend, kind='random_walk', simplified=False)
        
        f, ax = plt.subplots()
        ax.set_title('Seasonal fluctuations')
        ax.plot(data_Hc[0], c * data_Hc[0]**H, color="deepskyblue")
        ax.scatter(data_Hc[0], data_Hc[1], color="purple")
        
        print("Hurst exponent (H):", H)
        # A = prony(data_Hc[0], data_Hc[1])
        f = np.fft.fft(data['MeanTemp'])
        ff = f.real * f.real + f.imag * f.imag
        sz = len(ff)
        ff = ff[0:100]
        plt.plot(ff)
        plt.grid()
        for delta in [1, 8]:
            ff = ff[delta:100]
            print(sz / ((ff.argmax() + delta)), "days")    
        plt.show()

