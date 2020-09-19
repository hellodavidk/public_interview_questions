'''
Given a 2d array of integers, return a dictionary with a key value pair in the
following format:

islands = {
    '1': [3, 4, 5]
    '2': [4, 5, 6]
}
The key represents the integer that makes up the island(s).
The value represents the size of each island group in a list in ascending
order by island size.

An island consists of any size group of the same integer that is connected to
the same integer from the top, bottom, left, or right.  Integers that are
connected diagonally are not in the same island.

Ex:
The following 2d array
islands_map = [
    [1, 1, 1, 2, 2, 2, 3, 3, 3],
    [1, 1, 1, 2, 2, 2, 3, 3, 3],
    [1, 1, 1, 2, 2, 2, 3, 3, 3],
    [1, 1, 1, 2, 2, 2, 3, 3, 3],
    [1, 1, 1, 2, 2, 2, 3, 3, 3],
]
would return the following:
return_valu = {
    '1': [15],
    '2': [15],
    '3': [15]
}

Ex 2:
The following 2d array
islands_map = [
    [1, 1, 2],
    [1, 3, 2],
    [1, 2, 3]
]
would return the following:
return_value = {
    '1': [4],
    '2': [1, 2],
    '3': [1, 1]
}
'''
from __future__ import annotations
from typing import List, Dict


class IslandSize():

    def get_size_islands(self: IslandSize,
                         islands_map: List[List[int]]) -> Dict:
        island_size = {}
        for col in range(len(islands_map)):
            for row in range(len(islands_map[0])):
                current_num = islands_map[col][row]
                if current_num != -1:
                    current_count = 0
                    current_count = self.mark_island(
                        islands_map, col, row, current_count, current_num)
                    if str(current_num) in island_size:
                        island_size[str(current_num)].append(current_count)
                    else:
                        island_size[str(current_num)] = [current_count]
        for val in island_size.values():
            val.sort()
        return island_size

    def mark_island(self: IslandSize,
                    islands_map: List[List[int]],
                    col: int,
                    row: int,
                    current_count: int,
                    current_num: int) -> int:
        if islands_map[col][row] == current_num:
            current_count += 1
            islands_map[col][row] = -1

            if row > 0:
                current_count = self.mark_island(
                    islands_map, col, row - 1, current_count, current_num)
            if row < len(islands_map[0]) - 1:
                current_count = self.mark_island(
                    islands_map, col, row + 1, current_count, current_num)
            if col > 0:
                current_count = self.mark_island(
                    islands_map, col - 1, row, current_count, current_num)
            if col < len(islands_map) - 1:
                current_count = self.mark_island(
                    islands_map, col + 1, row, current_count, current_num)
        return current_count
