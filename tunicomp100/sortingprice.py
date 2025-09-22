"""
COMP.CS.100 Sorting price
Creator: Ishan Malu
Student id number: 154138420
"""

PRICES = {
    "milk": 1.09,
    "bread": 2.10,
    "chocolate": 2.70,
    "Pepsi": 3.15,
    "pizza": 4.15,
    "fish": 4.56,
    "beans": 0.87,
    "noodles": 0.97,
    "bananas": 1.05,
    "grasshopper": 13.25,
    "sushi": 19.90
}

def main():

    for product, price in sorted(PRICES.items(), key=lambda item: item[1]):
        print(f"{product} {price:.2f}")

if __name__ == "__main__":
    main()