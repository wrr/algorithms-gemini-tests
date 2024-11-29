
import unittest
from algorithms.matrix.rotate_image import rotate


class RotateImageGeminiTest(unittest.TestCase):
    def test_gemini_rotate_image_empty_matrix(self):
        self.assertEqual([], rotate([]))

    def test_gemini_rotate_image_single_element(self):
        self.assertEqual([[1]], rotate([[1]]))

    def test_gemini_rotate_image_2x2_matrix(self):
        matrix = [[1, 2],
                  [3, 4]]
        expected = [[3, 1],
                    [4, 2]]
        self.assertEqual(expected, rotate(matrix))

    def test_gemini_rotate_image_3x3_matrix(self):
        matrix = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]
        expected = [[7, 4, 1],
                    [8, 5, 2],
                    [9, 6, 3]]
        self.assertEqual(expected, rotate(matrix))
