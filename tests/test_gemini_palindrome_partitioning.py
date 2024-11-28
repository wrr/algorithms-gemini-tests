
import unittest
from algorithms.backtrack.palindrome_partitioning import palindromic_substrings, palindromic_substrings_iter


class PalindromePartitioningGeminiTest(unittest.TestCase):
    def test_gemini_palindromic_substrings_empty(self):
        self.assertEqual([[]], palindromic_substrings(""))

    def test_gemini_palindromic_substrings_single_char(self):
        self.assertEqual([['a']], palindromic_substrings("a"))

    def test_gemini_palindromic_substrings_palindrome(self):
        expected_result = [['aba'], ['a', 'b', 'a']]
        self.assertEqual(expected_result, palindromic_substrings("aba"))

    def test_gemini_palindromic_substrings_double_char(self):
        expected_result = [['a', 'b']]
        self.assertEqual(expected_result, palindromic_substrings("ab"))

    def test_gemini_palindromic_substrings_example(self):
        expected_result = [['abcba', 'b'], ['a', 'bcb', 'a', 'b'],
                          ['a', 'b', 'c', 'bab'], ['a', 'b', 'c', 'b', 'a', 'b']]
        self.assertEqual(sorted(expected_result),
                         sorted(palindromic_substrings('abcbab')))

    def test_gemini_palindromic_substrings_iter_empty(self):
        self.assertEqual([[]], list(palindromic_substrings_iter("")))

    def test_gemini_palindromic_substrings_iter_single_char(self):
        self.assertEqual([['a']], list(palindromic_substrings_iter("a")))

    def test_gemini_palindromic_substrings_iter_palindrome(self):
        expected_result = [['aba'], ['a', 'b', 'a']]
        self.assertEqual(sorted(expected_result),
                         sorted(list(palindromic_substrings_iter("aba"))))

    def test_gemini_palindromic_substrings_iter_double_char(self):
        expected_result = [['a', 'b']]
        self.assertEqual(expected_result,
                         list(palindromic_substrings_iter("ab")))

    def test_gemini_palindromic_substrings_iter_example(self):
        expected_result = [['abcba', 'b'], ['a', 'bcb', 'a', 'b'],
                          ['a', 'b', 'c', 'bab'], ['a', 'b', 'c', 'b', 'a', 'b']]
        self.assertEqual(sorted(expected_result),
                         sorted(list(palindromic_substrings_iter('abcbab'))))

