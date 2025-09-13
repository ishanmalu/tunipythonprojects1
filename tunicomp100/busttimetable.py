"""
COMP.CS.100 Bus Time Table
Creator: Ishan Malu
Student id number: 154138420
"""

def main():
    busTimetable = [630, 1015, 1415, 1620, 1720, 2000]
    userIn= int(input("Enter the time (as an integer): "))
    x=0
    while x<6:
        if userIn <= busTimetable[x]:
            y=x
            break
        elif x==5:
            y=0
        x+=1

    print("The next buses leave:")
    print(busTimetable[y])
    if y+1>5:
        print(busTimetable[0])
        print(busTimetable[1])
    elif y+2>5:
        print(busTimetable[5])
        print(busTimetable[0])
    else:
        print(busTimetable[y+1])
        print(busTimetable[y+2])


if __name__ == "__main__":
    main()