
import unittest
from algorithms.tree.traversal.inorder import inorder, inorder_rec, Node


class InorderTraversalGeminiTest(unittest.TestCase):
    def test_gemini_inorder_traversal_empty_tree(self):
        self.assertEqual([], inorder(None))
        self.assertEqual([], inorder_rec(None))

    def test_gemini_inorder_traversal_single_node(self):
        tree = Node(1)
        self.assertEqual([1], inorder(tree))
        self.assertEqual([1], inorder_rec(tree))

    def test_gemini_inorder_traversal_general_case(self):
        tree = Node(1)
        tree.left = Node(2)
        tree.right = Node(3)
        tree.left.left = Node(4)
        tree.left.right = Node(5)
        self.assertEqual([4, 2, 5, 1, 3], inorder(tree))
        self.assertEqual([4, 2, 5, 1, 3], inorder_rec(tree))
