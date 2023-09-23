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
        self.exp001 = slide_exp(self.sample, 0.01)
        print("\nSlide exp, alpha = 0.01:\n", self.exp001)
        self.exp005 = slide_exp(self.sample, 0.05)
        print("\nSlide exp, alpha = 0.05:\n", self.exp005)
        self.exp01 = slide_exp(self.sample, 0.1)
        print("\nSlide exp, alpha = 0.1:\n", self.exp01)
        self.exp03 = slide_exp(self.sample, 0.3)
        print("\nSlide exp, alpha = 0.3:\n", self.exp03)
        plt.figure()
        plt.title("\nTask 2")
        plt.plot(self.sample, 'o', color = 'black', label = "sample")
        plt.plot(self.model, label = "model")
        plt.plot(self.exp001, label = "Slide Exp mean, alpha = 0.01")
        plt.plot(self.exp005, label = "Slide Exp mean, alpha = 0.05")
        plt.plot(self.exp01, label = "Slide Exp mean, alpha = 0.1")
        plt.plot(self.exp03, label = "Slide Exp mean, alpha = 0.3")
        plt.legend()
        plt.grid(True)  
        plt.show()
    def task4(self):
        print("\nTASK 4:")
        if self.sample is None or self.model is None:
            print("Please run Task 1 and Task 2 first to generate the sample and model.")
            return
        amplitude_spectrum, main_frequency, frequencies = calculate_amplitude_spectrum(self.sample, self.k)
        print(f"Amplitude Spectrum Main Frequency: {main_frequency} Hz")
        plt.figure()
        plt.title("Amplitude Spectrum")
        plt.plot(frequencies, amplitude_spectrum)
        plt.xlabel("Frequency (Hz)")
        plt.ylabel("Amplitude")
        plt.grid(True)
        plt.show()
    def task5(self):
        print("\nTASK 5:")
        if self.sample is None or self.model is None:
            print("Please run Task 1 and Task 2 first to generate the sample and model.")
            return
        print_task5("Slide Exp mean, 0.01", self.exp001, self.sample, self.k)
        print_task5("Slide Exp mean, 0.05", self.exp005, self.sample, self.k)
        print_task5("Slide Exp mean, 0.1", self.exp01, self.sample, self.k)
        print_task5("Slide Exp mean, 0.3", self.exp03, self.sample, self.k)