"""
COMP.CS.100 Zip Boing Game Loop
Creator: Ishan Malu
Student id number: 154138420
"""

def main():
    n = int(input("How many numbers would you like to have? "))
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 7 == 0:
            print("zip boing")
        elif i % 3 == 0:
            print("zip")
        elif i % 7 == 0:
            print("boing")
        else:
            print(i)

main()