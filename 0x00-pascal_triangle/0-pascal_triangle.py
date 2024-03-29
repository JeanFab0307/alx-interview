#!/usr/bin/python3
"""
Pascal triangle
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal’s triangle of n
    """
    triangle = []
    if n <= 0:
        return triangle
    for i in range(n):
        sequence = [1]
        if i == 0:
            sequence = []
        elif i == 1:
            sequence = [1]
        else:
            for j in range(len(triangle[i - 1]) - 1):
                sequence.append(triangle[i - 1][j] + triangle[i - 1][j + 1])
        sequence.append(1)
        triangle.append(sequence)
    return triangle
