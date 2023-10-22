from scipy import stats
from prettytable import PrettyTable
from lib import *

class Task:
    def __init__(self):
        self.N = 10000
        self.sample_size = 100
        self.distributions = {
            "N(0,1)": stats.norm.rvs,
            "C(0,1)": stats.cauchy.rvs,
            "0.9N(0,1) + 0.1C(0,1)": lambda size: 0.9 * stats.norm.rvs(size=size) + 0.1 * stats.cauchy.rvs(size=size) 
        }
        self.measures = {
            "mean": np.mean,
            "median": np.median,
            "huber": lambda x: huber(x, 1.44),
            "two_factor": double_stage_mean
        }
    def task(self):
        for dname, grvs in self.distributions.items():
            table = PrettyTable()
            table.field_names = ["Measure", "mu", "var"]
            table.title = dname

            for mname, measure in self.measures.items():
                mu, var = monte_karlo(self.N, self.sample_size, grvs, measure)
                table.add_row([mname, f"{mu:.6f}", f"{var:.6f}"])

            print(table)