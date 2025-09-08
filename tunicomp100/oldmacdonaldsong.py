"""
COMP.CS.100 Old MacDonald had a farm
Creator: Ishan Malu
Student id number: 154138420
"""

def print_verse(x,y):
    """
    This is the function which prints the song
    :param x: the names of the animals
    :param y: what sounds the animals make
    """
    print("Old MACDONALD had a farm\nE-I-E-I-O\nAnd on his farm he had a ", x,"\nE-I-E-I-O", sep="")
    print("With a" , y,y,"here\nAnd a",y,y,"there")
    print("Here a ", y,", there a ", y,"\nEverywhere a ", y," ", y, sep="")
    print("Old MacDonald had a farm\nE-I-E-I-O")

def main():
    print_verse("cow", "moo")
    print_verse("pig", "oink")
    print_verse("duck", "quack")
    print_verse("horse", "neigh")
    print_verse("lamb", "baa")

if __name__ == "__main__":
    main()