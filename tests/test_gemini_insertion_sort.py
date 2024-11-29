
import unittest
from algorithms.sort.insertion_sort import insertion_sort


class InsertionSortGeminiTest(unittest.TestCase):
    def test_gemini_insertion_sort_empty_list(self):
        self.assertEqual([], insertion_sort([]))

    def test_gemini_insertion_sort_single_element(self):
        self.assertEqual([1], insertion_sort([1]))

    def test_gemini_insertion_sort_already_sorted(self):
        self.assertEqual([1, 2, 3, 4, 5], insertion_sort([1, 2, 3, 4, 5]))

    def test_gemini_insertion_sort_reverse_sorted(self):
        self.assertEqual([1, 2, 3, 4, 5], insertion_sort([5, 4, 3, 2, 1]))

    def test_gemini_insertion_sort_general_case(self):
        self.assertEqual([1, 2, 3, 4, 5], insertion_sort([4, 2, 5, 1, 3]))
