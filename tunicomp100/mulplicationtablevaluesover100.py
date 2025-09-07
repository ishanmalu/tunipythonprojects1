"""
COMP.CS.100 Multiplication Table Values Over 100
Creator: Ishan Malu
Student id number: 154138420
"""

def main():
    number = int(input("Choose a number: "))
    i = 1
    while i * number <= 100:
        print(i, "*", number, "=", i * number)
        i = i + 1

    print(i, "*", number, "=", i * number)

main()