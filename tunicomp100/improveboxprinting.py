"""
COMP.CS.100 Improve Box Printing
Creator: Ishan Malu
Student id number: 154138420
"""

def print_box(width, height, border_mark="#", inner_mark=" "):
    """
    Print a box of size width x height.
    border_mark is used for the border,
    inner_mark for the inside.
    """
    w = int(width)
    h = int(height)

    for row in range(h):
        for col in range(w):
            # Top or bottom row → border
            if row == 0 or row == h - 1 or col == 0 or col == w - 1:
                print(border_mark, end="")
            else:
                print(inner_mark, end="")
        print()  # newline at end of each row


def main():
    print_box(5, 4)
    print_box(3, 8, "*")
    print_box(5, 4, "O", "o")
    print_box(inner_mark=".", border_mark="O", height=4, width=6)


if __name__ == "__main__":
    main()
