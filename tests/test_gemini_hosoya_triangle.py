
import unittest
from algorithms.dp.hosoya_triangle import hosoya_testing


class HosoyaTriangleGeminiTest(unittest.TestCase):
    def test_gemini_hosoya_triangle_height_1(self):
        self.assertEqual([1], hosoya_testing(1))

    def test_gemini_hosoya_triangle_height_6(self):
        self.assertEqual([1,
                          1, 1,
                          2, 1, 2,
                          3, 2, 2, 3,
                          5, 3, 4, 3, 5,
                          8, 5, 6, 6, 5, 8],
                         hosoya_testing(6))

    def test_gemini_hosoya_triangle_height_10(self):
        self.assertEqual([1,
                          1, 1,
                          2, 1, 2,
                          3, 2, 2, 3,
                          5, 3, 4, 3, 5,
                          8, 5, 6, 6, 5, 8,
                          13, 8, 10, 9, 10, 8, 13,
                          21, 13, 16, 15, 15, 16, 13, 21,
                          34, 21, 26, 24, 25, 24, 26, 21, 34,
                          55, 34, 42, 39, 40, 40, 39, 42, 34, 55],
                         hosoya_testing(10))
