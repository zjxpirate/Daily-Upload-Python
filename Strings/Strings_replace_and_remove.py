
input = ['a', 'b', 'b', 'c', 'a', 'a']
input_size = len(input)


def replace_and_remove(size, s):
    # Forward iteration: remove 'b's and count the number of 'a's
    write_idx, a_count = 0, 0
    for i in range(size):
        if s[i] != 'b':
            s[write_idx] = s[i]
            write_idx += 1
        if s[i] == 'a':
            a_count += 1


    # Backward iteration: replace 'a's with 'dd's starting fron the end.
    cur_idx =  write_idx - 1
    write_idx += a_count - 1
    final_size = write_idx + 1
    while cur_idx >= 0:
        if s[cur_idx] == 'a':
            s[write_idx - 1 : write_idx + 1] = 'dd'
            write_idx -= 2
        else:
            s[write_idx] = s[cur_idx]
            write_idx -= 1
        cur_idx -= 1
    return final_size


result = replace_and_remove(input_size, input)

print("New length is: ", result)

print("New list will looks like: ", input)
