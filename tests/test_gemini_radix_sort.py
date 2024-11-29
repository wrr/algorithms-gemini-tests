
"""
radix sort
complexity: O(nk + n) . n is the size of input list and k is the digit length of the number
"""
def radix_sort(arr, simulation=False):
    position = 1
    if len(arr) == 0:
        return arr
    max_number = max(arr)

    iteration = 0
    if simulation:
        print("iteration", iteration, ":", *arr)

    while position <= max_number:
        queue_list = [list() for _ in range(10)]

        for num in arr:
            digit_number = (abs(num) // position) % 10
            queue_list[digit_number].append(num)

        index = 0
        for numbers in queue_list:
            for num in numbers:
                arr[index] = num
                index += 1

        if simulation:
            iteration = iteration + 1
            print("iteration", iteration, ":", *arr)

        position *= 10
    return arr

import unittest


class RadixSortGeminiTest(unittest.TestCase):
    def test_gemini_radix_sort_empty_list(self):
        self.assertEqual(radix_sort([]), [])

    def test_gemini_radix_sort_positive_numbers(self):
        self.assertEqual(radix_sort([170, 45, 75, 90, 802, 24, 2, 66]),
                         [2, 24, 45, 66, 75, 90, 170, 802])

    def test_gemini_radix_sort_with_duplicates(self):
        self.assertEqual(radix_sort([170, 45, 75, 90, 802, 24, 2, 66, 45]),
                         [2, 24, 45, 45, 66, 75, 90, 170, 802])

    def test_gemini_radix_sort_already_sorted(self):
        self.assertEqual(radix_sort([2, 24, 45, 66, 75, 90, 170, 802]),
                         [2, 24, 45, 66, 75, 90, 170, 802])

    def test_gemini_radix_sort_reversed(self):
        self.assertEqual(radix_sort([802, 170, 90, 75, 66, 45, 24, 2]),
                         [2, 24, 45, 66, 75, 90, 170, 802])

    def test_gemini_radix_sort_negative_numbers(self):
        self.assertEqual(radix_sort([-170, -45, -75, -90, -2, -24, -66, -802]),
                         [-802, -170, -90, -75, -66, -45, -24, -2])

    def test_gemini_radix_sort_with_simulation(self):
        self.assertEqual(radix_sort([170, 45, 75, 90, 802, 24, 2, 66],
                                     simulation=True),
                         [2, 24, 45, 66, 75, 90, 170, 802])

    def test_gemini_radix_sort_mixed_numbers(self):
        self.assertEqual(radix_sort([170, -45, 75, -90, 802, -24, 2, 66]),
                         [-90, -45, -24, 2, 66, 75, 170, 802])

