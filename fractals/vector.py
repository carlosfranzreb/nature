import math


class Vector:
    def norm(v):
        try:
            max_ = max(v)
            min_ = abs(min(v))
            if max_ >= min_:
                return [i / max_ for i in v]
            elif max_ < min_:
                return [i / min_ for i in v]
        except ZeroDivisionError:
            return v

    def rotate(v, angle):  # rotates counterclockwise
        radians = math.radians(angle)
        x = v[0]*math.cos(radians) - v[1]*math.sin(radians)
        y = v[0]*math.sin(radians) + v[1]*math.cos(radians)
        return [x, y]

    def mag(v):
        return (v[0]**2 + v[1]**2)**0.5

    def div(start, end, n):
        new_end = [i / n for i in Vector.sub(end, start)]
        return [start, Vector.add(start, new_end)]

    def sub(a, b):
        if len(a) != len(b):
            raise ValueError("Vectors do not have the same length")
        else:
            return [a[i] - b[i] for i in range(len(a))]

    def add(a, b):
        if len(a) != len(b):
            raise ValueError("Vectors do not have the same length")
        else:
            return [a[i] + b[i] for i in range(len(a))]

    def dot(a, b):
        if len(a) != len(b):
            raise ValueError("Vectors do not have the same length")
        else:
            return sum([a[i] * b[i] for i in range(len(a))])
