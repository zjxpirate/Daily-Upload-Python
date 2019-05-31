

# 3. Generate all nonattacking placements of n-queens

def n_queens(n):
    def solve_n_queens(row):
        if row == n:
            # All queens are legally placed.
            result.append(list(col_placement))
            return

        for col in range(n):

            # test if a newly placed queen will conflict any earlier queens placed before.
            if all(abs(c - col) not in (0, row - i) for i, c in enumerate(col_placement[:row])):

                print("col: ", col)
                col_placement[row] = col

                print("col_placement[row]: ", col_placement[row])
                print("col_placement: ", col_placement)

                print("row: ", row)
                print("\n")
                solve_n_queens(row + 1)

    result, col_placement = [], [0] * n
    solve_n_queens(0)
    return result

print(n_queens(4))





# list1 = [6, 5, 4, 3]
#
# for i, c in enumerate(list1):
#     print("i: ", i)
#     print("c: ", c)

