

input = 'Hello_World'

def snake_string_pythonic(s):
    return s[1::4] + s[::2] + s[3::4]


snake = snake_string_pythonic(input)

print(snake)
