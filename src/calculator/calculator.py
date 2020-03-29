from calculator.subtraction import subtraction
from calculator.addition import addition
from calculator.division import division
from calculator.multiplication import multiplication


class Calculator:
    result = 0

    def __init__(self, result):
        self.result = result

    def add(self, num_one, num_two):
        self.result = addition(num_one, num_two)
        return self.result

    def subtract(self, num_one, num_two):
        self.result = subtraction(num_one, num_two)
        return self.result

    def multiply(self, num_one, num_two):
        self.result = multiplication(num_one, num_two)
        return self.result

    def divide(sefl, num_one, num_two):
        self.result = division(num_one, num_two)
        return self.result

    def sq_root(self, data):
        self.result = data ** 0.5
        return self.result
