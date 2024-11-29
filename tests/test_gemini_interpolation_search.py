
import unittest
from algorithms.search.interpolation_search import interpolation_search


class InterpolationSearchGeminiTest(unittest.TestCase):
    def test_gemini_interpolation_search_target_present(self):
        array = [-25, -12, -1, 10, 12, 15, 20, 41, 55]
        self.assertEqual(2, interpolation_search(array, -1))

    def test_gemini_interpolation_search_target_not_present(self):
        array = [5, 10, 12, 14, 17, 20, 21]
        self.assertEqual(-1, interpolation_search(array, 55))

    def test_gemini_interpolation_search_target_smaller_than_smallest(self):
        array = [5, 10, 12, 14, 17, 20, 21]
        self.assertEqual(-1, interpolation_search(array, -5))
