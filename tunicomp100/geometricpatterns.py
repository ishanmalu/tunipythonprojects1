"""
COMP.CS.100 Geometric patterns
Creator: Ishan Malu
Student id number: 154138420
"""

from math import sqrt,pi,pow

def printF(a,c):
    """
    this function prints the last line
    :param a: int, area
    :param c: int, circumference
    :return:
    """
    print(f"The circumference is {c:.2f}")
    print(f"The surface area is {a:.2f}")

def takeInput(x):
    """
    takes input and makes sure it's greater than zero

    :param x: string, prompt the user will see
    :return: int, user input
    """
    while True:
        userIn = float(input(x))
        if userIn>0:
            return userIn
            break
        else:
            continue

def square():
    """
    this function calculates and shows the surface ara and circumference of a square

    :return:
    """
    x= takeInput("Enter the length of the square's side: ")

    area = pow(x,2)
    circum = 4*x

    printF(area,circum)

def circle():
    """
    this function calculates and shows the surface ara and circumference of a circle
    :return:
    """
    r= takeInput("Enter the circle's radius: ")

    area = pi * pow(r,2)
    circum= 2 * pi * r

    printF(area,circum)

def rectangle():
    """
     this function calculates and shows the surface ara and circumference of a rectangle
    :return:
    """
    a= takeInput("Enter the length of the rectangle's side 1: ")
    b= takeInput("Enter the length of the rectangle's side 2: ")

    area= a*b
    circum= (a+a+b+b)

    printF(area,circum)

def menu():
    """
    This function prints a menu for user to select which
    geometric shape to use in calculations.
    """

    while True:
        answer = input("Enter the pattern's first letter or (q)uit: ")
        if answer == "s":
            square()

        elif answer == "r":
            rectangle()

        elif answer == "c":
            circle()

        elif answer == "q":
            return

        else:
            error()

        print()  # Empty row for the sake of readability

def error():
    """
    this function is called if the users inputs an invalid entry
    :return:
    """
    print("Incorrect entry, try again!")

def main():
    menu()
    print("Goodbye!")


if __name__ == "__main__":
    main()