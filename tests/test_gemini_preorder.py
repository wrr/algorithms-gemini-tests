
'''
Time complexity : O(n)
'''


class Node:
    """ This is a class of Node """

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder(root):
    """ Function to Preorder """
    res = []
    if not root:
        return res
    stack = []
    stack.append(root)
    while stack:
        root = stack.pop()
        res.append(root.val)
        if root.right:
            stack.append(root.right)
        if root.left:
            stack.append(root.left)
    return res


def preorder_rec(root, res=None):
    """ Recursive Implementation """
    if root is None:
        return []
    if res is None:
        res = []
    res.append(root.val)
    preorder_rec(root.left, res)
    preorder_rec(root.right, res)
    return res


import unittest


class PreorderGeminiTest(unittest.TestCase):
    def test_gemini_preorder_empty_tree(self):
        self.assertEqual(preorder(None), [])

    def test_gemini_preorder_single_node(self):
        root = Node(1)
        self.assertEqual(preorder(root), [1])

    def test_gemini_preorder_small_tree(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        self.assertEqual(preorder(root), [1, 2, 3])

    def test_gemini_preorder_rec_empty_tree(self):
        self.assertEqual(preorder_rec(None), [])

    def test_gemini_preorder_rec_single_node(self):
        root = Node(1)
        self.assertEqual(preorder_rec(root), [1])

    def test_gemini_preorder_rec_small_tree(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        self.assertEqual(preorder_rec(root), [1, 2, 3])

