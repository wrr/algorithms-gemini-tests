
import unittest
from algorithms.strings.repeat_string import repeat_string


class RepeatStringGeminiTest(unittest.TestCase):
    def test_gemini_repeat_string_example(self):
        self.assertEqual(3, repeat_string("abcd", "cdabcdab"))

    def test_gemini_repeat_string_substring(self):
        self.assertEqual(1, repeat_string("abcd", "bc"))

    def test_gemini_repeat_string_no_solution(self):
        self.assertEqual(-1, repeat_string("abcd", "efgh"))

    def test_gemini_repeat_string_empty_b(self):
        self.assertEqual(1, repeat_string("abcd", ""))

    def test_gemini_repeat_string_empty_a(self):
        # TODO: fix the program logic to make this test pass:
        # self.assertEqual(-1, repeat_string("", "abcd"))
        pass
