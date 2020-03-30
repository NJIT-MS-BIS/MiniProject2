from src.statistics.median import median


def quartiles(data: list):
    try:
        N = len(data)

        lower_q = data[int((N + 1) * 1 / 4)]
        middle_q = data[int((N + 1) * 2 / 4)]
        upper_q = data[int((N + 1) * 3 / 4)]
        return lower_q, middle_q, upper_q
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
    except ValueError:
        print("Error: Check your data inputs")