"""
COMP.CS.100 Printing a Box
Creator: Ishan Malu
Student id number: 154138420
"""

def print_box(w, h, ch):
    """
    Prints a box of width w and height h using character ch.
    Parameters:
        w (int): width of the box
        h (int): height of the box
        ch (str): the print character
    """
    for _ in range(h):
        print(ch * w)


def main():
    width = int(input("Enter the width of a frame: "))
    height = int(input("Enter the height of a frame: "))
    mark = input("Enter a print mark: ")

    print()
    print_box(width, height, mark)


if __name__ == "__main__":
    main()
