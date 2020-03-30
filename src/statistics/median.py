from src.calculator.addition import addition
from src.calculator.division import division
from src.calculator.subtraction import subtraction


def median(num_list: list):
    """returns the median of list. List must be passed as an argument."""
    try:
        n = len(num_list)
        num_list.sort()
        if n % 2 == 0:
            first_half = num_list[int(n // 2)]
            second_half = num_list[int(subtraction(n // 2, 1))]
            median = division(addition(first_half, second_half), 2)
        else:
            median = num_list[int(division(n, 2))]
        return median
    except ZeroDivisionError as err:
        print(err)
