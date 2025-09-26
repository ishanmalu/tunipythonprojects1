"""
COMP.CS.100 Classified Car
Creator: Ishan Malu
Student id number: 154138420
"""

class Car:
    def __init__(self, tank_size, gas_consumption):
        """
        Constructor for Car.

        :param tank_size: float, capacity of the gas tank in liters
        :param gas_consumption: float, liters per 100 kilometers
        """
        self.__tank_size = tank_size
        self.__gas_consumption = gas_consumption
        self.__gas = 0.0
        self.__odometer = 0.0

    def print_information(self):
        """
        Prints current gas and odometer reading.
        """
        print(f"The tank contains {self.__gas:.1f} liters of gas "
              f"and the odometer shows {self.__odometer:.1f} kilometers.")

    def fill(self, amount):
        """
        Refuels the car.

        :param amount: float, liters of gas to add
        """
        if amount < 0:
            print("You cannot remove gas from the tank")
        else:
            self.__gas += amount
            if self.__gas > self.__tank_size:
                self.__gas = self.__tank_size

    def drive(self, distance):
        """
        Drives the car if enough gas is available.
        If not enough gas, drives as far as possible.

        :param distance: float, kilometers to drive
        """
        if distance < 0:
            print("You cannot travel a negative distance")
            return

        max_possible = (self.__gas / self.__gas_consumption) * 100

        if distance <= max_possible:
            # Enough fuel for the requested distance
            self.__odometer += distance
            self.__gas -= distance * self.__gas_consumption / 100
        else:
            # Not enough fuel → drive as far as possible
            self.__odometer += max_possible
            self.__gas = 0.0


def main():
    tank_size = float(input("How much does the vehicle's gas tank hold? "))
    consumption = float(input("How many liters of gas does the car consume per hundred kilometers? "))

    car = Car(tank_size, consumption)
    car.print_information()

    while True:
        print("1) Fill 2) Drive 3) Quit")
        choice = input("-> ")

        if choice == "1":
            amount = float(input("How many liters of gas to fill up? "))
            car.fill(amount)
            car.print_information()
        elif choice == "2":
            distance = float(input("How many kilometers to drive? "))
            car.drive(distance)
            car.print_information()
        elif choice == "3":
            print("Thank you and bye!")
            break
        else:
            print("Unknown selection, please choose again.")


if __name__ == "__main__":
    main()