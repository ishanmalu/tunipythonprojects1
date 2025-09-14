"""
COMP.CS.100 ROT-13
Creator: Ishan Malu
Student id number: 154138420
"""

def encrypt(char):
    """
    Perform ROT-13 encryption for a single character.

    Parameters:
        char (str): A single character to be encrypted.

    Returns:
        str: The ROT-13 encrypted character. If the character is not
             a letter, it is returned unchanged.
    """
    if 'a' <= char <= 'z':
        return chr(((ord(char) - ord('a') + 13) % 26) + ord('a'))
    elif 'A' <= char <= 'Z':
        return chr(((ord(char) - ord('A') + 13) % 26) + ord('A'))
    else:
        return char


def row_encryption(text):
    """
    Perform ROT-13 encryption for an entire string.

    Parameters:
        text (str): A string of any length.

    Returns:
        str: The ROT-13 encrypted version of the string. Non-alphabetic
             characters remain unchanged. Returns an empty string if input is empty.
    """
    encrypted_text = ""
    for char in text:
        encrypted_text += encrypt(char)
    return encrypted_text


def main():
    """
    Ask the user for a string and print its ROT-13 encrypted version.
    """
    user_input = input("Enter text to encrypt: ")
    result = row_encryption(user_input)
    print(result)


if __name__ == "__main__":
    main()