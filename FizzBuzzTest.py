import unittest

from FizzBuzz import *


class FizzBuzzTest(unittest.TestCase):
    def setUp(self):
        self.fizzbuzz = FizzBuzz()

    def test_should_return_number_when_not_divisible(self):
        self.assertEqual("1", self.fizzbuzz.getValue(1))
        self.assertEqual("2", self.fizzbuzz.getValue(2))

    def test_should_return_fizz_when_divisible_by_3(self):
        self.assertEqual("Fizz", self.fizzbuzz.getValue(3))
        self.assertEqual("Fizz", self.fizzbuzz.getValue(6))

    def test_should_return_buzz_when_divisible_by_5(self):
        self.assertEqual("Buzz", self.fizzbuzz.getValue(5))
        self.assertEqual("Buzz", self.fizzbuzz.getValue(10))

    def test_should_return_fizzbuss_when_dvisible_by_3_and_5(self):
        self.assertEqual("FizzBuzz", self.fizzbuzz.getValue(15))
        self.assertEqual("FizzBuzz", self.fizzbuzz.getValue(30))

    def test_should_return_numbers_up_to_15(self):
        expected = """1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
"""

        result = self.fizzbuzz.getNumbersUpTo(15)

        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
