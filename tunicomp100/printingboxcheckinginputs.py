"""
COMP.CS.100 Printing a Box and checking the inputs
Creator: Ishan Malu
Student id number: 154138420
"""


def read_input(prompt):
    """
    Asks the user to enter a positive integer.

    Parameters:
        prompt (str): the text shown to the user

    Returns:
        int: the first positive integer entered by the user
    """
    while True:
        value = int(input(prompt))
        if value > 0:
            return value


def print_box(w, h, ch):
    """
    Prints a box of width w and height h using character ch.

    Parameters:
        w (int): width of the box
        h (int): height of the box
        ch (str): character used for printing
    """
    for _ in range(h):
        print(ch * w)


def main():
    width = read_input("Enter the width of a frame: ")
    height = read_input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")

    print()
    print_box(width, height, mark)


if __name__ == "__main__":
    main()
