


arr1 = "Python is interesting"


input = bytearray(arr1, 'utf-8')

# Assume s is a string encoded as bytearray.
def reverse_words(s):
    # First, reverse the whole string.
    s.reverse()

    def reverse_range(s, start, finish):
        while start < finish:
            s[start], s[finish] = s[finish], s[start]
            start, finish = start + 1, finish - 1

    start = 0
    while True:
        finish = s.find(b' ', start)
        if finish < 0:
            break
        # Reverses each word in the string.
        reverse_range(s, start, finish - 1)
        start = finish + 1

    # Reverses the last word
    reverse_range(s, start, len(s) - 1)
    s1 = s.decode("utf-8")
    return s1


result = reverse_words(input)

print(result)
