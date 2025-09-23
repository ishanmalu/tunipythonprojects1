"""
COMP.CS.100 Writing numbered lines to a file
Creator: Ishan Malu
Student id number: 154138420
"""

"""
Program that writes user input into a file with line numbers.
Author: Your Name
"""

def read_message():
    """
    Reads the text entered by the user.
    list: A list of strings. Each line is a text entered by the user
    """
    print("Enter rows of text. Quit by entering an empty row.")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    return lines


def main():
    """
   Asks for a filename, saves the users text with line numbers,
   and prints success or error if writing fails.
    """
    filename = input("Enter the name of the file: ")

    try:
        with open(filename, "w") as file:
            lines = read_message()
            for index, line in enumerate(lines, start=1):
                file.write(f"{index} {line}\n")

        print(f"File {filename} has been written.")
    except:
        print(f"Writing the file {filename} was not successful.")


if __name__ == "__main__":
    main()
