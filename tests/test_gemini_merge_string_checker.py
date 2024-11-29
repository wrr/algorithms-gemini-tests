
import unittest
from algorithms.strings.merge_string_checker import is_merge_iterative
from algorithms.strings.merge_string_checker import is_merge_recursive


class MergeStringCheckerGeminiTest(unittest.TestCase):
    def test_gemini_is_merge_recursive(self):
        self.assertTrue(is_merge_recursive('codewars', 'code', 'wars'))
        self.assertTrue(is_merge_recursive('codewars', 'cdw', 'oears'))
        self.assertFalse(is_merge_recursive('codewars', 'cod', 'wars'))
        self.assertTrue(is_merge_recursive('', '', ''))
        self.assertFalse(is_merge_recursive('codewars', 'codewar', ''))

    def test_gemini_is_merge_iterative(self):
        self.assertTrue(is_merge_iterative('codewars', 'code', 'wars'))
        self.assertTrue(is_merge_iterative('codewars', 'cdw', 'oears'))
        self.assertFalse(is_merge_iterative('codewars', 'cod', 'wars'))
        self.assertTrue(is_merge_iterative('', '', ''))
        self.assertFalse(is_merge_iterative('codewars', 'codewar', ''))
