"""
COMP.CS.100 Triangles Area
Creator: Ishan Malu
Student id number: 154138420
"""

from math import sqrt

def area(a, b, c):
    """
    Calculate the area of a triangle using Heron's formula.

    Parameters:
        a (float): length of the first side
        b (float): length of the second side
        c (float): length of the third side

    Returns:
        float: the area of the triangle
    """
    s = (a + b + c) / 2
    x = (s - a) * (s - b) * (s - c)
    ar = sqrt(s * x)
    return ar


def main():
    """
    Ask the user for the lengths of the sides of a triangle,
    compute the area using Heron's formula, and print it.
    """
    firstSide = float(input("Enter the length of the first side: "))
    secondSide = float(input("Enter the length of the second side: "))
    thirdSide = float(input("Enter the length of the third side: "))
    areaOfTri = area(firstSide, secondSide, thirdSide)
    print(f"The triangle's area is {areaOfTri:.1f}")


if __name__ == "__main__":
    main()
