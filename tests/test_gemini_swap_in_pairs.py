
"""
Given a linked list, swap every two adjacent nodes
and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space.
You may not modify the values in the list,
only nodes itself can be changed.
"""
class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def swap_pairs(head):
    if not head:
        return head
    start = Node(0)
    start.next = head
    current = start
    while current.next and current.next.next:
        first = current.next
        second = current.next.next
        first.next = second.next
        current.next = second
        current.next.next = first
        current = current.next.next
    return start.next

import unittest


class SwapInPairsGeminiTest(unittest.TestCase):
    def test_gemini_swap_pairs_empty_list(self):
        self.assertIsNone(swap_pairs(None))

    def test_gemini_swap_pairs_single_node(self):
        head = Node(1)
        self.assertEqual(swap_pairs(head).val, 1)

    def test_gemini_swap_pairs_two_nodes(self):
        head = Node(1)
        head.next = Node(2)
        swapped = swap_pairs(head)
        self.assertEqual(swapped.val, 2)
        self.assertEqual(swapped.next.val, 1)

    def test_gemini_swap_pairs_multiple_nodes(self):
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        head.next.next.next = Node(4)
        swapped = swap_pairs(head)
        self.assertEqual(swapped.val, 2)
        self.assertEqual(swapped.next.val, 1)
        self.assertEqual(swapped.next.next.val, 4)
        self.assertEqual(swapped.next.next.next.val, 3)

