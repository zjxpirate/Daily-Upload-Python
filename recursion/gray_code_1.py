


# 14. compute a gray code 1


def gray_code(num_bits):

    def directed_gray_code(history):

        counter.append(1)
        def differs_by_one_bit(x, y):
            bit_difference = x ^ y
            return bit_difference and not (bit_difference & (bit_difference - 1))


        if len(result) == 1 << num_bits:
            # check if the first and last codes differ by one bit.
            return differs_by_one_bit(result[0], result[-1])

        for i in range(num_bits):
            previous_code = result[-1]

            print("previous_code: ", previous_code)

            candidate_next_code = previous_code ^ (1 << i)

            print("candidate_next_code: ", candidate_next_code)
            print("i: ", i)
            print("counter: ", len(counter))
            print("\n")

            if candidate_next_code not in history:
                history.add(candidate_next_code)
                result.append(candidate_next_code)

                if directed_gray_code(history):
                    return True

        return False

    counter = []
    result = [0]
    directed_gray_code(set([0]))
    return result

print(gray_code(3))












