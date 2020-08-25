'''
Given an m x n matrix of non-negative integers representing the height of each
unit cell in a continent, the "Pacific ocean" touches the left and top edges of
the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell
to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and
Atlantic ocean.

Note:

The order of returned grid coordinates does not matter.
Both m and n are less than 150.


Example:

Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with
parentheses in above matrix).
'''
from __future__ import annotations
from typing import List
from collections import deque


class Solution:
    def pacificAtlantic(
            self: Solution,
            matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        vert_length = len(matrix)
        hor_length = len(matrix[0])

        # Matrices to track if a specific coordinate is able to reach an ocean
        pacific_matrix = [[False] * hor_length for _ in range(vert_length)]
        atlantic_matrix = [[False] * hor_length for _ in range(vert_length)]

        # Used for BST
        pacific_queue = deque()
        atlantic_queue = deque()

        # Set verticals of matrices to True and add to queues
        last_horizontal_index = hor_length - 1
        for vert_coord in range(vert_length):
            pacific_matrix[vert_coord][0] = True
            atlantic_matrix[vert_coord][-1] = True
            pacific_queue.append((vert_coord, 0))
            atlantic_queue.append((vert_coord, last_horizontal_index))

        # Set horizontals of matrices to True
        last_vertical_index = vert_length - 1
        for hor_coord in range(hor_length):
            pacific_matrix[0][hor_coord] = True
            atlantic_matrix[last_vertical_index][hor_coord] = True
            pacific_queue.append((0, hor_coord))
            atlantic_queue.append((last_vertical_index, hor_coord))

        self.mark_coord_with_access_to_ocean(
            matrix, pacific_matrix, pacific_queue)
        self.mark_coord_with_access_to_ocean(
            matrix, atlantic_matrix, atlantic_queue)

        pacific_and_antlantic_flow_coords = []
        for vert in range(vert_length):
            for hor in range(hor_length):
                if pacific_matrix[vert][hor] is True and \
                        atlantic_matrix[vert][hor] is True:
                    pacific_and_antlantic_flow_coords.append([vert, hor])

        return pacific_and_antlantic_flow_coords

    def mark_coord_with_access_to_ocean(
            self: Solution,
            ocean_val_matrix: List[List[int]],
            ocean_bool_matrix: List[List[int]],
            ocean_queue: deque) -> None:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        vert_length = len(ocean_bool_matrix)
        hor_length = len(ocean_bool_matrix[0])
        while ocean_queue:
            curr_coord = ocean_queue.popleft()
            for direction in directions:
                new_vert_coord = curr_coord[0] + direction[0]
                new_hor_coord = curr_coord[1] + direction[1]

                # Check boundaries
                if new_vert_coord < 0 or \
                        new_vert_coord >= vert_length or \
                        new_hor_coord < 0 or \
                        new_hor_coord >= hor_length:
                    continue

                # Check new coordinate height is higher than current or if
                # we've already marked the new coordinate
                curr_value = ocean_val_matrix[curr_coord[0]][curr_coord[1]]
                if (ocean_val_matrix
                        [new_vert_coord][new_hor_coord] < curr_value or
                        ocean_bool_matrix
                        [new_vert_coord][new_hor_coord]):
                    continue
                ocean_queue.append((new_vert_coord, new_hor_coord))
                ocean_bool_matrix[new_vert_coord][new_hor_coord] = True
