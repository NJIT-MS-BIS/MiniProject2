from calculator.calculator import Calculator



class Statistics(Calculator):


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


