from __future__ import annotations
import unittest

from solutions.spiral_matrix_solution import Solution


class SpiralMatrixTest(unittest.TestCase):
    def setUp(self: SpiralMatrixTest) -> None:
        self.solution = Solution()

    def tearDown(self: SpiralMatrixTest) -> None:
        pass

    def test_example_one(self: SpiralMatrixTest) -> None:
        test_input = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        expected_output = [1, 2, 3, 6, 9, 8, 7, 4, 5]
        actual_output = self.solution.spiralOrder(test_input)
        self.assertEqual(expected_output, actual_output)

    def test_example_two(self: SpiralMatrixTest) -> None:
        test_input = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]
        ]
        expected_output = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
        actual_output = self.solution.spiralOrder(test_input)
        self.assertEqual(expected_output, actual_output)

    def test_empty(self: SpiralMatrixTest) -> None:
        test_input = []
        expected_output = []
        actual_output = self.solution.spiralOrder(test_input)
        self.assertEqual(expected_output, actual_output)

    def test_one_dimension_horizontal(self: SpiralMatrixTest) -> None:
        test_input = [[1, 2, 3, 4, 5]]
        expected_output = [1, 2, 3, 4, 5]
        actual_output = self.solution.spiralOrder(test_input)
        self.assertEqual(expected_output, actual_output)

    def test_one_dimension_vertical(self: SpiralMatrixTest) -> None:
        test_input = [
            [1],
            [2],
            [3],
            [4],
            [5],
        ]
        expected_output = [1, 2, 3, 4, 5]
        actual_output = self.solution.spiralOrder(test_input)
        self.assertEqual(expected_output, actual_output)

    def test_big(self: SpiralMatrixTest) -> None:
        test_input = [
            [1, 2, 3, 4, 5, 6, 7],
            [8, 9, 10, 11, 12, 13, 14],
            [15, 16, 17, 18, 19, 20, 21],
            [22, 23, 24, 25, 26, 27, 28],
            [29, 30, 31, 32, 33, 34, 35],
            [36, 37, 38, 39, 40, 41, 42]
        ]
        expected_output = \
            [1, 2, 3, 4, 5, 6, 7, 14, 21, 28, 35, 42, 41, 40, 39,
             38, 37, 36, 29, 22, 15, 8, 9, 10, 11, 12, 13, 20, 27, 34,
             33, 32, 31, 30, 23, 16, 17, 18, 19, 26, 25, 24]
        actual_output = self.solution.spiralOrder(test_input)
        self.assertEqual(expected_output, actual_output)


if __name__ == '__main__':
    unittest.main()
