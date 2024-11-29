
"""
Solves system of equations using the chinese remainder theorem if possible.
"""
from typing import List
from algorithms.maths.gcd import gcd

def solve_chinese_remainder(nums : List[int], rems : List[int]):
    """
    Computes the smallest x that satisfies the chinese remainder theorem
    for a system of equations.
    The system of equations has the form:
    x % nums[0] = rems[0]
    x % nums[1] = rems[1]
    ...
    x % nums[k - 1] = rems[k - 1]
    Where k is the number of elements in nums and rems, k > 0.
    All numbers in nums needs to be pariwise coprime otherwise an exception is raised
    returns x: the smallest value for x that satisfies the system of equations
    """
    if not len(nums) == len(rems):
        raise Exception("nums and rems should have equal length")
    if not len(nums) > 0:
        raise Exception("Lists nums and rems need to contain at least one element")
    for num in nums:
        if not num > 1:
            raise Exception("All numbers in nums needs to be > 1")
    if not _check_coprime(nums):
        raise Exception("All pairs of numbers in nums are not coprime")
    k = len(nums)
    x = 1
    while True:
        i = 0
        while i < k:
            if x % nums[i] != rems[i]:
                break
            i += 1
        if i == k:
            return x
        x += 1

def _check_coprime(list_to_check : List[int]):
    for ind, num in enumerate(list_to_check):
        for num2 in list_to_check[ind + 1:]:
            if gcd(num, num2) != 1:
                return False
    return True

import unittest


class ChineseRemainderTheoremGeminiTest(unittest.TestCase):
    def test_gemini_solve_chinese_remainder_valid_input(self):
        nums = [3, 5, 7]
        rems = [2, 3, 2]
        self.assertEqual(solve_chinese_remainder(nums, rems), 23)

    def test_gemini_solve_chinese_remainder_invalid_input_length(self):
        nums = [3, 5, 7]
        rems = [2, 3]
        with self.assertRaises(Exception):
            solve_chinese_remainder(nums, rems)

    def test_gemini_solve_chinese_remainder_invalid_input_empty(self):
        nums = []
        rems = []
        with self.assertRaises(Exception):
            solve_chinese_remainder(nums, rems)

    def test_gemini_solve_chinese_remainder_invalid_input_not_coprime(self):
        nums = [3, 6, 9]
        rems = [2, 3, 2]
        with self.assertRaises(Exception):
            solve_chinese_remainder(nums, rems)

    def test_gemini_solve_chinese_remainder_invalid_input_nums_less_than_2(self):
        nums = [1, 5, 7]
        rems = [2, 3, 2]
        with self.assertRaises(Exception):
            solve_chinese_remainder(nums, rems)

