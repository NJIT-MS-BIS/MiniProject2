from statistics.mean import mean
from statistics.stddev import std_dev


def zscore(num):
    zmean = mean(num)
    sd = std_dev(num)
    zlist = []
    for x in num:
        z = round(((x - zmean) / sd), 6)
        zlist.append(z)
    return zlist
