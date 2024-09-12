#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
	"""
		Takes  matrix and rotate it clockwise
		Return:
		Nothing, the matrix is edited in place
	"""
	for x in range(0, int(len(matrix)/2)):
		for y in range(x ,len(matrix) - x - 1):
			temp = matrix[x][y]

			matrix[x][y] = matrix[len(matrix) - 1 - y][x]

			matrix[len(matrix) - 1 - y][x] = matrix[len(matrix) - 1 - x][len(matrix) - 1 - y]

			matrix[len(matrix) - 1 - x][len(matrix) - 1 - y] = matrix[y][len(matrix) - 1 - x]

			matrix[y][len(matrix) - 1 - x] = temp