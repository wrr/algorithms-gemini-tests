
import unittest
from algorithms.strings.first_unique_char import first_unique_char


class FirstUniqueCharGeminiTest(unittest.TestCase):
    def test_gemini_first_unique_char_leetcode_example(self):
        self.assertEqual(0, first_unique_char("leetcode"))

    def test_gemini_first_unique_char_loveleetcode_example(self):
        self.assertEqual(2, first_unique_char("loveleetcode"))

    def test_gemini_first_unique_char_empty_string(self):
        self.assertEqual(-1, first_unique_char(""))

    def test_gemini_first_unique_char_single_char(self):
        self.assertEqual(0, first_unique_char("a"))

    def test_gemini_first_unique_char_all_duplicates(self):
        self.assertEqual(-1, first_unique_char("aabbcc"))
