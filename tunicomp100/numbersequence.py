"""
COMP.CS.100 Number Sequence
Creator: Ishan Malu
Student id number: 154138420
"""

def printEven(begin,end):
    """
    This function prints even number in ascending and then descending format
    """
    realBegin=begin
    runLoop= True

    while runLoop:
        print(begin)
        if begin==end:
            while runLoop:
                print(end)
                if end == realBegin:
                    runLoop = False
                end -= 2

        begin += 2




def main():
    printEven(0,100)

if __name__ == "__main__":
    main()