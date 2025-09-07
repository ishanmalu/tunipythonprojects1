"""
COMP.CS.100 Bored Improved
Creator: Ishan Malu
Student id number: 154138420
"""

def main():
    while True:
        while True:
            answer = input("Bored? (y/n) ").strip()
            if answer in ("y", "Y", "n", "N"):
                break
            else:
                print("Incorrect entry.")
        if answer.lower() == "y":
            print("Well, let's stop this, then.")
            break

main()