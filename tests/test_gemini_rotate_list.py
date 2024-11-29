
"""
Given a list, rotate the list to the right by k places,
where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def rotate_right(head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """
    if not head or not head.next:
        return head
    current = head
    length = 1
    # count length of the list
    while current.next:
        current = current.next
        length += 1
    # make it circular
    current.next = head
    k = k % length
    # rotate until length-k
    for i in range(length-k):
        current = current.next
    head = current.next
    current.next = None
    return head

import unittest


class RotateListGeminiTest(unittest.TestCase):
    def test_gemini_rotate_right_empty_list(self):
        self.assertEqual(rotate_right(None, 2), None)

    def test_gemini_rotate_right_single_node(self):
        head = ListNode(1)
        self.assertEqual(rotate_right(head, 2).val, 1)

    def test_gemini_rotate_right_multiple_nodes(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = ListNode(5)
        rotated = rotate_right(head, 2)
        self.assertEqual(rotated.val, 4)
        self.assertEqual(rotated.next.val, 5)
        self.assertEqual(rotated.next.next.val, 1)
        self.assertEqual(rotated.next.next.next.val, 2)
        self.assertEqual(rotated.next.next.next.next.val, 3)

