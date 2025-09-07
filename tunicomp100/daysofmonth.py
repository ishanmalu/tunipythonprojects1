"""
COMP.CS.100 Dates of the year
Creator: Ishan Malu
Student id number: 154138420
"""

def main():
    for month in range(1, 13):
        if month in (1, 3, 5, 7, 8, 10, 12):
            days = 31
        elif month == 2:
            days = 28
        else:
            days = 30
        for day in range(1, days + 1):
            print(day, ".", month, ".", sep="")

if __name__ == "__main__":
    main()