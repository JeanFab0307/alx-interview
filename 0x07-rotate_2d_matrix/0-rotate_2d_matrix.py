#!/usr/bin/python3
"""Rotate 2D Matrix."""


def rotate_2d_matrix(matrix):
    """
    Takes matrix and rotate it clockwise
    Return:
    Nothing, the matrix is edited in place
    """
    size = len(matrix)
    for x in range(0, int(size/2)):
        for y in range(x, size - x - 1):
            temp = matrix[x][y]

            matrix[x][y] = matrix[size - 1 - y][x]

            matrix[size - 1 - y][x] = matrix[size - 1 - x][size - 1 - y]

            matrix[size - 1 - x][size - 1 - y] = matrix[y][size - 1 - x]

            matrix[y][size - 1 - x] = temp
