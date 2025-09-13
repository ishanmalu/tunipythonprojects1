"""
COMP.CS.100 List as a Return value
Creator: Ishan Malu
Student id number: 154138420
"""

def input_to_list(num):
    """
    This is a function that creates a list
    """
    list= []
    print(f"Enter {num} numbers: ")
    for x in range(num):
        x=int(input())
        list.append(x)

    return list

def main():
    time=int(input("How many numbers do you want to process: "))
    count=0
    the_list=input_to_list(time)
    search = int(input("Enter the number to be searched: "))
    for x in the_list:
        if x == search:
            count += 1
    if count>0:
        print(f"{search} shows up {count} times among the numbers you have entered.")
    else:
        print(f"{search} is not among the numbers you have entered.")

if __name__ == "__main__":
    main()