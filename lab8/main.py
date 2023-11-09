import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from lib import PolyRegularRegression, models
from scipy import stats

plt.rcParams.update({"font.size": 3, "lines.linewidth": 1})
data = np.array([[-2, -7], [-1, 0], [0, 1], [1, 2], [2, 9]])
sigmas = [0.1, 0.2, 0.3]

noises = [stats.norm.rvs(size=len(data), scale=var) for var in sigmas]
opt_nois = noises[0]
x = data[:, 0]
y = data[:, 1]

degree = 11

alfas = [1, 0.1, 0.01, 0.001]
opt_alfa = 0.01

x_test = np.linspace(-2, 2, 100)

fig, axs = plt.subplots(len(models), len(alfas))
params = pd.DataFrame()

for i, alfa in enumerate(alfas):
    for j, (model_name, model_class) in enumerate(models.items()):
        name = f"{model_name}, alfa={alfa}"

        model = PolyRegularRegression(model=model_class, alfa=alfa, degree=degree)
        model.fit(x, y + opt_nois)

        line_color = 'g'
        data_point_color = 'r*'

        axs[j, i].plot(x_test, model.predict(x_test), color=line_color)
        axs[j, i].plot(x, y, data_point_color, markersize=2)
        axs[j, i].set_title(name)
        axs[j, i].grid()

        params[name] = model.model.coef_

for name in params:
    params[name].apply(lambda x: None if x == 0. else x)
print(params)
plt.show()

fig, axs = plt.subplots(len(models), len(noises))
params = pd.DataFrame()

for i, nois in enumerate(noises):
    for j, (model_name, model_class) in enumerate(models.items()):
        name = f"{model_name}, sigma={sigmas[i]}"

        model = PolyRegularRegression(model=model_class, alfa=opt_alfa, degree=degree)
        model.fit(x, y + nois)

        line_color = 'g'
        data_point_color = 'r*'

        axs[j, i].grid()
        axs[j, i].plot(x_test, model.predict(x_test), color=line_color)
        axs[j, i].plot(x, y, data_point_color, markersize=2)
        axs[j, i].set_title(name)

        params[name] = model.model.coef_

for name in params:
    params[name].apply(lambda x: None if x == 0. else x)
print(params)
plt.show()
