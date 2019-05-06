
import functools

# 1. string hash
dict1 = "a"

def string_hash(s, modulus):
    MULT = 997
    return functools.reduce(lambda v, c: (v * MULT + ord(c)) % modulus, s, 0)

print(string_hash(dict1, 2))