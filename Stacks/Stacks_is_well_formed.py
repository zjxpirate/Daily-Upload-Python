




def is_well_formed(s):
    left_chars, LOOKUP = [], {'(': ')', '{': '}', '[': ']'}

    for c in s:
        if c in LOOKUP:
            left_chars.append(c)
        elif not left_chars or LOOKUP[left_chars.pop()] != c:
            # Unmatched right char or mismatched chars.
            return False

    return not left_chars


input = "(){[]}"


print(is_well_formed(input))





list1 = {'(': ')', '{': '}', '[': ']'}






