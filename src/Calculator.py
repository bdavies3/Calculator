from CsvReader import CsvReader
import math

def addition(a, b):
    c = a + b
    return c


def subtraction(a, b):
    c = b - a
    return c


def division(a, b):
    return float(a) / float(b)


def mean(data):
    mean = data
    return mean


def multiplication(a, b) -> object:
    c = float(a) * float(b)
    return c


def squared(a, b) -> object:
    c = a ** b
    return c

def square_root(a, b) -> object:
    b = math.sqrt(a)


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def mean(self, a, b):
        self.result = mean(a, b)
        return self.result

    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def squared(self, a, b):
        self.result = squared(a, b)
        return self.result

    def square_root(self, a, b):
        self.result = square_root(a, b)
        return self.result




class CSVStats(Calculator):
    data = []

    def __init__(self, data_file):
        self.data = CsvReader(data_file)
        pass

    def mean(self):
        mean(self.data)
