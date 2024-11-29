
def pancake_sort(arr):
    """
    Pancake_sort
    Sorting a given array
    mutation of selection sort

    reference: https://www.geeksforgeeks.org/pancake-sorting/
    
    Overall time complexity : O(N^2)
    """

    len_arr = len(arr)
    if len_arr <= 1:
        return arr
    for cur in range(len(arr), 1, -1):
        #Finding index of maximum number in arr
        index_max = arr.index(max(arr[0:cur]))
        if index_max+1 != cur:
            #Needs moving
            if index_max != 0:
                #reverse from 0 to index_max
                arr[:index_max+1] = reversed(arr[:index_max+1])
            # Reverse list
            arr[:cur] = reversed(arr[:cur])
    return arr

import unittest


class PancakeSortGeminiTest(unittest.TestCase):
    def test_gemini_pancake_sort_empty_list(self):
        self.assertEqual(pancake_sort([]), [])

    def test_gemini_pancake_sort_single_element(self):
        self.assertEqual(pancake_sort([1]), [1])

    def test_gemini_pancake_sort_positive_numbers(self):
        self.assertEqual(pancake_sort([3, 1, 4, 2, 5]), [1, 2, 3, 4, 5])

    def test_gemini_pancake_sort_with_duplicates(self):
        self.assertEqual(pancake_sort([3, 1, 4, 2, 5, 3]), [1, 2, 3, 3, 4, 5])

