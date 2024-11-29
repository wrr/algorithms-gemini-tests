
import unittest
from algorithms.graph.find_path import find_path, find_all_path, find_shortest_path


class TestFindPathGeminiTest(unittest.TestCase):
    def test_gemini_find_path_no_path(self):
        graph = {'A': ['B', 'C'],
                 'B': ['C', 'D'],
                 'C': ['D'],
                 'D': ['C'],
                 'E': ['F'],
                 'F': ['C']}
        self.assertIsNone(find_path(graph, 'A', 'E'))

    def test_gemini_find_path_path_exists(self):
        graph = {'A': ['B', 'C'],
                 'B': ['C', 'D'],
                 'C': ['D'],
                 'D': ['C'],
                 'E': ['F'],
                 'F': ['C']}
        self.assertEqual(['A', 'B', 'C', 'D'], find_path(graph, 'A', 'D'))

    def test_gemini_find_all_paths_no_path(self):
        graph = {'A': ['B', 'C'],
                 'B': ['C', 'D'],
                 'C': ['D'],
                 'D': ['C'],
                 'E': ['F'],
                 'F': ['C']}
        self.assertEqual([], find_all_path(graph, 'A', 'E'))

    def test_gemini_find_all_paths_path_exists(self):
        graph = {'A': ['B', 'C'],
                 'B': ['C', 'D'],
                 'C': ['D'],
                 'D': ['C'],
                 'E': ['F'],
                 'F': ['C']}
        expected_paths = [['A', 'B', 'C', 'D'], ['A', 'B', 'D'], ['A', 'C', 'D']]
        self.assertEqual(sorted(expected_paths), sorted(find_all_path(graph, 'A', 'D')))

    def test_gemini_find_shortest_path_no_path(self):
        graph = {'A': ['B', 'C'],
                 'B': ['C', 'D'],
                 'C': ['D'],
                 'D': ['C'],
                 'E': ['F'],
                 'F': ['C']}
        self.assertIsNone(find_shortest_path(graph, 'A', 'E'))

    def test_gemini_find_shortest_path_path_exists(self):
        graph = {'A': ['B', 'C'],
                 'B': ['C', 'D'],
                 'C': ['D'],
                 'D': ['C'],
                 'E': ['F'],
                 'F': ['C']}
        self.assertEqual(['A', 'B', 'D'], find_shortest_path(graph, 'A', 'D'))
