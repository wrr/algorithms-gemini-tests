
'''
Given string s, find the longest palindromic substring.

Example1:

* input: "dasdasdasdasdasdadsa"
* output: "asdadsa"

Example2:

* input: "acdbbdaa"
* output: "dbbd"

Manacher's algorithm

'''

def longest_palindrome(s):
    if len(s) < 2:
        return s

    n_str = '#' + '#'.join(s) + '#'
    p = [0] * len(n_str)
    mx, loc = 0, 0
    index, maxlen = 0, 0
    for i in range(len(n_str)):
        if i < mx and 2 * loc - i < len(n_str):
            p[i] = min(mx - i, p[2 * loc - i])
        else:
            p[i] = 1

        while p[i] + i < len(n_str) and i - p[i] >= 0 and n_str[
                i - p[i]] == n_str[i + p[i]]:
            p[i] += 1

        if i + p[i] > mx:
            mx = i + p[i]
            loc = i

        if p[i] > maxlen:
            index = i
            maxlen = p[i]
    s = n_str[index - p[index] + 1:index + p[index]]
    return s.replace('#', '')

import unittest


class LongestPalindromicSubstringGeminiTest(unittest.TestCase):
    def test_gemini_longest_palindrome_empty_string(self):
        self.assertEqual(longest_palindrome(""), "")

    def test_gemini_longest_palindrome_single_character(self):
        self.assertEqual(longest_palindrome("a"), "a")

    def test_gemini_longest_palindrome_even_length(self):
        self.assertEqual(longest_palindrome("acdbbdaa"), "dbbd")

    def test_gemini_longest_palindrome_odd_length(self):
        self.assertEqual(longest_palindrome("dasdasdasdasdasdadsa"), "asdadsa")

