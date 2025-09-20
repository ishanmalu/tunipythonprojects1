"""
COMP.CS.100 More features dictionary
Creator: Ishan Malu
Student id number: 154138420
"""

def main():
    print("Enter rows of text for word counting. Empty row to quit.")
    counts = {}

    while True:
        line = input()
        if line == "":
            break

        words = line.lower().split()
        for word in words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1

    for word in sorted(counts):
        print(f"{word} : {counts[word]} times")


if __name__ == "__main__":
    main()