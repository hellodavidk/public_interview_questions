from __future__ import annotations
from typing import List
import unittest

from solutions.three_sum_solution import Solution


class ThreeSumTest(unittest.TestCase):
    def setUp(self: ThreeSumTest) -> None:
        self.solution = Solution()

    def tearDown(self: ThreeSumTest) -> None:
        pass

    def compare_nested_lists(
            self: ThreeSumTest,
            expected_output: List[List[int]],
            actual_output: List[List[int]]) -> None:
        self.sort_answer_combos(expected_output)
        self.sort_answer_combos(actual_output)
        self.assertEqual(expected_output, actual_output)

    def sort_answer_combos(
            self: ThreeSumTest, answer_list: List[List[int]]) -> None:
        for answer_combo in answer_list:
            answer_combo.sort()
        answer_list.sort()

    def test_example(self: ThreeSumTest) -> None:
        test_input = [-1, 0, 1, 2, -1, -4]
        expected_output = [
            [-1, 0, 1],
            [-1, -1, 2]
        ]
        actual_output = self.solution.threeSum(test_input)
        self.compare_nested_lists(expected_output, actual_output)

    def test_no_solution(self: ThreeSumTest) -> None:
        test_input = [-1, 0, 2]
        expected_output = []
        actual_output = self.solution.threeSum(test_input)
        self.compare_nested_lists(expected_output, actual_output)

    def test_duplicate_answers_separated(self: ThreeSumTest) -> None:
        test_input = [-1, -1, 2, -1, -1, 2]
        expected_output = [[-1, -1, 2]]
        actual_output = self.solution.threeSum(test_input)
        self.compare_nested_lists(expected_output, actual_output)

    def test_duplicate_answers_together(self: ThreeSumTest) -> None:
        test_input = [-1, -1, -1, -1, 2, 2]
        expected_output = [[-1, -1, 2]]
        actual_output = self.solution.threeSum(test_input)
        self.compare_nested_lists(expected_output, actual_output)

    def test_first_three(self: ThreeSumTest) -> None:
        test_input = [-1, -1, 2, 3]
        expected_output = [[-1, -1, 2]]
        actual_output = self.solution.threeSum(test_input)
        self.compare_nested_lists(expected_output, actual_output)

    def test_middle_three(self: ThreeSumTest) -> None:
        test_input = [-2, -1, 0, 1, 4]
        expected_output = [[-1, 0, 1]]
        actual_output = self.solution.threeSum(test_input)
        self.compare_nested_lists(expected_output, actual_output)

    def test_last_three(self: ThreeSumTest) -> None:
        test_input = [-4, -1, 0, 1]
        expected_output = [[-1, 0, 1]]
        actual_output = self.solution.threeSum(test_input)
        self.compare_nested_lists(expected_output, actual_output)

    def test_use_elements_multiple_times(self: ThreeSumTest) -> None:
        test_input = [-2, -1, 0, 1, 2, 3]
        expected_output = [
            [-2, -1, 3],
            [-2, 0, 2],
            [-1, 0, 1],
        ]
        actual_output = self.solution.threeSum(test_input)
        self.compare_nested_lists(expected_output, actual_output)


if __name__ == '__main__':
    unittest.main()
