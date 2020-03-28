from calculator.calculator import Calculator



class Statistics(Calculator):

    @staticmethod
    def mean(data):
        """Pass a list"""
        return sum(data) // len(data)

    @staticmethod
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

    @staticmethod
    def mode(data):
        """Pass a list"""
        count_dictionary = {}
        for number in data:
            frequency = data.count(number)
            a = {number: frequency}
            count_dictionary.update(a)
        mode_num = count_dictionary[max(count_dictionary.values())]


    @staticmethod
    def variance(data):
        mu = mean(data)
        return mean([(x - mu) ** 2 for x in data])

    @staticmethod
    def stddev(data):
        return sq_root(variance(data))

    @staticmethod
    def quartile(data):
        pass


