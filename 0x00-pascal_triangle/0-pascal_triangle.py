#!/usr/bin/python3
"""
pascal_triangle
"""


def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to the nth row.

    Args:
    n (int): The number of rows.

    Returns:
    list: A list of lists representing Pascal's Triangle.
    """
    if n <= 0:
        return []

    res = [[1]]

    for i in range(1, n):
        tmp = [0] + res[-1] + [0]
        row = []
        for j in range(len(tmp) - 1):
            row.append(tmp[j] + tmp[j + 1])
        res.append(row)
    return res
