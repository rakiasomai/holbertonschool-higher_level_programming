#!/usr/bin/python3


def pascal_triangle(n):

    if n <= 0:
        return []

    triangle = [[1]]
    for y in range(1, n):
        row = [1]
        for z in range(1, y):
            elem = triangle[y-1][z-1] + triangle[y-1][z]
            print(elem)
            row.append(elem)
        row.append(1)
        triangle.append(row)
    return triangle
