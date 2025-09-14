"""
COMP.CS.100 ROT-13 Encryption for a Whole Message
Creator: Ishan Malu
Student id number: 154138420
"""


def encrypt(char):
    """
    Encrypt a single character with ROT13.
    Non-alphabetic characters stay the same.
    """
    if "a" <= char <= "z":
        return chr((ord(char) - ord("a") + 13) % 26 + ord("a"))
    if "A" <= char <= "Z":
        return chr((ord(char) - ord("A") + 13) % 26 + ord("A"))
    return char


def row_encryption(text):
    """
    Apply ROT13 to an entire line.
    """
    return "".join(encrypt(c) for c in text)


def read_message():
    """
    Read user input lines until an empty line is entered.
    Return them as a list (without the empty line).
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
    Ask the user for a message, then print it encrypted with ROT13.
    """
    print("Enter text rows to the message. Quit by entering an empty row.")
    rows = read_message()

    print("ROT13:")
    for row in rows:
        print(row_encryption(row))


if __name__ == "__main__":
    main()