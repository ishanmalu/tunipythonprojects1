"""
COMP.CS.100 Capitalization
Creator: Ishan Malu
Student id number: 154138420
"""

def capitalize_initial_letters(text):
    """
    Return a string with the first letter of each word capitalized
    and the remaining letters in lowercase.

    Parameters:
        text (str): A string that may contain one or more words.
                    Can be empty.

    Returns:
        str: The input string with each word starting with an uppercase letter
             and the rest of the letters in lowercase. Returns an empty string
             if the input is empty.
    """
    return text.title()


def main():
    """
    Ask the user for a string and print it with capitalized initial letters.
    """
    user_input = input("Enter text: ")
    result = capitalize_initial_letters(user_input)
    print(result)


if __name__ == "__main__":
    main()