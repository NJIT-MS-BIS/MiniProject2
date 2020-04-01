from src.statistics.median import median


def quartiles(data: list):
    try:
        N = len(data)

        lower_q = data[int((N + 1) * 1 / 4)]
        middle_q = data[int((N + 1) * 2 / 4)]
        upper_q = data[int((N + 1) * 3 / 4)]
        return (round(lower_q, 9), round(middle_q, 9), round(upper_q, 9))
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
    except ValueError:
        print("Error: Check your data inputs")
