
import unittest
from algorithms.dp.word_break import word_break


class WordBreakGeminiTest(unittest.TestCase):
    def test_gemini_word_break_leetcode_example(self):
        self.assertTrue(word_break("leetcode", {"leet", "code"}))

    def test_gemini_word_break_empty_string(self):
        self.assertTrue(word_break("", {"leet", "code"}))

    def test_gemini_word_break_single_word(self):
        self.assertTrue(word_break("code", {"leet", "code"}))

    def test_gemini_word_break_no_match(self):
        self.assertFalse(word_break("leetcoder", {"leet", "code"}))

    def test_gemini_word_break_multiple_matches(self):
        self.assertTrue(word_break("applepenapple", {"apple", "pen"}))
