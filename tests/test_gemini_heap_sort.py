
import unittest
from algorithms.sort import heap_sort


class HeapSortGeminiTest(unittest.TestCase):
    def test_gemini_heap_sort_ascending(self):
        input_list = [4, 2, 5, 1, 6, 3]
        sorted_list = heap_sort.max_heap_sort(input_list)
        self.assertListEqual(sorted_list, [1, 2, 3, 4, 5, 6])

    def test_gemini_heap_sort_empty(self):
        input_list = []
        sorted_list = heap_sort.max_heap_sort(input_list)
        self.assertListEqual(sorted_list, [])

    def test_gemini_heap_sort_with_duplicates(self):
        input_list = [4, 2, 5, 1, 6, 3, 4, 2, 5, 1, 6, 3]
        sorted_list = heap_sort.max_heap_sort(input_list)
        self.assertListEqual(sorted_list, [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6])

    def test_gemini_min_heap_sort_ascending(self):
        input_list = [4, 2, 5, 1, 6, 3]
        sorted_list = heap_sort.min_heap_sort(input_list)
        self.assertListEqual(sorted_list, [1, 2, 3, 4, 5, 6])

    def test_gemini_min_heap_sort_empty(self):
        input_list = []
        sorted_list = heap_sort.min_heap_sort(input_list)
        self.assertListEqual(sorted_list, [])

    def test_gemini_min_heap_sort_with_duplicates(self):
        input_list = [4, 2, 5, 1, 6, 3, 4, 2, 5, 1, 6, 3]
        sorted_list = heap_sort.min_heap_sort(input_list)
        self.assertListEqual(sorted_list, [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6])

    def test_gemini_max_heap_sort_simulation(self):
        input_list = [4, 2, 5, 1, 6, 3]
        sorted_list = heap_sort.max_heap_sort(input_list, simulation=True)
        self.assertListEqual(sorted_list, [1, 2, 3, 4, 5, 6])

    def test_gemini_min_heap_sort_simulation(self):
        input_list = [4, 2, 5, 1, 6, 3]
        sorted_list = heap_sort.min_heap_sort(input_list, simulation=True)
        self.assertListEqual(sorted_list, [1, 2, 3, 4, 5, 6])
