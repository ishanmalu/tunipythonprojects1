"""
COMP.CS.100 Fully justified text
Creator: Ishan Malu
Student id number: 154138420
"""

def read_text():
    """
    Read text rows from the user until an empty row is entered.

    Prompts the user: "Enter text rows. Quit by entering an empty row."
    Returns a list where each element is one input line (leading/trailing
    whitespace removed). The empty row that ends input is not included.

    :return: list of strings containing the entered text lines
    """
    print("Enter text rows. Quit by entering an empty row.")
    lines = []
    while True:
        row = input()
        if row == "":
            break
        lines.append(row.strip())
    return lines


def split_into_words(lines):
    """
    Split a list of text lines into a flat list of words.

    Each line is split on whitespace; the words are collected into one list.

    :param lines: list of strings (text rows)
    :return: list of strings (all words in order)
    """
    words = []
    for line in lines:
        words.extend(line.split())
    return words


def justify_line(words, width, is_last=False):
    """
    Build one justified line from a list of words.

    If `is_last` is True or there is only one word, words are joined with
    single spaces (no extra padding). Otherwise, spaces are added between
    words so that the line length equals `width`. Extra spaces are inserted
    starting from the leftmost gaps.

    :param words: list of words for this line
    :param width: integer, desired character width for the line
    :param is_last: boolean, True if this is the final line of the paragraph
    :return: string containing the justified line
    """
    if len(words) == 1 or is_last:
        return " ".join(words)

    total_chars = sum(len(w) for w in words)
    spaces_needed = width - total_chars
    gaps = len(words) - 1

    base_spaces = spaces_needed // gaps
    extra = spaces_needed % gaps

    parts = []
    for i, w in enumerate(words[:-1]):
        parts.append(w)
        spaces = base_spaces + (1 if i < extra else 0)
        parts.append(" " * spaces)
    parts.append(words[-1])
    return "".join(parts)


def justify_text(words, width):
    """
    Format a list of words into fully justified lines.

    Breaks words into lines so that each line’s length is <= `width`.
    Calls `justify_line` to add spaces so each line is exactly `width`
    characters (except the last, which is left ragged).

    :param words: list of all words in reading order
    :param width: integer, number of characters per line
    :return: list of strings, each representing a justified line
    """
    lines = []
    current = []
    current_len = 0

    for w in words:
        if current_len + len(current) + len(w) > width:
            lines.append(justify_line(current, width))
            current = [w]
            current_len = len(w)
        else:
            current.append(w)
            current_len += len(w)

    if current:
        lines.append(justify_line(current, width, is_last=True))

    return lines


def main():
    text_rows = read_text()
    words = split_into_words(text_rows)
    width = int(input("Enter the number of characters per line: "))
    for line in justify_text(words, width):
        print(line)


if __name__ == "__main__":
    main()