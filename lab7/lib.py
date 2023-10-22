import numpy as np
from sklearn import linear_model
from mlxtend.feature_selection import SequentialFeatureSelector
from sklearn import preprocessing

def init_linear_regression(X, y):
    mlr = linear_model.LinearRegression()
    mlr.fit(X=X, y=y)
    return mlr


def output_linear_regrestion_errors(new_y : np.array, origin_y : np.array):
    err = np.array(origin_y - new_y)
    n = len(err)
    
    rss = err.dot(err)
    rse = np.sqrt(rss / (n - 2))
    tss = np.var(origin_y) * n
    nu = (tss - rss) / tss
    return rss, tss, rse, nu


def init_polynomial(degree: int, X : np.array, y : np.array):
    poly_reg = preprocessing.PolynomialFeatures(degree=degree)
    X_poly = poly_reg.fit_transform(X)
    lr_model = linear_model.LinearRegression()

    max_features = X_poly.shape[1]
    k_features = max_features

    feature_selector = SequentialFeatureSelector(lr_model, 
        k_features=k_features, 
        forward=True
    )

    features = feature_selector.fit(X=X_poly, y=y)
    mX = X_poly[:, features.k_feature_idx_]
    lr_model.fit(X=mX, y=y)
    return mX, lr_model