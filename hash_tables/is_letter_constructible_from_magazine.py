

# 5. Is an anonoymous letter constructible

import collections

letter = "abcdef"
magazine = "abcdefgh"


# 1. Normal way
def is_letter_constructible_from_magazine(letter_text, magazine_text):
    # compute the frequencies for all chars in letter_text.
    char_frequency_for_letter = collections.Counter(letter_text)
    print(char_frequency_for_letter)
    # checks if characters in magazine_text can cover characters in char_frequency_for_letter.
    for c in magazine_text:
        if c in char_frequency_for_letter:
            char_frequency_for_letter[c] -= 1
            if char_frequency_for_letter[c] == 0:
                del char_frequency_for_letter[c]
                if not char_frequency_for_letter:
                    # all characters for letter_text are matched.
                    return True

    # empty char_frequency_for_letter means every char in letter_text can be
    # covered by a character in magazine_text.
    return not char_frequency_for_letter

#print(is_letter_constructible_from_magazine(letter, magazine))


# 2. Pythonic way

# Pythonic solution that exploits collections. Counter. Note that the
# subtraction only keeps keys with positive counts.
def is_letter_constructible_from_magazine_pythonic(letter_text, magazine_text):
    return (not collections.Counter(letter_text) - collections.Counter(magazine_text))

print(is_letter_constructible_from_magazine_pythonic(letter, magazine))



