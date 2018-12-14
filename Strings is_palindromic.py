

input = "asddsa"


def is_palindromic(s):
    return all(s[i] == s[~i] for i in range(len(s) // 2))


result = is_palindromic(input)

print(result)

