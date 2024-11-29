
import unittest
from algorithms.maths.find_primitive_root_simple import find_primitive_root


class TestFindPrimitiveRootSimpleGeminiTest(unittest.TestCase):
    def test_gemini_find_primitive_root_simple_one(self):
        self.assertEqual([0], find_primitive_root(1))

    def test_gemini_find_primitive_root_simple_prime(self):
        self.assertEqual([2, 3], find_primitive_root(5))

    def test_gemini_find_primitive_root_simple_no_root(self):
        self.assertEqual([], find_primitive_root(24))

    def test_gemini_find_primitive_root_simple_large_number(self):
        self.assertEqual([2, 5, 13, 15, 17, 18, 19, 20, 22, 24, 32, 35], find_primitive_root(37))
