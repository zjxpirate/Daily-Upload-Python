
import functools


def ss_decode_col_id(col):
    return functools.reduce(lambda result, c: result * 26 + ord(c) - ord('A') + 1, col, 0)


result = ss_decode_col_id("ZZ")

print(result)
