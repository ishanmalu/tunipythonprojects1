"""
COMP.CS.100 Calculating scores
Creator: Ishan Malu
Student id number: 154138420
"""

def main():
    filename = input("Enter the name of the score file: ")
    scores = {}

    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            name, score_str = line.split()
            score = int(score_str)
            if name in scores:
                scores[name] += score
            else:
                scores[name] = score

    print("Contestant score:")
    for name in sorted(scores):
        print(name, scores[name])

if __name__ == "__main__":
    main()