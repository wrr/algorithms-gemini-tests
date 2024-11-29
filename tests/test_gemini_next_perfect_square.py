
"""
This program will look for the next perfect square.
Check the argument to see if it is a perfect square itself, if it is not then return -1 otherwise
look for the next perfect square.
for instance if you pass 121 then the script should return the next perfect square which is 144.
"""

def find_next_square(sq):
    root = sq ** 0.5
    if root.is_integer():
        return (root + 1)**2
    return -1

def find_next_square2(sq):
    """ Alternative method, works by evaluating anything non-zero as True (0.000001 --> True) """
    root = sq**0.5
    return -1 if root % 1 else (root+1)**2

import unittest


class NextPerfectSquareGeminiTest(unittest.TestCase):
    def test_gemini_find_next_square_perfect_square(self):
        self.assertEqual(find_next_square(121), 144)

    def test_gemini_find_next_square_not_perfect_square(self):
        self.assertEqual(find_next_square(155), -1)

    def test_gemini_find_next_square2_perfect_square(self):
        self.assertEqual(find_next_square2(121), 144)

    def test_gemini_find_next_square2_not_perfect_square(self):
        self.assertEqual(find_next_square2(155), -1)

