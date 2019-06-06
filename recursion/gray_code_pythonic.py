


# 16. compute a gray code pythonic


def gray_code_pythonic(num_bits):
    result = [0]
    for i in range(num_bits):
        result += [x + 2**i for x in reversed(result)]
    return result


print(gray_code_pythonic(3))




