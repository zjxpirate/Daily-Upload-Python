
waiting_for_decode = '3e4f2e'


def decoding(s):
    count, result = 0, []
    for c in s:
        if c.isdigit():
            count = count * 10 + int(c)
        else:   # c is a letter of alphabet.
            result.append(c * count)   # Appends count copies of c to result.
            count = 0

    return ''.join(result)


decode_result = decoding(waiting_for_decode)
print(decode_result)





waiting_for_encode = 'aaaabcccaa'


def encoding(s):
    result, count = [], 1
    for i in range(1, len(s) + 1):
        if i == len(s) or s[i] != s[i - 1]:
            # Found new character so write the count of previous character.
            result.append(str(count) + s[i - 1])
            count = 1
        else:   # s[i] == s[i - 1]
            count += 1

    return ''.join(result)

encode_result = encoding(waiting_for_encode)
print(encode_result)

