


import itertools

input = 4
# Pythonic solution uses the power of itertools.groupby().

def look_and_say_pythonic(n):
    s = '1'
    for _ in range(n - 1):
        s = ''.join(str(len(list(group))) + key for key, group in itertools.groupby(s))
    return s


result = look_and_say_pythonic(input)
print(result)


