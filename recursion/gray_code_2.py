


# 15. compute a gray code 2


def gray_code(num_bits):
    if num_bits == 0:
        return [0]

    # these implicitly begin with 0 at bit-index (num_bits - 1).

    gray_code_num_bits_minus_1 = gray_code(num_bits - 1)

    # now, add a 1 at bit-index (num_bits - 1) to all entries in gray_code_num_bits_minus_1.

    leading_bit_one = 1 << (num_bits - 1)

    # process in reverse order to achieve reflection of gray_code_num_bits_minus_1.

    return gray_code_num_bits_minus_1 + [leading_bit_one | i for i in reversed(gray_code_num_bits_minus_1)]

print(gray_code(3))


print(1 | 2)








