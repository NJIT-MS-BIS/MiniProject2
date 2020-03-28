
from statistics.statistics import mean
from statistics.stddev import stddev


def zscore(num):
    zmean = mean(num)
    sd = stddev(num)
    zlist = []
    for x in num:
        z = round(((x - zmean) / sd), 6)
        zlist.append(z)
    return zlist