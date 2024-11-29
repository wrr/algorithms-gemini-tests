
import unittest
from algorithms.strings.reverse_words import reverse_words


class ReverseWordsGeminiTest(unittest.TestCase):
    def test_gemini_reverse_words_single_word(self):
        self.assertEqual("hello", reverse_words("hello"))

    def test_gemini_reverse_words_multiple_words(self):
        self.assertEqual("pizza like I and kim keon am I", reverse_words("I am keon kim and I like pizza"))

    def test_gemini_reverse_words_leading_and_trailing_spaces(self):
        self.assertEqual("world hello", reverse_words("  hello world  "))
