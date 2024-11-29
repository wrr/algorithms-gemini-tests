
import unittest
from algorithms.dfs.sudoku_solver import Sudoku


class SudokuSolverGeminiTest(unittest.TestCase):
    def test_gemini_sudoku_solver_empty_board(self):
        board = [["." for _ in range(9)] for _ in range(9)]
        sudoku = Sudoku(board, 9, 9)
        self.assertTrue(sudoku.solve())

    def test_gemini_sudoku_solver_easy_board(self):
        board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
                 ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                 [".", "9", "8", ".", ".", ".", ".", "6", "."],
                 ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                 ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                 ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                 [".", "6", ".", ".", ".", ".", "2", "8", "."],
                 [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                 [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
        sudoku = Sudoku(board, 9, 9)
        self.assertTrue(sudoku.solve())

    def test_gemini_sudoku_solver_hard_board(self):
        board = [[".", ".", "9", "7", "4", "8", ".", ".", "."],
                 ["7", ".", ".", ".", ".", ".", ".", ".", "."],
                 [".", "2", ".", "1", ".", "9", ".", ".", "."],
                 [".", ".", "7", ".", ".", ".", "2", "4", "."],
                 [".", "6", "4", ".", "1", ".", "5", "9", "."],
                 [".", "9", "8", ".", ".", ".", "3", ".", "."],
                 [".", ".", ".", "8", ".", "3", ".", "2", "."],
                 [".", ".", ".", ".", ".", ".", ".", ".", "6"],
                 [".", ".", ".", "2", "7", "5", "9", ".", "."]]
        sudoku = Sudoku(board, 9, 9)
        self.assertTrue(sudoku.solve())
