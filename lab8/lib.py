import numpy as np
import pandas as pd
from scipy import stats
from sklearn import linear_model
import matplotlib as mpl

default_dpi = mpl.rcParamsDefault['figure.dpi']
mpl.rcParams['figure.dpi'] = default_dpi * 2.5
class PolyRegularRegression:
    def __init__(self, model, alfa: float, degree: int) -> None:
        self.model = model(alfa)
        self.degree = degree

    def fit(self, x: np.array, y: np.array):
        self.model.fit(self._polynomial(x), y)

    def predict(self, x: np.array):
        return self.model.predict(self._polynomial(x))

    def get_params(self):
        return self.model.get_params()

    def _polynomial(self, x: np.array) -> np.array:
        pol_x = np.array([x**(i + 1) for i in range(self.degree)]).T
        return pol_x

models = {
    "Ridge": linear_model.Ridge,
    "lasso": linear_model.Lasso
}
