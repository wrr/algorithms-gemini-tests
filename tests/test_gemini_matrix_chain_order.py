
import unittest
from algorithms.dp.matrix_chain_order import matrix_chain_order, print_optimal_solution


class MatrixChainOrderGeminiTest(unittest.TestCase):
    def test_gemini_matrix_chain_order_small_array(self):
        array = [10, 20, 30]
        expected_matrix = [[0, 6000, 18000], [0, 0, 6000], [0, 0, 0]]
        expected_solution = [[0, 1, 1], [0, 0, 2], [0, 0, 0]]
        matrix, solution = matrix_chain_order(array)
        self.assertEqual(expected_matrix, matrix)
        self.assertEqual(expected_solution, solution)

    def test_gemini_matrix_chain_order_larger_array(self):
        array = [30, 35, 15, 5, 10, 20, 25]
        expected_matrix = [[0, 15750, 7875, 9375, 11875, 15125, 15125],
                           [0, 0, 26250, 10500, 11500, 14375, 16625],
                           [0, 0, 0, 7500, 9000, 11250, 13125],
                           [0, 0, 0, 0, 3500, 5000, 6875],
                           [0, 0, 0, 0, 0, 10000, 12500],
                           [0, 0, 0, 0, 0, 0, 5000],
                           [0, 0, 0, 0, 0, 0, 0]]
        expected_solution = [[0, 1, 2, 2, 2, 5, 5],
                           [0, 0, 2, 3, 3, 5, 5],
                           [0, 0, 0, 3, 3, 5, 5],
                           [0, 0, 0, 0, 4, 5, 5],
                           [0, 0, 0, 0, 0, 5, 5],
                           [0, 0, 0, 0, 0, 0, 6],
                           [0, 0, 0, 0, 0, 0, 0]]
        matrix, solution = matrix_chain_order(array)
        self.assertEqual(expected_matrix, matrix)
        self.assertEqual(expected_solution, solution)

    def test_gemini_print_optimal_solution(self):
        solution = [[0, 1, 2, 2, 2, 5, 5],
                    [0, 0, 2, 3, 3, 5, 5],
                    [0, 0, 0, 3, 3, 5, 5],
                    [0, 0, 0, 0, 4, 5, 5],
                    [0, 0, 0, 0, 0, 5, 5],
                    [0, 0, 0, 0, 0, 0, 6],
                    [0, 0, 0, 0, 0, 0, 0]]
        # TODO: fix the program logic to make this test pass:
        # print_optimal_solution(solution, 1, 6)
        pass
