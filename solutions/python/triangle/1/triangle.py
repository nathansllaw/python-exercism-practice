def isTriangle (sides):
    a, b, c = sorted(sides)
    return a > 0 and (a + b >= c)

def equilateral(sides):
    if not isTriangle(sides):
        return False

    a, b, c = sides
    return a == b == c


def isosceles(sides):
    if not isTriangle(sides):
        return False

    a, b, c = sides
    return a == b or a == c or b == c

def scalene(sides):
    if not isTriangle(sides):
        return False

    a, b, c = sides
    return a != b and a != c and b != c
        
