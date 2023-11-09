import numpy as np
import matplotlib.pyplot as plt

def huber(x: np.array, k: float):
    phi = lambda elem: elem if abs(elem) < k else k * np.sign(elem)

    return np.mean([phi(elem) for elem in x])


def monte_karlo(N: int, sample_size: int, dist_grvs, measure):
    means = [measure(dist_grvs(size=sample_size)) for _ in range(N)]

    return np.mean(means), np.var(means)


def sigm3_rull(x: np.array):

    xmean = np.mean(x)
    xvar = np.var(x)
    is_in_3sigm = lambda xi: np.abs(xi - xmean) < 3*xvar

    clear_res = [val for val in x if is_in_3sigm(val)]

    return clear_res


def cut_off_outliers(data):
        q75, q25 = np.percentile(data, [75, 25])
        iqr = q75 - q25
        lower_bound = q25 - 1.5 * iqr
        upper_bound = q75 + 1.5 * iqr
        return [x for x in data if lower_bound <= x <= upper_bound]


def boxplot_rull(x: np.array):
    outlyings = plt.boxplot(x)
    clear_res = [i for i in x if not i in outlyings["fliers"]]
    # x = list(x)
    # for xx in outlyings["fliers"]:
    # x
    return clear_res
     


def double_stage_mean(x: np.array):
    x = sigm3_rull(x)
    return np.mean(x)
