from calculator.subtraction import subtraction
from calculator.addition import addition
from calculator.division import division
from calculator.multiplication import multiplication

class Calculator:
    result = 0

    def __init__(self, result):
        self.result = result

    @staticmethod
    def add(num_one, num_two):
        result = addition(num_one, num_two)
        return result

    @staticmethod
    def subtract(num_one, num_two):
        result = subtraction(num_one, num_two)
        return result

    @staticmethod
    def multiply(num_one, num_two):
        result = multiplication(num_one, num_two)
        return result

    @staticmethod
    def divide(num_one, num_two):
        result = division(num_one, num_two)
        return result

