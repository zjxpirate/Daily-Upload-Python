

input = 12345


def int_to_string(x):
    is_negative = False
    if x < 0:
        x, is_negative = -x, True


    s = []
    while True:
        s.append(chr(ord('0') + x % 10))
        x //= 10
        if x == 0:
            break


    # add the negative sign back if is_negative
    return ('-' if is_negative else '') + ''.join(reversed(s))


result = int_to_string(input)

print(result, type(result))