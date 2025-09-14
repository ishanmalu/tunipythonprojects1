"""
COMP.CS.100 Saving a message
Creator: Ishan Malu
Student id number: 154138420

This program reads several lines of text from the user,
stores them in a list, and then prints them in ALL CAPS.
"""


def read_message():
    """
    Reads lines of text from the user and returns them as a list.

    The user ends the input by giving an empty line, which is
    not included in the returned list.

    Returns:
        list[str]: Lines of text entered by the user.
    """
    rows = []
    while True:
        line = input()
        if line == "":
            break
        rows.append(line)
    return rows


def main():
    """
    Main program:
    - Prompts the user for text rows.
    - Prints them back in all capital letters.
    """
    print("Enter text rows to the message. Quit by entering an empty row.")
    rows = read_message()
    print("The same, shouting:")
    for row in rows:
        print(row.upper())


if __name__ == "__main__":
    main()
