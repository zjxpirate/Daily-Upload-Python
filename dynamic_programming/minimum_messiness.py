

# 14. the pretty printing problem

list1 = ['aaa', 'bbb', 'c', 'd', 'ee', 'ff', 'ggggggg']

def minimum_messiness(words, line_length):

    num_remaining_blanks = line_length - len(words[0])

    # min_messiness[i] is the minimum messiness when placing words[0:i+1].
    min_messiness = ([num_remaining_blanks ** 2] + [float('inf')] * (len(words) - 1))


    for i in range(1, len(words)):
        print("i: ", i)
        num_remaining_blanks = line_length - len(words[i])
        print(num_remaining_blanks)

        min_messiness[i] = min_messiness[i - 1] + num_remaining_blanks ** 2

        print("here: ", min_messiness)
        # try adding words[i - 1], words[i - 2], ...
        for j in reversed(range(i)):
            print("j: ", j)
            num_remaining_blanks -= len(words[j]) + 1
            print(num_remaining_blanks)
            if num_remaining_blanks < 0:
                # not enough space to add more words.
                break

            first_j_messiness = 0 if j - 1 < 0 else min_messiness[j - 1]
            print("first_j_messiness: ", first_j_messiness)

            current_line_messiness = num_remaining_blanks ** 2
            print("current_line_messiness: ", current_line_messiness)

            min_messiness[i] = min(min_messiness[i], first_j_messiness + current_line_messiness)
            print("min_messiness[i]: ", min_messiness[i])
        print("\n")


    return min_messiness[-1]


print(minimum_messiness(list1, 11))




