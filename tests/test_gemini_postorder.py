
'''
Time complexity : O(n)
'''

class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def postorder(root):
    res_temp = []
    res = []
    if not root:
        return res
    stack = []
    stack.append(root)
    while stack:
        root = stack.pop()
        res_temp.append(root.val)
        if root.left:
            stack.append(root.left)
        if root.right:
            stack.append(root.right)
    while res_temp:
        res.append(res_temp.pop())
    return res

# Recursive Implementation
def postorder_rec(root, res=None):
    if root is None:
        return []
    if res is None:
        res = []
    postorder_rec(root.left, res)
    postorder_rec(root.right, res)
    res.append(root.val)
    return res

import unittest


class PostorderGeminiTest(unittest.TestCase):
    def test_gemini_postorder_empty_tree(self):
        self.assertEqual(postorder(None), [])

    def test_gemini_postorder_single_node(self):
        root = Node(1)
        self.assertEqual(postorder(root), [1])

    def test_gemini_postorder_small_tree(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        self.assertEqual(postorder(root), [2, 3, 1])

    def test_gemini_postorder_rec_empty_tree(self):
        self.assertEqual(postorder_rec(None), [])

    def test_gemini_postorder_rec_single_node(self):
        root = Node(1)
        self.assertEqual(postorder_rec(root), [1])

    def test_gemini_postorder_rec_small_tree(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        self.assertEqual(postorder_rec(root), [2, 3, 1])

