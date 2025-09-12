"""
COMP.CS.100 Bored Improved
Creator: Ishan Malu
Student id number: 154138420
"""

EPSILON = 0.000000001

def compare_floats(a,b,c):
    """
    comparing two floating point values
    :param a: a float value, one number
    :param b: a float value,  one number
    :param c: a float value, the acceptable margin
    :return: boolean, if they are same then true else false
    """
    if abs(a-b) < c:
        return True
    else:
        return False

def main():
    pass

if __name__ == "__main__":
    main()