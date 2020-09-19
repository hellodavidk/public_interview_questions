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


class IslandSize():

    def get_size_islands(self, islands_map):
        pass
