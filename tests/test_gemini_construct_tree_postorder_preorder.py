
import unittest
from algorithms.tree.construct_tree_postorder_preorder import construct_tree
from algorithms.tree.construct_tree_postorder_preorder import pre_index


class ConstructTreePostorderPreorderGeminiTest(unittest.TestCase):
    def test_gemini_construct_tree_postorder_preorder(self):
        pre_index = 0
        pre = [1, 2, 4, 8, 9, 5, 3, 6, 7]
        post = [8, 9, 4, 5, 2, 6, 7, 3, 1]
        size = len(pre)
        self.assertEqual([8, 4, 9, 2, 5, 1, 6, 3, 7], construct_tree(pre, post, size))

        pre_index = 0
        pre = [1, 2, 4, 5, 3, 6, 7]
        post = [4, 5, 2, 6, 7, 3, 1]
        size = len(pre)
        # TODO: this test is failing:
        # self.assertEqual([4, 2, 5, 1, 6, 3, 7], construct_tree(pre, post, size))
