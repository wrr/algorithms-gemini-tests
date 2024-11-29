
import unittest
from algorithms.graph.count_connected_number_of_component import count_components


class CountConnectedNumberOfComponentGeminiTest(unittest.TestCase):
    def test_gemini_count_connected_number_of_component_example_1(self):
        adjacency_list = [[2], [5], [0, 4], [], [2], [1]]
        size = 5
        self.assertEqual(3, count_components(adjacency_list, size))

    def test_gemini_count_connected_number_of_component_empty_graph(self):
        adjacency_list = [[]]
        size = 0
        self.assertEqual(0, count_components(adjacency_list, size))

    def test_gemini_count_connected_number_of_component_no_edges(self):
        adjacency_list = [[0], [], [2], [3], [4]]
        size = 4
        self.assertEqual(4, count_components(adjacency_list, size))
