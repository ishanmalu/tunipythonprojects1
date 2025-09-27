"""
COMP.CS.100 Project: Energy Statistics
Creator: Ishan Malu
Student id number: 154138420
"""

"""
This program reads non-negative energy consumption values (kWh) 
and prints them as a histogram. Values are grouped into classes 
(0–9, 10–99, 100–999, ...), and each line shows the range with 
'*' marks for how many values belong there.
"""


def class_maximum_value(class_number):
    """Return the maximum value for the given class."""
    return 10 ** class_number - 1


def class_minimum_value(class_number):
    """Return the minimum value for the given class."""
    return 10 ** class_number // 100 * 10


def determine_class_number(value):
    """Return which class a value belongs to."""
    class_number = 1
    while True:
        if class_minimum_value(class_number) <= value <= class_maximum_value(class_number):
            return class_number
        class_number += 1


def number_of_classes(values):
    """Return how many classes are needed for all values."""
    maximum = max(values)
    return determine_class_number(maximum)


def build_class_counts(values, num_classes):
    """Return a list of counts per class (index 0 unused)."""
    counts = [0] * (num_classes + 1)
    for v in values:
        c = determine_class_number(v)
        counts[c] += 1
    return counts


def print_single_histogram_line(class_number, count, largest_class_number):
    """Print one histogram line for the given class."""
    min_value = class_minimum_value(class_number)
    max_value = class_maximum_value(class_number)
    range_string = f"{min_value}-{max_value}"

    largest_range = f"{class_minimum_value(largest_class_number)}-{class_maximum_value(largest_class_number)}"
    width = len(largest_range)

    print(f"{range_string:>{width}}: {'*' * count}")


def print_histogram(values):
    """Print the full histogram."""
    num_classes = number_of_classes(values)
    counts = build_class_counts(values, num_classes)

    for class_number in range(1, num_classes + 1):
        print_single_histogram_line(class_number, counts[class_number], num_classes)


def read_input():
    """Read input values until empty line, reject negatives."""
    values = []
    while True:
        entry = input("Enter energy consumption (kWh): ")
        if entry == "":
            break
        try:
            num = int(entry)
            if num < 0:
                print(f"You entered: {num}. Enter non-negative numbers only!")
            else:
                values.append(num)
        except ValueError:
            print(f"You entered: {entry}. Enter non-negative numbers only!")
    return values


def main():
    """Main program flow."""
    print("Enter energy consumption data.")
    print("End by entering an empty line.\n")

    input_values = read_input()

    if not input_values:
        print("Nothing to print. Done.")
    else:
        print_histogram(input_values)


if __name__ == "__main__":
    main()
