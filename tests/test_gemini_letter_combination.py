
"""
Given a digit string, return all possible letter
combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below:
2: "abc"
3: "def"
4: "ghi"
5: "jkl"
6: "mno"
7: "pqrs"
8: "tuv"
9: "wxyz"

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""


def letter_combinations(digits):
    if digits == "":
        return []
    kmaps = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }
    ans = [""]
    for num in digits:
        tmp = []
        for an in ans:
            for char in kmaps[num]:
                tmp.append(an + char)
        ans = tmp
    return ans

import unittest


class LetterCombinationGeminiTest(unittest.TestCase):
    def test_gemini_letter_combinations_empty_string(self):
        self.assertEqual(letter_combinations(""), [])

    def test_gemini_letter_combinations_single_digit(self):
        self.assertEqual(sorted(letter_combinations("2")), sorted(["a", "b", "c"]))

    def test_gemini_letter_combinations_two_digits(self):
        expected_combinations = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        self.assertEqual(sorted(letter_combinations("23")), sorted(expected_combinations))

