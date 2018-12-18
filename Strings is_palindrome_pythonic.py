

input = "asdfgfdsa"


def is_palindrome_pythonic(s):
    return all(a == b for a, b in zip(map(str.lower, filter(str.isalnum, s)), map(str.lower, filter(str.isalnum, reversed(s)))))


result = is_palindrome_pythonic(input)

print(result)