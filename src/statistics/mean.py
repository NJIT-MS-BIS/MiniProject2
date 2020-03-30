from src.calculator.addition import addition
from src.calculator.division import division


def mean(num_list: list):
    try:
        num_values = len(num_list)
        total = sum(num_list)
        return round(division(total, num_values), 8)
    except ZeroDivisionError:
        print("Error: Can not be divided by 0")
