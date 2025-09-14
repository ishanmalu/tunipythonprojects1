"""
COMP.CS.100 Reverse the names
Creator: Ishan Malu
Student id number: 154138420
"""

def reverse_name(name):
    """
    Reformat a name written as 'Last, First' into 'First Last'.

    Parameters:
        name (str): A string containing at most one comma. It may
                    have leading/trailing or extra internal spaces.
                    Either side of the comma may be empty.

    Returns:
        str: The name in the order 'First Last', with one space
             between the parts, or just the part that exists.
             Returns an empty string if both sides are empty.
             If there is no comma, returns the name unchanged.
    """
    name = name.strip()

    if ',' not in name:
        return name

    parts = name.split(',', 1)
    last = parts[0].strip()
    first = parts[1].strip()

    if not first and not last:
        return ""
    if not first:
        return last
    if not last:
        return first
    return f"{first} {last}"


def main():
    """
    Ask the user for a name and print it in the correct order.
    """
    text = input("Enter a name: ")
    result = reverse_name(text)
    print(result)


if __name__ == "__main__":
    main()