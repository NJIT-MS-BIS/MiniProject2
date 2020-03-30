from src.calculator.squareRoot import squarerooting
from src.statistics.variance import variance


def std_dev(num):
    try:
        variance_float = variance(num)
        return round(squarerooting(variance_float), 5)
    except ZeroDivisionError as err:
        print(err)
    except ValueError:
        print("Error: Check your data inputs")