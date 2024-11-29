
import unittest
from algorithms.sort.selection_sort import selection_sort


class SelectionSortGeminiTest(unittest.TestCase):
    def test_gemini_selection_sort_empty_list(self):
        self.assertEqual([], selection_sort([]))

    def test_gemini_selection_sort_single_element(self):
        self.assertEqual([1], selection_sort([1]))

    def test_gemini_selection_sort_already_sorted(self):
        self.assertEqual([1, 2, 3, 4, 5], selection_sort([1, 2, 3, 4, 5]))

    def test_gemini_selection_sort_reverse_sorted(self):
        self.assertEqual([1, 2, 3, 4, 5], selection_sort([5, 4, 3, 2, 1]))

    def test_gemini_selection_sort_general_case(self):
        self.assertEqual([1, 2, 3, 4, 5], selection_sort([4, 2, 5, 1, 3]))
