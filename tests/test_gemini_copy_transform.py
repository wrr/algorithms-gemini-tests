
import unittest
from algorithms.matrix.copy_transform import rotate_clockwise, rotate_counterclockwise, top_left_invert, bottom_left_invert


class TestCopyTransformGeminiTest(unittest.TestCase):
    def test_gemini_rotate_clockwise(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
        self.assertEqual(expected, rotate_clockwise(matrix))

    def test_gemini_rotate_counterclockwise(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected = [[3, 6, 9], [2, 5, 8], [1, 4, 7]]
        self.assertEqual(expected, rotate_counterclockwise(matrix))

    def test_gemini_top_left_invert(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
        self.assertEqual(expected, top_left_invert(matrix))

    def test_gemini_bottom_left_invert(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected = [[9, 6, 3], [8, 5, 2], [7, 4, 1]]
        self.assertEqual(expected, bottom_left_invert(matrix))
