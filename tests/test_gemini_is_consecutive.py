
import unittest
from algorithms.stack.is_consecutive import first_is_consecutive, second_is_consecutive


class IsConsecutiveGeminiTest(unittest.TestCase):
    def test_gemini_first_is_consecutive_true(self):
        stack = [3, 4, 5, 6, 7]
        self.assertTrue(first_is_consecutive(stack))
        # TODO: fix the program logic to make this test pass:
        # self.assertEqual([3, 4, 5, 6, 7], stack)

    def test_gemini_first_is_consecutive_false(self):
        stack = [3, 4, 6, 7]
        self.assertFalse(first_is_consecutive(stack))
        # TODO: fix the program logic to make this test pass:
        # self.assertEqual([3, 4, 6, 7], stack)

    def test_gemini_first_is_consecutive_reverse_order(self):
        stack = [3, 2, 1]
        self.assertFalse(first_is_consecutive(stack))
        # TODO: fix the program logic to make this test pass:
        # self.assertEqual([3, 2, 1], stack)

    def test_gemini_second_is_consecutive_true(self):
        stack = [3, 4, 5, 6, 7]
        self.assertTrue(second_is_consecutive(stack))
        # TODO: fix the program logic to make this test pass:
        # self.assertEqual([3, 4, 5, 6, 7], stack)

    def test_gemini_second_is_consecutive_false(self):
        stack = [3, 4, 6, 7]
        self.assertFalse(second_is_consecutive(stack))
        # TODO: fix the program logic to make this test pass:
        # self.assertEqual([3, 4, 6, 7], stack)

    def test_gemini_second_is_consecutive_reverse_order(self):
        stack = [3, 2, 1]
        self.assertFalse(second_is_consecutive(stack))
        # TODO: fix the program logic to make this test pass:
        # self.assertEqual([3, 2, 1], stack)
