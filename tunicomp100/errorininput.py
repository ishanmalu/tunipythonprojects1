"""
COMP.CS.100 Error in the reading the inputs
Creator: Ishan Malu
Student id number: 154138420
"""

def read_input(prompt):
    while True:
        user_input = input(prompt)
        try:
            value = int(user_input)
            if value > 0:
                return value
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    width = read_input("Enter the width of a frame: ")
    height = read_input("Enter the height of the frame: ")
    mark = input("Enter a print mark: ")

    for _ in range(height):
        print(mark * width)

if __name__ == "__main__":
    main()
