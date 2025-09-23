"""
COMP.CS.100 Project: Energy Statistics
Creator: Ishan Malu
Student id number: 154138420
"""
from zipapp import create_archive


def read_values():
    """
    Reads the not negative energy consumption values
    Returns:
    List: A list of integers put in by the user. 
    """
    values = []
    print("Enter energy consumption data.\nEnd by entering an empty line.")
    while True:
        s = input()
        if s == '':
            break
        try:
            val = int(s)
            if val < 0:
                print(f" You entered: {val}. Enter non-negative numbers only!")
            else:
                values.append(val)
        except ValueError:
            print(f" You entered: {s}. Enter non-negative numbers only!")
    return values

def find_category(value):
    """
    Determines the logarithmic category of the value that belongs to the index.
    Parameters:
        value (int): Energy consumption value
    Returns:
        int: Category index
    """
    if value == 0:
        return 0
    cat = 0
    lower = 0
    upper = 9
    while True:
        if lower <= value <= upper:
            return cat
        cat += 1
        lower = 10 ** cat
        upper = (10 ** (cat + 1)) - 1

def count_categories(values):
    """
    Counts the number of values in every single category.
    Parameters:
    values (list): List of integers (energy consumption)
    Returns:
        list: List with each count per category.
    """
    if not values:
        return []
    max_value = max(values)
    num_categories = len(str(max_value))
    counts = [0] * (num_categories + 1)
    for value in values:
        cat = find_category(value)
        counts[cat] += 1
    return counts

def print_single_histogram_line(lower, upper, count):
    """
    Prints a single histogram line    :param lower: 
    Parameters: 
    lower (int): The lower bound of the category
    upper (int): The upper bound of the category
    count (int): The number of categories
    """
    print(f"{lower}-{upper}: {"*" * count}")

def print_histogram(counts):
    """
    Prints the whole histogram.
    Parameters:
    counts (list): List of units per category
    """
    for i, c in enumerate(counts):
        lower = 0 if i == 0 else 10 ** i
        upper = 9 if i == 0 else (10 ** (i+1)) - 1
        print_single_histogram_line(lower, upper, c)

def main():
    values = read_values()
    if not values:
        print("Nothing to print. Done.")
        return
    counts = count_categories(values)
    print_histogram(counts)

if __name__ == "__main__":
    main()