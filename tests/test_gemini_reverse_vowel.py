
def reverse_vowel(s):
    vowels = "AEIOUaeiou"
    i, j = 0, len(s)-1
    s = list(s)
    while i < j:
        while i < j and s[i] not in vowels:
            i += 1
        while i < j and s[j] not in vowels:
            j -= 1
        s[i], s[j] = s[j], s[i]
        i, j = i + 1, j - 1
    return "".join(s)

import unittest


class ReverseVowelGeminiTest(unittest.TestCase):
    def test_gemini_reverse_vowel_all_vowels(self):
        self.assertEqual(reverse_vowel("aeiou"), "uoiea")

    def test_gemini_reverse_vowel_no_vowels(self):
        self.assertEqual(reverse_vowel("bcdfghjklmnpqrstvwxyz"), "bcdfghjklmnpqrstvwxyz")

    def test_gemini_reverse_vowel_mixed(self):
        self.assertEqual(reverse_vowel("leetcode"), "leotcede")

