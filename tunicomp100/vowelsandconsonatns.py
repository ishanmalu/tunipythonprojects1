"""
COMP.CS.100 Vowels and Consonants¶
Creator: Ishan Malu
Student id number: 154138420
"""

def main():
    word = input("Enter a word: ")
    vowels = "aeiouy"
    vowel_count = 0
    consonant_count = 0

    for ch in word:
        if ch in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

    print(f'The word "{word}" contains {vowel_count} vowels and {consonant_count} consonants.')


if __name__ == "__main__":
    main()
