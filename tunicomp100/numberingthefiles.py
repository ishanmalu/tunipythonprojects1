"""
COMP.CS.100 Numbering the file lines
Creator: Ishan Malu
Student id number: 154138420
"""

def main():
    filename = input("Enter the name of the file: ")

    try:
        with open(filename, "r") as file:
            for line_number, line in enumerate(file, start=1):
                print(f"{line_number} {line.rstrip()}")

    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")

if __name__ == "__main__":
    main()