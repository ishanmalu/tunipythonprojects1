"""
COMP.CS.100 Price List
Creator: Ishan Malu
Student id number: 154138420
"""

PRICES = {
    "milk": 1.09,
    "bread": 2.15,
    "butter": 3.10,
    "eggs": 2.80
}


def main():
    """
    Main program loop.
    The program ends when the user enters an empty line.
    """
    while True:
        product = input("Enter product name: ").strip()
        if product == "":
            print("Bye!")
            break
        if product in PRICES:
            print(f"The price of {product} is {PRICES[product]:.2f} e")
        else:
            print(f"Error: {product} is unknown.")


if __name__ == "__main__":
    main()