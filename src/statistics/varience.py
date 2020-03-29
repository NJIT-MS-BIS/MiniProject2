from statistics.mean import mean


def variance(data):
    mu = mean(data)
    return mean([(x - mu) ** 2 for x in data])