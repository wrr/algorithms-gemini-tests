
"""
Jump Search

Find an element in a sorted array.
"""

import math

def jump_search(arr,target):
    """
    Worst-case Complexity: O(√n) (root(n))
    All items in list must be sorted like binary search

    Find block that contains target value and search it linearly in that block
    It returns a first target value in array

    reference: https://en.wikipedia.org/wiki/Jump_search
    """

    length = len(arr)
    if length == 0:
        return -1
    block_size = int(math.sqrt(length))
    block_prev = 0
    block= block_size

    # return -1 means that array doesn't contain target value
    # find block that contains target value

    if arr[length - 1] < target:
        return -1
    while block <= length and arr[block - 1] < target:
        block_prev = block
        block += block_size

    # find target value in block

    while arr[block_prev] < target :
        block_prev += 1
        if block_prev == min(block, length) :
            return -1

    # if there is target value in array, return it

    if arr[block_prev] == target :
        return block_prev
    return -1

import unittest


class JumpSearchGeminiTest(unittest.TestCase):
    def test_gemini_jump_search_found(self):
        array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        self.assertEqual(jump_search(array, 5), 4)

    def test_gemini_jump_search_not_found(self):
        array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        self.assertEqual(jump_search(array, 13), -1)

    def test_gemini_jump_search_empty_list(self):
        array = []
        self.assertEqual(jump_search(array, 5), -1)

