
def quick_sort(arr, simulation=False):
    """ Quick sort
        Complexity: best O(n log(n)) avg O(n log(n)), worst O(N^2)
    """
    
    iteration = 0
    if simulation:
        print("iteration",iteration,":",*arr)
    arr, _ = quick_sort_recur(arr, 0, len(arr) - 1, iteration, simulation)
    return arr

def quick_sort_recur(arr, first, last, iteration, simulation):
    if first < last:
        pos = partition(arr, first, last)
        # Start our two recursive calls
        if simulation:
            iteration = iteration + 1
            print("iteration",iteration,":",*arr)
            
        _, iteration = quick_sort_recur(arr, first, pos - 1, iteration, simulation)
        _, iteration = quick_sort_recur(arr, pos + 1, last, iteration, simulation)

    return arr, iteration

def partition(arr, first, last):
    wall = first
    for pos in range(first, last):
        if arr[pos] < arr[last]:  # last is the pivot
            arr[pos], arr[wall] = arr[wall], arr[pos]
            wall += 1
    arr[wall], arr[last] = arr[last], arr[wall]
    return wall

import unittest


class QuickSortGeminiTest(unittest.TestCase):
    def test_gemini_quick_sort_empty_list(self):
        self.assertEqual(quick_sort([]), [])

    def test_gemini_quick_sort_positive_numbers(self):
        self.assertEqual(quick_sort([4, 2, 1, 9, 6, 7, 5, 3]),
                         [1, 2, 3, 4, 5, 6, 7, 9])

    def test_gemini_quick_sort_with_duplicates(self):
        self.assertEqual(quick_sort([4, 2, 1, 9, 4, 7, 5, 3, 1]),
                         [1, 1, 2, 3, 4, 4, 5, 7, 9])

    def test_gemini_quick_sort_already_sorted(self):
        self.assertEqual(quick_sort([1, 2, 3, 4, 5, 6, 7, 9]),
                         [1, 2, 3, 4, 5, 6, 7, 9])

    def test_gemini_quick_sort_reversed(self):
        self.assertEqual(quick_sort([9, 7, 6, 5, 4, 3, 2, 1]),
                         [1, 2, 3, 4, 5, 6, 7, 9])

    def test_gemini_quick_sort_negative_numbers(self):
        self.assertEqual(quick_sort([-5, -1, -10, -3, 2, 1]),
                         [-10, -5, -3, -1, 1, 2])

    def test_gemini_quick_sort_with_simulation(self):
        self.assertEqual(quick_sort([4, 2, 1, 9, 6, 7, 5, 3], simulation=True),
                         [1, 2, 3, 4, 5, 6, 7, 9])

