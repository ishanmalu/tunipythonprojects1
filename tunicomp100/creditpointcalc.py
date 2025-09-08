"""
COMP.CS.100 Credit Point Calculator
Creator: Ishan Malu
Student id number: 154138420
"""


def main():
    months = int(input("Enter the number of months: "))
    total_credits = 0
    consecutive_zero = 0

    for i in range(1, months + 1):
        credits = int(input(f"Enter the number of credits in month {i}: "))
        total_credits += credits
        if credits == 0:
            consecutive_zero += 1
            if consecutive_zero == 2:
                print("You did have too many study breaks!")
                print()
                return
        else:
            consecutive_zero = 0

    average = total_credits / months
    if average >= 5:
        print(
            f"You are a full time student and your monthly credit point average is {average:.1f}.")
    else:
        print(
            f"Your monthly credit point average {average:.1f} does not classify you as a full time student.")

    print()


main()