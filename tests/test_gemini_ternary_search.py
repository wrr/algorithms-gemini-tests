
"""
Ternary search is a divide and conquer algorithm that can be used to find an element in an array.
It is similar to binary search where we divide the array into two parts but in this algorithm,
we divide the given array into three parts and determine which has the key (searched element).
We can divide the array into three parts by taking mid1 and mid2.
Initially, l and r will be equal to 0 and n-1 respectively, where n is the length of the array.
mid1 = l + (r-l)/3
mid2 = r – (r-l)/3

Note: Array needs to be sorted to perform ternary search on it.
T(N) = O(log3(N))
log3 = log base 3
"""
def ternary_search(left, right, key, arr):
    """
    Find the given value (key) in an array sorted in ascending order.
    Returns the index of the value if found, and -1 otherwise.
    If the index is not in the range left..right (ie. left <= index < right) returns -1.
    """

    while right >= left:
        mid1 = left + (right-left) // 3
        mid2 = right - (right-left) // 3

        if key == arr[mid1]:
            return mid1
        if key == arr[mid2]:
            return mid2

        if key < arr[mid1]:
            # key lies between l and mid1
            right = mid1 - 1
        elif key > arr[mid2]:
            # key lies between mid2 and r
            left = mid2 + 1
        else:
            # key lies between mid1 and mid2
            left = mid1 + 1
            right = mid2 - 1

    # key not found
    return -1

import unittest


class TernarySearchGeminiTest(unittest.TestCase):
    def test_gemini_ternary_search_present(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(ternary_search(0, len(arr) - 1, 5, arr), 4)

    def test_gemini_ternary_search_not_present(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(ternary_search(0, len(arr) - 1, 11, arr), -1)

    def test_gemini_ternary_search_out_of_bounds(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(ternary_search(2, 5, 1, arr), -1)

