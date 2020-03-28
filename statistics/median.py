def median(data):
    """Pass a list"""
    n = len(data)
    data.sort()
    if n % 2 == 0:
        first_half = data[n // 2]
        second_half = data[n // 2 - 1]
        median = (first_half + second_half) / 2
    else:
        median = data[n // 2]
    return median