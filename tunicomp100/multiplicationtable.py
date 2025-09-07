"""
COMP.CS.100 Multiplication Table
Creator: Ishan Malu
Student id number: 154138420
"""

def main():
    number = int(input("Choose a number: "))
    i = 1
    while i <= 10:
        print(i, "*", number, "=", i * number)
        i = i + 1

main()