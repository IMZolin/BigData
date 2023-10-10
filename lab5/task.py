from lib import *
import matplotlib.pyplot as plt

class Task:
    def __init__(self):
        self.k = 500
        self.h = 0.05
        self.sample = None
        self.model = None
        self.exp001 = None
        self.exp005 = None
        self.exp01 = None
        self.exp03 = None
    def task1(self):
        print("TASK 1:")
        self.sample = generate_data()
        print("Sample:\n", self.sample)
        mean = np.mean(self.sample)
        var = np.var(self.sample)
        is_outlying = lambda x: np.abs(x - mean) > 3*var
        outlyings = [val for i, val in enumerate(self.sample) if is_outlying(val)]
        outlyings_indexes = [i for i, val in enumerate(self.sample) if is_outlying(val)]
        sample = np.delete(self.sample, outlyings_indexes)
        print("Sigma's outlyings: ", outlyings)
        plt.figure()
        plt.plot(sample, '*', label = 'sample')
        plt.plot(outlyings, 'o', label = 'outlyings')
        plt.grid()
        plt.legend()
        plt.show()
    def task2(self):
        print("TASK 2:")
        plt.figure()
        outlyings = plt.boxplot(self.sample)
        print("Boxplot's outlyings: ", [x.get_ydata() for x in outlyings["fliers"]])
        plt.show()