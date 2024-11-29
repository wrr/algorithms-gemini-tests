
import unittest
from algorithms.matrix.sparse_dot_vector import vector_to_index_value_list, dot_product


class SparseDotVectorGeminiTest(unittest.TestCase):
    def test_gemini_sparse_dot_vector_no_overlap(self):
        v1 = [1.0, 0.0, 0.0, 2.0]
        v2 = [0.0, 0.0, 3.0, 0.0]
        self.assertEqual(0.0, dot_product(vector_to_index_value_list(v1),
                                          vector_to_index_value_list(v2)))

    def test_gemini_sparse_dot_vector_some_overlap(self):
        v1 = [1.0, 0.0, 2.0, 0.0]
        v2 = [0.0, 3.0, 2.0, 0.0]
        self.assertEqual(4.0, dot_product(vector_to_index_value_list(v1),
                                          vector_to_index_value_list(v2)))

    def test_gemini_sparse_dot_vector_all_overlap(self):
        v1 = [1.0, 2.0, 3.0, 4.0]
        v2 = [5.0, 6.0, 7.0, 8.0]
        self.assertEqual(70.0, dot_product(vector_to_index_value_list(v1),
                                          vector_to_index_value_list(v2)))
