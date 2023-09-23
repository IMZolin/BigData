from lib import *
import matplotlib.pyplot as plt

class Task:
    def __init__(self):
        self.k = 500
        self.h = 0.05
        self.sample = None
        self.model = None
        self.mean10 = None
        self.mean25 = None
        self.mean55 = None
        self.median10 = None
        self.median25 = None
        self.median55 = None
    def task1(self):
        print("TASK 1:")
        self.sample = generate_sample(self.k, self.h)
        print("Sample:\n", self.sample)
        plt.figure()
        plt.title("Task 1")
        plt.plot(self.sample, 'o', color = 'black', label = "sample")
        plt.legend()
        plt.grid(True)  
        plt.show()  
    def task2(self):
        print("TASK 2:")
        self.model = generate_model(self.k, self.h)
        print("Trend:\n", self.model)
        self.mean10 = slide_mean(self.sample, 10)
        print("Slide mean, m = 10:\n", self.mean10)
        self.mean25 = slide_mean(self.sample, 25)
        print("Slide mean, m = 25:\n", self.mean25)
        self.mean55 = slide_mean(self.sample, 55)
        print("Slide mean, m = 55:\n", self.mean55)
        plt.figure()
        plt.title("\nTask 2")
        plt.plot(self.sample, 'o', color = 'black', label = "sample")
        plt.plot(self.model, label = "model")
        plt.plot(self.mean10, label = "Slide mean, m = 10")
        plt.plot(self.mean25, label = "Slide mean, m = 25")
        plt.plot(self.mean55, label = "Slide mean, m = 55")
        plt.legend()
        plt.grid(True)  
        plt.show()
    def task3(self):
        print("\nTASK 3:")
        self.median10 = slide_median(self.sample, 10)
        print("Slide median, m = 10:\n", self.median10)
        self.median25 = slide_median(self.sample, 25)
        print("Slide median, m = 25:\n", self.median25)
        self.median55 = slide_median(self.sample, 55)
        print("Slide median, m = 55:\n", self.median55)
        plt.figure()
        plt.title("Task 3")
        plt.plot(self.sample, 'o', color = 'black', label = "sample")
        plt.plot(self.model, label = "model")
        plt.plot(self.median10, label = "Slide median, m = 10")
        plt.plot(self.median25, label = "Slide median, m = 25")
        plt.plot(self.median55, label = "Slide median, m = 55")
        plt.legend()
        plt.grid(True)  
        plt.show()
    def task4(self):
        print("\nTASK 4:")
        if self.sample is None or self.model is None:
            print("Please run Task 1 and Task 2 first to generate the sample and model.")
            return
        print_task4("Slide Mean 10", self.mean10, self.sample, self.k)
        print_task4("Slide Mean 25", self.mean25, self.sample, self.k)
        print_task4("Slide Mean 55", self.mean55, self.sample, self.k)
        print_task4("Slide Median 10", self.median10, self.sample, self.k)
        print_task4("Slide Median 25", self.median25, self.sample, self.k)
        print_task4("Slide Median 55", self.median55, self.sample, self.k)