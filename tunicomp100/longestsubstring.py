"""
COMP.CS.100 Longest substring in order
Creator: Ishan Malu
Student id number: 154138420
"""

def longest_substring_in_order(text):
    """
    This code will return the longest substring of text in order, to the charactersr
    that are in non-decreasing order.


    :param text: str, the lowercase letters
    :return: str, the longest substring in order
    """
    if len(text) <= 1:
        return text

    best = text[0]
    current = text[0]

    for i in range(1, len(text)):
        if text[i] >= text[i-1]:
            current += text[i]
        else:
            if len(current) > len(best):
                best = current
            current = text[i]

    if len(current) > len(best):
        best = current

    if len(best) > 1 and len(set(best)) == 1:
        return best [0]

    return best

if __name__ == "__main__":
    print(longest_substring_in_order("abcabcdefgabab"))  # 'abcdefg'
    print(longest_substring_in_order("acdkbarstyefgioprtyrtyx"))  # 'efgioprty'
    print(longest_substring_in_order("abcdefghijk"))  # 'abcdefghijk'
    print(longest_substring_in_order("aaa"))  # 'a'
    print(longest_substring_in_order(""))  # ''
    print(longest_substring_in_order("a"))  # 'a'


