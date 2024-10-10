#!/usr/bin/python3
""" 0. Island Perimeter """


def island_perimeter(grid):
    """returns the perimeter of the island described in grid
    """
    rows = len(grid)
    colunms = len(grid[0]) if grid else 0
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4

                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2

                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2
    return perimeter
