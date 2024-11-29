
import unittest
from algorithms.sort.cocktail_shaker_sort import cocktail_shaker_sort


class CocktailShakerSortGeminiTest(unittest.TestCase):
    def test_gemini_cocktail_shaker_sort_empty_list(self):
        self.assertEqual([], cocktail_shaker_sort([]))

    def test_gemini_cocktail_shaker_sort_positive_numbers(self):
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9],
                         cocktail_shaker_sort([9, 8, 7, 3, 2, 1, 4, 6, 5]))

    def test_gemini_cocktail_shaker_sort_negative_numbers(self):
        self.assertEqual([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5],
                         cocktail_shaker_sort([1, -1, 0, 3, 2, 5, -2, 4, -3, -4, -5]))
