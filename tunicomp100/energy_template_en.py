"""
COMP.CS.100 Project: Energy Statistics
Creator: Ishan Malu
Student id number: 154138420
"""

"""
This program reads non-negative energy consumption values (kWh)
and prints a logarithmic histogram (0-9, 10-99, 100-999, ...).
Each line shows the class range and '*' marks for how many values
fell into that class.
"""

def class_minimum_value(class_number):
    """
    Return the smallest value belonging to the class.

    :param class_number: int, class index (1 = 0-9, 2 = 10-99, ...)
    :return: int, smallest value in that class
    """
    # Use the formula from the assignment specification
    return 10 ** class_number // 100 * 10


def class_maximum_value(class_number):
    """
    Return the largest value belonging to the class.

    :param class_number: int, class index (1 = 0-9, 2 = 10-99, ...)
    :return: int, largest value in that class
    """
    return 10 ** class_number - 1


def determine_class_number(value):
    """
    Determine which class a single value belongs to.

    :param value: int, a non-negative energy consumption value
    :return: int, the class index the value belongs to
    """
    class_number = 1
    # iterate classes until value fits in the class limits
    while True:
        if class_minimum_value(class_number) <= value <= class_maximum_value(class_number):
            return class_number
        class_number += 1


def count_values_in_classes(values):
    """
    Count how many values fall into each class.

    :param values: list of int, the input values
    :return: list of int, counts per class where index i stores count for class i;
             index 0 is unused for convenience
    """
    if not values:
        return []

    largest_value = max(values)
    largest_class = determine_class_number(largest_value)

    counts = [0] * (largest_class + 1)  # index 0 unused
    for v in values:
        c = determine_class_number(v)
        counts[c] += 1
    return counts


def print_single_histogram_line(class_number, count, largest_class_number):
    """
    Print one correctly-indented histogram line.

    :param class_number: int, which class this line represents
    :param count: int, how many values belong to this class
    :param largest_class_number: int, the largest class index overall
    :return: None
    """
    min_value = class_minimum_value(class_number)
    max_value = class_maximum_value(class_number)
    range_string = f"{min_value}-{max_value}"

    # The template and assignment use this formula for width:
    largest_width = 2 * largest_class_number + 1

    # Right-align the range so all colons line up, then print stars.
    print(f"{range_string:>{largest_width}}: {'*' * count}")


def print_histogram(values):
    """
    Print the full histogram for the provided values.

    :param values: list of int, input values
    :return: None
    """
    counts = count_values_in_classes(values)
    if not counts:
        # Exact required output when user entered no values
        print("Nothing to print. Done.")
        return

    largest_class = len(counts) - 1
    # Print lines for all classes from 1 .. largest_class (include empty classes)
    for class_number in range(1, largest_class + 1):
        print_single_histogram_line(class_number, counts[class_number], largest_class)


def read_input():
    """
    Read non-negative integer inputs from the user until an empty line.

    :return: list of int, the entered non-negative values
    """
    values = []
    while True:
        entry = input("Enter energy consumption (kWh): ")
        if entry == "":
            break
        try:
            number = int(entry)
            if number < 0:
                # Exact required error message
                print(f"You entered: {number}. Enter non-negative numbers only!")
            else:
                values.append(number)
        except ValueError:
            # If non-integer is entered, show same error wording (safe behavior)
            print(f"You entered: {entry}. Enter non-negative numbers only!")
    return values


def main():
    """
    Main program: prompt user, read inputs, print histogram.
    """
    print("Enter energy consumption data.")
    print("End by entering an empty line.")
    print()

    values = read_input()
    print_histogram(values)


if __name__ == "__main__":
    main()
