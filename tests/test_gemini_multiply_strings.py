
import unittest
from algorithms.strings.multiply_strings import multiply


class MultiplyStringsGeminiTest(unittest.TestCase):
    def test_gemini_multiply_strings_one_by_number(self):
        self.assertEqual("23", multiply("1", "23"))

    def test_gemini_multiply_strings_two_digit_numbers(self):
        self.assertEqual("529", multiply("23", "23"))

    def test_gemini_multiply_strings_zero_by_number(self):
        self.assertEqual("0", multiply("0", "23"))

    def test_gemini_multiply_strings_by_power_of_ten(self):
        self.assertEqual("1000000", multiply("100", "10000"))
