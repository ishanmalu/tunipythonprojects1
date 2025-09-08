"""
COMP.CS.100 Yogi Bear
Creator: Ishan Malu
Student id number: 154138420
"""


def repeat_name(name, timesStr):
    """
    This is the repeat name function which repeats names.
    Parameter: name and number of repeats.
    No return value, just prints.
    """
    times = int(timesStr)
    while times:
        print(name, ", ", name, " Bear", sep="")
        times -= 1


def verse(firstLine, secondLine):
    """
    This function prints a verse of the song.
    Parameters:
        firstLine: the first line of the verse
        secondLine: the name that gets repeated
    """
    print(firstLine)
    print(secondLine, ", ", secondLine, sep="")
    print(firstLine)
    repeat_name(secondLine, 3)
    print(firstLine)
    repeat_name(secondLine, 1)


def main():
    verse("I know someone you don't know", "Yogi")
    print()
    verse("Yogi has a best friend too", "Boo Boo")
    print()
    verse("Yogi has a sweet girlfriend", "Cindy")


if __name__ == "__main__":
    main()
    