
import unittest
from algorithms.dp.min_cost_path import min_cost


class MinCostPathGeminiTest(unittest.TestCase):
    def test_gemini_min_cost_path_example(self):
        costs = [[0, 15, 80, 90],
                 [-1, 0, 40, 50],
                 [-1, -1, 0, 70],
                 [-1, -1, -1, 0]]
        self.assertEqual(65, min_cost(costs))

    def test_gemini_min_cost_path_single_station(self):
        costs = [[0]]
        self.assertEqual(0, min_cost(costs))

    def test_gemini_min_cost_path_two_stations(self):
        costs = [[0, 10],
                 [-1, 0]]
        self.assertEqual(10, min_cost(costs))
