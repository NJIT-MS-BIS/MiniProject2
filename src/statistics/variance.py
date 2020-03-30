from src.calculator.square import squaring
from src.calculator.division import division
from src.statistics.mean import mean


def variance(num: list):
    try:
        pop_mean = mean(num)
        num_values = len(num)
        x = 0
        for i in num:
            x = x + squaring(i-pop_mean)
        return division(x, num_values)
    except ZeroDivisionError as err:
        print(err)
    except (ValueError, TypeError):
        print ("Error: Check your data inputs")