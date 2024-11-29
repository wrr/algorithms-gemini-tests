
import unittest
from algorithms.maths.find_order_simple import find_order


class TestFindOrderSimpleGeminiTest(unittest.TestCase):
    def test_gemini_find_order_simple_exception(self):
        self.assertEqual(1, find_order(1, 1))

    def test_gemini_find_order_simple_relative_prime(self):
        self.assertEqual(6, find_order(3, 7))

    def test_gemini_find_order_simple_not_relative_prime(self):
        self.assertEqual(-1, find_order(128, 256))

    def test_gemini_find_order_simple_large_numbers(self):
        self.assertEqual(352, find_order(3, 353))
