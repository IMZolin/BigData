from lib import *
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
from dateutil import parser, rrule
from datetime import datetime, time, date

class Task:
    def __init__(self):
        self.series_size = 20
        self.variables_nums = 3
        self.noise_distr = lambda size : stats.norm.rvs(size = size)
        self.x_distr = lambda size : stats.uniform.rvs(size=size, scale = 30)
        self.y_distr = lambda x1, x2, x3, noise = None : 1 + 3 * x1 - 2 * x2 + x3 + noise
        self.X = None
        self.y = None
        self.mlr = None
        self.polynom_degree = 6
    # check multi-linear-regresstion
    def task1(self):
        print("TASK 1:")
        X = [self.x_distr(self.series_size) for _ in range(self.variables_nums)]
        print("Vector X")
        for i, x_var in enumerate(X):
            print(f"X{i + 1}:", x_var)
        noise = self.noise_distr(self.series_size)
        y = self.y_distr(*(X[i] for i in range(self.variables_nums)), noise)
        print("\nVector y")
        for i, x_var in enumerate(X):
            print(f"y{i + 1}:", x_var)
        X = np.array(X).transpose()
        mlr = init_linear_regression(X, y)
        self.X = X
        self.y = y
        self.mlr = mlr
        print("\nMulti-Linear Regression Coefficients:")
        for i, coef in enumerate(mlr.coef_):
            print(f"X{i + 1} Coefficient:", coef)


    # check multi-linear-model
    def task2(self):
        print("\nTASK 2:")
        rss, tss, rse, nu = output_linear_regrestion_errors(self.mlr.predict(X=self.X), self.y)
        print("RSS = {:.6f}".format(rss))
        print("TSS = {:.6f}".format(tss))
        print("RSE = {:.6f}".format(rse))
        print("NU = {:.6f}".format(nu))


    def task3(self):
        print("\nTASK 3:")
        data_raw = pd.read_csv('kemerovo.csv')
        data_raw['MeanTemp'] = data_raw['MeanTemp'].astype(float)
        data = data_raw[['Year', 'MeanTemp']]
        print("Processed Data:")
        print(data)
        
        X, mlr = init_polynomial(self.polynom_degree, data[['Year']].values, data['MeanTemp'].values)
        print("Polynomial Regression Coefficients:")
        print(mlr.coef_)
        rss, tss, rse, nu = output_linear_regrestion_errors(mlr.predict(X=X), data['MeanTemp'].values)
        print("RSS = {:.6f}".format(rss))
        print("TSS = {:.6f}".format(tss))
        print("RSE = {:.6f}".format(rse))
        print("NU = {:.6f}".format(nu))