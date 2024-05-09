#!/usr/bin/python3
"""
island_perimeter function
"""


def island_perimeter(grid):
    """ returns the perimeter of the island described in grid"""
    perimeter = 0
    first = True
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                perimeter += 4 if first else 3
                first = False
                if grid[i - 1][j] and grid[i - 1][j] == 1:
                    perimeter -= 1
                if grid[i][j - 1] and grid[i][j - 1] == 1:
                    perimeter -= 1
    return perimeter
