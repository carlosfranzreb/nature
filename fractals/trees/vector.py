"""
This time for 2D vectors
"""


import math


class Vector:
    def get_xy(v):
        return [v[1][0] - v[0][0], v[1][1] - v[0][1]]

    def rotate(v, angle):  # rotates counterclockwise
        radians = math.radians(angle)
        x, y = Vector.get_xy(v)
        new_x = x*math.cos(radians) - y*math.sin(radians)
        new_y = x*math.sin(radians) + y*math.cos(radians)
        return [v[0], [v[0][0] + new_x, v[0][1] + new_y]]

    def mag(v):
        x, y = Vector.get_xy(v)
        return (x**2 + y**2)**0.5

    def neg(v):
        x, y = Vector.get_xy(v)
        return [v[0], [v[0][0] - x, v[0][1] - y]]

    def div(v, n):
        x, y = Vector.get_xy(v)
        new_end = [x/n, y/n]
        return [v[0], [v[0][0]+new_end[0], v[0][1]+new_end[1]]]

    def sub(a, b):
        return Vector.add(a, Vector.neg(b))

    def add(a, b):
        if a[0] != b[0]:
            raise ValueError("Vectors don't have the same starting pos.")
        else:
            a_x, a_y = Vector.get_xy(a)
            return [a[0], [a_x+b[1][0], a_y+b[1][1]]]

    def move(a, b):
        if a[0] != b[0]:
            raise ValueError("Vectors don't have the same starting pos.")
        else:
            b_x, b_y = Vector.get_xy(b)
            v = []
            for pos in a:
                v.append([pos[0] + b_x, pos[1] + b_y])
            return v
