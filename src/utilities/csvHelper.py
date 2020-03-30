import csv
from src.utilities.absolutepath import absolute_path


def class_factory(class_name, dictionary):
    return type(class_name, (object,), dictionary)


class CsvReader:
    data = []

    def __init__(self, filepath):
        self.data = []
        try:
            with open(absolute_path(filepath)) as text_data:
                csv_data = csv.DictReader(text_data, delimiter=',')
                for row in csv_data:
                    self.data.append(row)
        except OSError as err:
            print(err)

    def return_data_as_class(self, class_name):
        objects = []
        for row in self.data:
            objects.append(class_factory(class_name, row))
        return objects
