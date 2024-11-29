
import unittest
from algorithms.dp.num_decodings import num_decodings, num_decodings2


class NumDecodingsGeminiTest(unittest.TestCase):
    def test_gemini_num_decodings_empty(self):
        self.assertEqual(0, num_decodings(""))
        self.assertEqual(0, num_decodings2(""))

    def test_gemini_num_decodings_single_digit(self):
        self.assertEqual(1, num_decodings("1"))
        self.assertEqual(1, num_decodings2("1"))

    def test_gemini_num_decodings_two_digits(self):
        self.assertEqual(2, num_decodings("12"))
        self.assertEqual(2, num_decodings2("12"))

    def test_gemini_num_decodings_three_digits(self):
        self.assertEqual(3, num_decodings("123"))
        self.assertEqual(3, num_decodings2("123"))

    def test_gemini_num_decodings_leading_zero(self):
        self.assertEqual(0, num_decodings("01"))
        self.assertEqual(0, num_decodings2("01"))

    def test_gemini_num_decodings_double_zero(self):
        self.assertEqual(0, num_decodings("100"))
        self.assertEqual(0, num_decodings2("100"))

    def test_gemini_num_decodings_invalid_two_digits(self):
        self.assertEqual(0, num_decodings("30"))
        self.assertEqual(0, num_decodings2("30"))

    def test_gemini_num_decodings_other_case(self):
        self.assertEqual(1, num_decodings("27"))
        self.assertEqual(1, num_decodings2("27"))
