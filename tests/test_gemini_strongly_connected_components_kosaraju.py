
import unittest
from algorithms.graph.strongly_connected_components_kosaraju import Kosaraju


class StronglyConnectedComponentsKosarajuGeminiTest(unittest.TestCase):
    def test_gemini_kosaraju_algorithm_example_1(self):
        V = 6
        adj = [[2], [0], [3], [1, 4], [5], [4]]
        self.assertEqual(2, Kosaraju().kosaraju(V, adj))

    def test_gemini_kosaraju_algorithm_example_2(self):
        V = 5
        adj = [[1, 3], [2], [3, 4], [], [2]]
        self.assertEqual(4, Kosaraju().kosaraju(V, adj))
