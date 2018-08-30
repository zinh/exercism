def is_equilateral(sides):
    if not valid_triangle(sides):
        return False
    return sides[0] == sides[1] and sides[1] == sides[2]

def is_isosceles(sides):
    if not valid_triangle(sides):
        return False
    return sides[0] == sides[1] or sides[1] == sides[2] or sides[2] == sides[0]

def is_scalene(sides):
    if not valid_triangle(sides):
        return False
    return not is_equilateral(sides) and not is_isosceles(sides)

def valid_triangle(sides):
    return all(side != 0 for side in sides) and all([sides[idx[0]] + sides[idx[1]] >= sides[idx[2]]for idx in [(0,1,2), (1, 2,0), (2, 0, 1)]])
