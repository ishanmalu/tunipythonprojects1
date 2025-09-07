"""
COMP.CS.100 TGIF
Creator: Ishan Malu
Student id number: 154138420
"""

def main():
    month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = 3
    month = 1
    while month <= 12:
        print(day, ".", month, ".", sep="")
        day += 7
        if day > month_lengths[month - 1]:
            day -= month_lengths[month - 1]
            month += 1

if __name__ == "__main__":
    main()