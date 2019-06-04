

import math, itertools


# 13. implement a sudoku solver

list1 = [[0, 0, 6, 0, 0, 8, 1, 0, 0], [0, 0, 2, 0, 0, 9, 0, 0, 7], [8, 4, 0, 1, 0, 0, 0, 0, 6], [7, 0, 4, 3, 0, 0, 8, 0, 9], [0, 0, 0, 5, 0, 6, 0, 1, 0], [0, 9, 0, 0, 4, 0, 3, 0, 2], [0, 2, 3, 7, 0, 0, 0, 0, 0], [0, 8, 0, 0, 1, 0, 4, 3, 0], [1, 0, 0, 6, 0, 0, 0, 7, 0]]

def solve_sudoku(partial_assignment):

    def solve_partial_sudoku(i, j):
        if i == len(partial_assignment):
            i = 0   # starts a row.
            j += 1
            if j == len(partial_assignment[i]):
                return True   # entire matrix has been filled without conflict.

        # skips nonempty entries.
        if partial_assignment[i][j] != EMPTY_ENTRY:
            return solve_partial_sudoku(i + 1, j)

        def valid_to_add(i, j, val):
            # check row constraints.
            if any(val == partial_assignment[k][j] for k in range(len(partial_assignment))):
                return False

            # check column constraints.
            if val in partial_assignment[i]:
                return False

            # check region constraints.
            region_size = int(math.sqrt(len(partial_assignment)))
            I = i // region_size
            J = j // region_size
            return not any(val == partial_assignment[region_size * I + a][region_size * J + b] for a, b in itertools.product(range(region_size), repeat=2))

        # it's substantially quicker to check if entry val with any of the constraints if we add
        # it at (i, j) adding it, rather than adding it and then checking all constraints. the reason
        # is that we know we are starting with a valid configuration, and the only entry which can
        # cause a problem is entry val at (i, j).

        for val in range(1, len(partial_assignment) + 1):
            if valid_to_add(i, j, val):
                partial_assignment[i][j] = val
                if solve_partial_sudoku(i + 1, j):
                    return True

        partial_assignment[i][j] = EMPTY_ENTRY   # undo assignment.
        return False

    EMPTY_ENTRY = 0
    return solve_partial_sudoku(0, 0)


print(solve_sudoku(list1))



