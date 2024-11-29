
import unittest
from algorithms.sort.insertion_sort import insertion_sort


class InsertionSortGeminiTest(unittest.TestCase):

    def test_gemini_insertion_sort_empty_list(self):
        array = []
        sorted_array = insertion_sort(array)
        self.assertEqual([], sorted_array)

    def test_gemini_insertion_sort_one_element(self):
        array = [1]
        sorted_array = insertion_sort(array)
        self.assertEqual([1], sorted_array)

    def test_gemini_insertion_sort_two_elements(self):
        array = [2, 1]
        sorted_array = insertion_sort(array)
        self.assertEqual([1, 2], sorted_array)

    def test_gemini_insertion_sort_odd_number_of_elements(self):
        array = [1, 5, 3, 2, 4]
        sorted_array = insertion_sort(array)
        self.assertEqual([1, 2, 3, 4, 5], sorted_array)

    def test_gemini_insertion_sort_even_number_of_elements(self):
        array = [1, 6, 3, 2, 5, 4]
        sorted_array = insertion_sort(array)
        self.assertEqual([1, 2, 3, 4, 5, 6], sorted_array)

    def test_gemini_insertion_sort_duplicate_elements(self):
        array = [1, 3, 3, 2, 4, 4, 2]
        sorted_array = insertion_sort(array)
        self.assertEqual([1, 2, 2, 3, 3, 4, 4], sorted_array)
