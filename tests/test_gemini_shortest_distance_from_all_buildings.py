import collections
import unittest
from algorithms.bfs import shortest_distance_from_all_buildings


class ShortestDistanceFromAllBuildingsGeminiTest(unittest.TestCase):
    def test_gemini_example_1(self):
        grid = [[1, 0, 2, 0, 1],
                [0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0]]
        expected = 7
        self.assertEqual(shortest_distance_from_all_buildings.shortest_distance(grid), expected)

    def test_gemini_example_2(self):
        grid = [[1]]
        expected = -1
        self.assertEqual(shortest_distance_from_all_buildings.shortest_distance(grid), expected)

    def test_gemini_example_3(self):
        grid = [[1, 2, 0]]
        expected = -1
        self.assertEqual(shortest_distance_from_all_buildings.shortest_distance(grid), expected)

    def test_gemini_example_4(self):
        grid = [[1, 0]]
        expected = 1
        self.assertEqual(shortest_distance_from_all_buildings.shortest_distance(grid), expected)

