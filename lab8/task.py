from lib import *
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
from dateutil import parser, rrule
from datetime import datetime, time, date

class Task:
    def __init__(self):
        self.series_size = 20