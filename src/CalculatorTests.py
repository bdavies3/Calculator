import unittest
from Calculator import Calculator
from CsvReader import CsvReader
from pprint import pprint

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        calculator = Calculator
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property_calculator(self):
       calculator = Calculator()
       self.assertEqual(calculator.result, 0)

    def test_add_method_calculator(self):
       test_data = CsvReader('/src/Unit Test Addition.csv')
       calculator = Calculator()
       self.assertEqual(calculator.add(2, 2), 4)
       self.assertEqual(calculator.result, 4)

    def test_subtract_method_calculator(self):
       test_data = CsvReader('/src/Unit Test Subtraction.csv')
       calculator = Calculator()
       self.assertEqual(calculator.subtract(2, 2), 0)
       self.assertEqual(calculator.result, 0)

    def test_divide_method_calculator(self):
        test_data = CsvReader('/src/Unit Test Division.csv')
        calculator = Calculator()
        self.assertEqual(calculator.divide(10, 5), 2)
        self.assertEqual(calculator.result, 2)

    def test_multiply_method_calculator(self):
        test_data = CsvReader('/src/Unit Test Multiplication.csv')
        calculator = Calculator()
        self.assertEqual(calculator.multiply(2, 5), 10)
        self.assertEqual(calculator.result, 10)

    def test_squared_method_calculator(self):
        test_data = CsvReader('/src/Unit Test Square.csv')
        calculator = Calculator()
        self.assertEqual(calculator.multiply(2, 2), 4)
        self.assertEqual(calculator.result, 4)

    def test_multiply_method_calculator(self):
        test_data = CsvReader('/src/Unit Test Square Root.csv')
        calculator = Calculator()
        self.assertEqual(calculator.multiply(25, 2), 50)
        self.assertEqual(calculator.result, 50)




if __name__ == '__main__':
   unittest.main()
