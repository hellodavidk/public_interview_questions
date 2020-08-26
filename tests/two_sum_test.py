from __future__ import annotations
import unittest

from solutions.two_sum_solution import Solution


class TwoSumTests(unittest.TestCase):
    def setUp(self: TwoSumTests) -> None:
        self.solution = Solution()

    def tearDown(self: TwoSumTests) -> None:
        pass

    def test_two_nums(self: TwoSumTests) -> None:
        list_of_nums = [1, 2]
        target = 3
        expected = [0, 1]
        answer = self.solution.two_sum(list_of_nums, target)
        self.assertEqual(sorted(answer), expected)

    def test_solution_at_front(self: TwoSumTests) -> None:
        list_of_nums = [1, 2, 4]
        target = 3
        expected = [0, 1]
        answer = self.solution.two_sum(list_of_nums, target)
        self.assertEqual(sorted(answer), expected)

    def test_solution_at_end(self: TwoSumTests) -> None:
        list_of_nums = [1, 2, 4]
        target = 6
        expected = [1, 2]
        answer = self.solution.two_sum(list_of_nums, target)
        self.assertEqual(sorted(answer), expected)

    def test_solution_split(self: TwoSumTests) -> None:
        list_of_nums = [1, 2, 4]
        target = 5
        expected = [0, 2]
        answer = self.solution.two_sum(list_of_nums, target)
        self.assertEqual(sorted(answer), expected)

    def test_negatives(self: TwoSumTests) -> None:
        list_of_nums = [-1, -2, -4]
        target = -5
        expected = [0, 2]
        answer = self.solution.two_sum(list_of_nums, target)
        self.assertEqual(sorted(answer), expected)

    def test_negatives_and_postives(self: TwoSumTests) -> None:
        list_of_nums = [-1, 2, 4]
        target = 3
        expected = [0, 2]
        answer = self.solution.two_sum(list_of_nums, target)
        self.assertEqual(sorted(answer), expected)

    def test_unsorted(self: TwoSumTests) -> None:
        list_of_nums = [3, 2, 4]
        target = 7
        expected = [0, 2]
        answer = self.solution.two_sum(list_of_nums, target)
        self.assertEqual(sorted(answer), expected)

    def test_reverse_order(self: TwoSumTests) -> None:
        list_of_nums = [4, 3, 2]
        target = 7
        expected = [0, 1]
        answer = self.solution.two_sum(list_of_nums, target)
        self.assertEqual(sorted(answer), expected)

    def test_solution_in_list(self: TwoSumTests) -> None:
        list_of_nums = [1, 2, 3]
        target = 3
        expected = [0, 1]
        answer = self.solution.two_sum(list_of_nums, target)
        self.assertEqual(sorted(answer), expected)


if __name__ == '__main__':
    unittest.main()
