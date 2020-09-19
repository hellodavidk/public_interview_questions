from __future__ import annotations
import unittest
from solutions.island_size_solution import IslandSize


class IslandSizeTests(unittest.TestCase):

    def setUp(self: IslandSizeTests) -> None:
        self.island_size = IslandSize()

    def tearDown(self: IslandSizeTests) -> None:
        pass

    def test_simple(self: IslandSizeTests) -> None:
        islands_map = [
            [1, 1, 1, 2, 2, 2, 3, 3, 3],
            [1, 1, 1, 2, 2, 2, 3, 3, 3],
            [1, 1, 1, 2, 2, 2, 3, 3, 3],
            [1, 1, 1, 2, 2, 2, 3, 3, 3],
            [1, 1, 1, 2, 2, 2, 3, 3, 3],
        ]
        ret_val = self.island_size.get_size_islands(islands_map)
        expected_val = {
            '1': [15],
            '2': [15],
            '3': [15]
        }
        self.assertEqual(ret_val, expected_val)

    def test_surrounded(self: IslandSizeTests) -> None:
        islands_map = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 2, 2, 2, 2, 2, 2, 2, 1],
            [1, 2, 3, 3, 3, 3, 3, 2, 1],
            [1, 2, 2, 2, 2, 2, 2, 2, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]
        ret_val = self.island_size.get_size_islands(islands_map)
        expected_val = {
            '1': [24],
            '2': [16],
            '3': [5]
        }
        self.assertEqual(ret_val, expected_val)

    def test_one_column_one_island(self: IslandSizeTests) -> None:
        islands_map = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]
        ret_val = self.island_size.get_size_islands(islands_map)
        expected_val = {
            '1': [9]
        }
        self.assertEqual(ret_val, expected_val)

    def test_one_column_two_island(self: IslandSizeTests) -> None:
        islands_map = [
            [1, 1, 1, 1, 2, 2, 2, 2, 2],
        ]
        ret_val = self.island_size.get_size_islands(islands_map)
        expected_val = {
            '1': [4],
            '2': [5]
        }
        self.assertEqual(ret_val, expected_val)

    def test_one_column_different_island(self: IslandSizeTests) -> None:
        islands_map = [
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
        ]
        ret_val = self.island_size.get_size_islands(islands_map)
        expected_val = {
            '1': [1],
            '2': [1],
            '3': [1],
            '4': [1],
            '5': [1],
            '6': [1],
            '7': [1],
            '8': [1],
            '9': [1]
        }
        self.assertEqual(ret_val, expected_val)

    def test_one_row_one_island(self: IslandSizeTests) -> None:
        islands_map = [
            [1],
            [1],
            [1],
            [1],
            [1],
            [1],
            [1]
        ]
        ret_val = self.island_size.get_size_islands(islands_map)
        expected_val = {
            '1': [7]
        }
        self.assertEqual(ret_val, expected_val)

    def test_one_row_two_island(self: IslandSizeTests) -> None:
        islands_map = [
            [1],
            [1],
            [1],
            [2],
            [2],
            [2],
            [2]
        ]
        ret_val = self.island_size.get_size_islands(islands_map)
        expected_val = {
            '1': [3],
            '2': [4]
        }
        self.assertEqual(ret_val, expected_val)

    def test_one_row_different_island(self: IslandSizeTests) -> None:
        islands_map = [
            [1],
            [2],
            [3],
            [4],
            [5],
            [6],
            [7]
        ]
        ret_val = self.island_size.get_size_islands(islands_map)
        expected_val = {
            '1': [1],
            '2': [1],
            '3': [1],
            '4': [1],
            '5': [1],
            '6': [1],
            '7': [1],
        }
        self.assertEqual(ret_val, expected_val)

    def test_no_same_islands(self: IslandSizeTests) -> None:
        islands_map = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]
        ret_val = self.island_size.get_size_islands(islands_map)
        expected_val = {
            '1': [1],
            '2': [1],
            '3': [1],
            '4': [1],
            '5': [1],
            '6': [1],
            '7': [1],
            '8': [1],
            '9': [1]
        }
        self.assertEqual(ret_val, expected_val)

    def test_all_same_islands(self: IslandSizeTests) -> None:
        islands_map = [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1],
        ]
        ret_val = self.island_size.get_size_islands(islands_map)
        expected_val = {
            '1': [9]
        }
        self.assertEqual(ret_val, expected_val)

    def test_no_islands(self: IslandSizeTests) -> None:
        islands_map = [[]]
        ret_val = self.island_size.get_size_islands(islands_map)
        expected_val = {}
        self.assertEqual(ret_val, expected_val)

    def test_diagonal_islands(self: IslandSizeTests) -> None:
        islands_map = [
            [1, 2, 2],
            [2, 1, 2],
            [2, 2, 1],
        ]
        ret_val = self.island_size.get_size_islands(islands_map)
        expected_val = {
            '1': [1, 1, 1],
            '2': [3, 3]
        }
        self.assertEqual(ret_val, expected_val)

    def test_multiple_islands(self: IslandSizeTests) -> None:
        islands_map = [
            [1, 2, 2, 1, 1, 1],
            [2, 1, 2, 2, 2, 2],
            [2, 2, 1, 3, 3, 3],
        ]
        ret_val = self.island_size.get_size_islands(islands_map)
        expected_val = {
            '1': [1, 1, 1, 3],
            '2': [3, 6],
            '3': [3]
        }
        self.assertEqual(ret_val, expected_val)

    def test_checkered_islands(self: IslandSizeTests) -> None:
        islands_map = [
            [1, 2, 1, 2, 1, 2],
            [2, 1, 2, 1, 2, 1],
            [1, 2, 1, 2, 1, 2]
        ]
        ret_val = self.island_size.get_size_islands(islands_map)
        expected_val = {
            '1': [1, 1, 1, 1, 1, 1, 1, 1, 1],
            '2': [1, 1, 1, 1, 1, 1, 1, 1, 1]
        }
        self.assertEqual(ret_val, expected_val)


# class IslandSizeWrapTests(unittest.TestCase):

#     def setUp(self: IslandSizeTests) -> None:
#         self.island_size = IslandSize()

#     def tearDown(self: IslandSizeTests) -> None:
#         pass

#     def test_corners_islands(self: IslandSizeTests) -> None:
#         islands_map = [
#             [1, 2, 1],
#             [2, 2, 2],
#             [1, 2, 1]
#         ]
#         ret_val = self.island_size.get_size_islands(islands_map)
#         expected_val = {
#             '1': [4],
#             '2': [5]
#         }
#         self.assertEqual(ret_val, expected_val)

#     def test_no_corners_islands(self: IslandSizeTests) -> None:
#         islands_map = [
#             [1, 2, 3],
#             [2, 2, 2],
#             [3, 2, 1]
#         ]
#         ret_val = self.island_size.get_size_islands(islands_map)
#         expected_val = {
#             '1': [1, 1],
#             '2': [5],
#             '3': [1, 1]
#         }
#         self.assertEqual(ret_val, expected_val)


if __name__ == '__main__':
    unittest.main()
