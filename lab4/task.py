from lib import *
import matplotlib.pyplot as plt

class Task:
    def __init__(self):
        self.N = 200
        self.h = 0.02
        self.sample = None
    def task1(self):
        print("TASK 1:")
        sample = generate_sample(self.N, self.h)
        print("Sample:\n", sample)
        plt.figure()
        plt.title("Task 1")
        plt.plot(sample, 'o', color = 'black', label = "sample")
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