
"""
Given a linked list, is_sort function returns true if the list is in sorted
(increasing) order and return false otherwise. An empty list is considered
to be sorted.

For example:
Null :List is sorted
1 2 3 4 :List is sorted
1 2 -1 3 :List is not sorted
"""
class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

def is_sorted(head):
    if not head:
        return True
    current = head
    while current.next:
        if current.val > current.next.val:
            return False
        current = current.next
    return True

import unittest


class IsSortedGeminiTest(unittest.TestCase):
    def test_gemini_is_sorted_empty_list(self):
        self.assertTrue(is_sorted(None))

    def test_gemini_is_sorted_sorted_list(self):
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        head.next.next.next = Node(4)
        self.assertTrue(is_sorted(head))

    def test_gemini_is_sorted_unsorted_list(self):
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(-1)
        head.next.next.next = Node(3)
        self.assertFalse(is_sorted(head))

