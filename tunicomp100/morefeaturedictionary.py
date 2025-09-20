"""
COMP.CS.100 More features dictionary
Creator: Ishan Malu
Student id number: 154138420
"""

english_spanish = {
    "hey": "hola",
    "thanks": "gracias",
    "home": "casa"
}


def print_contents(dictionary):
    """Print the dictionary contents in alphabetical order, separated by commas."""
    words = ", ".join(sorted(dictionary))
    print(f"Dictionary contents:\n{words}")


def translate_word(dictionary):
    """Translate a single word."""
    word = input("Enter the word to be translated: ")
    if word in dictionary:
        print(f"{word} in Spanish is {dictionary[word]}")
    else:
        print(f"The word {word} could not be found from the dictionary.")


def add_word(dictionary):
    """Add a new English→Spanish word pair and show updated contents."""
    eng = input("Give the word to be added in English: ")
    spa = input("Give the word to be added in Spanish: ")
    dictionary[eng] = spa
    print_contents(dictionary)


def remove_word(dictionary):
    """Remove a word from the dictionary."""
    eng = input("Give the word to be removed: ")
    if eng in dictionary:
        del dictionary[eng]
    else:
        print(f"The word {eng} could not be found from the dictionary.")


def print_dictionary(dictionary):
    """Print all word pairs alphabetically by English word."""
    for eng in sorted(dictionary):
        print(f"{eng} {dictionary[eng]}")


def translate_sentence(dictionary):
    """Translate an entire sentence, leaving unknown words as-is."""
    text = input("Enter the text to be translated into Spanish: ")
    words = text.split()
    print("The text, translated by the dictionary:")
    translated = [dictionary[w] if w in dictionary else w for w in words]
    print(" ".join(translated))


def main():
    # Show initial contents
    print_contents(english_spanish)

    while True:
        choice = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ").upper()
        if choice == "W":
            translate_word(english_spanish)
        elif choice == "A":
            add_word(english_spanish)
        elif choice == "R":
            remove_word(english_spanish)
        elif choice == "P":
            print_dictionary(english_spanish)
        elif choice == "T":
            translate_sentence(english_spanish)
        elif choice == "Q":
            print("Adios!")
            break


if __name__ == "__main__":
    main()