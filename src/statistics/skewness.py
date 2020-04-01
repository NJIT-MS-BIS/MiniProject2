from src.statistics.mean import mean
from src.statistics.median import median
from src.statistics.stddev import std_dev
from utilities.csvHelper import CsvReader


def skewness(data: list):
    try:

        mean_data = mean(data)
        median_data = median(data)
        stddev_data = std_dev(data)
        skewness = 3 * (mean_data - median_data) / stddev_data
        return round(skewness, 9)
    except ZeroDivisionError:
        print("Error: Can't Divide by 0")
    except ValueError:
        print("Error: Check your data inputs")


# import csv
#
# test_data = CsvReader('../../data/Test_Data.csv').data
# column1 = [int(row['value1']) for row in test_data]
# answers = skewness(column1)
# print(answers)
# # with open('some.csv', 'w', newline='') as f:
# #     writer = csv.writer(f)
# #     writer.writerows(answers)