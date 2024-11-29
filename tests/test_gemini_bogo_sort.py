
import unittest
from algorithms.sort.bogo_sort import bogo_sort


class BogoSortGeminiTest(unittest.TestCase):
    def test_gemini_bogo_sort_empty_list(self):
        self.assertEqual([], bogo_sort([]))

    def test_gemini_bogo_sort_positive_numbers(self):
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9],
                         bogo_sort([9, 8, 7, 3, 2, 1, 4, 6, 5]))

    def test_gemini_bogo_sort_negative_numbers(self):
        self.assertEqual([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5],
                         bogo_sort([1, -1, 0, 3, 2, 5, -2, 4, -3, -4, -5]))
