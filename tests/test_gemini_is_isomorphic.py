
"""
Given two strings s and t, determine if they are isomorphic.
Two strings are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while
preserving the order of characters. No two characters may map to the same
character but a character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true
Reference: https://leetcode.com/problems/isomorphic-strings/description/
"""
def is_isomorphic(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s) != len(t):
        return False
    dict = {}
    set_value = set()
    for i in range(len(s)):
        if s[i] not in dict:
            if t[i] in set_value:
                return False
            dict[s[i]] = t[i]
            set_value.add(t[i])
        else:
            if dict[s[i]] != t[i]:
                return False
    return True

import unittest


class IsIsomorphicGeminiTest(unittest.TestCase):
    def test_gemini_is_isomorphic_true(self):
        self.assertTrue(is_isomorphic("egg", "add"))
        self.assertTrue(is_isomorphic("paper", "title"))

    def test_gemini_is_isomorphic_false(self):
        self.assertFalse(is_isomorphic("foo", "bar"))
        self.assertFalse(is_isomorphic("ab", "aa"))

