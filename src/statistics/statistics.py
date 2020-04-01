from src.calculator.calculator import Calculator
from src.statistics.median import median
from src.statistics.mode import mode
from src.statistics.variance import variance
from src.statistics.stddev import std_dev
from src.statistics.mean import mean
from src.statistics.proportion import proportion
from src.statistics.zscore import zscore
from src.statistics.correlation import correlation
from src.statistics.quartiles import quartiles
from src.statistics.skewness import skewness


class Statistics(Calculator):
    data = []

    def __init__(self):
        super().__init__()

    def mean(self, data):
        self._result = mean(data)
        return self._result

    def population_mean(self, data):
        self._result = mean(data)
        return self._result

    def median(self, data):
        self._result = median(data)
        return self._result

    def mode(self, data):
        self._result = mode(data)
        return self._result

    def stddev(self, data):
        self._result = std_dev(data)
        return self._result

    def variance(self, data):
        self._result = variance(data)
        return self._result

    def proportion(self, data):
        self._result = proportion(data)
        return self._result

    def zscore(self, data):
        self._result = zscore(data)
        return self._result

    def correlation_coefficient(self, data, data1):
        self._result = correlation(data, data1)
        return self._result

    def quartiles(self, data):
        self._result = quartiles(data)
        return self._result

    def skewness(self, data):
        self._result = skewness(data)
        return self._result
