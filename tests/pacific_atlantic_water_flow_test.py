from __future__ import annotations
from typing import List, Set
import unittest

from solutions.pacific_atlantic_water_flow_solution import Solution


class PacificAtlanticWaterFlowTest(unittest.TestCase):
    def setUp(self: PacificAtlanticWaterFlowTest) -> None:
        self.solution = Solution()

    def tearDown(self: PacificAtlanticWaterFlowTest) -> None:
        pass

    def compare_expected_and_actual_outputs(
            self: PacificAtlanticWaterFlowTest,
            expected_output: List[List[int]],
            actual_output: List[List[int]]) -> None:
        expected_output_set = set()
        actual_output_set = set()
        self.convert_nested_list_to_set(expected_output, expected_output_set)
        self.convert_nested_list_to_set(actual_output, actual_output_set)
        self.assertEqual(expected_output_set, actual_output_set)

    def convert_nested_list_to_set(
            self: PacificAtlanticWaterFlowTest,
            nested_list: List[List[int]],
            output_set: Set) -> None:
        for coordinate in nested_list:
            output_set.add(tuple(coordinate))
        return output_set

    def test_example(self: PacificAtlanticWaterFlowTest) -> None:
        test_input = [
            [1, 2, 2, 3, 5],
            [3, 2, 3, 4, 4],
            [2, 4, 5, 3, 1],
            [6, 7, 1, 4, 5],
            [5, 1, 1, 2, 4]
        ]
        expected_output = \
            [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
        actual_output = self.solution.pacificAtlantic(test_input)
        self.compare_expected_and_actual_outputs(
            expected_output, actual_output)

    def test_vertical(self: PacificAtlanticWaterFlowTest) -> None:
        test_input = [
            [1],
            [2],
            [3]
        ]
        expected_output = \
            [[0, 0], [1, 0], [2, 0]]
        actual_output = self.solution.pacificAtlantic(test_input)
        self.compare_expected_and_actual_outputs(
            expected_output, actual_output)

    def test_horizontal(self: PacificAtlanticWaterFlowTest) -> None:
        test_input = [
            [1, 2, 3]
        ]
        expected_output = \
            [[0, 0], [0, 1], [0, 2]]
        actual_output = self.solution.pacificAtlantic(test_input)
        self.compare_expected_and_actual_outputs(
            expected_output, actual_output)

    def test_all_valid(self: PacificAtlanticWaterFlowTest) -> None:
        test_input = [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1],
        ]
        expected_output = [
            [0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1],
            [2, 2]]
        actual_output = self.solution.pacificAtlantic(test_input)
        self.compare_expected_and_actual_outputs(
            expected_output, actual_output)


if __name__ == '__main__':
    unittest.main()
