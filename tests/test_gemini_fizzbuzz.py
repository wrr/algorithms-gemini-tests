
import unittest
from algorithms.strings import fizzbuzz


class TestFizzbuzz(unittest.TestCase):
    """[summary]
    Tests for the fizzbuzz method in file fizzbuzz.py
    """
    def test_fizzbuzz(self):
        # Testing that n < 0 returns a Value Error
        self.assertRaises(ValueError, fizzbuzz.fizzbuzz, -2)

        # Testing that a string returns a Type Error.
        self.assertRaises(TypeError, fizzbuzz.fizzbuzz, "hello")

        # Testing a base case, n = 3
        result = fizzbuzz.fizzbuzz(3)
        expected = [1, 2, "Fizz"]
        self.assertEqual(result, expected)

        # Testing a base case, n = 5
        result = fizzbuzz.fizzbuzz(5)
        expected = [1, 2, "Fizz", 4, "Buzz"]
        self.assertEqual(result, expected)

        # Testing a base case, n = 15 i.e. mod 3 and 5
        result = fizzbuzz.fizzbuzz(15)
        expected = [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11,
                    "Fizz", 13, 14, "FizzBuzz"]
        self.assertEqual(result, expected)

    def test_fizzbuzz_with_helper_func(self):
        # Testing that n < 0 returns a Value Error
        # TODO: fix the program logic to make this test pass:
        # self.assertRaises(ValueError, fizzbuzz.fizzbuzz_with_helper_func, -2)

        # Testing that a string returns a Type Error.
        self.assertRaises(TypeError, fizzbuzz.fizzbuzz_with_helper_func, "hello")

        # Testing a base case, n = 3
        result = fizzbuzz.fizzbuzz_with_helper_func(3)
        expected = [1, 2, "Fizz"]
        self.assertEqual(result, expected)

        # Testing a base case, n = 5
        result = fizzbuzz.fizzbuzz_with_helper_func(5)
        expected = [1, 2, "Fizz", 4, "Buzz"]
        self.assertEqual(result, expected)

        # Testing a base case, n = 15 i.e. mod 3 and 5
        result = fizzbuzz.fizzbuzz_with_helper_func(15)
        expected = [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11,
                    "Fizz", 13, 14, "FizzBuzz"]
        self.assertEqual(result, expected)
