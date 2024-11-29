
import unittest
from algorithms.graph.maximum_flow import ford_fulkerson, edmonds_karp, dinic


class TestMaximumFlowGeminiTest(unittest.TestCase):
    def test_gemini_maximum_flow_ford_fulkerson_example(self):
        capacity = [[0, 10, 10, 0, 0, 0, 0],
                    [0, 0, 2, 0, 4, 8, 0],
                    [0, 0, 0, 0, 0, 9, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 10],
                    [0, 0, 0, 0, 6, 0, 10],
                    [0, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(19, ford_fulkerson(capacity, 0, 6))

    def test_gemini_maximum_flow_edmonds_karp_example(self):
        capacity = [[0, 10, 10, 0, 0, 0, 0],
                    [0, 0, 2, 0, 4, 8, 0],
                    [0, 0, 0, 0, 0, 9, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 10],
                    [0, 0, 0, 0, 6, 0, 10],
                    [0, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(19, edmonds_karp(capacity, 0, 6))

    def test_gemini_maximum_flow_dinic_example(self):
        capacity = [[0, 10, 10, 0, 0, 0, 0],
                    [0, 0, 2, 0, 4, 8, 0],
                    [0, 0, 0, 0, 0, 9, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 10],
                    [0, 0, 0, 0, 6, 0, 10],
                    [0, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(19, dinic(capacity, 0, 6))
