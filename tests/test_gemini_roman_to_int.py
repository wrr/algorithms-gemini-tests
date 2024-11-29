
import unittest
from algorithms.strings.roman_to_int import roman_to_int


class RomanToIntGeminiTest(unittest.TestCase):
    def test_gemini_roman_to_int_single_digit(self):
        self.assertEqual(1, roman_to_int("I"))

    def test_gemini_roman_to_int_two_digits(self):
        self.assertEqual(12, roman_to_int("XII"))

    def test_gemini_roman_to_int_three_digits(self):
        self.assertEqual(123, roman_to_int("CXXIII"))

    def test_gemini_roman_to_int_four_digits(self):
        self.assertEqual(1994, roman_to_int("MCMXCIV"))

    def test_gemini_roman_to_int_example(self):
        self.assertEqual(621, roman_to_int("DCXXI"))
