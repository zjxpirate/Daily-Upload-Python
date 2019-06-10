

# 8. search for a sequence in a 2D array

g = [[1, 2, 3], [3, 4, 5], [5, 6, 7]]
s = [1, 3, 4, 6]

def is_pattern_contained_in_grid(grid, S):

    def is_pattern_suffix_contained_starting_at_xy(x, y, offset):

        if len(S) == offset:
            # nothing left to complete
            return True

        # check if (x, y) lies outside the grid.
        if (0 <= x < len(grid) and 0 <= y < len(grid[x]) and grid[x][y] == S[offset] and (x, y, offset) not in previous_attempts and any(is_pattern_suffix_contained_starting_at_xy(x + a, y + b, offset + 1) for a, b in ((-1, 0), (1, 0), (0, -1), (0, 1)))):
            return True

        previous_attempts.add((x, y, offset))
        return False


    # each entry in previous_attempts is a point in the grid and suffix of
    # pattern (identified by its offset). presence in previous_attempts
    # indicates the suffix is not contained in the grid starting from that point.

    previous_attempts = set()

    return any(is_pattern_suffix_contained_starting_at_xy(i, j, 0) for i in range(len(grid)) for j in range(len(grid[i])))


print(is_pattern_contained_in_grid(g, s))










