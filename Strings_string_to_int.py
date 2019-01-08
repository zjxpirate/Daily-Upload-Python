

import string, functools

input = '-12345'

def string_to_int(s):
    return functools.reduce(lambda running_sum, c: running_sum * 10 + string.digits.index(c), s[s[0] == '-':], 0) * (-1 if s[0] == '-' else 1)


result = string_to_int(input)

print(result)




