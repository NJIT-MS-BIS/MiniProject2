from calculator.calculator import Calculator
from statistics.median import median
from statistics.mode import mode
from statistics.stddev import stddev
from statistics.varience import variance
from statistics.mean import populationmean
from statistics.proportion import proportion
from statistics.zscore import zscore
from statistics.correlation import correlation



class Statistics(Calculator):
    data = []

    def __init__(self):
        super().__init__()

    def population_mean(self, data):
        self.result = populationmean(data)
        return self.result

    def median(self, data):
        self.result = median(data)
        return self.result

    def mode(self, data):
        self.result = mode(data)
        return self.result

    def stddev(self, data):
        self.result = stddev(data)
        return self.result

    def variance(self, data):
        self.result = variance(data)
        return self.result

    def proportion(self, data):
        self.result = proportion(data)
        return self.result

    def zscore(self, data):
        self.result = zscore(data)
        return self.result

    def correlation_coefficient(self, data, data1):
        self.result = correlation(data, data1)
        return self.result


    pass