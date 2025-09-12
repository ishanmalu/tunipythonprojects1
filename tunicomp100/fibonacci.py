"""
COMP.CS.100 Fibonacci Series
Creator: Ishan Malu
Student id number: 154138420
"""

def main():
    count = int(input("How many Fibonacci numbers do you want? "))

    previous_fib = 0
    current_fib = 1

    i = 1
    while i <= count:
        print(f"{i}. {current_fib}")
        next_fib = previous_fib + current_fib
        previous_fib = current_fib
        current_fib = next_fib
        i += 1

if __name__ == "__main__":
    main()