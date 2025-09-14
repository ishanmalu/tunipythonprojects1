"""
COMP.CS.100 Forming an acronym
Creator: Ishan Malu
Student id number: 154138420
"""

def create_an_acronym(name):
    """
    Create an acronym from a given name.

    Parameters:
        name (str): A string containing one or more words separated by spaces.

    Returns:
        str: A string that is the acronym formed by the first letter of each word,
             all capitalized.
    """
    words = name.split()
    acronym = "".join(word[0].upper() for word in words)
    return acronym


def main():
    text = input("Enter a name: ")
    result = create_an_acronym(text)
    print(result)


if __name__ == "__main__":
    main()