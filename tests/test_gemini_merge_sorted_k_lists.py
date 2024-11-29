
import unittest
from algorithms.heap.merge_sorted_k_lists import ListNode, merge_k_lists


class MergeSortedKListsGeminiTest(unittest.TestCase):
    def test_gemini_merge_k_lists_empty_list(self):
        self.assertIsNone(merge_k_lists([]))

    def test_gemini_merge_k_lists_single_list(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        self.assertEqual(head.val, merge_k_lists([head]).val)

    def test_gemini_merge_k_lists_two_lists(self):
        head1 = ListNode(1)
        head1.next = ListNode(3)
        head1.next.next = ListNode(5)
        head2 = ListNode(2)
        head2.next = ListNode(4)
        head2.next.next = ListNode(6)
        merged = merge_k_lists([head1, head2])
        self.assertEqual(1, merged.val)
        self.assertEqual(2, merged.next.val)
        self.assertEqual(3, merged.next.next.val)
        self.assertEqual(4, merged.next.next.next.val)
        self.assertEqual(5, merged.next.next.next.next.val)
        self.assertEqual(6, merged.next.next.next.next.next.val)

    def test_gemini_merge_k_lists_three_lists(self):
        head1 = ListNode(1)
        head1.next = ListNode(4)
        head1.next.next = ListNode(7)
        head2 = ListNode(2)
        head2.next = ListNode(5)
        head2.next.next = ListNode(8)
        head3 = ListNode(3)
        head3.next = ListNode(6)
        head3.next.next = ListNode(9)
        merged = merge_k_lists([head1, head2, head3])
        self.assertEqual(1, merged.val)
        self.assertEqual(2, merged.next.val)
        self.assertEqual(3, merged.next.next.val)
        self.assertEqual(4, merged.next.next.next.val)
        self.assertEqual(5, merged.next.next.next.next.val)
        self.assertEqual(6, merged.next.next.next.next.next.val)
        self.assertEqual(7, merged.next.next.next.next.next.next.val)
        self.assertEqual(8, merged.next.next.next.next.next.next.next.val)
        self.assertEqual(9, merged.next.next.next.next.next.next.next.next.val)
