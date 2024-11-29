
import unittest
from algorithms.strings.one_edit_distance import is_one_edit, is_one_edit2


class OneEditDistanceGeminiTest(unittest.TestCase):
    def test_gemini_is_one_edit_empty_strings(self):
        self.assertFalse(is_one_edit("", ""))

    def test_gemini_is_one_edit_one_empty_string(self):
        self.assertTrue(is_one_edit("", "a"))

    def test_gemini_is_one_edit_one_edit_distance(self):
        self.assertTrue(is_one_edit("abc", "abd"))

    def test_gemini_is_one_edit_more_than_one_edit_distance(self):
        self.assertFalse(is_one_edit("abc", "aed"))

    def test_gemini_is_one_edit_same_strings(self):
        self.assertFalse(is_one_edit("abc", "abc"))

    def test_gemini_is_one_edit2_empty_strings(self):
        self.assertFalse(is_one_edit2("", ""))

    def test_gemini_is_one_edit2_one_empty_string(self):
        self.assertTrue(is_one_edit2("", "a"))

    def test_gemini_is_one_edit2_one_edit_distance(self):
        self.assertTrue(is_one_edit2("abc", "abd"))

    def test_gemini_is_one_edit2_more_than_one_edit_distance(self):
        self.assertFalse(is_one_edit2("abc", "aed"))

    def test_gemini_is_one_edit2_same_strings(self):
        self.assertFalse(is_one_edit2("abc", "abc"))
