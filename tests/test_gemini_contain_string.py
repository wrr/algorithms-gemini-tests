
import unittest
from algorithms.strings.contain_string import contain_string


class ContainStringGeminiTest(unittest.TestCase):
    def test_gemini_contain_string_needle_in_haystack(self):
        self.assertEqual(2, contain_string("hello", "ll"))

    def test_gemini_contain_string_needle_not_in_haystack(self):
        self.assertEqual(-1, contain_string("aaaaa", "bba"))

    def test_gemini_contain_string_empty_needle(self):
        self.assertEqual(0, contain_string("hello", ""))

    def test_gemini_contain_string_needle_longer_than_haystack(self):
        self.assertEqual(-1, contain_string("hello", "helloworld"))

    def test_gemini_contain_string_needle_at_end_of_haystack(self):
        self.assertEqual(2, contain_string("hello", "llo"))

    def test_gemini_contain_string_needle_not_at_end_of_haystack(self):
        self.assertEqual(-1, contain_string("mississippi", "issipi"))
