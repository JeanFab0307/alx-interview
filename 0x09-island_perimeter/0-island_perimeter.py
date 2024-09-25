#!/usr/bin/python3
"""Island perimeter"""


def island_perimeter(grid):
    """
    Return:
        the perimeter of the island described in grid
    """
    perimeter = 0
    first = False
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                perimeter += 3

                if first is False:
                    first = True
                    perimeter += 1

                if grid[i - 1][j] and i - 1 >= 0:
                    perimeter -= 1

                if grid[i][j - 1] and j - 1 >= 0:
                    perimeter -= 1

                if grid[i - 1][j - 1] and grid[i][j - 1] and
                grid[i - 1][j] and i - 1 >= 0 and j - 1 >= 0:
                    perimeter -= 1

    return perimeter
