

# 15. test the collatz conjecture

def test_collatz_conjecture(n):
    # stores odd numbers already tested to converge to 1.
    verified_numbers = set()

    # starts from 3, hypothesis holds trivially for 1.
    for i in range(3, n + 1):
        sequence = set()
        test_i = i
        while test_i >= i:
            if test_i in sequence:
                # we previously encountered test_i, so the collatz sequence has
                # fallen into a loop. this disproves the hypothesis, so we short-circuit, returning false.
                return False
            sequence.add(test_i)

            if test_i % 2:   # odd number
                if test_i in verified_numbers:
                    break   # test_i has already been verified to converge to 1.
                verified_numbers.add(test_i)
                test_i = 3 * test_i + 1   # multiply by 3 and add 1.
            else:
                test_i //= 2   # even number, halve it.

    return True


print(test_collatz_conjecture(899))


