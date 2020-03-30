import unittest2
from src.utilities.csvHelper import class_factory, CsvReader


class CsvTestCase(unittest2.TestCase):

    def setUp(self) -> None:
        self.csv_reader = CsvReader('data/UnitTestAddition.csv')

    def test_return_data_as_objects(self):
        people = self.csv_reader.return_data_as_class('Value 1')
        self.assertIsInstance(people, list)
        test_class = class_factory('Value 1', self.csv_reader.data[0])
        for person in people:
            self.assertEqual(person.__name__, test_class.__name__)


if __name__ == '__main__':
    unittest2.main()
