"""
COMP.CS.100 Old MacDonald had a farm
Creator: Ishan Malu
Student id number: 154138420
"""

def print_verse(animal, sound):
    """
    Prints one verse of the song 'Old MACDONALD had a farm'.

    :param animal: Name of the animal (string)
    :param sound: Sound the animal makes (string)
    """
    print("Old MACDONALD had a farm")
    print("E-I-E-I-O")
    print(f"And on his farm he had a {animal}")
    print("E-I-E-I-O")
    print(f"With a {sound} {sound} here")
    print(f"And a {sound} {sound} there")
    print(f"Here a {sound}, there a {sound}")
    print(f"Everywhere a {sound} {sound}")
    print("Old MacDonald had a farm")
    print("E-I-E-I-O")


def main():
    animals = [("cow", "moo"),
               ("pig", "oink"),
               ("duck", "quack"),
               ("horse", "neigh"),
               ("lamb", "baa")]

    for i, (animal, sound) in enumerate(animals):
        print_verse(animal, sound)
        if i < len(animals) - 1:
            print()


if __name__ == "__main__":
    main()