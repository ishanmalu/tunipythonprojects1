"""
COMP.CS.100 Tourist Dictionary
Creator: Ishan Malu
Student id number: 154138420
"""

english_spanish = {
    "hey": "hola",
    "thanks": "gracias",
    "home": "casa"
}


def word(dictionary):
    """
    Ask for a single English word and print its Spanish translation.
    """
    eng = input("Enter the word to be translated: ")
    if eng in dictionary:
        print(f"{eng} in Spanish is {dictionary[eng]}")
    else:
        print(f"The word {eng} could not be found from the dictionary.")


def add(dictionary):
    """
    Add a new word pair (English -> Spanish) into the dictionary.
    """
    eng = input("Give the word to be added in English: ")
    spa = input("Give the word to be added in Spanish: ")
    dictionary[eng] = spa


def remove(dictionary):
    """
    Remove a word from the dictionary if it exists.
    """
    eng = input("Give the word to be removed: ")
    if eng in dictionary:
        del dictionary[eng]
    else:
        print(f"The word {eng} could not be found from the dictionary.")


def print_dict(dictionary):
    """
    Print all word pairs in alphabetical order by English word.
    """
    for eng in sorted(dictionary):
        print(f"{eng} {dictionary[eng]}")


def translate_text(dictionary):
    """
    Translate an entire sentence into Spanish.
    Unknown words remain unchanged.
    """
    text = input("Enter the text to be translated into Spanish: ")
    words = text.split()
    print("The text, translated by the dictionary:")
    translated = [
        dictionary[word] if word in dictionary else word
        for word in words
    ]
    print(" ".join(translated))


def main():
    while True:
        command = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ").upper()
        if command == "W":
            word(english_spanish)
        elif command == "A":
            add(english_spanish)
        elif command == "R":
            remove(english_spanish)
        elif command == "P":
            print_dict(english_spanish)
        elif command == "T":
            translate_text(english_spanish)
        elif command == "Q":
            print("Adios!")
            break


if __name__ == "__main__":
    main()