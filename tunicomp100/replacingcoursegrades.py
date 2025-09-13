"""
COMP.CS.100 Replacing Course Grades
Creator: Ishan Malu
Student id number: 154138420
"""


def convert_grades(list):
    """
    determines pass or fail in course

    """
    for x in range(0, len(list), 1):
        if list[x] > 0:
            list[x] = 6


def main():
    grades = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0]
    convert_grades(grades)
    print(grades)  # Should print [0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0]


if __name__ == "__main__":
    main()