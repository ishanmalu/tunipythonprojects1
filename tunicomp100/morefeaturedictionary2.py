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


def print_contents(dictionary):
    """Print dictionary contents (English keys) as a comma-separated list."""
    words = ", ".join(sorted(dictionary))
    print(f"Dictionary contents:\n{words}")


def translate_word(dictionary):
    """Translate a single English word."""
    word = input("Enter the word to be translated: ")
    if word in dictionary:
        print(f"{word} in Spanish is {dictionary[word]}")
    else:
        print(f"The word {word} could not be found from the dictionary.")


def add_word(dictionary):
    """Add a new English→Spanish pair and show updated contents."""
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
    """Print all word pairs in two orders: English→Spanish and Spanish→English."""
    print()
    print("English-Spanish")
    for eng in sorted(dictionary):
        print(f"{eng} {dictionary[eng]}")

    # Build Spanish→English mapping
    spanish_english = {spa: eng for eng, spa in dictionary.items()}

    print()
    print("Spanish-English")
    for spa in sorted(spanish_english):
        print(f"{spa} {spanish_english[spa]}")
    print()


def translate_sentence(dictionary):
    """Translate a sentence, leaving unknown words as-is."""
    text = input("Enter the text to be translated into Spanish: ")
    words = text.split()
    translated = [dictionary[w] if w in dictionary else w for w in words]
    print("The text, translated by the dictionary:")
    print(" ".join(translated))


def main():
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