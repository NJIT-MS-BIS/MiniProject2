def mode(data):
    """Pass a list"""
    count_dictionary = {}
    for number in data:
        frequency = data.count(number)
        a = {number: frequency}
        count_dictionary.update(a)
    mode_num = count_dictionary[max(count_dictionary.values())]
    return mode_num
