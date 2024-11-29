
import unittest

from algorithms.sort import bubble_sort


class TestBubbleSort(unittest.TestCase):
    def test_bubble_sort(self):
        self.assertEqual(bubble_sort([4, 2, 1, 9, 6, 7, 5, 3]),
                         [1, 2, 3, 4, 5, 6, 7, 9])

    def test_bubble_sort_empty_list(self):
        self.assertEqual(bubble_sort([]), [])

    def test_bubble_sort_with_duplicates(self):
        self.assertEqual(bubble_sort([4, 2, 1, 9, 4, 7, 5, 3, 1]),
                         [1, 1, 2, 3, 4, 4, 5, 7, 9])

    def test_bubble_sort_already_sorted(self):
        self.assertEqual(bubble_sort([1, 2, 3, 4, 5, 6, 7, 9]),
                         [1, 2, 3, 4, 5, 6, 7, 9])

    def test_bubble_sort_reversed(self):
        self.assertEqual(bubble_sort([9, 7, 6, 5, 4, 3, 2, 1]),
                         [1, 2, 3, 4, 5, 6, 7, 9])

    def test_bubble_sort_negative_numbers(self):
        self.assertEqual(bubble_sort([-5, -1, -10, -3, 2, 1]),
                         [-10, -5, -3, -1, 1, 2])

    def test_bubble_sort_with_simulation(self):
        self.assertEqual(bubble_sort([4, 2, 1, 9, 6, 7, 5, 3], simulation=True),
                         [1, 2, 3, 4, 5, 6, 7, 9])

