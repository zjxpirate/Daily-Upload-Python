


# 10. generate palindromic decompositions

list1 = "0204451881"

def palindrome_decompositions(input):

    def directed_palindrome_decompositions(offset, partial_partition):

        if offset == len(input):
            result.append(list(partial_partition))
            return

        for i in range(offset + 1, len(input) + 1):
            prefix = input[offset:i]


            if prefix == prefix[::-1]:

                print("offset: ", offset)
                print("i: ", i)
                print("prefix: ", prefix)
                print("prefix[::-1]: ", prefix[::-1])
                print("\n")

                directed_palindrome_decompositions(i, partial_partition + [prefix])

    result = []
    directed_palindrome_decompositions(0, [])
    return result


print(palindrome_decompositions(list1))



