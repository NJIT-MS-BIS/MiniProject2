from calculator.calculator import Calculator
from statistics.mean import mean
from statistics.median import median
from statistics.mode import mode
from statistics.stddev import stddev
from statistics.varience import variance
from statistics.mean import mean
from statistics.proportion import proportion
from statistics.zscore import zscore
from statistics.correlation import correlation


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
        self._result = stddev(data)
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
