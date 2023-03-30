#!/usr/bin/python3
"""Function that returns the perimeter of an island"""


def island_perimeter(grid):
    """
    Input: List of lists
    Returns: Perimeter of the island
    """
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                perimeter += 4
                # cells with 2 sides touching other cells on top & bottom
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                # cells with 2 sides touching other cells left & right
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter
