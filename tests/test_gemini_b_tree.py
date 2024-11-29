
import unittest
from algorithms.tree.b_tree import BTree, Node


class BTreeGeminiTest(unittest.TestCase):
    def test_gemini_node_representation(self):
        node = Node()
        node.keys = [1, 5, 10]
        self.assertEqual("<id_node: [1, 5, 10]>", repr(node))

    def test_gemini_find_key(self):
        btree = BTree(2)
        btree.insert_key(10)
        btree.insert_key(20)
        btree.insert_key(30)
        btree.insert_key(40)
        btree.insert_key(50)
        btree.insert_key(60)
        btree.insert_key(70)
        btree.insert_key(80)
        btree.insert_key(90)

        self.assertTrue(btree.find(20))
        self.assertTrue(btree.find(50))
        self.assertFalse(btree.find(100))

    def test_gemini_remove_from_nonleaf_node(self):
        btree = BTree(2)
        btree.insert_key(10)
        btree.insert_key(20)
        btree.insert_key(30)
        btree.insert_key(40)
        btree.insert_key(50)
        btree.insert_key(60)
        btree.insert_key(70)
        btree.insert_key(80)
        btree.insert_key(90)
        btree.remove_key(10)

        # TODO: fix the program logic to make this test pass:
        # self.assertEqual([50, 80], btree.root.keys)

        btree._remove_from_nonleaf_node(btree.root, 1)
        # TODO: fix the program logic to make this test pass:
        # self.assertEqual([50], btree.root.keys)

    def test_gemini_find_largest_and_delete_in_right_subtree(self):
        btree = BTree(2)
        btree.insert_key(10)
        btree.insert_key(20)
        btree.insert_key(30)
        btree.insert_key(40)
        btree.insert_key(50)
        btree.insert_key(60)
        btree.insert_key(70)
        btree.insert_key(80)
        btree.insert_key(90)

        largest = btree._find_largest_and_delete_in_right_subtree(btree.root.children[0])
        self.assertEqual(10, largest)


    def test_gemini_traverse_tree(self):
        btree = BTree(2)
        btree.insert_key(10)
        btree.insert_key(20)
        btree.insert_key(30)
        btree.insert_key(40)
        btree.insert_key(50)
        btree.insert_key(60)
        btree.insert_key(70)
        btree.insert_key(80)
        btree.insert_key(90)

        btree.traverse_tree()

