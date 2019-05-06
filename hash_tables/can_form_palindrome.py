

# 4. Test for palindrome permutations

import collections

ss = "rotator"

def can_form_palindrome(s):
    # a string can be permuted to form a palindrome if and only if the number
    # of chars whose frequencies is odd is at most 1.
    return sum(v % 2 for v in collections.Counter(s).values()) <= 1

print(can_form_palindrome(ss))