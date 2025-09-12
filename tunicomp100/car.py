"""
COMP.CS.100 Car
Creator: Ishan Malu
Student id number: 154138420
"""

from math import sqrt


def menu():
    """
    Text-based menu. Handles user input and calls helper functions.
    """
    tank_size = read_number("How much does the vehicle's gas tank hold? ")
    gas = tank_size  # tank is full at start
    gas_consumption = read_number("How many liters of gas does the car "
                                  "consume per hundred kilometers? ")
    x = 0.0
    y = 0.0

    while True:
        print(f"Coordinates x={x:.1f}, y={y:.1f}, "
              f"the tank contains {gas:.1f} liters of gas.")

        choice = input("1) Fill 2) Drive 3) Quit\n-> ")

        if choice == "1":
            to_fill = read_number("How many liters of gas to fill up? ")
            gas = fill(tank_size, to_fill, gas)

        elif choice == "2":
            new_x = read_number("x: ")
            new_y = read_number("y: ")
            gas, x, y = drive(x, y, new_x, new_y, gas, gas_consumption)

        elif choice == "3":
            break

    print("Thank you and bye!")


def fill(size, gas_fill, gas_in_tank):
    """
    Return new amount of gas after filling, not exceeding tank size.
    """
    after = gas_in_tank + gas_fill
    return after if after <= size else size


def drive(current_x, current_y, dest_x, dest_y, gas_in_tank, gas_consump):
    """
    Simulate driving the car.

    Returns:
        (remaining_gas, new_x, new_y)

    - If there is enough fuel -> reach the destination.
    - If not enough fuel -> drive as far as possible towards
      the destination, gas becomes 0.
    """
    dx = dest_x - current_x
    dy = dest_y - current_y
    dist = sqrt(dx * dx + dy * dy)

    # No movement if distance is zero
    if dist == 0:
        return gas_in_tank, current_x, current_y

    fuel_needed = dist * (gas_consump / 100.0)

    if fuel_needed <= gas_in_tank:
        return gas_in_tank - fuel_needed, dest_x, dest_y

    # Not enough fuel: travel proportionally along the line
    max_dist = gas_in_tank * (100.0 / gas_consump)
    ratio = max_dist / dist
    new_x = current_x + dx * ratio
    new_y = current_y + dy * ratio
    return 0.0, new_x, new_y


def fuelCheck(travel, consump, in_tank):
    """
    Checks if travel is possible with the existing fuel.
    """
    return travel * (consump / 100.0) <= in_tank


def distance(x1, x2):
    """
    Returns squared difference (not used anymore but kept for compatibility).
    """
    return (x2 - x1) ** 2


def read_number(prompt, error_message="Incorrect input!"):
    """
    DO NOT TOUCH.
    Reads a float from the user and repeats until valid.
    """
    try:
        return float(input(prompt))
    except ValueError:
        print(error_message)
        return read_number(prompt, error_message)


def main():
    menu()


if __name__ == "__main__":
    main()
