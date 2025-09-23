"""
COMP.CS.100 Error of Calculating Scores
Creator: Ishan Malu
Student id number: 154138420
"""


def main():
    filename = input("Enter the name of the score file: ")

    scores = {}

    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                parts = line.split()

                if len(parts) != 2:
                    print("There was an erroneous line in the file:")
                    print(line)
                    return

                name, score_str = parts

                try:
                    score = int(score_str)
                except ValueError:
                    print("There was an erroneous score in the file:")
                    print(score_str)
                    return

                # Add score to dictionary
                scores[name] = scores.get(name, 0) + score
    except OSError:
        print("There was an error in reading the file.")
        return

    print("Contestant score:")
    for name in sorted(scores):
        print(name, scores[name])


if __name__ == "__main__":
    main()
