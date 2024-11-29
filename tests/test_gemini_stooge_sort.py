
import unittest
from algorithms.sort.stooge_sort import stoogesort


class StoogeSortGeminiTest(unittest.TestCase):

    def test_gemini_stooge_sort_empty_list(self):
        array = []
        stoogesort(array, 0, len(array) - 1)
        self.assertEqual([], array)

    def test_gemini_stooge_sort_one_element(self):
        array = [1]
        stoogesort(array, 0, len(array) - 1)
        self.assertEqual([1], array)

    def test_gemini_stooge_sort_two_elements(self):
        array = [2, 1]
        stoogesort(array, 0, len(array) - 1)
        self.assertEqual([1, 2], array)

    def test_gemini_stooge_sort_odd_number_of_elements(self):
        array = [1, 5, 3, 2, 4]
        stoogesort(array, 0, len(array) - 1)
        self.assertEqual([1, 2, 3, 4, 5], array)

    def test_gemini_stooge_sort_even_number_of_elements(self):
        array = [1, 6, 3, 2, 5, 4]
        stoogesort(array, 0, len(array) - 1)
        self.assertEqual([1, 2, 3, 4, 5, 6], array)

    def test_gemini_stooge_sort_duplicate_elements(self):
        array = [1, 3, 3, 2, 4, 4, 2]
        stoogesort(array, 0, len(array) - 1)
        self.assertEqual([1, 2, 2, 3, 3, 4, 4], array)
