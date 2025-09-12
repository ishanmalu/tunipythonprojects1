"""
COMP.CS.100 Lottery Probabilities
Creator: Ishan Malu
Student id number: 154138420
"""

def factorial(n):
   """
   calculate the factorial

   :param n: int, the number
   :return: int, the factorial
   """
   if n == 1:
       return n
   else:
       return n*factorial(n-1)

def ask1(x,y):
    """
    This function asks the user for input in first line and returns it only if meets the criteria
    :param x: string, prompt to show the use
    :param y: int, conditional value
    :return: int, the user input if it meets the condition  or else false
    """
    userin = int(input(x))

    if userin>y:
        return userin
    else:
        return False

def ask2(x,y):
    """
    This function asks the user for input in second line and returns it only if meets the criteria
    :param x: string, prompt to show the use
    :param y: int, conditional value
    :return: int, the user input if it meets the condition or else false
    """
    userin = int(input(x))

    if userin<=y:
        return userin
    else:
        return False


def main():
    total_ball=ask1("Enter the total number of lottery balls: ",0)
    drawn_ball=ask2("Enter the number of the drawn balls: ", total_ball)

    if not total_ball:
        print("The number of balls must be a positive number.")
    elif not drawn_ball:
        print("At most the total number of balls can be drawn.")
    else:
        denom= (factorial(total_ball) / (factorial(total_ball-drawn_ball)* factorial(drawn_ball)))
        print(f"The probability of guessing all {drawn_ball} balls correctly is 1/{denom:.0f}")


if __name__ == "__main__":
    main()