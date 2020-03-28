from calculator.calculator import Calculator



class Statistics(Calculator):



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


