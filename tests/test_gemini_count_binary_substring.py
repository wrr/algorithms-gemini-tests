
import unittest
from algorithms.strings.count_binary_substring import count_binary_substring


class CountBinarySubstringGeminiTest(unittest.TestCase):
    def test_gemini_count_binary_substring(self):
        self.assertEqual(6, count_binary_substring("00110011"))
        self.assertEqual(4, count_binary_substring("10101"))
        self.assertEqual(3, count_binary_substring("00110"))
        self.assertEqual(0, count_binary_substring("0"))
        self.assertEqual(0, count_binary_substring(""))

