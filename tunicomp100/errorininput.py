"""
COMP.CS.100 Error in the reading the inputs
Creator: Ishan Malu
Student id number: 154138420
"""

def read_input(prompt):
    """
    Keep asking until the user gives a positive integer.

    Args:
        prompt (str): Message shown to the user.

    Returns:
        int: The valid positive integer entered.
    """
    while True:
        user_input = input(prompt)
        try:
            value = int(user_input)
            if value > 0:
                return value
        except ValueError:
            pass  # no error message, just ask again


def main():
    width = read_input("Enter the width of a frame: ")
    height = read_input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")
    print()

    for _ in range(height):
        print(mark * width)


if __name__ == "__main__":
    main()
