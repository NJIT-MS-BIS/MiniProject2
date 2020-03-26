from calculator.calculator import Calculator
from statistics.mean import mean


class Statistics(Calculator):

    def mean(self, data):
        self.result = mean(data)
        return self.result
