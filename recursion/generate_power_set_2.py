
import math

# 7. generate the power set improved

list1 = [0, 1, 2]

def generate_power_set(S):
    power_set = []
    for int_for_subset in range(1 << len(S)):
        bit_array = int_for_subset
        subset = []
        while bit_array:
            subset.append(int(math.log2(bit_array & ~(bit_array - 1))))
            bit_array &= bit_array - 1
        power_set.append(subset)
    return power_set

print(generate_power_set(list1))









