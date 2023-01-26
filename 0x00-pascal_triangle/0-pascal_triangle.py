#!/usr/bin/python3
"""
Pascal's Triangle
"""


def pascal_triangle(n):
    """
    A list of lists of integers representing Pascal's triangle

    Attributes:
        n (int): no. of rows of Pascal's triangle
    Return:
        (list of lists of ints): repr. of Pascal's triangle
    """
    if type(n) is not int:
        raise TypeError("n must be integer")
    triangle = []
    if n <= 0:
        return triangle
    fig = [1]
    for row_index in range(n):
        rowlist = []
        if row_index == 0:
            rowlist = [1]
        else:
            for i in range(row_index + 1):
                if i == 0:
                    rowlist.append(0 + fig[i])
                elif i == (row_index):
                    rowlist.append(fig[i - 1] + 0)
                else:
                    rowlist.append(fig[i - 1] + fig[i])
        fig = rowlist
        triangle.append(rowlist)
    return triangle
