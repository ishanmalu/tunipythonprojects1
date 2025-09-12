"""
COMP.CS.100 Credit Point Calculator
Creator: Ishan Malu
Student id number: 154138420
"""

def main():
    months = int(input("Enter the number of months: "))
    total_credits = 0
    previous_zero = False

    for i in range(1, months + 1):
        credits = int(input(f"Enter the number of credits in month {i}: "))
        if credits == 0:
            if previous_zero:
                print("You did have too many study breaks!", end="")
                return
            previous_zero = True
        else:
            previous_zero = False
        total_credits += credits

    average = total_credits / months
    if average >= 5:
        print(f"You are a full time student and your monthly credit point average is {average:.1f}.", end="")
    else:
        print(f"Your monthly credit point average {average:.1f} does not classify you as a full time student.", end="")

if __name__ == "__main__":
    main()