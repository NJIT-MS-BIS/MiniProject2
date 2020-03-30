from calculator.square import squaring
from calculator.squareRoot import squarerooting
from calculator.subtraction import subtraction
from calculator.addition import addition
from calculator.division import division
from calculator.multiplication import multiplication


class Calculator:
    _result = 0

    def __init__(self, result):
        self._result = result

    @property
    def get_result(self):
        return self._result

    def add(self, num_one, num_two):
        self._result = addition(num_one, num_two)
        return self._result

    def subtract(self, num_one, num_two):
        self._result = subtraction(num_one, num_two)
        return self._result

    def multiply(self, num_one, num_two):
        self._result = multiplication(num_one, num_two)
        return self._result

    def divide(self, num_one, num_two):
        self._result = division(num_one, num_two)
        return self._result

    def square_root(self, num):
        self._result = squarerooting(num)
        return self._result

    def square(self, num):
        self._result = squaring(num)
        return self._result
