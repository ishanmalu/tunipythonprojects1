"""
COMP.CS.100 How Many Abbas
Creator: Ishan Malu
Student id number: 154138420
"""

def count_abbas(text):
    """
    Count how many times the loop "abba" occurs, including the overlapping occurrences.
    :param text: str
    :return: int, number of times abba
    """
    target = "abba"
    length = len(target)
    count = 0

    for i in range(len(text) - length + 1):
        if text [i:i + length] == target:
            count += 1

    return count

if __name__ == '__main__':
    print(count_abbas("abbabbabba"))
    print(count_abbas("barbapapa"))
    print(count_abbas("abbaabba"))

    